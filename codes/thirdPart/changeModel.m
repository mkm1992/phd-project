weight = [1, 100, 10];
demand_service1 = sorting(demand_service, N_resource, weight, N_service);
resource_server1 = sorting(resource_server, N_resource, weight, N_server);
%% mapping
mappingVar1 = zeros(N_service, N_server);
i = N_service;
mapStatus = ones(1,N_service);
resourceShare = resource_server1(:,2:4);
for j = N_server:-1:1
    for i = N_service:-1:1
        if mapStatus(i)==1
            rs = resourceShare(j,:)-demand_service1(i,2:4);
            if all(rs >= 0) 
                mappingVar1(i,j) = 1;
                mapStatus(i) = 0;
                resourceShare(j,:) = resourceShare(j,:)-demand_service1(i,2:4);
            end
        end
    end
end
%% if service need more than one VM
 %mapStatus = sum(mappingVar,2);
 index_notMap = find(mapStatus == 1);
 remain_source = sorting(resourceShare, N_resource, weight, N_server);
 resourceShare1 = remain_source(:,2:4);
 demand_service2= demand_service1(:,2:4);
 for i=index_notMap
    for j = N_server:-1:1
        demand_service2(i,:) = -resourceShare1(j,:)+ demand_service2(i,:);
        indMap = find(resourceShare1(j,1)==resourceShare(:,1));
        mappingVar1(i,indMap) = 1;
        if all(demand_service2(i,:) <= 0)
            j = 0;
            break;
        end
        
    end
 end

%% remap again for special case 
disp(sum(resource_server1(:,2:4)))
disp(sum(demand_service1(:,2:4)))
sum_vector = demand_service1(:,2:4)'*mappingVar1;
ind1(1,:) = find(sum_vector(1,:)>0);
ind1(2,:) = find(sum_vector(2,:)>0);
temp1 = zeros(1,N_server);
for j= 1: N_server
    if all(sum_vector(:,j)>0)
        temp1(j)= 1;
    end
end
i = ind1(1,1);
for j= 1: N_server
    if all(sum_vector(:,i)< resource_server1(j,2:4)') && temp1(j)==0
        temp1(i) = 0;
        temp1(j) = 1;
        i = i+1;
    end
end    

 disp(sum_vector)
 disp(resource_server1(:,2:4)')
