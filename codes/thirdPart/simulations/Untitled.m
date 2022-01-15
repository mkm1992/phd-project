xb = zeros(9,2);
xb(:,1) = wmeanCons1/max(wmeanCons);
xb(:,2) = wmeanCons/max(wmeanCons);
%xb(5,1) = 1/2*(xb(4,1)+xb(6,1));
bar(N_service_min:N_service_step:N_service_max,xb)


% aa(2) = 0.701e4;
% aa(3) = 0.9336e4;
% aa(1) = 0.5e4;
% aa = wmeanCons1