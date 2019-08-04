function milo1()
clear prob
N_service = 3;
N_server = 2;
Dmax = 60;
Rmax = 200;
N_resource = 1; % cpu, ram, storage
demand_service = rand(N_service,N_resource)*Dmax;
resource_server = rand(N_server,N_resource)*Rmax;
mappingVar = zeros(N_service, N_server, N_resource);
mappingVar1 = reshape(mappingVar,1,N_service*N_server);
%%
prob.c = ones(1,N_service*N_server);
prob.a =  [repmat(demand_service',N_server)];
prob.blc = zeros(1,N_server);
prob.buc = resource_server';
prob.blx = zeros(1,N_service*N_server);
prob.bux = ones(1,N_service*N_server);
% Specify indexes of variables that are integer
% constrained.
prob.ints.sub = 1:N_service*N_server;
[r,res] = mosekopt('maximize',prob);
try
% Display the optimal solution.
res.sol.int
res.sol.int.xx'
catch
fprintf('MSKERROR: Could not get solution')
end