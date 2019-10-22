y = zeros(2,nr);
for i =1:iter_max
    for j=1:nr
        if isnan(etha(j,i))==0
            y(1,j)=y(1,nr)+etha(j,i);
            y(2,j)= y(2,j)+1;
        end
    end
end
plot( N_min:N_step:N_max , y(1,:)./y(2,:))      