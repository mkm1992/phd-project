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
        mappingVar(i,indMap) = 1;
        if all(demand_service2(i,:) <= 0)
            j = 0;
            break;
        end
        
    end
 end