rate_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    rate_UE(i) = BW* log2(1 + (Popt(i)*abs((PrecodingMat(:,i)')*(ChannelGain(:,i).*rrh2Ut(:,i)))^2)/(Intf(i)/1e1+ BW*N0));
end
