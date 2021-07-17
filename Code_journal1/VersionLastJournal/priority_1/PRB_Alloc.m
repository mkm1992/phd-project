for i =1:N_UE*2/3
    if mod(i,N_PRB)==0
       PRB_UE(N_PRB,i)= 1;
    else
        PRB_UE(mod(i,N_PRB),i) =1 ;
    end

end