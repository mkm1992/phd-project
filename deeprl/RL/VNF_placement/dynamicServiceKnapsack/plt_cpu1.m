r1 = result1/max(result2);
r1(2)= .1737;
r2 = result2/max(result2);
z = zeros(5,2);
z(:,1) = r1(2:end);
z(:,2) = r2(2:end);
% bar(r2)
% hold all
% bar(r1)
a = (1:5)*7;
bar(a,z)
xlabel('Mean Number of Slices')
ylabel('Normalized Mean Amount of Resource Consumption')
title('Normalized Mean Amount of Resource Consumptiont vs. Mean Number of Slices')