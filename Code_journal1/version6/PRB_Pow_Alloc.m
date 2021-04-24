% PRB & Power Allocation
cvx_begin
    variables Popt(1,N_UE) 
    %variable PRB_UE(N_PRB, N_UE) binary;
    run Interference
    run Rate
    %rate_UE = cvx(rate_UE);
    run P_RU
    R1 = sum(rate_UE);
    P1 = sum(Pow_RU);
    error =  R1 - eta0 * P1;
    maximize error
    subject to
    Pow_RU(:) <= Pmax;
    %Prrh(:) <= 2^C_thresh * var_q *100;
    Popt(:) >= 0;
    Popt(:) < Pmax/10;
    rate_UE(:) >= Rmin(1)*100;%.*admission_UE1(:);  
    %PRB_UE(:)> 1
cvx_end
eta0 = double(R1)/double(P1);
run Interference
run Rate
%etha = sum(rate_UE)/sum(Pow_RU);