clear all
clc
run var_const
count_min1 = 16;
count_step1 = 2;
count_max1 = 16;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 10;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);

RU_iter_max = 10;%N_RU + 5;
delayIter = zeros(iter_max,RU_iter_max);
SumRate_prb = zeros(iter_max,numvar,RU_iter_max-1);
%% initializing
number_check = 0;
for i_count = count_min1:count_step1:count_max1
    number_check  = number_check +  1;
    for iter = 1:iter_max  
        RU_iter = 1;
        Pmax = 3;%i_count;%10;
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
            %if sumRate(number_check,iter) > 0 && RU_iter >2 
                %RU_iter = RU_iter_max + 10;

            %end
            delayIter(iter,RU_iter) = sum(Delay_Slice1);
            RU_iter = RU_iter + 1;
         end

         run RUAssociateDist 
         run setChGain
         run checkFeasibility
         sumRate(number_check,iter) = sum(rate_UE_1);
         A_final
    end
end
UE_num = count_min1:count_step1:count_max1;


sumRB =  zeros(1,numvar);
sumRB1 =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate1(i,j)) == 0  && sumRate1(i,j)>0
            sumRB(i) = sumRB(i) + sumRate1(i,j);
            num(i)=  num(i) + 1;
        end
    end
    sumRB1(i) = sumRB(i)/num(i);
end

sumR =  zeros(1,numvar);
sumR1 =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate(i,j)) == 0 
            sumR(i) = sumR(i) + sumRate(i,j);
            num(i)=  num(i) + 1;
        end
    end
    sumR1(i) = sumR(i)/num(i);
end
plot( UE_num , sumRB1/1e6,'-*')
hold on
plot( UE_num , sumR1/1e6,'-+')

xlabel('Number of UEs')
ylabel('Aggregate Throughput (Mbps)')
title('Aggregate Throughput vs. Number of UEs')
legend('Proposed Method (IABV) ','Fast Algorithm (FA)')
grid on
%plot(1:RU_iter_max-1,mean(SumRate_prb,1))
%plot(UE_num ,mean(sumRate,2))