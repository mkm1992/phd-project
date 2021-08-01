clear all
clc
run var_const
count_min1 = 0.1;
count_step1 = .2;
count_max1 = 0.9;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 20;
sumRate_eMBB = zeros(numvar,iter_max);
sumRate_URLLC = zeros(numvar,iter_max);
sumRate1_eMBB= zeros(numvar,iter_max);
sumRate1_URLLC = zeros(numvar,iter_max);
RU_iter_max = N_RU-1;
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
            %run PRB_rand
            run RUAssociateDist
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc1
            run findM
            run Rate_final
            run RUUESet
            sumRate1_eMBB(number_check,iter) = abs(sum(R_s_1(1)));
            sumRate1_URLLC(number_check,iter) = abs(sum(R_s_1(2)));           
    end
end
UE_num = count_min1:count_step1:count_max1;




sumRB_e =  zeros(1,numvar);
sumRB_u =  zeros(1,numvar);
sumRB1_e =  zeros(1,numvar);
sumRB1_u =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate1_eMBB(i,j)) == 0 
            sumRB_e(i) = sumRB_e(i) + sumRate1_eMBB(i,j);
            sumRB_u(i) = sumRB_u(i) + sumRate1_URLLC(i,j);
            num(i)=  num(i) + 1;
        end
    end
    sumRB1_e(i) = sumRB_e(i)/num(i);
    sumRB1_u(i) = sumRB_u(i)/num(i);
end

plot( UE_num , sumRB1_e/1e6,'-^')
hold on
plot( UE_num , sumRB1_u/1e6,'--')
hold on
xlabel('Priority Factor for eMBB Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput vs Priority Factor for eMBB Service')
%plot(UE_num ,mean(sumRate,2))