figure;
x = zeros(5,4);
x(:,1) = [2 4 5 7 8]; % mu 16e5 12 UE
x(:,2) = 3:2:11; %mu  12e5 12 UE
x(:,3) = 4:3:17; %mu 8e5  12 UE
x(:,4) = 5:4:21; %mu 6e5  12UE
x(:,5) = 5:5:25; %mu 5e5  12 UE
y = 0.2:0.2:1;
bar(y,x)
xlabel('Mean Arrival Rate \lambda (Mbps)')
ylabel('Number of Activated VNF in each Slice')
title('Number of Activated VNF vs. Mean Arrival Rate')