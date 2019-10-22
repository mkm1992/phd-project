clear all
clc
close all
%%
N_min = 2;
N_step = 1;
N_max = 7;
N_rrh = 10;
counter_max = 20;
iter_max = 100;
numRRh = N_min:N_step:N_max ;
etha = zeros(length(numRRh),iter_max,counter_max);
nr = 0;
for N_Service = N_min:N_step:N_max   
    nr = nr +1;
    for iter =1 :iter_max 
        run var1
        for  count_power=1:counter_max       
            %%
            run mappingSolution
            etha_u = (  lambda_r + tr + 1) * BW / log(2);
            mm_u = sum((abs( ChannelGain .* PrecodingMat) .^2).* (rrh2ut1),1);
            zetha_u = (BW * N0) + Intf.';
            keisi_u =  sum(( mu + Kr + etha(count_power))*(abs(PrecodingMat) .^2),1) ;
            %if (sum(Power(count_power)-Power(count_power)) < Power_cnvg_Thr) 
            for i = 1: N_Ut                       
                Power(count_power,i) = ((etha_u(i) .* mm_u(i)) - (zetha_u(i) .* keisi_u(i)))/(keisi_u(i) .* mm_u(i));
                Popt(i) = max(0,Power(count_power,i));
            end
            for i = 1: N_Ut
                if  Popt(i) >Pmax
                    Popt(i) = Pmax;
                end
            end
            run rate
            run FronthaulCap
            run FindDelay
            run update_var
            etha(nr,iter,count_power) = sum(rate_UE)/(sum(Popt));
        end
    end
end
plot( N_min:N_step:N_max , mean(etha(:,:,end),2))