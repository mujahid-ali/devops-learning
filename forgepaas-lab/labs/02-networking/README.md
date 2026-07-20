# Lab 02 — Networking and traffic diagnosis

Build traffic paths first with local containers and VMs, then repeat the Kubernetes-specific exercises after Lab 05.

| Exercise | Topics and fault to diagnose |
|---|---|
| 02.1 Layer map | OSI/TCP-IP: classify a failure as name resolution, route, TCP handshake, TLS, HTTP or application behavior |
| 02.2 DNS outage | broken resolver/search domain, stale record and positive/negative caching; inspect with `dig`, `resolvectl` or platform equivalents |
| 02.3 No return path | route table and asymmetric-routing failure between two VM networks |
| 02.4 Private egress | NAT source translation and security policy; prove source address before and after the gateway |
| 02.5 HTTPS trust | expired/wrong-host certificate, chain failure, SNI and TLS version/cipher diagnosis with `openssl s_client` and `curl -v` |
| 02.6 Edge routing | reverse proxy and load-balancer health-check mismatch; distinguish 502, 503 and 504 |
| 02.7 Encrypted tunnel | VPN concepts: draw a WireGuard/IPsec tunnel path and diagnose a peer route/key mismatch in a disposable environment |
| 02.8 Firewall | nftables/iptables rule order, stateful return traffic and least-privilege exposure |
| 02.9 Packet evidence | capture DNS, SYN/SYN-ACK, TLS and HTTP with tcpdump/Wireshark; annotate the failed packet sequence |
| 02.10 Cluster path | Pod-to-Pod, Pod-to-Service and ingress traffic; break a NetworkPolicy or Service selector and repair it |

## Break/fix 02.1 — DNS resolves locally but the service stays unreachable

**Inject:** Point a test client at a valid name whose endpoint is blocked or has no return route.

**Investigate:** Separate DNS (`dig`), route (`ip route get`), listener (`ss`), transport (`nc`/tcpdump) and HTTP (`curl -v`) evidence.

**Done when:** You can state the exact failed layer and show why a DNS change would not repair it.

## Break/fix 02.2 — TLS works by IP but not by hostname

**Inject:** Serve the echo service behind a test proxy with a certificate for a different hostname.

**Investigate:** Compare SNI, certificate SANs, chain trust and reverse-proxy upstream logs.

**Done when:** A hostname request succeeds with verified TLS and the redirect/health-check behavior is intentional.
