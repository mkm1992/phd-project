
RU_UE = zeros(N_RU,N_UE);
for u1 =  1:N_UE
    RU_first = randi(N_RU);
    RU_UE(RU_first,u1) = 1;
end