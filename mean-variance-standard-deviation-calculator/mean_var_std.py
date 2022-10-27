import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  calculations = {}
  list = np.array(list)
  list = np.reshape(list,(3,3))
  calculations['mean'] = [np.mean(list, axis=0).tolist(), np.mean(list,axis=1).tolist(), np.mean(list)]
  calculations['variance'] = [np.var(list, axis=0).tolist(), np.var(list,axis=1).tolist(), np.var(list)]
  calculations['standard deviation'] = [np.std(list, axis=0).tolist(), np.std(list,axis=1).tolist(), np.std(list)]
  calculations['max'] = [np.max(list, axis=0).tolist(), np.max(list,axis=1).tolist(), np.max(list)]
  calculations['min'] = [np.min(list, axis=0).tolist(), np.min(list,axis=1).tolist(), np.min(list)]
  calculations['sum'] = [np.sum(list, axis=0).tolist(), np.sum(list,axis=1).tolist(), np.sum(list)]
  return calculations