function [outMat] = modifiedMat(mat)
    [len, wid] = size(mat);
    outMat = zeros(len, wid);
    for i=1:len
        for j = 1:wid
           if  mat(i,j) > 0
               outMat(i,j) =1;
           end
        end
    end
end

