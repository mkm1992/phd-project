% Obtain PRB and Power 
beta = ones(1,N_UE)*Pmax/1;
alpha = ones(1,N_RU)*Pmax/.1;
lambda = ones(1,N_UE).*Rmin_UE/1000;
tr = ones(1,N_RU).*Capacity_RU/10000;
%zeta_s = ones(1,S)*(alpha_s+ frac1_t);
run Interference
run Rate
run P_RU
eps = 0.1;
for count = 1: counter_max
    for i = 1:N_UE
        temp = sum(alpha(:).*RU_UE(:,i));
        ze = -beta(i) + temp; 
        %ze = temp;
        tr_sum = sum(tr(:).*RU_UE(:,i));
        Popt(i) = max(0,(BW*(1+lambda(i)-tr_sum)/0.693/ze)-( Intf(i)+BW*N0)/sum(abs(ChannelGain(:,i).* RU_UE(:,i)))); 
        %Popt(i) = min(Pmax/N_RU, Popt(i));
    end
%     for z = 1:N_PRB
%        for i =1 :N_UE
%           if 
%        end
%     end
    Popt
    run Rate_PRB
    H_PRB = zeros(N_PRB, N_UE);
    for i = 1:N_UE
        for z = 1:N_PRB
            temp = sum(alpha(:).*RU_UE(:,i))*Popt(i);
            tr_temp = sum(tr(:).*RU_UE(:,i));
            H_PRB(z,i) = rate_PRB_UE(z,i) *(1+ lambda(i)-tr_temp)-temp + beta(i)*Popt(i);
        end
         [m, ind] = max(H_PRB(:,i));
         PRB_UE(ind,i) = 1;
         run Rate_PRB
    end
%     for i =1:N_UE
%         [m, ind] = max(H_PRB(:,i));
%         PRB_UE(ind,i) = 1;
%         run Rate_PRB
%     end
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