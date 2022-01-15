%% Find M


    VNF_NUM(:) = ceil((w1(:).*R_s(:)-w2(:))./((w3(:).*R_s(:)-w4(:))));


% for s = 1:S
%     Delay_Slice(s) = 1/(mu(s)- alpha_m(s)/VNF_NUM(s));
% end