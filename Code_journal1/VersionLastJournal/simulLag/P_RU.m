%% obtain Power of RU
Pow_RU =  (zeros(1,N_RU));
%Pow_RU =  zeros(1,N_RU);
% for i = 1:N_RU
%     for j = 1:N_UE
%         Pow_RU(i) = Pow_RU(i) +  Popt(j)*RU_UE(i,j);
%     end
% end
Popt1 = (eye(N_UE));
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