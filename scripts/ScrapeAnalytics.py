import argparse
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("folder", help="logs folder")
args = ap.parse_args()

if not os.path.isdir(args.folder):
    print("Invalid folder", file=sys.stderr)
    exit(1)

csv = [["time"],{}]

for file in os.listdir(args.folder):
    if csv[-1] != {}:
        csv.append({})
    rel_file = f"{args.folder}/{file}"
    with open(rel_file, "r") as f:
        try:
            dat = f.read()
        except UnicodeDecodeError as e:
            continue
        if "AnalyticsEngine" not in dat:
            continue
        if not ("Begin Match Analytics" in dat and "End Match Analytics" in dat):
            continue
        csv[-1]["time"] = file.replace("RobotLog-", "").replace(".txt", "")
        for line in dat.split("\n"):
            if "AnalyticsEngine" in line:
                vals = line.split(" ")
                if "-----" in vals[2] or "Cleared event map" in line:
                    continue
                vals = vals[2:]
                nline = (''.join([f"{v} " for v in vals])).split(":")
                action = nline[0]
                count = int(nline[1].strip())
                if action not in csv[0]:
                    csv[0].append(action)
                csv[-1][action] = count
                
print(''.join([f"{h}, " for h in csv[0]]))
for line in csv[1:]:
    line:dict=line
    for head in csv[0]:
        if head in line.keys():
            print(str(line[head])+", ", end="")
        else:
            print("0, ", end="")
    print("")
                