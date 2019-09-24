AllPRB2UT1= PRB2Slice* transpose(service2slice)*transpose(Ut2Service);
AllPRB2UT = modifiedMat(AllPRB2UT1);
PRB_Numbermap = zeros(1,N_PRB);

Ut_map = zeros(N_Ut, N_PRB);
for i =1:N_Ut
    if mod(i,N_PRB)==0
       Ut_map(i,N_PRB)= 1;
    else
        Ut_map(i,mod(i,N_PRB)) =1 ;
    end

end