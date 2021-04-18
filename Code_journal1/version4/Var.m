%% Initial Variable
R = 500;
S = 3;
BW = 120*1e3; %10*1e6;  
n0 = -174; %-174 dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 25;
Pmax = db2pow(Pt)/1000;
Rmin1 = 1*BW*randi([1,10],1,S);
[Rmin, I] = sort(Rmin1,'descend');
Rate_mid_max = BW*randi([6,10],1,S);
%% 
T_max = 50e-3*randi([1,10],1,S); % sec
N_UE_max = 10;
N_RU = 4;
counter_max = 10;
%%
C_tot_RU = sum(Rate_mid_max);
Capacity_RU = C_tot_RU * randi([10,50],1,N_RU)/100;
N_Antenna = 1;
%P_RU = zeros(1,N_RU);
%% changable variable
UE_S = randi(N_UE_max,1,S);
N_UE = sum(UE_S);
RU_UE = zeros(N_RU,N_UE);
%Popt = ones(1,N_UE)*Pmax;
Rmin_UE = zeros(1,N_UE);
t = 0;
for i = 1:S
    for j = 1:UE_S(i)
        t = t+1;
        Rmin_UE(t) = Rmin(i);
    end
end
N_PRB = 6;
%RU_PRB = randi([0 1],N_RU,N_PRB);
%PRB_UE = randi([0,1],N_PRB,N_UE);%zeros(N_PRB, N_UE);