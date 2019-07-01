import scipy.io as sio
mat_data = sio.loadmat('data/matlab_old.mat', squeeze_me=True)
print(mat_data['X'].shape)