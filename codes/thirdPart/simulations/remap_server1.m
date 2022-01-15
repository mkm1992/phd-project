%% remap again for special case 
clear ind10
% disp(sum(resource_server1(:,2:4)))
% disp(sum(demand_service1(:,2:4)))
sum_vector = demand_service1(:,2:4)'*map1;
ind10(1,:) = find(sum_vector(1,:)>0);
%ind10(2,:) = find(sum_vector(2,:)>0);
temp = zeros(1,N_server);
for j= 1: N_server
    if all(sum_vector(:,j)>0)
        temp(j)= 1;
    end
end
i = ind10(1,1);
for j= 1: N_server
    if all(sum_vector(:,i)< resource_server1(j,2:4)') && temp(j)==0
        temp(i) = 0;
        temp(j) = 1;
        for tt =1:N_service
            if map1(tt,i)==1
               map1(tt,j)=1;
               map1(tt,i)=0;
            end
        end
        i = i+1;
        if i> N_server
            break
        end
    end
end    

%  disp(sum_vector)
%  disp(resource_server1(:,2:4)')
