for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
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
        w1(:) = alpha_m(:).* delay_max(:);
        w2(:) = alpha_m(:).^2 .* delay_max(:) + alpha_m(:);
        w(3) = mu(:).* delay_max(:)-1;
        w4(:) = mu(:).* delay_max(:).*alpha_m(:)+mu(:) + alpha_m(:);
        
        alpha_m(:).*(delay_max(:) - xx(:))-(mu(:).*(delay_max(:) - xx(:))-1)*10 <= 0
    cvx_end

end