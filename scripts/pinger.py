import subprocess

# open file in append mode to write results
f = open("ping_results.txt", "a+")

# open file in read mode to parse hostnames
r = open("hosts.txt", "r")

for line in r:
    # options
    args=["ping", "-c4"]
    # append hostname
    args.append(line.strip())
    # run command, redirect stdout to file f
    ping = subprocess.run(
            args,
            stdout=f
    )

# close open file handles
f.close()
r.close()
