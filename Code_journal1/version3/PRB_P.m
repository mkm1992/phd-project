% Obtain PRB and Power 
beta = ones(1,N_UE)*Pmax/1;
alpha = ones(1,N_RU)*Pmax/.01;
lambda = ones(1,N_UE).*Rmin_UE/1000;
run Interference
run Rate
run P_RU
eps = 0.1;
for count = 1: counter_max
    for i = 1:N_UE
        temp = sum(alpha(:).*RU_UE(:,i));
        ze = -beta(i) + temp; 
        Popt(i) = max(0,(BW*(1+lambda(i))/0.693/ze)-( Intf(i)+BW*N0)/sum(abs(ChannelGain(:,i).* RU_UE(:,i)))); 
        %Popt(i) = min(Pmax/N_RU, Popt(i));
    end
%     for z = 1:N_PRB
%        for i =1 :N_UE
%           if 
%        end
%     end
    Popt
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