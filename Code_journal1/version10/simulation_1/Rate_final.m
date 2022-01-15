rate_UE_1 = zeros(1,N_UE);
for i = 1:N_UE
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE_1(i) = rate_UE_1(i) + BW* log(1 + (Popt(i)*abs((ChannelGain(:,i))'*beamForming(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
end