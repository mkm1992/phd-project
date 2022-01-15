Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_Antenna
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t && PRB_UE(z,i) ==1 && PRB_UE(z,t)
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) =Intf(i) + Popt(i)*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2;
                end
            end
           
        end
    end
end


rate_UE_1 = zeros(1,N_UE);
for i = 1:N_UE
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE_1(i) = rate_UE_1(i) + BW* log(1 + (Popt(i)*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
end