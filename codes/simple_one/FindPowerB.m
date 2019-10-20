counter_max = 100;
lambda_r = ones(1,N_Ut) * Rt/10;
mu = ones(1,N_Ut)* Pmax/100;
Kr = ones(1,N_Ut) * ( 2 * C_thresh * var_q)/10;
tr = ones(1,N_Ut) .* (1/(delay_max - mean(Delay_Slice))+ lambda_r)/10;
Power = zeros(counter_max, N_Ut);
Power_cnvg_Thr = 1;
etha = 0; 
Num_Itr = 1e1;

etha_u = ( -mu + lambda_r + Kr + 1) * BW / log(2);
mm_u = sum((abs( ChannelGain .* PrecodingMat) .^2).' * (service2slice),2).';
keisi_u = ( tr + etha) .* sum((abs(PrecodingMat) .^2),1) ;
zetha_u = (BW * N0) + Intf;

for j = 1: Num_Itr
    for count_power = 2: counter_max+1
        if (sum(Power(count_power)-Power(count_power-1)) < Power_cnvg_Thr) 
            for i = 1: N_Ut                       
                Power(count_power -1,i) = ((etha_u(i) .* mm_u(i)) - (zetha_u(i) .* keisi_u(i)))/(keisi_u(i) .* mm_u(i));  
            end

        end
        etha = sum(rate_UE)/sum(Power(count_power-1,:));
        run update_var
    end
    
end

P_ach = sum(Power,1)/length(Power);