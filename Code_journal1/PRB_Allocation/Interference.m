%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t 
                    Intf(i) = Intf(i);% + Popt(t)*abs(ChannelGain(j,i))^2 * PRB_UE(z,i) * PRB_UE(z,t)*admission_UE1(t);
                end
            end
           
        end
    end
end