b = reshape(mydata,[200,1200]);
c = mean(b);
plot(medfilt1(c,11))