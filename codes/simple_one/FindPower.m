counter_max = 20;
lambda_r = ones(1,N_Ut)*Rt;
mu = ones(1,N_rrh)*Pmax;
Kr = ones(1,N_rrh)*(2^C_thresh * var_q);
tr = ones(1,N_Ut)*(1/(delay_max-mean(Delay_Slice))+lamda);   
etha = zeros(1,counter_max);
Power = zeros(counter_max, N_Ut);
Power_cnvg_Thr = 0.01;
iter_max = 1;
for iter =1 :iter_max 
    for  count_power=1:counter_max
        etha_u = (  lambda_r + tr + 1) * BW / log(2);
        mm_u = sum((abs( ChannelGain .* PrecodingMat) .^2).' * (service2slice),2).';
        zetha_u = (BW * N0) + Intf.';
        keisi_u =  sum(( mu + Kr + etha(count_power))*(abs(PrecodingMat) .^2),1) ;
        %if (sum(Power(count_power)-Power(count_power)) < Power_cnvg_Thr) 
            for i = 1: N_Ut                       
                Power(count_power,i) = ((etha_u(i) .* mm_u(i)) - (zetha_u(i) .* keisi_u(i)))/(keisi_u(i) .* mm_u(i));
                Popt(i) = max(0,Power(count_power,i));
                %Popt(i) = min (Pmax , Popt(i));
            end
            run rate
            run FronthaulCap
            run FindDelay
            etha(count_power) = sum(rate_UE)/(sum(Popt)+0.001);
            run update_var


        %end

    end
end