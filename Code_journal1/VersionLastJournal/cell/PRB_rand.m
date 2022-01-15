PRB_UE = zeros(N_PRB, N_UE);
N_PRB1 = 20;
for i =1:N_UE
    temp_prb  = randi(N_PRB1);
    PRB_UE(temp_prb,i)= 1;
end

