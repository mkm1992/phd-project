w1(1,:) = alpha_m(:).* delay_max(:);
w2(1,:) = alpha_m(:).*lambda_m(:) .* delay_max(:) + alpha_m(:);
w3(1,:) = mu(:).* delay_max(:)-3;
w4(1,:) = mu(:).* delay_max(:).*lambda_m(:)+mu(:) - 3*lambda_m(:);
 t = 0;
a = zeros(1,S);
M_max = 100;
for s = 1:S
    for j = 1:UE_S(s)
        t = t+1;
        a(s) = (w2(s) - M_max*w4(s))./((w1(s) - M_max*w3(s)));
        %Popt(t) <= (2^(a(s)/BW)-1)*(Intf(t)*0+BW*N0)/(abs((ChannelGain(:,t))'*beamForming(:,t))^2)
        %rate_UE(t) >= max(a(s),0)
    end
end
Rmin_UE(:) = max(Rmin_UE(:),a(s));
Rmin_UE(:) = max(Rmin_UE(:), lambda_m+1/delay_max);