

rate_UE = (zeros(1,N_UE));

for i = 1:N_UE
    %for j = 1:N_RU
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE(i) = rate_UE(i) + BW* log(1 + (Popt(i)*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
    %end
end

R_s = (zeros(1,S));
t = 0;
for s = 1:S
    for j = 1:UE_S(s)
        t = t+1;
        R_s(s) = R_s(s) + rate_UE(t);
    end
end