Popt1 = Popt.^0.5;
for i = 1:N_rrh
    Prrh(i) = abs(norm(v(mm+M*(s-1),K*(s-1)+1:K*s)*(Popt1(:,s)))^2)+var_q;
end



for i = 1:N_rrh
    Prrh(i) = abs(norm(v(mm+M*(s-1),K*(s-1)+1:K*s)*(Popt1(:,s)))^2)+var_q;
    Crrh(i) = log2(Prrh(i)/var_q);
end