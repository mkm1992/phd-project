Popt1 = Popt.^0.5;
PrecodingMat = PrecodingMat.*rrh2Ut;

for i = 1:N_rrh
    Prrh(i) = abs(norm(PrecodingMat(i,:)*Popt1')^2)+var_q;
    Crrh(i) = log2(Prrh(i)/var_q);
end



