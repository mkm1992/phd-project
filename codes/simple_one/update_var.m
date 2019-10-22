mu_step = 2*Pmax/sqrt(count_power);
kr_step = .0001*(2^(C_thresh) * var_q)/sqrt(count_power);
lambdar_step = 5*Rt/sqrt(count_power);
tr_step = 1*(1/(delay_max-mean(Delay_Slice))+lamda)/sqrt(count_power);
Ut2Slice = Ut2Service*service2slice;
for ki=1:N_Ut
    lambda_r(ki)= max(0,lambda_r(ki) - lambdar_step* (rate_UE(ki) - Rt/10));
    for si = 1:N_Slice
        if Ut2Slice(ki,si) == 1
            tr(ki) = 0;%max(0,tr(ki)-tr_step*(rate_UE(ki)-1/(delay_max-(Delay_Slice(si)))+lamda));  
        end
    end
end

for mi=1:N_rrh
    Kr(mi) =  max(0,Kr(mi)-kr_step*(2^(C_thresh) * var_q - Prrh(mi)));
    mu(mi)= max(0,mu(mi)-mu_step*((Pmax*10 -Prrh(mi))));
end
