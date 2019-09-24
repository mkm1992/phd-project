% map slice to service
clear all
clc
run var
%% sort service
Priot_Service = (sum(Ut2Service,1)).^priority_service;
[~,idx] = sort(Priot_Service);
sort_UtService = Ut2Service(:,idx);
%% sort slice
W_PRB = 3;
W_RRH = 2;
W_VNF = 1;
Priot_Slice = sum(rrh2slice,1)*W_RRH + (sum(VNF2Slice1,1)+sum(VNF2Slice2,1))*W_VNF; % sum(PRB2Slice,1)*W_PRB 
[~,idx1] = sort(Priot_Slice);
sort_PRB2Slice = PRB2Slice(:,idx1);
sort_rrh2slice = rrh2slice(:,idx1);
sort_VNF2Slice1 = VNF2Slice1(:,idx1);
sort_VNF2Slice2 = VNF2Slice2(:,idx1);
%% mapping
mapStatusService = ones(1,N_Service);
mapStatusSlice = ones(1,N_Slice);
run channel
run precoding
count  = 0;
for jj = N_Slice:-1:1
    if mapStatusSlice(jj)==1
    for ii = N_Service:-1:1
         
        if mapStatusService(ii)==1
            count = count +1;
            service2slice(ii,jj)=1;
            run mappingOtherParameter
            run MapPRB2UT
            run interference
            run rate
            run FronthaulCap
            run FindDelay
            rate_service = rate_UE'.*Ut2Service(:,ii);
            rateService = rate_service(rate_service>0);
            Crrh_service = Crrh' .* rrh2slice(:,jj);
            CrrhSlice = Crrh_service(Crrh_service>0);
            Prrh_service = Prrh' .* rrh2slice(:,jj);
            PrrhSlice = Prrh_service(Prrh_service>0);
            if all(rateService(:)>Rt) && Delay_Slice(jj) < delay_max && all(PrrhSlice(:)<Pmax) && all(CrrhSlice(:)<C_thresh)
                all(rateService(:)>Rt)
            
                mapStatusService(ii) =0;
                mapStatusSlice(jj) = 0;
                break
            else
                service2slice(ii,jj)=0;
            end
        end
    end
    end
end
%run channel
ChannelGain = ChannelGain2;
run precoding 
%run mappingOtherParameter
%run MapPRB2UT
run interference
run rate
run FronthaulCap
run FindDelay
