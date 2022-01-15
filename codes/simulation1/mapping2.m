clear prob
%% PUe in snr
Rt = .1*BW;%0.1*BW; 
Popt = ones(1, N_Ut)*Pmax;
C_thresh = 3000*Rt/BW;
%%
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
%%
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
a_e= 0;
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
% Display the optimal solution.
try
res.sol.int
%res.sol.int.xx'
disp(reshape(res.sol.int.xx',N_Slice,N_Service)')
catch
    a_e= 1
fprintf('MSKERROR: Could not get solution')
end
if a_e == 0
    service2slice1 = reshape(res.sol.int.xx',N_Slice,N_Service)';
else
    service2slice1 = service2slice;
end
for i=1:N_Service
   if sum(service2slice1(i,:))==0
       num =  randi([1,N_Slice],1);
       service2slice1(i,num) = 1;
   end
end