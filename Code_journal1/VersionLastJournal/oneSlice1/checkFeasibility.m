
%% power and prb allocation
Popt(:) = Pmax/N_UE;
PRB_UE = zeros(N_PRB,N_UE);
for i =1:N_UE
    if mod(i,N_PRB)==0
       PRB_UE(N_PRB,i)= 1;
    else
        PRB_UE(mod(i,N_PRB),i) =1 ;
    end

end
%% interference 
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_Antenna
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t && PRB_UE(z,i) ==1 && PRB_UE(z,t)
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) =Intf(i) + Popt(t)*abs((ChannelGain1(:,i))'*beamForming1(:,t))^2;
                end
            end
           
        end
    end
end
%% rate
rate_UE_1 = zeros(1,N_UE);
for i = 1:N_UE
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE_1(i) = rate_UE_1(i) + BW* log(1 + (Popt(i)*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
end
%% power RU
Pow_RU =  zeros(1,N_RU);
Popt1 = eye(N_UE);
for i=1:N_UE
   Popt1(i,i) = Popt(i); 
end
for numRU =1:N_RU
   for numUE = 1:N_UE
       if RU_UE(numRU, numUE)==1
            Pow_RU(numRU) = Pow_RU(numRU) + (abs((beamForming1(:,numUE).')*beamForming1(:,numUE)))*Popt1(numUE,numUE)+var_q; 
       end
   end
end
%% Feasible
a1 =Pow_RU <= Pmax;
%a2 =Popt(:) >= 0; 
a2 =Popt(:) <= Pmax/3;
a3 =rate_UE(:) >= Rmin_UE(:);
sum(rate_UE_1)