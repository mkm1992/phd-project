%% Initial Variable
R = 500;
S = 3;
BW = 180*1e3; %10*1e6;  
n0 = -174; %-174 dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 30;
Pmax = db2pow(Pt)/1000;
Rmin1 =  [60000 ,90000 ,12000];%.1*BW*randi([1,5],1,S); %.1*BW*ones(1,S)
[Rmin, I] = sort(Rmin1,'descend');
Rate_mid_max = [600000,420000,50000];%0.5*BW*randi([1,10],1,S);
var_q = 1e-6;
alpha_s = .1*BW;
%delay_max = 3e-5*randi([1,20],1,S);
delay_max = [1e-3, 5e-3, 7e-3];
%mu = 1e9.*[1.5, 3, 5];%Rmin .* randi([500,520],1,S)/1000;
mu = [7734000, 8250000, 1808400]/10;%Rmin .* randi([1200,1520],1,S)/10;
%alpha_m  =10e8.*[0.1, 0.5, 1]; %Rmin .* randi([485,499],1,S)/1000;
%lambda_m = 1e6*ones(1,S);
lambda_m = [2994000, 2922000, 598800]/10;%Rmin .* randi([485,499],1,S)/10;
%C_thresh = 3000*Rt/BW;
%% 
T_max = 50e-5*randi([1,10],1,S); % sec
Delay_Slice = zeros(1,S);
VNF_NUM =  zeros(1,S);
N_UE_max = 10;
N_RU = 4;
counter_max = 5;
M_max = 10; %max number of vnf
%%
C_tot_RU = sum(Rate_mid_max);
Capacity_RU = [160500, 288900, 502900, 449400];%C_tot_RU * randi([10,50],1,N_RU)/100;
N_Antenna = 1;
%P_RU = zeros(1,N_RU);
%% changable variable
N_PRB = 20;

%RU_PRB = randi([0 1],N_RU,N_PRB);
%PRB_UE = randi([0,1],N_PRB,N_UE);%zeros(N_PRB, N_UE);