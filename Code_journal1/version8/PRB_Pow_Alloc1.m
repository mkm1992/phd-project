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
        w1(1,:) = alpha_m(:).* delay_max(:);
        w2(1,:) = alpha_m(:).*lambda_m(:) .* delay_max(:) + alpha_m(:);
        w3(1,:) = mu(:).* delay_max(:)-1;
        w4(1,:) = mu(:).* delay_max(:).*lambda_m(:)+mu(:) + lambda_m(:);
        %w1(:).*R_s(:)-w2(:)- M_max*(w3(:).*R_s(:)-w4(:)) <= 0;
        %R_s(:) <= (w2(:) - M_max*w4(:))./((w1(:) - M_max*w3(:)))
        t = 0;
        for s = 1:S
            for j = 1:UE_S_Admit(s)
            t = t+1;
            a = (w2(s) - M_max*w4(s))./((w1(s) - M_max*w3(s)));
            Popt(t) <= (2^(a/BW)-1)/(abs((ChannelGain(:,t))'*beamForming(:,t))^2)*(Intf(t)+BW*N0)
            end
        end
        
        %alpha_m(:).*(delay_max(:) - xx(:))-(mu(:).*(delay_max(:) - xx(:))-1)*10 <= 0
    cvx_end

end