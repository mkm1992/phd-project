% Physical layer introduce variable
%% Initial Variable
R = 500;
S = 2;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rmin = .2*BW*randi([1,10],1,S);
Rate_mid_max = BW*randi([1,10],1,S);
%% 
N_PRB = 24;
T_max = 50e-3; % sec
N_UE_max = 10;
N_RU = 4;
%%
Capacity_RU = zeros(1,N_RU);
C_tot_RU = sum(Rate_mid_max);
Capacity_RU = C_tot_RU * randi([20,70],1,4)/100;
% C_Fr1 = Rate_mid_max *randi(100)/100;
% Capacity_RU = C_Fr1;
% Capacity_RU(1) = Capacity_RU(1)*2;
% Capacity_RU(2) = Capacity_RU(2)*1.2;
N_Antenna = 1;