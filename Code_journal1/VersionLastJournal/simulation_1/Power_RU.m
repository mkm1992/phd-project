function [out] = Power_RU(N_UE,Popt,beamForming,var_q,N_RU,j)
    Popt1 = cvx(eye(N_UE));
    for i=1:N_UE
       Popt1(i,i) = Popt(i); 
    end
    for i =1:N_RU
       Pow_RU(i) = (abs(beamForming(i,:)*Popt1*beamForming(i,:).'))+var_q; 
    end
    out = Pow_RU(j);
end

