% Obtain PRB and Power 
beta = ones(1,N_UE)*Pmax/100;
alpha = ones(1,N_RU)*Pmax;
lambda = ones(1,N_UE).*Rmin_UE/1000;
run Interference
run Rate
run P_RU
eps = 0.1;
for count = 1: counter_max
    for i = 1:N_UE
        temp = sum(alpha*RU_UE(:,i));
        ze = -beta(i) + temp; 
        Popt(i) = max(0,(BW*(1+lambda(i))/0.693/ze)-( Intf(i)+BW*N0)/abs((ChannelGain(:,i))'*beamForming(:,i))^2);   
    end
    result_old = sum(rate_UE);
    run Interference
    run Rate
    run P_RU
    run update_var
    result_new = sum(rate_UE);
    if abs(result_new - result_old)< eps
        break
    end
end