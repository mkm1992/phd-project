for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
        %variable PRB_UE(N_PRB, N_UE);
        run Interference
        run Rate
        run P_RU
        maximize sum(rate_UE)
        subject to
        Pow_RU(:) <= Pmax;
        %Prrh(:) <= 2^C_thresh * var_q *100;
        Popt(:) > 0; 
        Popt(:) < Pmax/10;
        rate_UE(:) > Rmin(1)*5;%.*admission_UE1(:);  
        %PRB_UE(:)> 1
    cvx_end

end
