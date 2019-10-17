xb = zeros(9,2);
xb(:,1) = aa/max(wmeanCons);
xb(:,2) = wmeanCons/max(wmeanCons);
bar(N_service_min:N_service_step:N_service_max,xb)