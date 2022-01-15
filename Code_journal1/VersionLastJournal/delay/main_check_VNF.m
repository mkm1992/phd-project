clear all
clc
run var_const
count_min1 = 4e6;
count_step1 = 4e6;
count_max1 = 20e6;
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
        lambda_m = ones(1,S)*i_count;
        mu = ones(1,S)*20e6;
        PRB_UE = zeros(N_PRB,N_UE);
        number_check  = number_check +  1;
        RU_iter = 1;
        run PRB_Alloc
        %%
        
        %% BaseLine Scheme
            %run PRB_rand
            run RUAssociateDist
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc2
            run Rate_final
            run findM
            
            run RUUESet
            VNF_NUM
            sumRate1(number_check,iter) = abs(sum(rate_UE_1)); 
            DelayTot1(number_check,iter,:) = Delay_tot(:);
            Delay1_last_base(number_check,iter,:) = Delay_Slice1(:);
            VNFNumber1(number_check,iter,:) =VNF_NUM(:);
            Delay_tot
            Delay_Slice1
    end
end
 plot(sumRate1)