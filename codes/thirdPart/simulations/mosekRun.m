clear prob
G = zeros(N_service , N_server * N_service+N_server );
G1 = zeros(N_service , N_server * N_service + +N_server, N_resource);
for i = 1: N_service 
    for j = 1: N_server
        G(i,(N_server)*(i-1) + j) = 1;
        G1(i,(N_server)*(i-1) + j,:) = demand_service(i,:);
    end
end
%%
F = zeros(N_server*N_resource , (N_server * N_service) +N_server );
deman_n = repmat(demand_service',N_server');
for i = 1: N_server 
    for j = 1:  N_server * N_service
        if mod(j,N_server)== mod(i,N_server)
            F((i-1)*(N_resource)+1:i*N_resource,j)=1;
        end

    end
end
F1 = F;
F1(:,1:end-N_server) = F(:,1:end-N_server).*deman_n;
Res = zeros(1,N_server*N_resource);
k =1;
for i = 1: N_server 
    for tt=1:N_resource
       Res(k) = resource_server(i,tt);
       k = k+1;
    end
end
%%
T = zeros(N_server, (N_server * N_service) +N_server );
for i=1:N_server
   T(i,end-N_server+i) =1; 
   for j = 1:  N_server * N_service
        if mod(j,N_server)== mod(i,N_server)
            T(i,j)=-1/10;
        end

    end
end
%%
prob.c = [ones(1,N_service*N_server),-1*ones(1, N_server)];
prob.a =  [G;F1;T];
prob.blc = [zeros(1,N_service),zeros(1,N_server*N_resource),zeros(1,N_server)];
prob.buc = [ones(1,N_service)*2,Res,ones(1,N_server)];
prob.blx = zeros(1,N_service*N_server+N_server);
prob.bux = ones(1,N_service*N_server++N_server);
% Specify indexes of variables that are integer
% constrained.
prob.ints.sub = 1:N_service*N_server+N_server;

data.maxtime = 10.0;
callback.iterhandle = data;
[r,res] = mosekopt('maximize',prob,[],callback);
mapvec = transpose(res.sol.int.xx);
%sum(res.sol.int.xx)
mapMat = reshape(mapvec(1:N_service*N_server),N_server',N_service);
map1 = mapMat';