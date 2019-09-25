counter_max = 100;
lambda_r = ones(1,N_Ut)*Rt/10;
mu = ones(1,N_Ut)*Pmax/100;
Kr = ones(1,N_rrh)*(2^C_thresh * var_q)/10;
tr = ones(1,N_Ut)*(1/(delay_max-mean(Delay_Slice))+lamda)/10;   
eta = zeros(1,count_power);
for  count_power=1:counter_max
    for j=1:N_Ut
        x1 = 
    end
end