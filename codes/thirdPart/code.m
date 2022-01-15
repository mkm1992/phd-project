%% Mosek Optimazation for Source Allocation

close all; clear; clc;

%% Parameter Initialization

Num_Server = 2; Num_Service = 3; Num_Resource = 3; D_Max = 10; R_Max = 15;
Service_Pow = D_Max * rand(Num_Resource, Num_Service);
Server_Pow = R_Max * rand(Num_Resource, Num_Server);
Phi = reshape(4 * rand(Num_Resource, Num_Server * Num_Service),[1, Num_Resource * Num_Service * Num_Server]);
p = repmat(Service_Pow,1,Num_Server);

%% Optimization Structure

temp = p .* ones(Num_Resource,Num_Service * Num_Server);
temp = reshape(temp,[1,Num_Resource * Num_Service * Num_Server]);

F = zeros(Num_Server * Num_Resource, Num_Server * Num_Service * Num_Resource);

for i = 1: Num_Server * Num_Resource
    for j = 1: Num_Service
        F(i,(Num_Service)*(i-1) + j) = temp((Num_Server-1)*i + j);
    end
end

G = zeros(Num_Server * Num_Resource, Num_Server * Num_Service * Num_Resource);

for i = 1: Num_Server * Num_Resource
    for j = 1: Num_Service
        G(i,(Num_Service)*(i-1) + j) = 1;
    end
end

%% Probelm Structure

Prob.c = ones(1, Num_Service * Num_Server * Num_Resource); % Phi is avoidable
Prob.a = [G ; F];
Prob.blc = zeros(1,2 * ( Num_Resource * Num_Server) ).';
Prob.buc = [ones(1,(Num_Resource * Num_Server)) reshape(Server_Pow,[1,Num_Resource * Num_Server]) ].';
Prob.blx = zeros(1, Num_Resource * Num_Service * Num_Server);
Prob.bux = ones(1, Num_Resource * Num_Service * Num_Server);
Prob.ints.sub = 1: Num_Server * Num_Service * Num_Resource ;
%% Solution

[r, res] = mosekopt('maximize',Prob);

transpose(res.sol.int.xx)
sum(res.sol.int.xx)

%%
