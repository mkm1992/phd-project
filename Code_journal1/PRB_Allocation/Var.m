%% Initial Variable
R = 500;
S = 1;
BW = 120*1e3; %10*1e6;  
n0 = -174; %-174 dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rmin = .1*BW;
Rate_mid_max = 2*BW;
%% 
N_PRB = 8;
T_max = 50e-3; % sec
N_UE = 10;
N_RU = 4;
counter_max = 10;
ChannelGain =  zeros(N_RU ,N_UE);
RU_UE = zeros(N_RU ,N_UE);
%% 
Popt = zeros(1,N_UE);