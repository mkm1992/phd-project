clear all
clc
run var_const
count_min1 = 3;
count_step1 = 2;
count_max1 = 12;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 1;
sumRate = zeros(numvar,iter_max);
%% initializing
number_check = 0;
for i_count = count_min1:count_step1:count_max1
    number_check  = number_check +  1;
    for iter = 1:iter_max
        run parameter_UE_change
        alpha_m = lambda_m.*(UE_S);
        run PRB_Pow_Alloc1
        run findM
        run Rate_final
        sumRate(number_check,iter) = abs(sum(rate_UE_1));
        VNF_NUM

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