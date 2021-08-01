% Obtain PRB and Power 
beta = ones(1,N_UE)*Pmax/1;
alpha = ones(1,N_RU)*Pmax/10;
lambda = ones(1,N_UE).*Rmin_UE/100;
tr = ones(1,N_RU).*Capacity_RU/100;
zeta_s = ones(S,1).*(alpha_s+  1./delay_max(:));
run Parameter
eps = 0.1;
for count = 1: counter_max
    for i = 1:N_UE
        temp = sum(alpha(:).*RU_UE(:,i));
        ze = -beta(i) + temp; 
        %ze = temp;
        tr_sum = sum(tr(:).*RU_UE(:,i));
        Popt(i) = max(0,(BW*(1+lambda(i)-tr_sum)/0.693/ze)-( Intf(i)+BW*N0)/sum(abs(ChannelGain(:,i).* RU_UE(:,i)))); 
        Popt(i) = min(Pmax, Popt(i));
    end
%     for z = 1:N_PRB
%        for i =1 :N_UE
%           if 
%        end
%     end
    Popt
    run Rate_PRB
    H_PRB = zeros(N_PRB, N_UE);
    PRB_UE = zeros(N_PRB,N_UE);
    for i = 1:N_UE
        for z = 1:N_PRB
            temp = sum(alpha(:).*RU_UE(:,i))*Popt(i);
            tr_temp = sum(tr(:).*RU_UE(:,i));
            H_PRB(z,i) = rate_PRB_UE(z,i) *(1+ lambda(i)-tr_temp)-temp + beta(i)*Popt(i);
        end
         [m, ind] = max(H_PRB(:,i));
         PRB_UE(ind,i) = 1;
         run Parameter
    end
%     for i =1:N_UE
%         [m, ind] = max(H_PRB(:,i));
%         PRB_UE(ind,i) = 1;
%         run Rate_PRB
%     end
    result_old = sum(rate_UE);
    run Parameter
    run update_var
    result_new = sum(rate_UE);
%     if abs(result_new - result_old)< eps
%         break
%     end
end