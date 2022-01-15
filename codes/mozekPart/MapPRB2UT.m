AllPRB2UT1= PRB2Slice* transpose(service2slice)*transpose(Ut2Service);
AllPRB2UT =AllPRB2UT1;% modifiedMat(AllPRB2UT1);
PRB_Numbermap = zeros(1,N_PRB);

for j = 1:N_Ut
    indexUEPRB = find(AllPRB2UT(:,j)==1);
    [min_prb,ind] = min(PRB_Numbermap(indexUEPRB));
    PRB_Numbermap(indexUEPRB(ind)) = PRB_Numbermap(indexUEPRB(ind)) + 1;
    Ut_map(j,indexUEPRB(ind)) = 1;
    
end