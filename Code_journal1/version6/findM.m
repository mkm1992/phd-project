%% Find M
for s = 1:S
    VNF_NUM(s) = ceil(alpha_m(s)*(delay_max(s) - xx(s))/(mu(s)*(delay_max(s) - xx(s)) - 1));
end