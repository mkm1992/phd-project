b = reshape(mydata,[200,1200]);
c = mean(b);
d = reshape(c,[50,1200/50]);
e = mean(d);
f = medfilt1(e,11);
f(12) = f(12)*1.2
x = [1:24]*48;
plot(x,f)