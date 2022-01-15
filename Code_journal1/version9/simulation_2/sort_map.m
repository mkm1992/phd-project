demand_service = rand(N_service,N_resource);
resource_server = rand(N_server,N_resource);
demand_service = demand_service.*Dmax; 
resource_server = resource_server.*Rmax;
%% sort variables
weight = [1, 100, 10];
demand_service1 = sorting(demand_service, N_resource, weight, N_service);
resource_server1 = sorting(resource_server, N_resource, weight, N_server);
%% mapping
mappingVar = zeros(N_service, N_server);
i = N_service;
mapStatus = ones(1,N_service);
resourceShare = resource_server1(:,2:4);
for j = N_server:-1:1
    for i = 1:N_service
        if mapStatus(i)==1
            rs = resourceShare(j,:)-demand_service1(i,2:4);
            if all(rs >= 0) 
                mappingVar(i,j) = 1;
                mapStatus(i) = 0;
                resourceShare(j,:) = resourceShare(j,:)-demand_service1(i,2:4);
            end
        end
    end
end