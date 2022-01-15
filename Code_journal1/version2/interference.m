%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for z = 1:N_PRB
        for t = 1 : N_UE
            if i~=t 
                Intf(i) = Intf(i) + Pmax/10*abs((ChannelGain(:,t))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
            end
        end
    end
end