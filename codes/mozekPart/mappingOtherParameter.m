%% map rrh 2 slice
rrh2slice = randi([0 imax],N_rrh, N_Slice);
num_map = 0;
while any(sum(rrh2slice,1)<1) || any(sum(rrh2slice,2)<1)
    rrh2slice = randi([0 imax],N_rrh, N_Slice);
    num_map = num_map+1;
    if num_map >10
        rrh2slice = ones(N_rrh, N_Slice);
    end
end
%% map ut 2 service
k = 1;
Ut2Service = zeros(sum(NumOfUtInService),N_Service);
for i=1:N_Service
    Ut2Service(k:k+NumOfUtInService(i)-1,i) = 1;
    k = k+NumOfUtInService(i);
end
%% map PRB to Slice
PRB2Slice = randi([0 imax],N_PRB, N_Slice);
num_map = 0;
while any(sum(PRB2Slice,1)<1) || any(sum(PRB2Slice,2)<1)
    PRB2Slice = randi([0 imax],N_PRB, N_Slice);
    num_map = num_map+1;
    if num_map >10
        PRB2Slice = ones(N_PRB, N_Slice);
    end
end