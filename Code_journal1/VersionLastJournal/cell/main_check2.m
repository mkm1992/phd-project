number_check = 0;
for i_count = count_min1:count_step1:count_max1
    Pmax = i_count;
    Popt = ones(1,N_UE)*Pmax;
    PRB_UE = zeros(N_PRB,N_UE);
    run PRB_Alloc
    number_check  = number_check +  1;
    RU_iter = 1;
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
        run RUUESet

        sumRate(number_check,iter) = max(abs(sum(rate_UE_1)),sumRate(number_check,iter));
        DelayTot(number_check,iter,:) = Delay_tot(:);
        Delay1_last(number_check,iter,:) = Delay_Slice1(:);
        VNFNumber(number_check,iter,:) =VNF_NUM(:);
        if sumRate(number_check,iter) > 0 && RU_iter >3 
            RU_iter = RU_iter_max + 10;

        end
        iter
        i_count
        RU_iter
        VNF_NUM
        RU_iter = RU_iter + 1;
    end
end