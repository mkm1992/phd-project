%% Find M
VNF_NUM_UE =  zeros(1,N_UE);
VNF_NUM = zeros(1,S);
Delay_Slice1_UE = zeros(1,N_UE);
t = 0;
for s = 1:S
    for numberU = 1:UE_S(s)
        t = t+ 1;
        VNF_NUM_UE(t) = ceil((w1(s).*rate_UE(t)-w2(s))./((w3(s).*rate_UE(t)-w4(s))));
        Delay_Slice1_UE(t) = 1/(rate_UE(t)-lambda_m(s));
        VNF_NUM(s) =  max(VNF_NUM(s),VNF_NUM_UE(t));
        Delay_Slice1(s) = max(Delay_Slice1(s),Delay_Slice1_UE(t));
    end
    
end

VNF_NUM(:) = ceil((w1(:).*R_s(:)-w2(:))./((w3(:).*R_s(:)-w4(:))));

Delay_tot = zeros(1,S);
for s = 1:S
    Delay_Slice(s) = 3/(mu(s)- alpha_m(s)/VNF_NUM(s));
    %Delay_Slice1(s) =  1/(R_s(s)/UE_S(s)-lambda_m(s));
    Delay_tot(s) =  Delay_Slice(s) +Delay_Slice1(s);
end