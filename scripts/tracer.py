import subprocess

# open file in append mode to write results
f = open("traceroute_results.txt", "a+")

# open file in read mode to parse hostnames
r = open("hosts.txt", "r")

hostname=""
port=""

lines = r.readlines()
for line in lines:
    # options
    args=["traceroute"]
    # append hostname
    line=line.strip().split(" ")
    if len(line) == 2:
    	hostname, port = str(line[0]), str(line[1])
    	args.append(hostname, "-p", port)
    else:
    	hostname = str(line[0])
    	args.append(hostname)
    
    print(args)
    # run command, redirect stdout to file f
    ping = subprocess.run(
            args,
            stdout=f,
            encoding="UTF-8",
            
    )

# close open file handles
f.close()
r.close()
