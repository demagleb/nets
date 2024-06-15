import subprocess
import platform
import click

IP_HEADER_SIZE = 20
ICMP_HEADER_SIZE = 8

def ping(host: str, packet_size: int):
    payload_flag = "-l" if platform.system() == "Windows" else "-s"
    fragmentation_flag = ["-f"] if platform.system() == "Windows" else ["-M", "do"]
    res = subprocess.run(["ping", host, "-c", "1"] + fragmentation_flag + [payload_flag, str(packet_size - IP_HEADER_SIZE - ICMP_HEADER_SIZE)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return res.returncode == 0


@click.command()
@click.option("--host", help="Host")
def main(host):
    try:
        if subprocess.run(["ping", "-c", "1", host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            print(f"Host {host} is unreachable")
            return 1
    except Exception as e:
        print("Exception in subprocess")
        return 1

    l = 28
    r = 2281

    while r - l != 1:
        m = (l + r) // 2
        try:
            good = ping(host, m)
        except:
            print("Exception in subprocess")
            return 1
        if good:
            l = m
        else:
            r = m

    print(f"MTU on path to {host} is {l} bytes")

if __name__ == "__main__":
    main()
