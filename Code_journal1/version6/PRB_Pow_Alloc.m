for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
        variables xx(1,S);
        %variable PRB_UE(N_PRB, N_UE);
        run Interference
        run Rate
        run P_RU
        maximize sum(rate_UE)
        subject to
        Pow_RU(:) <= Pmax;
        %Pow_RU(:) <= 2.^(Capacity_RU(:)/1000) * var_q ;
        Popt(:) > 0; 
        Popt(:) < Pmax;
        rate_UE(:) > Rmin_UE(:);%.*admission_UE1(:); 
        %R_s(:) > alpha_s + 1./delay_max(:);
        R_s(:) > alpha_s + xx(:);
%         for s = 1:S
%            1/(R_s(s)-alpha_s) < delay_max(s);
%         end
        %rate_UE(:) > 
        %PRB_UE(:)> 1
    cvx_end

end