rate_UE = zeros(1,N_Ut);
P_UE = zeros(1,N_Ut);
eta_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    for j = 1:N_rrh
        P_UE(i) =  P_UE(i) + rrh2Ut(j,i).*Popt(i)*abs((PrecodingMat(j,i)')*ChannelGain(j,i))^2;
        rate_UE(i) =rate_UE(i)+ BW* log2(1 + (rrh2Ut(j,i).*Popt(i)*abs((PrecodingMat(j,i)')*ChannelGain(j,i))^2)/(Intf(i)+ BW*N0));
    end
    eta_UE(i) = P_UE(i)- (Intf(i)+ BW*N0)*(exp(Rt/BW)-1);
end



