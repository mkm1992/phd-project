%% obtain Power of RU
Pow_RU =  cvx(zeros(1,N_RU));
%Pow_RU =  zeros(1,N_RU);
% for i = 1:N_RU
%     for j = 1:N_UE
%         Pow_RU(i) = Pow_RU(i) +  Popt(j)*RU_UE(i,j);
%     end
% end
Popt1 = cvx(eye(N_UE));
for i=1:N_UE
   Popt1(i,i) = Popt(i); 
end
for i =1:N_RU
   Pow_RU(i) = (abs(beamForming(i,:)*Popt1*beamForming(i,:).'))+var_q; 
end