function milo1()
clear prob
%% variables
R = 500;
N_Service = 2;
N_Slice =  3;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rt = .1*BW;%0.1*BW; 
N_PRB = 8;
N_rrh = 3;
imax = 1;
NumOfUtInService = randi([1 3],1, N_Service);
N_Ut = sum(NumOfUtInService);
rrh2slice = randi([0 imax],N_rrh, N_Slice); %not map 1 -->true 
service2slice = zeros(N_Service, N_Slice);    %randi([0 imax],N_Service, N_Slice); %2 we want to find this!!!!!
Ut2Service = zeros(sum(NumOfUtInService),N_Service); %3 -->true
PRB2Slice = randi([0 imax],N_PRB, N_Slice); %4 
Ut_map = zeros(N_Ut, N_PRB);  % map it
Popt = ones(1, N_Ut)*Pmax/N_Ut;
iter_max =1;
N_BBU = 2;
BBU_map = zeros(N_BBU, N_Slice);
Crrh = zeros(1, N_rrh);
Prrh = zeros(1,N_rrh);
var_q = 1e-5;
C_thresh = 10*Rt;
% VNF MAC LAYER
N_VNF1 = 10;
VNF2Slice1 = randi([0 imax],N_VNF1, N_Slice); %5
N_VNF2 = 10;
VNF2Slice2 = randi([0 imax],N_VNF2, N_Slice); %6
mu1 = 10* Rt;
alpha_m1  = Rt;
mu2 = 10* Rt;
alpha_m2  = Rt;
lamda = Rt/10000;
delay_thresh = 9.2593e-06;
Delay_Slice1 = zeros(N_Slice,1);
Delay_Slice2 = zeros(N_Slice,1);
Delay_Transmission = zeros(N_Slice,1);
delay_max = 3e-4;
priority_service = ones(1,N_Service);
Delay_Slice = zeros(1,N_Slice);
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

    
%% mappingOtherParameter 
% map rrh 2 slice
rrh2slice = randi([0 imax],N_rrh, N_Slice);
num_map = 0;
while any(sum(rrh2slice,1)<1) || any(sum(rrh2slice,2)<1)
    rrh2slice = randi([0 imax],N_rrh, N_Slice);
    num_map = num_map+1;
    if num_map >10
        rrh2slice = ones(N_rrh, N_Slice);
    end
end
%  map ut 2 service
k = 1;
Ut2Service = zeros(sum(NumOfUtInService),N_Service);
for i=1:N_Service
    Ut2Service(k:k+NumOfUtInService(i)-1,i) = 1;
    k = k+NumOfUtInService(i);
end
% map PRB to Slice
PRB2Slice = randi([0 imax],N_PRB, N_Slice);
num_map = 0;
while any(sum(PRB2Slice,1)<1) || any(sum(PRB2Slice,2)<1)
    PRB2Slice = randi([0 imax],N_PRB, N_Slice);
    num_map = num_map+1;
    if num_map >10
        PRB2Slice = ones(N_PRB, N_Slice);
    end
end
%% MapPRB2UT
for j = 1:N_Ut
    numberPRB = randi([1 N_PRB],1, 1);
    Ut_map(j,numberPRB) =1;
end
%%
Intf = zeros(N_Ut,1);
rrh2ut1 = rrh2slice *transpose(service2slice)*transpose(Ut2Service);
rrh2Ut = rrh2ut1;% modifiedMat(rrh2ut1);
for i = 1: N_Ut
    if sum(rrh2Ut(:,i)) > 0
        Intf(i) = Intf(i) + var_q*abs((ChannelGain(:,i)')*ChannelGain(:,i));
        for j = 1:N_PRB
            if Ut_map(i,j)==1 
                for t = 1 : N_Ut
                    if i~=t && Ut_map(t,j)==1 && sum(rrh2Ut(:,t)) > 0
                        Intf(i) = Intf(i) + Popt(t)*abs((PrecodingMat(:,t)')*(ChannelGain(:,t).*rrh2Ut(:,t)))^2;
                    end
                end
            end
        end
    end
end

%%
run rate
run FronthaulCap
run FindDelay
prob.c = ones(1,N_Service*N_Slice);
prob.a =  [[demand_service',zeros(1,3)];[zeros(1,3),demand_service']];
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