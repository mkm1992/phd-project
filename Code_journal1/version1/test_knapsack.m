clear all;
global N w r c memo;
N = 3; % number of different items to chose from
w = [3,8,5]; % weights of each item
r = [4,6,5]; % value of each item
c = 8; % total weight that can be carried 
memo = [];
V = Val(1,c)
b=c;
items = zeros(1,N);
for k=1:N
      items(k) = memo(find(memo(:,1)==k & memo(:,2)==b,1),3);
      b=b-w(k)*items(k);
end
items
function V = Val(k,b)
global N w r memo;
% N - number of different items
% w - array of weights for each item
% r - array of values for each item
m = floor(b/w(k)); % determine max number of item k for budget b
p = 0:m; % array of possible numbers of each item given budget b
if k==N  
      [V,idx] = max(r(k)*p); % base case
      memo = [memo; [k,b,p(idx)]];
else
    temp = zeros(1,length(p));
      for n=1:length(p)
          % value of k+1 item given budget if p number of item k used
          temp(n) = Val(k+1,b-w(k)*p(n));% recursion step 
      end
      [V,idx] = max(r(k)*p + temp);
      memo = [memo; [k,b,p(idx)]];
end
end