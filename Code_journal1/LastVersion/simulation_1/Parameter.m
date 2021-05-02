%% obtain Power of RU
Pow_RU =  zeros(1,N_RU);
%Pow_RU =  zeros(1,N_RU);
% for i = 1:N_RU
%     for j = 1:N_UE
%         Pow_RU(i) = Pow_RU(i) +  Popt(j)*RU_UE(i,j);
%     end
% end
Popt1 = eye(N_UE);
for i=1:N_UE
   Popt1(i,i) = Popt(i); 
end
for i =1:N_RU
   Pow_RU(i) = (abs(beamForming(i,:)*Popt1*beamForming(i,:).'))+var_q; 
end
%%
%% Obtain Interference
Intf = zeros(1,N_UE);
for i = 1:N_UE
    for j = 1:N_RU
        for z = 1:N_PRB
            for t = 1 : N_UE
                if i~=t && PRB_UE(z,i) ==1 && PRB_UE(z,t)
                    %Intf(i) = Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2 * PRB_UE(z,i) * PRB_UE(z,t);
                    Intf(i) =Intf(i) + Pmax/100*abs((ChannelGain(:,i))'*beamForming(:,i))^2;
                end
            end
           
        end
    end
end
rate_UE = zeros(1,N_UE);
for i = 1:N_UE
    %for j = 1:N_RU
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE(i) = rate_UE(i) + BW* log(1 + (Popt(i)*abs((ChannelGain(:,i))'*beamForming(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
    %end
end

R_s = zeros(1,S);
t = 0;
for s = 1:S
    for j = 1:UE_S_Admit(s)
        t = t+1;
        R_s(s) = R_s(s) + rate_UE(t);
    end
end