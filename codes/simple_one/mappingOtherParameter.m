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
Ut2Service = randi([0 imax],N_Ut, N_Service);
num_map = 0;
while any(sum(Ut2Service,1)<1) || any(sum(Ut2Service,2)<1)
    Ut2Service = randi([0 imax],N_Ut, N_Service);
    num_map = num_map+1;
    if num_map >30
        break;
    end
end
sum_UT = sum(Ut2Service,2);
for kk = 1:N_Ut
   if  sum_UT(kk)>1
       rand_int = randi([1 2],1);
       Ut2Service(kk,rand_int)= 0;
   end
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