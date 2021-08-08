Intf_PRB = zeros(N_PRB,N_UE);
for z = 1:N_PRB
    for i = 1:N_UE
            for t = 1 : N_UE
                if i~=t  
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf_PRB(z,i) = Intf_PRB(z,i) + Pmax/10*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2 * PRB_UE(z,t);% * PRB_UE(z,i);
                end
            end
    end
end



rate_PRB_UE = zeros(N_PRB,N_UE);
for z = 1:N_PRB
    for i = 1:N_UE
        for j = 1:N_RU 
            rate_PRB_UE(z,i) = rate_PRB_UE(z,i) + BW* log(1 + (Popt(i)*abs((ChannelGain(j,i)).* RU_UE(j,i)))/(Intf_PRB(z,i)+BW*N0));%*PRB_UE(z,i);
        end
    end
end