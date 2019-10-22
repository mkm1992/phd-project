clear all
clc
close all
%%
N_min = 4;
N_step = 1;
N_max = 4;
N_rrh = 3;
counter_max = 10;
iter_max = 1;
numRRh = N_min:N_step:N_max ;
etha = zeros(length(numRRh),iter_max,counter_max);
nr = 0;
for N_Service1 = N_min:N_step:N_max   
    nr = nr +1;
    for iter =1 :iter_max 
        run var1
        eta0 = 0;
        for  count_power=1:counter_max       
            %%
            run mappingSolution
           
            %Popt = ones(1,N_Ut)*Pmax;
            cvx_begin
                variable Popt(1,N_Ut)
                run parameter
                error =  sum(rate_UE) - (eta0) * (sum(Prrh));
                maximize error
                subject to
                Prrh(:) <= Pmax*10;
                Prrh(:) <= 2^C_thresh * var_q ;
                Popt(:) > 0; 
                rate_UE(:) > Rt/100;  
                %rate_UE(:) >1/(delay_max-mean(Delay_Slice1+Delay_Slice2))
            cvx_end
            run interference
            run rate
            run FronthaulCap
            run FindDelay
            eta0 =  sum(rate_UE)/(sum(Prrh));
            etha(nr,iter,count_power) = sum(rate_UE)/(sum(Prrh));
            
        end
    end
end
%plot( N_min:N_step:N_max , mean(etha(:,:,end),2))