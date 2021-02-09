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
Rmin = .1*BW* ones(1,S); 

%% 
N_PRB = 24;
N_RU = 4;
T_max = 50e-3; % sec
N_UE_max = 10;
UE_S = randi(N_UE_max,1,S);
N_UE = sum(UE_S);
N_RU = 4;
ChannelGain = zeros(N_RU,N_UE);
RU_UE = zeros(N_RU,N_UE);
N_Antenna = 1;