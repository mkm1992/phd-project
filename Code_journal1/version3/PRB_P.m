% Obtain PRB and Power 
for count = 1: counter_max
    for i = 1:N_UE
        run update_var
        Popt(i) = max(0,(BW*(1+lambda(i))/0.693/ze)-( Intf1(k)+BW*N0)/abs((ChannelGain(:,t))'*beamForming(:,i))^2;
    end
end