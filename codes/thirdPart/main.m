clc
clear all
N_service = 4;
N_server = 3;
Dmax = 100;
Rmax = 120;
N_resource = 1; % cpu, ram, storage
demand_service = rand(N_service,N_resource)*Dmax;
demand_service = sort(demand_service);
resource_server = rand(N_server,N_resource)*Rmax;
resource_server = sort(resource_server);
mappingVar = zeros(N_service, N_server, N_resource);
for i = 1: N_service
    
