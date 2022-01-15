for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
        run Interference
        run Rate
        run P_RU
        maximize sum(rate_UE)
        subject to
        Pow_RU <= Pmax
        Popt(:) >= 0; 
        Popt(:) <= Pmax;
        rate_UE(:) >= Rmin_UE(:);%.*admission_UE1(:); 

    cvx_end

end