
# sudo mn --custom ~/mininet/custom/myTopo.py --topo mytopo

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        se1 = self.addHost( 'se1' )
        se2 = self.addHost( 'se2' )

        dns1 = self.addHost( 'dns1' )
        dns2 = self.addHost( 'dns2' )

        sw1 = self.addSwitch( 'sw1' )
        sw2 = self.addSwitch( 'sw2' )

        # Add links
        self.addLink( sw1, sw2 )

        self.addLink( sw1, h1 )
        self.addLink( sw1, h2 )
        
        self.addLink( sw1, dns1 )

        self.addLink( sw2, se1 )
        self.addLink( sw2, se2 )

        self.addLink( sw2, dns2 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
