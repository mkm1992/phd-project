clear all
clc
run var_const
count_min1 = 17;
count_step1 = 2;
count_max1 = 25;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 400;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);

RU_iter_max = 6;%N_RU + 5;
SumRate_prb = zeros(iter_max,numvar,RU_iter_max-1);
%% initializing
number_check = 0;
for i_count = count_min1:count_step1:count_max1
    number_check  = number_check +  1;
    for iter = 1:iter_max  
        RU_iter = 1;
        Pmax = 5;
        run parameter_UE_change
        run PRB_Alloc
         while  RU_iter < RU_iter_max

        if RU_iter == 1
          run RUAssociateDist  
        end
        %%
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run delay_const
            run PRB_P
            %run PRB_Pow_Alloc1
            run findM
            run Rate_final
            run RUUESet
            SumRate_prb(iter,number_check,RU_iter) = sum(rate_UE_1);
            sumRate1(number_check,iter) = max(abs(sum(rate_UE_1)),sumRate1(number_check,iter));       
            i_count
            RU_iter
            VNF_NUM
            if sumRate(number_check,iter) > 0 && RU_iter >2 
                %RU_iter = RU_iter_max + 10;

            end
            
            RU_iter = RU_iter + 1;
         end
    end
end
UE_num = count_min1:count_step1:count_max1;


sumRB =  zeros(1,numvar);
sumRB1 =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate1(i,j)) == 0 
            sumRB(i) = sumRB(i) + sumRate1(i,j);
            num(i)=  num(i) + 1;
        end
    end
    sumRB1(i) = sumRB(i)/num(i);
end

plot( UE_num , sumRB1/1e6,'-+')
%plot(1:RU_iter_max-1,mean(SumRate_prb,1))
%plot(UE_num ,mean(sumRate,2))