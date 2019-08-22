rate_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    for j = 1:N_rrh
        rate_UE(i) =rate_UE(i)+ BW* log2(1 + (Popt(i)*abs((PrecodingMat(j,i)')*ChannelGain(j,i))^2)/(Intf(i)+ BW*N0)).*rrh2Ut(j,i);
    end
    if rate_UE(i)<0
        rate_UE(i) =0;
    end
end



