for  count_power=1:1 
    cvx_begin
        variables Popt(1,N_UE); 
        run Interference
        run Rate
        run P_RU
        maximize sum(rate_UE)
        subject to
        %Power_RU(N_UE,Popt,beamForming,var_q,N_RU,1:N_RU)<2.^(Capacity_RU(1)/1e4) * var_q*100 ;
        %Power_RU(N_UE,Popt,beamForming,var_q,N_RU,1:N_RU)<Pmax;
        Pow_RU <= Pmax*6;
        Popt(:) >= 0; 
        Popt(:) <= Pmax*2;
        
        %Find_Rate(BW,Popt,ChannelGain,beamForming,PRB_UE,N_PRB,N_UE,N0,Intf,1:N_UE)>= Rmin_UE(1);
        rate_UE(:) >= Rmin_UE(:)/2;%.*admission_UE1(:); 
        w1(1,:) = alpha_m(:).* delay_max(:);
        w2(1,:) = alpha_m(:).*lambda_m(:) .* delay_max(:) + alpha_m(:);
        w3(1,:) = mu(:).* delay_max(:)-3;
        w4(1,:) = mu(:).* delay_max(:).*lambda_m(:)+mu(:) - 3*lambda_m(:);
        %w1(:).*R_s(:)-w2(:)- M_max*(w3(:).*R_s(:)-w4(:)) <= 0;
        %R_s(:) <= (w2(:) - M_max*w4(:))./((w1(:) - M_max*w3(:)))
        t = 0;
        a = zeros(1,S);
        M_max = 25;
        for s = 1:S
            for j = 1:UE_S(s)
                t = t+1;
                a(s) = (w2(s) - M_max*w4(s))./((w1(s) - M_max*w3(s)));
                %Popt(t) <= (2^(a(s)/BW)-1)*(Intf(t)*0+BW*N0)/(abs((ChannelGain(:,t))'*beamForming(:,t))^2)
                rate_UE(t) >= max(a(s),0)
            end
        end
        
        %alpha_m(:).*(delay_max(:) - xx(:))-(mu(:).*(delay_max(:) - xx(:))-1)*10 <= 0
    cvx_end

end