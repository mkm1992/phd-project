clc
clear all
N_service = 4;
N_server = 3;
Dmax = 100;
Rmax = 150;
N_resource = 1; % cpu, ram, storage
demand_service = rand(N_service,N_resource)*Dmax;
demand_service = sort(demand_service);
resource_server = rand(N_server,N_resource)*Rmax;
resource_server = sort(resource_server);
mappingVar = zeros(N_service, N_server, N_resource);
j = N_server;
resourceShare = resource_server;
for i =  N_service:-1:1
    resourceShare(j)= resourceShare(j)-demand_service(i);
    if resourceShare(j)<0 
        j = j -1;
    end
    if j>0
        mappingVar(i,j) = 1;
    end
end


    
    
