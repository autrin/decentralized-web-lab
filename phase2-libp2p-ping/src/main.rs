use std::{error::Error, time::Duration};

use libp2p::{noise, ping, tcp, yamux, Multiaddr};
use tracing_subscriber::EnvFilter;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let _ = tracing_subscriber::fmt()
        .with_env_filter(EnvFilter::from_default_env())
        .try_init();

    let mut swarm = libp2p::SwarmBuilder::with_new_identity()
        .with_tokio()
        .with_tcp(
            tcp::Config::default(),
            noise::Config::new,
            yamux::Config::default,
        )?
        .with_behaviour(|_| ping::Behaviour::default())?
        .with_swarm_config(|cfg| {cfg.with_idle_connection_timeout(Duration::from_secs(u64::MAX))
        })
        .build();

    swarm.listen_on("/ip4/0.0.0.0/tcp/0".parse()?)?; // listen to all interfaces and a random os-assigned port
    
    if let Some(addr) = std::env::args().nth(1) { // Dial the peer identified by multi-address
        let remote: Multiaddr = addr.parse()?;
        swarm.dial(remote)?;
        println!("Dialed {addr}")
    }
    Ok(())
}