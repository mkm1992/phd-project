
r1 = 1e7*[1.5495,1.5905,1.6075,1.6172,1.6212];

r2 = 1e7*[1.6241,1.6192,1.6076,1.58901,1.5528];

plot( UE_num , r1/1e6,'-*')
hold on
plot( UE_num , r2/1e6,'-+')
hold on
grid on
% plot( UE_num , sumRB1_e/1e6,'-^')
% hold on
% plot( UE_num , sumRB1_u/1e6,'--')
% hold on
xlabel('Priority Factor for eMBB Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput vs Priority Factor for eMBB Service')
%plot( UE_num , (r1+r2)/1e6,'--')