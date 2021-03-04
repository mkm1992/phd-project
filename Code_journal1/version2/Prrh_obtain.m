%% obtain Power of each RU
for n = 1:N_RU
    for i = 1:N_UE
        P_RU(n) = P_RU(n)+ Popt(i)*RU_UE(n,i)*admission_UE1(i);
    end
end