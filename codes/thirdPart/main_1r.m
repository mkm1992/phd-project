clc
clear all
N_service = 10;
N_server = 7;
Dmax = 100;
Rmax = 200;
N_resource = 1; % cpu, ram, storage
demand_service = rand(N_service,N_resource)*Dmax;
demand_service = sort(demand_service);
resource_server = rand(N_server,N_resource)*Rmax;
resource_server = sort(resource_server);
mappingVar = zeros(N_service, N_server, N_resource);
i = N_service;
i1 = ones(1,N_service);
resourceShare = resource_server;
for j = N_server:-1:1
    for i = N_service:-1:1
        if i1(i)==1
            rs = resourceShare(j)-demand_service(i);
            if rs >= 0
                mappingVar(i,j) = 1;
                i1(i) = 0;
                resourceShare(j) = resourceShare(j)-demand_service(i);
            end
        end
    end
end
disp(sum(resource_server))
disp(sum(demand_service))
sum_vector = demand_service'*mappingVar;
ind = find(sum_vector>0);

temp = zeros(1,N_server);
for j= 1: N_server
    if sum_vector(j)>0
        temp(j)= 1;
    end
end
i = ind(1);
for j= 1: N_server
    if sum_vector(i)< resource_server(j) & temp(j)==0
        temp(i) = 0;
        temp(j) = 1;
        i = i+1;
    end
end    

sum_vector
resource_server'