clear all
clc
close all
%% variables
N_min = 10;
N_step = 2;
N_max = 10;
counter_max = 1;
iter_max = 3;
numVar = N_min:N_step:N_max ;
etha = zeros(length(numVar),iter_max,counter_max);
etha1 = zeros(length(numVar),iter_max,counter_max);
%% loops
nr = 0;
for N_var = N_min:N_step:N_max   
    nr = nr +1;
    %N_rrh = N_var;
    for iter =1 :iter_max 
        run var
        eta0 = 0;
        run mapping
        run mapping2
        for  count_power=1:counter_max  
             cvx_begin
                variable Popt(1,N_Ut)
                run parameter
                maximize error
                subject to
                Prrh(:) <= 10*Pmax;
                %Prrh(:) <= 2^C_thresh * var_q *100;
                Popt(:) > 0; 
                Popt(:) < Pmax*3;
                rate_UE(:) > Rt;  
                rate_UE(:) >1/(delay_max-mean(Delay_Slice1+Delay_Slice2))
            cvx_end
            eta0 = double(R1)/double(P1);
            run interference
            run rate
            etha(nr,iter,count_power) = sum(rate_UE)/(sum(Prrh));
        end
        %%
        eta01 = 0;
        for  count_power=1:counter_max  
            cvx_begin
                variable Popt(1,N_Ut)
                run parameter1
                maximize error
                subject to
                Prrh(:) <= 10*Pmax;
                %Prrh(:) <= 2^C_thresh * var_q *100;
                Popt(:) > 0; 
                Popt(:) < Pmax*3;
                rate_UE(:) > Rt;  
                rate_UE(:) >1/(delay_max-mean(Delay_Slice1+Delay_Slice2))
            cvx_end
            eta01 = double(R11)/double(P11);
            run interference
            run rate
            etha1(nr,iter,count_power) = sum(rate_UE)/(sum(Prrh));
        end
    end
end
plot( N_min:N_step:N_max , mean(etha(:,:,end),2))
