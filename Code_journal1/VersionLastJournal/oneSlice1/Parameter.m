%% obtain Power of RU
Pow_RU =  zeros(1,N_RU);
%Pow_RU =  zeros(1,N_RU);
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

%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_Antenna
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t && PRB_UE(z,i) ==1 && PRB_UE(z,t)
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) =Intf(i) + Pmax/10*abs((ChannelGain1(:,i))'*beamForming1(:,t))^2;
                end
            end
           
        end
    end
end
%Intf = ones(1,N_UE)*db2pow(i_count)/1000;
rate_UE = zeros(1,N_UE);
for i = 1:N_UE
    %for j = 1:N_RU
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE(i) = rate_UE(i) + BW* log(1 + (Popt(i)*abs((ChannelGain1(:,i))'*beamForming1(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
    %end
end