T_max = 5e-6*randi([1,10],1,S);
mu = 2* Rmin;
alpha_m  = Rmin;


for s = 1:S
    if mu(s)< 1/T_max(s)
      T_max(s) = 1/mu(s)*(1+randi(100)/100) ;  
    end
    VNF_NUM(s) = ceil(alpha_m(s)/(mu(s)- 1/T_max(s)));
end

for s = 1:S
    Delay_Slice(s) = 1/(mu(s)- alpha_m(s)/VNF_NUM(s));
end