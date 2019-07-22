function [sort_vector] = sorting(vector, N_resource, weight ,len)
    weightSumVector  = zeros(len,1);
    for i = 1 :N_resource
         weightSumVector(:) = vector(:,i)*weight(i) + weightSumVector(:);
    end
    weightSumVector = [weightSumVector, vector];
    sort_vector = sort(weightSumVector,1);
    

end

