%% UE Admission
admission_UE = ones(1,N_UE);
admission_UE1 =  zeros(1,N_UE);
for s =1:S
    if s ==1 
        [best admission_UE1(1:sum(UE_S(1:1)))] = knapsack(Rmin(s)*ones(1,UE_S(s)), admission_UE(1:sum(UE_S(1:1))), Rate_mid_max(s));
    else
        [best admission_UE1(sum(UE_S(1:s-1)+1):sum(UE_S(1:s)))] = knapsack(Rmin(s)*ones(1,UE_S(s)), admission_UE(sum(UE_S(1:s-1)+1):sum(UE_S(1:s))), Rate_mid_max(s));
    end
end
disp(best)
items = find(admission_UE1);
disp(items)