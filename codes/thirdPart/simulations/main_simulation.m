clc
clear all
clear prob
run var
for count = 1: counter_max
    kk = 1;
    for N_service = N_service_min:N_service_step:N_service_max 
        %N_server = ceil(N_service * 1.2);
        run sort_map
        %run moreVM
        %run remap_server
        %%
        sum_vector = demand_service1(:,2:4)'*mappingVar;
        temp = zeros(1,N_server);
        for j= 1: N_server
            if all(sum_vector(:,j)>0)
                temp(j)= 1;
            end
        end
        
        %%
        NumService(kk,count) = sum(sum(mappingVar));
        NumServerEnd(kk,count) = sum(temp);
        sum_vector1 = demand_service1(:,2:4)'*mappingVar;
        sum_sumVec(:,kk,count) =  sum(sum_vector1,2);
        sum_ConsResource(:,kk,count) = resource_server1(:,2:4)'*makeone(sum(mappingVar))';
        sum_ResResource(:,kk,count) = resource_server1(:,2:4)'*(1-makeone(sum(mappingVar))');
        run mosekRun
        NumServerEnd1(kk,count) = sum(mapvec(1:N_service*N_server));
        sum_vector12 = demand_service'*map1;
        sum_sumVec1(:,kk,count) =  sum(sum_vector12,2);
        sum_ConsResource1(:,kk,count) = resource_server'*makeone(sum(map1))';
        sum_ResResource1(:,kk,count) = resource_server'*(1-makeone(sum(map1))');
        NumService1(kk,count) = sum(sum(map1));
        
        kk = kk +1;
    end
   disp('hhhhhhhh')
   count
end 
%%
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
%%
meanCons1 = mean(sum_ConsResource1,3);
meanRes1 = mean(sum_ResResource1,3);
meanVec1 = mean(sum_sumVec1,3);
wmeanRes1 = zeros(1,len1);
wmeanVec1 = zeros(1,len1);
wmeanCons1  = zeros(1,len1);
for i = 1 :N_resource
     wmeanCons1 = meanCons1(i,:)*weight(i) + wmeanCons1;
     wmeanVec1 = meanVec1(i,:)*weight(i) + wmeanVec1;
     wmeanRes1 = meanRes1(i,:)*weight(i) + wmeanRes1;
end
%%
xx = N_service_min:N_service_step:N_service_max;
figure;
plot(N_service_min:N_service_step:N_service_max ,mean(NumService,2)./xx')
hold on
plot(N_service_min:N_service_step:N_service_max ,mean(NumService1,2)./xx')
% figure;
% plot(N_service_min:N_service_step:N_service_max ,mean(NumServerEnd,2))
% hold on
% plot(N_service_min:N_service_step:N_service_max ,mean(NumServerEnd1,2))
% figure;
% plot(N_service_min:N_service_step:N_service_max ,wmeanCons)
% hold on
% plot(N_service_min:N_service_step:N_service_max ,wmeanCons1)
% figure;
% plot(N_service_min:N_service_step:N_service_max ,wmeanVec)
% hold on
% plot(N_service_min:N_service_step:N_service_max ,wmeanVec1)
% figure;
% plot(N_service_min:N_service_step:N_service_max ,wmeanRes)
% hold on
% plot(N_service_min:N_service_step:N_service_max ,wmeanRes1)
% figure;
% plot(N_service_min:N_service_step:N_service_max ,wmeanVec./(wmeanCons+wmeanRes))
% hold on
% plot(N_service_min:N_service_step:N_service_max ,wmeanVec1./(wmeanCons1+wmeanRes1))
% figure;
% plot(N_service_min:N_service_step:N_service_max ,wmeanCons./wmeanVec)
% hold on
% plot(N_service_min:N_service_step:N_service_max ,wmeanCons1./wmeanVec1)