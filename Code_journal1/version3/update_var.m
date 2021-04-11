alpha_step = 0.1*Pmax/sqrt(count);
for i = 1:N_UE
    beta_step = 0.1*Pmax/100/sqrt(count);
    lambda_step = 0.1*Rmin_UE(i)/sqrt(count);
    lambda(i)= max(0,lambda(i) - lambda_step* (rate_UE(i) - Rmin_UE(i)));
    beta(i) = max(0, beta(i) - beta_step* (Popt(i)- 0));
    
end
for j = 1:N_RU
   alpha(j) = max(0, alpha(j) -alpha_step* (Pmax - Pow_RU(j))); 
end