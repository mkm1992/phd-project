rate_UE = zeros(1,N_Ut);
for i = 1:N_Ut
    rate_UE(i) = BW* log2(1 + (Popt(i)*abs((PrecodingMat(:,i)')*ChannelGain(:,i))^2)/(Intf(i)+ BW*N0));
    if rate_UE<0
        rate_UE =0;
    end
end
