alpha_step = Pmax/sqrt(count)/1;

for i = 1:N_UE
    beta_step = 1/1/sqrt(count);
    lambda_step = Rmin_UE(i)/sqrt(count)/1000;
    lambda(i)= max(0,lambda(i) - lambda_step* (rate_UE(i) - Rmin_UE(i)));
    for z = 1:N_PRB
        beta(i) = max(0, beta(i) - beta_step* (PRB_UE(z,i)- 1));
    end
    
end
for j = 1:N_RU

   alpha(j) = max(0, alpha(j) -alpha_step* (Pmax - Pow_RU(j))); 
end