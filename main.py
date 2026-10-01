"""6.1.0.4 Man in the Middle.

Build on your poisoning from the previous exercise: copy your main.py, arp.py and
ethernet.py into this folder. Keep poisoning BOTH endpoints — and this time also forward
the traffic that arrives at you, so the two stay connected (a real MITM, not a DoS).
"""
import json


def main() -> int:
    cfg = json.load(open("config.json"))
    iface = cfg["iface"]
    endpoint_a, endpoint_b = cfg["endpoints"]

    # TODO: poison both endpoints (as before), AND make sure the packets that now arrive
    #       at you are forwarded on to their real destination. See the README appendix on
    #       /proc/sys/net/ipv4/ip_forward.
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
