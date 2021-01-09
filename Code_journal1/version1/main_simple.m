clear all
clc
%% Varibale
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
%% Rate
rate_UE = zeros(1,N_UE);
admission_UE = zeros(1,N_UE);
RU_UE = zeros(N_RU,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        rate_UE(i) = rate_UE(i) + BW* log2(1 + (Popt(i)*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(BW*N0))*admission_UE(i);
    end
end