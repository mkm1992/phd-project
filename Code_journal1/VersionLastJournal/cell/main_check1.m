clear all
clc
run var_const
count_min1 = 0.1;
count_step1 = 0.1;
count_max1 = 0.9;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 1;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);
RateEmbb = zeros(numvar,iter_max);
RateUrllc= zeros(numvar,iter_max);
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
    Pmax = 5;
    for i_count = count_min1:count_step1:count_max1
        %delay_max = ones(1,S)*i_count;
        Fact_1 = i_count;
        Fact_2 = 1 - i_count;
        %lambda_m = ones(1,S)*N_UE;
        Popt = ones(1,N_UE)*Pmax;
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
            run findM
            run Rate_final
            run RUUESet
            VNF_NUM
            rate_sum1 =abs(Fact_1*sum(rate_UE(1:UE_S(1)))+Fact_2*sum(rate_UE(6:10)));
            sumRate1(number_check,iter) = max(rate_sum1,sumRate1(number_check,iter));
            RateEmbb(number_check,iter) =abs(Fact_1*sum(rate_UE(1:UE_S(1))));
            RateUrllc(number_check,iter)=Fact_2*sum(rate_UE(6:10));
            DelayTot1(number_check,iter,:) = Delay_tot(:);
            Delay1_last_base(number_check,iter,:) = Delay_Slice1(:);
            VNFNumber1(number_check,iter,:) =VNF_NUM(:);
    end
end
 plot(sumRate1)
%  (sum(DelayTot1,3)/3)'
%   (sum(Delay1_last_base,3)/3)'