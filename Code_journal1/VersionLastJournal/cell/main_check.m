clear all
clc
run var_const
count_min1 = 1;
count_step1 = 2;
count_max1 = 10;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 1;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);
DelayTot= zeros(numvar,iter_max,S);
Delay1_last= zeros(numvar,iter_max,S);
DelayTot1= zeros(numvar,iter_max,S);
Delay1_last_base= zeros(numvar,iter_max,S);
VNFNumber = zeros(numvar,iter_max,S);
VNFNumber1 = zeros(numvar,iter_max,S);
RU_iter_max = N_RU;
%% initializing
for iter = 1:iter_max 
    number_check = 0;
    run parameter_UE_change
    for i_count = count_min1:count_step1:count_max1
        Pmax = i_count;
        number_check  = number_check +  1;
        RU_iter = 1;
        run PRB_Alloc
        %%
        while  RU_iter < RU_iter_max
            
            if RU_iter == 1
              run RUAssociateDist  
            end
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc1
            run findM
            run Rate_final
            %run RUUESet
            
            sumRate(number_check,iter) = max(abs(sum(rate_UE_1)),sumRate(number_check,iter));
            DelayTot(number_check,iter,:) = Delay_tot(:);
            Delay1_last(number_check,iter,:) = Delay_Slice1(:);
            VNFNumber(number_check,iter,:) =VNF_NUM(:);
            if sumRate(number_check,iter) > 0 && RU_iter >0 
                RU_iter = RU_iter_max + 10;
                
            end
            iter
            i_count
            RU_iter
            VNF_NUM
            RU_iter = RU_iter + 1;
        end
    end
end
