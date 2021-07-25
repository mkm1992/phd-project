%% initializing
    number_check = 0;
run PRB_rand   
for i_count = count_min1:count_step1:count_max1
    %Pmax = i_count;
    lambda_m = ones(1,S)*i_count;
    Popt = ones(1,N_UE)*Pmax;
    %PRB_UE = zeros(N_PRB,N_UE);
    number_check  = number_check +  1;
    RU_iter = 1;
    %run PRB_Alloc
    %%
    
    %% BaseLine Scheme
        
        run RUAssociateDist
        run setChGain
        alpha_m = lambda_m.*(UE_S);
        run PRB_Pow_Alloc2
        run findM
        run Rate_final
        run RUUESet
        VNF_NUM
        sumRate1(number_check,iter) = abs(sum(rate_UE_1)); 
        DelayTot1(number_check,iter,:) = Delay_tot(:);
        Delay1_last_base(number_check,iter,:) = Delay_Slice1(:);
        VNFNumber1(number_check,iter,:) =VNF_NUM(:);
end

 plot(sumRate1)