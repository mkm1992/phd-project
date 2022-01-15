alpha_step = Pmax/sqrt(count)/1;

for i = 1:N_UE
    beta_step = Pmax/1/sqrt(count);
    lambda_step = Rmin_UE(i)/sqrt(count)/1000;
    lambda(i)= max(0,lambda(i) - lambda_step* (rate_UE(i) - Rmin_UE(i)));
    beta(i) = max(0, beta(i) - beta_step* (Popt(i)- 0));
    
end
for j = 1:N_RU
   tr_step = Capacity_RU(j)/sqrt(count)/10000000;
   Sum_Rate = sum(rate_UE.*RU_UE(j,:));
   tr(j) = max(0, tr(j) - tr_step*(Capacity_RU(j)-Sum_Rate));
   alpha(j) = max(0, alpha(j) -alpha_step* (Pmax - Pow_RU(j))); 
end