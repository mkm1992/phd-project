clear all
clc
run var_const
count_min1 = 1;
count_step1 = 2;
count_max1 = 10;
numvar = length(count_min1:count_step1:count_max1);
iter_max = 1;
sumRate = zeros(numvar,iter_max);
sumRate1= zeros(numvar,iter_max);
DelayTot= zeros(numvar,iter_max,S);
Delay1_last= zeros(numvar,iter_max,S);
DelayTot1= zeros(numvar,iter_max,S);
Delay1_last_base= zeros(numvar,iter_max,S);
VNFNumber = zeros(numvar,iter_max,S);
VNFNumber1 = zeros(numvar,iter_max,S);
RU_iter_max = 2;
%% initializing
for iter = 1:iter_max 
    number_check = 0;
    run parameter_UE_change
    for i_count = count_min1:count_step1:count_max1
        Pmax = i_count;
        number_check  = number_check +  1;
        RU_iter = 5;
        PRB_UE = zeros(N_PRB,N_UE);
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
        
        %% BaseLine Scheme
            %PRB_UE = zeros(N_PRB,N_UE);
            %run PRB_rand
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
end

UE_num = count_min1:count_step1:count_max1;
sumR =  zeros(1,numvar);
sumR1 =  zeros(1,numvar);
TDelay =  zeros(S,numvar);
TDelay1 =  zeros(S,numvar);
TDelayP1 =zeros(S,numvar);
TDelayB1 =zeros(S,numvar);
VNFNumP = zeros(S,numvar);
VNFNumB = zeros(S,numvar);
VNFNumP1 = zeros(S,numvar);
VNFNumB1 = zeros(S,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate(i,j)) == 0 
            sumR(i) = sumR(i) + sumRate(i,j);
            for s = 1:S
                TDelay(s,i) = TDelay(s,i) + DelayTot(i,j,s);
                TDelayP1(s,i) = TDelayP1(s,i) + Delay1_last(i,j,s);
                VNFNumP(s,i) = VNFNumP(s,i) + VNFNumber(i,j,s);
            end
            num(i)=  num(i) + 1;
        end
    end
    sumR1(i) = sumR(i)/num(i);
    TDelay(:,i) = TDelay(:,i)./num(i);
    TDelayP1(:,i) = TDelayP1(:,i)./num(i);
    VNFNumP1(:,i) = VNFNumP(:,i)./num(i);
end


sumRB =  zeros(1,numvar);
sumRB1 =  zeros(1,numvar);
num = zeros(1,numvar);
for i =1:numvar
    for j =1:iter_max
        if isnan(sumRate1(i,j)) == 0 
            sumRB(i) = sumRB(i) + sumRate1(i,j);
            for s = 1:S
                TDelay1(s,i) = TDelay1(s,i) + DelayTot1(i,j,s);
                TDelayB1(s,i) = TDelayB1(s,i) + Delay1_last_base(i,j,s);
                VNFNumB(s,i) = VNFNumB(s,i) + VNFNumber1(i,j,s);
            end
            num(i)=  num(i) + 1;
        end
    end
    sumRB1(i) = sumRB(i)/num(i);
    TDelay1(:,i) = TDelay1(:,i)./num(i);
    TDelayB1(:,i) = TDelayB1(:,i)./num(i);
    VNFNumB1(:,i) = VNFNumB(:,i)./num(i);
end
figure;
plot( UE_num , sumR1,'-*')
hold on
plot( UE_num , sumRB1,'-+')
% figure;
 plot( UE_num , sum(TDelayP1),'--')
hold on
 plot( UE_num , sum(TDelayB1),'-.')
     