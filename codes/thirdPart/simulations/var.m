counter_max = 2000;
N_service_min = 2;
N_service_max = 16;
N_service_step = 3;
lenfinder = N_service_min:N_service_step:N_service_max;
len1 = length(lenfinder);
N_server = 12;
Dmax = [1000, 10, 100];
Rmax = [3000, 30, 300];
N_resource = 3; % cpu, ram, storage
NumServerEnd = zeros(len1,counter_max);
sum_sumVec = zeros(N_resource,len1,counter_max);
sum_ConsResource = zeros(N_resource,len1,counter_max);
sum_ResResource = zeros(N_resource,len1,counter_max);
%%
NumServerEnd1 = zeros(len1,counter_max);
sum_sumVec1 = zeros(N_resource,len1,counter_max);
sum_ConsResource1 = zeros(N_resource,len1,counter_max);
sum_ResResource1 = zeros(N_resource,len1,counter_max);