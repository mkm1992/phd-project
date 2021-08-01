% Obtain PRB and Power 
beta = ones(N_PRB,N_UE)*1;
alpha = ones(1,N_RU)*Pmax/1000;
lambda = ones(1,N_UE).*Rmin_UE/100;
run Interference
run Rate
run P_RU
eps = 0.1;
counter_max = 100;


zeta_pow = zeros(1,N_UE);
for  numRU =1:N_RU
    for numUE = 1:N_UE
       if  RU_UE(numRU,numUE)==1
           zeta_pow(numUE) = zeta_pow(numUE) +(abs((beamForming1(:,numUE).')*beamForming1(:,numUE)))*alpha(numRU);
       end
    end
end

for count = 1: counter_max
    for i = 1:N_UE
        Popt(i) = max(0,(BW*(1+lambda(i))/0.693/zeta_pow(i))-( Intf(i)+BW*N0)/abs((ChannelGain1(:,i))'*beamForming1(:,i))^2); 
    end
    Popt
    run Rate_PRB
    H_PRB = zeros(N_PRB, N_UE);
    for i = 1:N_UE
        for z = 1:N_PRB
            %temp = sum(alpha(:).*RU_UE(:,i))*Popt(i);
            %tr_temp = sum(tr(:).*RU_UE(:,i));
            H_PRB(z,i) = rate_PRB_UE(z,i) *(1+ lambda(i)) + zeta_pow(numUE) - beta(z,i);
        end
         [m, ind] = max(H_PRB(:,i));
         PRB_UE(ind,i) = 1;
         run Rate_PRB
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