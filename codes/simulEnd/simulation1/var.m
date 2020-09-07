%% Physical layer
R = 500;
%N_Service = 5;
N_Slice =  30;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 30;
Pmax = 10*db2pow(Pt)/1000;
Rt =.01*BW;% .1*BW;%0.1*BW; 
N_PRB = 12;
N_rrh = 30;
N_var = 2;
imax = 1;
NumOfUtInService =N_var*ones(1,N_Service);%randi([1 10],1, N_Service); 
N_Ut = sum(NumOfUtInService);
rrh2slice = randi([0 imax],N_rrh, N_Slice); %not map 1 -->true 
service2slice = zeros(N_Service, N_Slice);    %randi([0 imax],N_Service, N_Slice); %2 we want to find this!!!!!
Ut2Service = zeros(sum(NumOfUtInService),N_Service); %3 -->true
PRB2Slice = randi([0 imax],N_PRB, N_Slice); %4 
Ut_map = zeros(N_Ut, N_PRB);  % map it
Popt = ones(1, N_Ut)*Pmax/N_Ut;
N_BBU = 2;
BBU_map = zeros(N_BBU, N_Slice);
Crrh = zeros(1, N_rrh);
Prrh = zeros(1,N_rrh);
var_q = 1e-6;
C_thresh = 3000*Rt/BW;
%% VNF MAC LAYER
N_VNF1 = 10;
VNF2Slice1 = randi([0 imax],N_VNF1, N_Slice); %5
N_VNF2 = N_VNF1;
VNF2Slice2 = randi([0 imax],N_VNF2, N_Slice); %6
mu1 = 10* Rt;
alpha_m1  = Rt;
mu2 = 10* Rt;
alpha_m2  = Rt;
lamda = Rt/10000;
delay_thresh = 9.2593e-06;
Delay_Slice1 = zeros(N_Slice,1);
Delay_Slice2 = zeros(N_Slice,1);
Delay_Transmission = zeros(N_Slice,1);
delay_max = 1e-4;
priority_service = ones(1,N_Service);
Delay_Slice = zeros(1,N_Slice);