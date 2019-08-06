R = 500;
N_Service = 2;
N_Slice =  2;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rt = .1*BW;%0.1*BW; 
N_PRB = 8;
N_Ut = 10;
N_rrh = 3;
rrh2slice = zeros(N_rrh, N_Slice);
service2slice = zeros(N_Service, N_Slice);
Ut2Service = zeros(N_Ut, N_Service);
Ut_map = zeros(N_Ut, N_PRB);
rate = zeros(1, N_Ut);
Popt = zeros(1, N_Ut);
iter_max =10;
N_BBU = 2;
BBU_map = zeros(N_BBU, N_Slice);
Copt = zeros(N_BBU, N_rrh);
%%

