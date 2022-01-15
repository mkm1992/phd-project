#!/bin/bash

# Image and model names
TEST_IMG=ADE_val_00001519.jpg
MODEL_PATH=baseline-resnet101-upernet
RESULT_PATH=./

ENCODER=$MODEL_PATH/encoder_epoch_25.pth
DECODER=$MODEL_PATH/decoder_epoch_25.pth

# Download model weights and image
if [ ! -e $MODEL_PATH ]; then
  mkdir $MODEL_PATH
fi


# Inference
python -u test.py \
  --model_path $MODEL_PATH \
  --test_imgs $TEST_IMG \
  --arch_encoder resnet101 \
  --arch_decoder upernet \
  --fc_dim 2048 \
  --result $RESULT_PATH
