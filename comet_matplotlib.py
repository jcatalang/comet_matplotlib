def comet(x,y, step = 1,time=0.01):
    """

    Displays a 2D comet plot: 2D trajectory along time.

    """
    import numpy as np
    import matplotlib.pyplot as plt

    x, y = np.asarray(x[::step]), np.asarray(y[::step])
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    plot = plt.plot(x[0], y[0])[0] 
    for i in range(len(x)):
        plot.set_data(x[:i+1], y[:i+1])
        plot2 = plt.plot(x[i], y[i],'k.')
        plt.pause(time)
        plot2.pop(0).remove()
    return None

def comet3(x,y,z, step=1, ani_interval = 10, lims = [[0,0],[0,0],[0,0]]):
    """

    Displays a 3D comet plot: 3D trajectory along time.

    """
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import animation

    # Plotting mesh
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    plt.ioff()

    x, y, z = np.asarray(x[::step]), np.asarray(y[::step]), np.asarray(z[::step])
    try:
        data  = np.transpose(np.concatenate((x,y,z), axis = 1))
    except:
        data  = np.transpose(np.concatenate((x[:,None],y[:,None],z[:,None]), axis = 1))

    line , = ax.plot(x[:1], y[:1], z[:1])
    point, = ax.plot(x[:1], y[:1], z[:1], markerfacecolor='k', markeredgecolor='k', marker='.', markersize=10)

    def update(i, data, line, point):
        line.set_data(data[:2, :i])
        line.set_3d_properties(data[2, :i])
        point.set_data(data[:2, i])
        point.set_3d_properties(data[2, i])

    # Setting the axes properties
    lims = np.array(lims)
    xmin, xmax = lims[0,:]
    ymin, ymax = lims[1,:]
    zmin, zmax = lims[2,:]
    if np.all(lims==0):
        xmin, xmax = np.min(x), np.max(x)
        ymin, ymax = np.min(y), np.max(y)
        zmin, zmax = np.min(z), np.max(z)
    else:
        xmin, xmax = lims[0,:]
        ymin, ymax = lims[1,:]
        zmin, zmax = lims[2,:]
    

    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.set_zlim(zmin,zmax)
    xrange , yrange , zrange  = abs(xmax - xmin), abs(ymax - ymin), abs(zmax - zmin)
    xaspect, yaspect, zaspect = 1.4 * xrange/xrange, 1.4 * yrange/xrange,  1.4 * zrange/xrange
    ax.pbaspect = [xaspect, yaspect, zaspect]
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    frs = len(x)

    # fargs need to be the arguments of func, without taking into account the first one, which is the counter.
    # they need to be iterable
    ani = animation.FuncAnimation(fig, func=update, frames=frs,\
                     fargs=(data, line, point), interval = ani_interval, blit=False, repeat = False)

    plt.show()
    plt.ion()

    return None


## Examples:

# t = np.arange(0, 4*np.pi, np.pi/50)
# x = -np.sin(t)**2 + np.sin(t/2)
# y =  np.cos(t)**3 + np.cos(t/2)**2
 
# comet(x,y)

# t = np.arange(0, 4*np.pi, np.pi/50)
# x = -np.sin(t)**2 + np.sin(t/2)
# y =  np.cos(t)**3 + np.cos(t/2)**2
# z =  np.cos(t)    + np.cos(t/2)

# comet3(x,y,z)