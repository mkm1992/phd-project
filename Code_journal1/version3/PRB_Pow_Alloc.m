% PRB & Power Allocation
cvx_begin
    variables Popt(1,N_UE) 
    variable PRB_UE(N_PRB, N_UE) binary;
    run Interference
    run Rate
    run P_RU
    maximize sum(rate_UE)
    subject to
    Pow_RU(:) <= Pmax*10;
    %Prrh(:) <= 2^C_thresh * var_q *100;
    Popt(:) >= 0; 
    rate_UE(:) >= Rmin(1)/1000;%.*admission_UE1(:);  
    %PRB_UE(:)> 1
cvx_end