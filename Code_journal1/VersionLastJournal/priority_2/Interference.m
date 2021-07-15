%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_Antenna
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t && PRB_UE(z,i) ==1 && PRB_UE(z,t)
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) =Intf(i) + Pmax/100000*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2;
                end
            end
           
        end
    end
end