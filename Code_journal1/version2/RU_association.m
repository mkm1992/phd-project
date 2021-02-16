
[Sort_rate, I] = sort(rate_UE_min,'descend');
sum(Capacity_RU)
sum(rate_UE_min)
RU_UE = zeros(N_RU,N_UE);
for j = 1:N_RU
    for i = 1:N_UE 
        if Capacity_RU(j)> Sort_rate(i) && sum(RU_UE(:,i))==0 && admission_UE1(i)==1
            Capacity_RU(j) = Capacity_RU(j) - Sort_rate(i);
            RU_UE(j,i) = 1;
        end
    end
end