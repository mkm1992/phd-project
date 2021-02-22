%% PRB and Power allocation
cvx_begin
    variable Popt(1,N_UE) 
    maximize error
    subject to
    Prrh(:) <= Pmax;
    %Prrh(:) <= 2^C_thresh * var_q *100;
    Popt(:) > 0; 
    Popt(:) < Pmax/10;
    rate_UE(:) > Rt*1000;  
    rate_UE(:) >1/(delay_max-mean(Delay_Slice1+Delay_Slice2))
cvx_end
