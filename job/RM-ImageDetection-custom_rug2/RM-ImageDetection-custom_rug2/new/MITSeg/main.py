import os
import datetime
import argparse
from distutils.version import LooseVersion
# Numerical libs
import numpy as np
import torch
import torch.nn as nn
from scipy.io import loadmat
# Our libs
from dataset import TestDataset
from models import ModelBuilder, SegmentationModule
from utils import colorEncode
from lib.nn import user_scattered_collate, async_copy_to
from lib.utils import as_numpy, mark_volatile
import lib.utils.data as torchdata
import cv2
from tqdm import tqdm

colors = loadmat('data/color150.mat')['colors']


def visualize_result(data, pred):
    (img, info) = data
    result='.'
    # prediction
    pred[np.where(np.isin(pred,[3,6,29,25,13,52,54]))]=3

    #pred[np.where(~(np.isin(pred,[3,6,29,13,52,54])))]=25

    pred_color = colorEncode(pred, colors)

    # aggregate images and save
    im_vis = np.concatenate((img, pred_color),
                            axis=1).astype(np.uint8)

    img_name = info.split('/')[-1]
    cv2.imwrite("output"+os.path.join(result,
                img_name.replace('.jpg', '.png')), pred_color)
    return pred

def test(segmentation_module, loader):
    segmentation_module.eval()

    pbar = tqdm(total=len(loader))
    for batch_data in loader:
        # process data
        batch_data = batch_data[0]
        segSize = (batch_data['img_ori'].shape[0],
                   batch_data['img_ori'].shape[1])
        img_resized_list = batch_data['img_data']

        with torch.no_grad():
            scores = torch.zeros(1, num_class, segSize[0], segSize[1])
            #scores = async_copy_to(scores, gpu_id)

            for img in img_resized_list:
                feed_dict = batch_data.copy()
                feed_dict['img_data'] = img
                del feed_dict['img_ori']
                del feed_dict['info']
                #feed_dict = async_copy_to(feed_dict, gpu_id)

                # forward pass
                pred_tmp = segmentation_module(feed_dict, segSize=segSize)
                scores = scores + pred_tmp / len(imgSize)

            _, pred = torch.max(scores, dim=1)
            pred = as_numpy(pred.squeeze(0).cpu())

        # visualization
        pred=visualize_result(
            (batch_data['img_ori'], batch_data['info']),
            pred)

        pbar.update(1)
        return pred


def main():
    suffix='_epoch_50.pth'
    test_imgs=["input/m1.jpg"]
    model_path='baseline-resnet101-upernet'
    #model_path = 'a'

    # Model related arguments
    arch_encoder='resnet101'
    arch_decoder='upernet'
    #arch_encoder='resnet101dilated'
    #arch_decoder='ppm_deepsup'

    fc_dim=2048


    # Data related arguments
    num_val=-1
    num_class=150
    batch_size=1

    imgSize=[300, 400, 500, 600]

    imgMaxSize=1000
    padding_constant=8
    segm_downsampling_rate=8

    # Misc arguments
    result='.',

    gpu_id=0
    #torch.cuda.set_device(gpu_id)

    # Network Builders
    builder = ModelBuilder()
    net_encoder = builder.build_encoder(
        arch=arch_encoder,
        fc_dim=fc_dim,
        weights=weights_encoder)
    net_decoder = builder.build_decoder(
        arch=arch_decoder,
        fc_dim=fc_dim,
        num_class=num_class,
        weights=weights_decoder,
        use_softmax=True)

    crit = nn.NLLLoss(ignore_index=-1)

    segmentation_module = SegmentationModule(net_encoder, net_decoder, crit)

    # Dataset and Loader
    # list_test = [{'fpath_img': args.test_img}]
    list_test = [{'fpath_img': x} for x in test_imgs]
    dataset_test = TestDataset(
        list_test, max_sample=num_val)
    loader_test = torchdata.DataLoader(
        dataset_test,
        batch_size=batch_size,
        shuffle=False,
        collate_fn=user_scattered_collate,
        num_workers=5,
        drop_last=True)

    segmentation_module

    # Main loop
    pred=test(segmentation_module, loader_test)
    print(pred)
    print('Inference done!')


if __name__ == '__main__':
    assert LooseVersion(torch.__version__) >= LooseVersion('0.4.0'), \
        'PyTorch>=0.4.0 is required'

    #parser = argparse.ArgumentParser()
    # Path related arguments
    suffix='_epoch_50.pth'
    test_imgs='input/m11.jpg'
    model_path='baseline-resnet101-upernet'
    #model_path = 'a'

    # Model related arguments
    arch_encoder='resnet101'
    arch_decoder='upernet'
    #arch_encoder='resnet101dilated'
    #arch_decoder='ppm_deepsup'
    fc_dim=2048


    # Data related arguments
    num_val=-1
    num_class=150
    batch_size=1

    imgSize=[300, 400, 500, 600]

    imgMaxSize=1000
    padding_constant=8
    segm_downsampling_rate=8

    # Misc arguments
    result='.',

    gpu_id=0



    # absolute paths of model weights
    weights_encoder = os.path.join(model_path,
                                        'encoder' + suffix)
    weights_decoder = os.path.join(model_path,
                                        'decoder' + suffix)

    assert os.path.exists(weights_encoder) and \
        os.path.exists(weights_decoder), 'checkpoint does not exitst!'



    main()
