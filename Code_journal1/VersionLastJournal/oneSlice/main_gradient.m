clear all
clc
run var_const
count_min1 = 2;
count_step1 = 2;
count_max1 = 16;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 100;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);
RU_iter_max = N_RU + 5;
%% initializing
number_check = 0;
for i_count = count_min1:count_step1:count_max1
    number_check  = number_check +  1;
    for iter = 1:iter_max  
        RU_iter = 1;
        run parameter_UE_change
        run PRB_Alloc
        %%
        %% BaseLine Scheme
            run RUAssociateDist
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc1
            run findM
            run Rate_final
            %run RUUESet
            sumRate1(number_check,iter) = abs(sum(rate_UE_1));            
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

%plot(UE_num ,mean(sumRate,2))