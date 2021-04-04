%% obtain Power of RU
Pow_RU =  cvx(zeros(1,N_RU));
%Pow_RU =  zeros(1,N_RU);
for i = 1:N_RU
    for j = 1:N_UE
        Pow_RU(i) = Pow_RU(i) +  Popt(j)*RU_UE(i,j);
    end
end