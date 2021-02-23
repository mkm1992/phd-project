%% obtain rate for UE
%Intf = zeros(1,N_UE);
rate_UE = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        for z = 1:N_PRB
            rate_UE(i) = rate_UE(i) + BW* log2(1 + (Popt(i)*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(Intf(i)+BW*N0))*PRB_UE(z,i)*admission_UE1(i);
        end
    end
end