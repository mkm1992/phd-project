v = zeros(N_rrh,N_Ut);
for i=1:N_Ut
    g = G(:,i);
    v(:,i) = conj(g)/norm(g);
end
ro = 0;
%v = H*(H'*H+ro*eye(K*S))^(-1);
v(:,:) = v(:,:)/norm(v(:,:));
