function [mat_sum] = makeone(mat_sum)
      for i = 1:length(mat_sum)
        if mat_sum(i)>0
            mat_sum(i) = 1;
        end
      end
end

