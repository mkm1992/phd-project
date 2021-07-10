clear all
clc
run var_const
count_min1 = 2;
count_step1 = 2;
count_max1 = 10;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 2;
sumRate = zeros(numvar,iter_max);
%% initializing
number_check = 0;
for i_count = count_min1:count_step1:count_max1
    number_check  = number_check +  1;
    for iter = 1:iter_max  
        RU_iter = 1;
        while  RU_iter < N_RU + 1
            run parameter_UE_change
            if RU_iter == 1
              run RUUEFirst  
            end
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc1
            run findM
            run Rate_final
            run RUUESet
            sumRate(number_check,iter) = abs(sum(rate_UE_1));
            if sumRate(number_check,iter) > 0
                RU_iter = N_RU + 10;
                
            end
            iter
            i_count
            VNF_NUM
        end

    end
end
UE_num = count_min1:count_step1:count_max1;
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
plot( UE_num , sumR1)

%plot(UE_num ,mean(sumRate,2))