clear all
clc
run var_const
count_min1 = 0.1;
count_step1 = .1;
count_max1 = 0.9;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 1;
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
            sumRate_eMBB(number_check,iter) = abs(sum(rate_UE_1(1:4)));
            sumRate_URLLC(number_check,iter) = abs(sum(rate_UE_1(5:8)));
            if sumRate_eMBB(number_check,iter) > 0
                RU_iter = RU_iter_max + 10;
                
            end
            iter
            i_count
            RU_iter
            VNF_NUM
            RU_iter = RU_iter + 1;
        end
        %% BaseLine Scheme
            run PRB_rand
            run RUAssociateDist
            run setChGain
            alpha_m = lambda_m.*(UE_S);
            run PRB_Pow_Alloc2
            run findM
            run Rate_final
            run RUUESet
            sumRate1_eMBB(number_check,iter) = abs(sum(R_s_1(1)));
            sumRate1_URLLC(number_check,iter) = abs(sum(R_s_1(2)));           
    end
end
UE_num = count_min1:count_step1:count_max1;
sumR_e =  zeros(1,numvar);
sumR_u =  zeros(1,numvar);
sumR1_e =  zeros(1,numvar);
sumR1_u =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate_eMBB(i,j)) == 0 
            sumR_e(i) = sumR_e(i) + sumRate_eMBB(i,j);
            sumR_u(i) = sumR_u(i) + sumRate_URLLC(i,j);
            num(i)=  num(i) + 1;
        end
    end
    sumR1_e(i) = sumR_e(i)/num(i);
    sumR1_u(i) = sumR_u(i)/num(i);
end


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

plot( UE_num , sumR1_e/1e6,'-*')
hold on
plot( UE_num , sumR1_u/1e6,'-+')
hold on
plot( UE_num , sumRB1_e/1e6,'-^')
hold on
plot( UE_num , sumRB1_u/1e6,'--')
hold on
xlabel('Priority Factor for eMBB Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput vs Priority Factor for eMBB Service')
%plot(UE_num ,mean(sumRate,2))