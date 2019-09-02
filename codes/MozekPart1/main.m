function milo1()
clear prob
%%
R = 500;
N_Service = 2;
NumOfUtInService = randi([1 10],1, N_Service);
N_Ut = sum(NumOfUtInService);
N_Slice =  2;
N_rrh = 2;
BW = 120*1e3;  
n0 = -174; %dbm
N0 = db2pow(n0)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rt = .1*BW;%0.1*BW; 
Popt = ones(1, N_Ut)*Pmax/N_Ut;
%% ut to service
k = 1;
Ut2Service = zeros(sum(NumOfUtInService),N_Service);
for i=1:N_Service
    Ut2Service(k:k+NumOfUtInService(i)-1,i) = 1;
    k = k+NumOfUtInService(i);
end
%% rrh 2 slice
rrh2slice = zeros(N_rrh, N_Slice);
num_map = 0;
while any(sum(rrh2slice,1)<1) || any(sum(rrh2slice,2)<1)
    rrh2slice = randi([0 1],N_rrh, N_Slice);
    num_map = num_map+1;
    if num_map >10
        rrh2slice = ones(N_rrh, N_Slice);
    end
end
%% channel 
ChannelGain = zeros(N_rrh,N_Ut);
for i=1:N_rrh
    for j=1:N_Ut
       distance(i,j)= randi(R,1,1);
       if distance(i,j)==0
           distance(i,j) = randi(R,1,1);
       end
       var_fading = db2pow(10);
       N_Ute = lognrnd(0,var_fading);
       loss(i,j) = N_Ute*1/(distance(i,j)^3.8);
       ChannelGain(i,j) = (loss(i,j)^0.5)/sqrt(2)*(randn(1)+1i*randn(1));
    end
end
%% precoding
PrecodingMat = zeros(N_rrh,N_Ut);
for i=1:N_Ut
    g = ChannelGain(:,i);
    PrecodingMat(:,i) = conj(g)/norm(g);
end
ro = 0;
%v = H*(H'*H+ro*eye(K*S))^(-1);
PrecodingMat(:,:) = PrecodingMat(:,:)/norm(PrecodingMat(:,:));
%% 

P_UE = zeros(N_Ut, N_Slice, N_Service);
eta_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    for j = 1:N_rrh
        for t = 1:N_Slice
            for z = 1:N_Service
                P_UE(i,t,z) =  P_UE(i,t,z) +Ut2Service(i,z)* rrh2slice(j,t)*Popt(i)*abs((PrecodingMat(j,i)')*ChannelGain(j,i))^2;
            end
        end
    end
    eta_UE(i) = P_UE(i)- (BW*N0)*(exp(Rt/BW)-1);
end
%%
P_UE1 = reshape(P_UE,N_Ut,N_Slice*N_Service);
%%
sumR = sum(P_UE,1);
sumR =permute(sumR,[2,3,1]);
sumR_reshaped = reshape(sumR,1,N_Slice*N_Service);
prob.c = sumR_reshaped;
prob.a =  P_UE1;
prob.blc = (BW*N0)*(exp(Rt/BW)-1)*ones(1,N_Ut)*1000;
prob.buc = inf*ones(1,N_Ut);
prob.blx = zeros(1,N_Service*N_Slice);
prob.bux = ones(1,N_Service*N_Slice);
% Specify indexes of variables that are integer
% constrained.
prob.ints.sub = 1:N_Service*N_Slice;
[r,res] = mosekopt('maximize',prob);
try
% Display the optimal solution.
res.sol.int
res.sol.int.xx'
catch
fprintf('MSKERROR: Could not get solution')
end