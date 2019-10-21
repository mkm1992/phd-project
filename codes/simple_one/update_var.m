mu_step = 0.01*Pmax/sqrt(count_power);
kr_step = 10*(2^C_thresh * var_q)/sqrt(count_power);
lambdar_step = 10*Rt/sqrt(count_power);
tr_step = 1*(1/(delay_max-mean(Delay_Slice))+lamda)/sqrt(count_power);
Ut2Slice = Ut2Service*service2slice;
for ki=1:N_Ut
    lambda_r(ki)= max(0,lambda_r(ki) - lambdar_step* (rate_UE(ki) - Rt));
    for si = 1:N_Slice
        if Ut2Slice(ki,si) == 1
            tr(ki) = max(0,tr(ki)-tr_step*(rate_UE(ki)-1/(delay_max-(Delay_Slice(si)))+lamda));  
        end
    end
end

for mi=1:N_rrh
    Kr(mi) =  max(0,Kr(mi)-kr_step*(2^C_thresh * var_q - Prrh(mi)));
    mu(mi)= max(0,mu(mi)-mu_step*((Pmax -Prrh(mi))));
end
