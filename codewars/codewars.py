def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
      return 0 
    else:
      total = sum(range(begin_number, end_number+1, step))
      return total
sequence_sum(1,5,3)