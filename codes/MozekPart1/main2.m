function milo1()
clear prob
%%
R = 500;
N_Service = 2;
NumOfUtInService = randi([1 10],1, N_Service);
N_Ut = sum(NumOfUtInService);
N_Slice =  2;
N_rrh = 4;
BW = 120*1e3;  
N_PRB = 100;
n0 = -174; %dbm
N0 = db2pow(n0)/1000;
Pt = 30;
Pmax = db2pow(Pt)/1000;
Rt = .01*BW;%0.1*BW; 
Popt = ones(1, N_Ut)*Pmax;
var_q = 1e-8;
C_thresh = 3000*Rt/BW;
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
%% PRB 2 Slice
PRB2Slice = randi([0 1],N_PRB, N_Slice);
num_map = 0;
while any(sum(PRB2Slice,1)<1) || any(sum(PRB2Slice,2)<1)
    PRB2Slice = randi([0 1],N_PRB, N_Slice);
    num_map = num_map+1;
    if num_map >10
        PRB2Slice = ones(N_PRB, N_Slice);
    end
end
%%
Ut_map = zeros(N_Ut, N_PRB);
for i =1:N_Ut
    if mod(i,N_PRB)==0
       Ut_map(i,N_PRB)= 1;
    else
        Ut_map(i,mod(i,N_PRB)) =1 ;
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
%% PUe in snr
P_UE = zeros(N_Ut, N_Slice, N_Service);
%eta_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    for j = 1:N_rrh
        for t = 1:N_Slice
            for z = 1:N_Service
                P_UE(i,t,z) =  P_UE(i,t,z) +Ut2Service(i,z)* rrh2slice(j,t)*Popt(i)*abs((PrecodingMat(j,i)')*ChannelGain(j,i))^2;
            end
        end
    end
    %eta_UE(i) = P_UE(i)- (BW*N0)*(exp(Rt/BW)-1);
end
%% prrh & crrh
P_rrh = zeros(N_rrh, N_Slice, N_Service);
SNR_rrh = zeros(N_rrh, N_Slice, N_Service);
for j = 1:N_rrh
    for i = 1:N_Ut
        for t = 1:N_Slice
            for z = 1:N_Service
                P_rrh(j,t,z) =  P_rrh(j,t,z) +Ut2Service(i,z)* rrh2slice(j,t)*(Popt(i)*abs(PrecodingMat(j,i))^2);
                SNR_rrh(j,t,z) =  SNR_rrh(j,t,z) +Ut2Service(i,z)* rrh2slice(j,t)*(Popt(i)*abs(PrecodingMat(j,i))^2)/var_q;
            end
        end
    end
end
%% interference 1
Intf1 = zeros(N_Ut, N_Slice, N_Service);
for tt = 1:N_Slice
    for z = 1:N_Service
        for i = 1: N_Ut
            for rr =1:N_rrh
                Intf1(i,tt,z) = Intf1(i,tt,z) + var_q*abs((ChannelGain(rr,i)')*ChannelGain(rr,i))*Ut2Service(i,z)*rrh2slice(rr,tt);
            end
        end
    end
end
%% interference 2
Intf2 = zeros(N_Ut, N_Slice, N_Service);
for tt = 1:N_Slice
    for z = 1:N_Service
        for i = 1: N_Ut
            for rr =1:N_rrh
                for ii =1:N_Ut
                    ind_prb = find(Ut_map(i,:)==1);
                    if i~=ii && Ut_map(ii,ind_prb)==1
                        Intf2(i,tt,z) = Intf2(i,tt,z) +  Popt(ii)*abs((PrecodingMat(rr,ii)')*(ChannelGain(rr,ii)))^2*Ut2Service(i,z)*rrh2slice(rr,tt);
                    end
                end
            end
        end
    end
end
%% Delay initialize
delay_thresh = 9.2593e-06;
Delay_Slice1 = zeros(N_Slice,1);
Delay_Slice2 = zeros(N_Slice,1);
Delay_Transmission = zeros(N_Slice,N_Service);
delay_max = 3e-4;
Delay_Slice = zeros(1,N_Slice);
N_VNF1 = 10;
VNF2Slice1 = randi([0 1],N_VNF1, N_Slice); %5
N_VNF2 = 10;
VNF2Slice2 = randi([0 1],N_VNF2, N_Slice); %6
mu1 = 10* Rt;
alpha_m1  = Rt;
mu2 = 10* Rt;
alpha_m2  = Rt;
lamda = Rt/10000;
%% Delay finder
for i = 1:N_Slice
 Delay_Slice1(i) = 1/(mu1- alpha_m1/sum(VNF2Slice1(:,i)));
 Delay_Slice2(i) =  1/(mu2- alpha_m2/sum(VNF2Slice2(:,i)));
end

Delay_Slice = Delay_Slice1 + Delay_Slice2;
%%
Intf11 = reshape(Intf1,N_Ut,N_Slice*N_Service);
Intf22 = reshape(Intf2,N_Ut,N_Slice*N_Service);
P_UE1 = reshape(P_UE,N_Ut,N_Slice*N_Service);
P_rrh1 = reshape(P_rrh,N_rrh, N_Slice*N_Service);
SNR_rrh1 = reshape(SNR_rrh,N_rrh, N_Slice*N_Service);
%%
q1 = zeros(N_Service, N_Slice*N_Service);
for i=1:N_Service
    q1(i,(i-1)*N_Slice+1:i*N_Slice)=1;
end
q2 = zeros(N_Slice, N_Slice*N_Service);
for i=1:N_Slice
    for j =1:N_Slice*N_Service
        if mod(j,N_Slice)==i
            q2(i,j)=1;
        end
        if mod(j,N_Slice)==0
            q2(N_Slice,j)=1;
        end
    end
end
%%
sumR = sum(P_UE,1);
sumR =permute(sumR,[2,3,1]);
sumR_reshaped = reshape(sumR,1,N_Slice*N_Service);
prob.c = sumR_reshaped;
prob.a =  [P_UE1-(Intf11+Intf22)*(2^(Rt/BW)-1); P_rrh1;SNR_rrh1;P_UE1-(Intf11+Intf22+BW*N0)*(2^(min(Delay_Slice)+lamda)-1);q1;q2];
prob.blc = [(BW*N0)*(2^(Rt/BW)-1)*ones(1,N_Ut)*1000, zeros(1,N_rrh), zeros(1,N_rrh),zeros(1,N_Ut),zeros(1,N_Service),zeros(1,N_Slice)];
prob.buc = [inf*ones(1,N_Ut), Pmax*ones(1,N_rrh)-var_q, 2^(C_thresh-1)*ones(1,N_rrh),inf*ones(1,N_Ut),ones(1,N_Service),ones(1,N_Slice)];
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