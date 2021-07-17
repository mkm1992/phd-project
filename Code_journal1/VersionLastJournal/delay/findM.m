%% Find M


    VNF_NUM(:) = ceil((w1(:).*R_s(:)-w2(:))./((w3(:).*R_s(:)-w4(:))));

Delay_tot = zeros(1,S);
for s = 1:S
    Delay_Slice(s) = 3/(mu(s)- alpha_m(s)/VNF_NUM(s));
    Delay_Slice1(s) =  1/(R_s(s)/UE_S(s)-lambda_m(s));
    Delay_tot(s) =  Delay_Slice(s) +Delay_Slice1(s);
end