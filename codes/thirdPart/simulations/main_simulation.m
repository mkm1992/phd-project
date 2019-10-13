clc
clear all
run var
for count = 1: counter_max
    kk = 1;
    for N_service = N_service_min:N_service_step:N_service_max 
        run sort_map
        run moreVM
        run remap_server
        NumServerEnd(kk,count) = sum(temp);
        sum_vector1 = demand_service1(:,2:4)'*mappingVar;
        sum_sumVec(:,kk,count) =  sum(sum_vector1,2);
        sum_ConsResource(:,kk,count) = resource_server1(:,2:4)'*makeone(sum(mappingVar))';
        sum_ResResource(:,kk,count) = resource_server1(:,2:4)'*makeone(sum(mappingVar))';
        kk = kk +1;
   end
end 
meanCons = mean(sum_ConsResource,3);
meanRes = mean(sum_ResResource,3);
meanVec = mean(sum_sumVec,3);
wmeanRes = zeros(1,len1);
wmeanVec = zeros(1,len1);
wmeanCons  = zeros(1,len1);
for i = 1 :N_resource
     wmeanCons = meanCons(i,:)*weight(i) + wmeanCons;
     wmeanVec = meanVec(i,:)*weight(i) + wmeanVec;
     wmeanRes = meanRes(i,:)*weight(i) + wmeanRes;
end
hold on
plot(N_service_min:N_service_step:N_service_max ,mean(NumServerEnd,2))
plot(N_service_min:N_service_step:N_service_max ,wmeanCons)
plot(N_service_min:N_service_step:N_service_max ,wmeanVec)
plot(N_service_min:N_service_step:N_service_max ,wmeanRes)
plot(N_service_min:N_service_step:N_service_max ,wmeanVec./wmeanCons)
plot(N_service_min:N_service_step:N_service_max ,wmeanCons./wmeanVec)