

#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def armyNet():

    # Create an instance of Mininet
    net = Mininet( controller=RemoteController )

    # Add a remote controller
    info( '*** Adding the remote controller\n' )
    net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=8762 )

    # Add 100 hosts
    info( '*** Adding hosts\n' )
    for i in range(100):
        net.addHost( 'h%s' % i )

    # Add a switch
    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )

    # Add links between hosts and switch
    info( '*** Creating links\n' )
    for i in range(100):
        net.addLink( 'h%s' % i, s1 )

    # Start network
    info( '*** Starting network\n')
    net.start()

    # Configure the army sdn
    info( '*** Configuring army sdn\n' )
    s1.cmd( 'ovs-vsctl set-manager tcp:127.0.0.1:6633' )
    s1.cmd( 'ovs-vsctl set bridge s1 protocols=OpenFlow13' )

    # Run Mininet CLI
    CLI( net )

    # Stop network
    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    armyNet()
