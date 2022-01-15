rate_UE_min =  zeros(1,N_UE);
Intf = zeros(1,N_UE);

for j=1:N_UE
    RU2UE = 0;
    temp = 0;
    for i=1:N_RU
        if abs(ChannelGain(i,j))> abs(temp)
            temp = ChannelGain(i,j);
            RU2UE = i;
        end
    end
    RU_UE(RU2UE,j) = 1;
end

for i = 1:N_UE
    for j = 1:N_RU
        for t = 1 : N_UE
            if i~=t 
                Intf(i) = Intf(i) + Popt(t)*abs(ChannelGain(j,i))^2 * (1 - RU_UE(j,i));
            end
        end
        rate_UE_min(i) = rate_UE_min(i) + BW* log2(1 + (Popt(i)/100*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(Intf(i)+BW*N0));
    end
end
[Sort_rate, I] = sort(rate_UE_min,'descend');
% sum(Capacity_RU)
% sum(rate_UE_min)
RU_UE = zeros(N_RU,N_UE);
for j = 1:N_RU
    for i = 1:N_UE 
        if Capacity_RU(j)> Rmin_UE(i) && sum(RU_UE(:,i))==0 && admission_UE1(i)==1
            Capacity_RU(j) = Capacity_RU(j) - Rmin_UE(i);
            RU_UE(j,i) = 1;
        end
    end
end