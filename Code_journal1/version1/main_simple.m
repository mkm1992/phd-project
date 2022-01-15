clear all
clc
%% Variable
R = 500;
S = 1;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rt = .1*BW;%0.1*BW;
%% Channel Gain
N_UE = randi(10,1);
Popt = ones(1,N_UE)*Pmax;
N_RU =  4;
ChannelGain = zeros(N_RU,N_UE);
for i=1:N_RU
    for j=1:N_UE
       distance(i,j)= randi(R,1,1);
       if distance(i,j)==0
           distance(i,j) = randi(R,1,1);
       end
       var_fading = db2pow(10);
       N_Ute = lognrnd(0,var_fading);
       loss(i,j) = N_Ute*1/(distance(i,j)^3.8);
       ChannelGain(i,j) = 100*(loss(i,j)^0.5)/sqrt(2)*(randn(1)+1i*randn(1));
    end
end
RU_UE = zeros(N_RU,N_UE);
for j=1:N_UE
    RU2UE = 0;
    temp = 0;
    for i=1:N_RU
        if abs(ChannelGain(i,j))> abs(temp)
            temp = ChannelGain(i,j);
            RU2UE = i;
        end
    end
    RU_UE(RU2UE,j) = 1;
end
%% UE Admission
rate_UE_min = zeros(1,N_UE);
admission_UE = ones(1,N_UE);
admission_UE1 =  zeros(1,N_UE);
%RU_UE = zeros(N_RU,N_UE);
rate_UE_min = zeros(1,N_UE);
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        for t = 1 : N_UE
            if i~=t 
                Intf(i) = Intf(i) + Popt(t)*abs(ChannelGain(j,i))^2 * (1 - RU_UE(j,i));
            end
        end
        rate_UE_min(i) = rate_UE_min(i) + BW* log2(1 + (Popt(i)/100*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(Intf(i)+BW*N0));
    end
end
C_Fr = sum(rate_UE_min);
Rate_fr_max = ceil(sum(rate_UE_min)*2/3);
[best admission_UE1] = knapsack(ceil(rate_UE_min), admission_UE, Rate_fr_max);
disp(best)
items = find(admission_UE1);
disp(items)
%% RU Association
% rate_UE_min = zeros(1,N_UE);
% Intf = zeros(1,N_UE);
% for i = 1:N_UE
%     for j = 1:N_RU
%         for t = 1 : N_UE
%             if i~=t 
%                 Intf(i) = Intf(i) + Popt(t)*abs(ChannelGain(j,i))^2 * (1 - RU_UE(j,i));
%             end
%         end
%         rate_UE_min(i) = rate_UE_min(i) + BW* log2(1 + (Popt(i)/20*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(Intf(i)+BW*N0));
%     end
% end
%%%%%%%%%% 
C_Fr1 = C_Fr/(N_RU);
Capacity_RU = ones(1, N_RU)*C_Fr1;
Capacity_RU(1) = Capacity_RU(1)*2;
Capacity_RU(2) = Capacity_RU(2)*1.2;
[Sort_rate, I] = sort(rate_UE_min,'descend');
sum(Capacity_RU)
sum(rate_UE_min)
RU_UE = zeros(N_RU,N_UE);
for j = 1:N_RU
    for i = 1:N_UE 
        if Capacity_RU(j)> Sort_rate(i) && sum(RU_UE(:,i))==0 && admission_UE1(i)==1
            Capacity_RU(j) = Capacity_RU(j) - Sort_rate(i);
            RU_UE(j,i) = 1;
        end
    end
end
%% PRB and Power allocation
% cvx_begin
%     variable Popt(1,N_UE)
%     maximize error
%     subject to
%     Prrh(:) <= Pmax;
%     Prrh(:) <= 2^C_thresh * var_q *100;
%     Popt(:) > 0; 
%     Popt(:) < Pmax/10;
%     rate_UE(:) > Rt*1000;  
%     rate_UE(:) >1/(delay_max-mean(Delay_Slice1+Delay_Slice2))
% cvx_end
