clc
clear all
close all
clear prob
N_service = 3;
N_server = 2;
Dmax = [1000, 10, 100];
Rmax = [3000, 30, 300];
N_resource = 3; % cpu, ram, storage
demand_service = rand(N_service,N_resource);
resource_server = rand(N_server,N_resource);
demand_service = demand_service.*Dmax; 
resource_server = resource_server.*Rmax;
%%
prob.c = ones(1,N_service*N_server);
prob.a =  [[demand_service',zeros(1,3)];[zeros(1,3),demand_service']];
prob.blc = zeros(1,N_server);
prob.buc = resource_server';
prob.blx = zeros(1,N_service*N_server);
prob.bux = ones(1,N_service*N_server);
% Specify indexes of variables that are integer
% constrained.
prob.ints.sub = 1:N_service*N_server;
[r,res] = mosekopt('minimize',prob);
