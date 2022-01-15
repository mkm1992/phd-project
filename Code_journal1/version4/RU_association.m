RU_UE = zeros(N_RU,N_UE);
for j = 1:N_RU
    for i = 1:N_UE 
        if Capacity_RU(j)> Rmin_UE(i) && sum(RU_UE(:,i))==0 
            Capacity_RU(j) = Capacity_RU(j) - Rmin_UE(i);
            RU_UE(j,i) = 1;
        end
    end
end