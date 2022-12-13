def hough_lines(orig_im, edge_im, rho_steps=480, theta_steps=480, min_votes=100):
    # Get image width and height
    h, w = orig_im.shape
 
    # Pythagoras to get diagonal line: c = sqrt(w^2+h^2)
    c = np.int16(np.sqrt(np.square(w) + np.square(h))) 
    
    # parameter space lattice settings
    rho_dim = np.arange(-c, c, step=2*c/rho_steps)
    theta_dim = np.arange(0, 180, step=180/theta_steps)

    # move origin to middle in point of view of edge pixels
    # by substracting half of image height and width
    h_half, w_half = h/2, w/2
    edge_mid = np.argwhere(edge_im>0) - np.array([[h_half, w_half]])
    
    # calculate rho values for the nonzero edgepoints
    # precalculate cos and sin to a np array to make multiplication faster
    stct_list = np.array([np.sin(np.deg2rad(theta_dim)), np.cos(np.deg2rad(theta_dim))])
    # rho = y*np.sin(theta)+x*np.cos(theta):  edge_mid_{i} stct_list^i
    rho = np.dot(edge_mid, stct_list)

    # collect votes by using histogram to speed up things
    # numpy.histogram2d(x, y, bins=10, range=None, normed=None, weights=None, density=None)
    # Returns:
    #  H : ndarray (nx, ny)
    #  xedges: The bin edges along the first dimension.
    #  yedges: The bin edges along the second dimension.
    accumulator, thetas, rhos = np.histogram2d(x=np.tile(theta_dim, rho.shape[0]), #need xy later to be same shape
                                               y=rho.flatten(),
                                               bins=[theta_dim, rho_dim]
                                               ) 
    # transpose to get proper lines
    accumulator = np.transpose(accumulator)
    
    # filter lines based on votes
    # and get their index
    lines = np.argwhere(accumulator >= min_votes)
    
    return accumulator, lines, thetas, rhos, theta_dim, rho_dim
