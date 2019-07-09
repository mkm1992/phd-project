clc
clear all
N_service = 4;
N_server = 3;
Dmax = 100;
Rmax = 120;
N_resource = 1; % cpu, ram, storage
demand_service = rand(N_service,N_resource)*Dmax;
resource_server = rand(N_server,N_resource)*Rmax;
mappingVar = zeros(N_service, N_server, N_resource);