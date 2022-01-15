%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t 
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) = 0;%Intf(i) + Pmax/100*abs(ChannelGain(j,i).* RU_UE(j,i)) * PRB_UE(z,i) * PRB_UE(z,t);
                end
            end
           
        end
    end
end



