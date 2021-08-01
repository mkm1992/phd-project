RU_UE = zeros(N_RU,N_UE);
for u1 =  1:N_UE
    [val, RU_connect] = min(distance(:,u1));
    RU_UE(RU_connect,u1) = 1;
end



