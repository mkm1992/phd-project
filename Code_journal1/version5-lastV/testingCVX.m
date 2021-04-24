% PRB & Power Allocation
cvx_begin
    variables Popt(1,N_UE) 
    run Interference
    run Rate
    run P_RU
    maximize sum(rate_UE)
    subject to
    power_RU(Popt,RU_UE,N_RU,N_UE) <= Pmax*3;
    %Prrh(:) <= 2^C_thresh * var_q *100;
    Popt(:) >= 0; 
    %rate_UE(:) >= Rmin(1);%.*admission_UE1(:);  
    %PRB_UE(:)> 1
cvx_end