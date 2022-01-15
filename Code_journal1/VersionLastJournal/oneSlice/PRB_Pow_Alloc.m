for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
        variables xx(1,S);
        variables m(1,S);
        %variable PRB_UE(N_PRB, N_UE);
        run Interference
        run Rate
        run P_RU
        maximize sum(rate_UE)
        subject to
        Pow_RU(:) <= Pmax;
        %Pow_RU(:) <= 2.^(Capacity_RU(:)/1000) * var_q ;
        Popt(:) >= 0; 
        Popt(:) <= Pmax;
        rate_UE(:) >= Rmin_UE(:);%.*admission_UE1(:); 
        %R_s(:) > alpha_s + 1./delay_max(:);
        %xx(:).*(R_s(:)-alpha_s) >= 1.;
        %t(:) = R_s(:) - alpha_s;
        xx(:) > 0
        %xx(:) - 1/((R_s(:)-alpha_s))> 0
        delay_max(:) - xx(:) >= 0
        alpha_m(:).*(delay_max(:) - xx(:))-(mu(:).*(delay_max(:) - xx(:))-1)*10 <= 0
    cvx_end

end