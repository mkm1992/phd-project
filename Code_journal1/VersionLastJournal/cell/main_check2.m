number_check = 0;
DelayTot= zeros(numvar,iter_max,S)+10;
Delay1_last= zeros(numvar,iter_max,S)+10;
for i_count = count_min1:count_step1:count_max1
    %Pmax = i_count;
    lambda_m = ones(1,S)*i_count;
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
        run PRB_Pow_Alloc2
        run findM
        run Rate_final
        run RUUESet
        rate_sum1 =abs(Fact_1*sum(rate_UE(1:UE_S(1)))+Fact_2*sum(rate_UE(6:10)));
        sumRate(number_check,iter) = max(rate_sum1,sumRate(number_check,iter));
        for s = 1:S
            DelayTot(number_check,iter,s) = min(Delay_tot(s),DelayTot(number_check,iter,s));
            Delay1_last(number_check,iter,s) = min(Delay_Slice1(s),Delay1_last(number_check,iter,s));
        end
        
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
 (sum(DelayTot,3)/3)'
 (sum(Delay1_last,3)/3)'