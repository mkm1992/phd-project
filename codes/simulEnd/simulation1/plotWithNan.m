y1 = zeros(2,nr);
for i =1:iter_max
    for j=1:nr
        if isnan(etha(j,i))==0 && etha1(j,i)>0 
            y1(1,j)=y1(1,j)+etha(j,i);
            y1(2,j)= y1(2,j)+1;
        end
    end
end
plot( N_min:N_step:N_max , y1(1,:)./y1(2,:)/BW)  

hold on
y = zeros(2,nr);
for i =1:iter_max
    for j=1:nr
        if isnan(etha1(j,i))==0 && etha1(j,i)>0 
            y(1,j)=y(1,j)+etha1(j,i);
            y(2,j)= y(2,j)+1;
        end
    end
end
plot( N_min:N_step:N_max , y(1,:)./y(2,:)/BW)   
%%
b1 = y1(1,:)./y1(2,:);
b = y(1,:)./y(2,:);
plot( N_min:N_step:N_max , a1/BW)
hold on
plot( N_min:N_step:N_max , a/BW) 
%%
plot( N_min:N_step:N_max , b1/BW)
hold on
plot( N_min:N_step:N_max , b/BW) 