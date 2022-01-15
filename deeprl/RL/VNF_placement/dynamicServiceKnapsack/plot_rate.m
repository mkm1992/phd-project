result2(6)=23.5;
r1 = result1/max(result2);
r2 = result2/max(result2);
plot(r2)
hold all
plot(r1)
xlabel('Number of Slices')
ylabel('Normalized Mean Number of Admitted Request')
title('Normalized Mean Number of Admitted Request vs. Number of Slices')