from tqdm import tqdm  # progress bar

# Hex strings copied from output.txt
n_hex = """905767d77c44a3239d3c9306fc84d3058a630ced36f307b6297e4894519cf0a36d669b5f3b40220231531015a798af04d5bdac63abc8d14c2e2163fb51988e21fed21f049ef91b86afbce4236be5da60bf5f9f0017661351a11ba2eb2a0a0d273b4c864781d46d54255061719fef02027c3fb53bfea9ce173331e9be49c241c92857dbe383e7b234e483b39548c0422caee93c132d5e0032940f69963feb6f0ba169187a0d8c76ca8754d0d24d438df3a96b847e40f9b9b078644018c8c7ad706fc3841b6115510243c1f3215723884440e8259103db2ee4da96f2397bd6548aab7327826ec345af43f498781c2a7d3da797976591a458d0d0b6ae33dbbe7325"""
c_hex = """197dc99317cf5d378be7ee49eb10f018b6467abe4c671447c7dbf0aad3a0c1005bbaa4ddeb4e52c79a9dee0632e4065a5d2d7f8d2171079c8fe9940093166d6e1ef34723f1e127a3245d746c5bfeedd21fccdd365c43517efdb885b0a01069a603139f2411bb88c30729fc1a85a1c49718f103d3730f4a58900e339cde4243ec1ae98798368b956be1b98997e56f1ad1766057346ccee4cdbdb3e7f16a2387d724ac8be54673f4abba53af16f3774b16378484235eaceb126a4b2e95b7fef78add7914353828c13df6d07bd0a838e7c09e88d2944f73e1d609001998e77b90f106d451072004e554c1b0c13b6cf5e0b43620d94039c45fb055e1263d54c6b82f"""

# Convert hex strings to integers
n = int(n_hex, 16)
c = int(c_hex, 16)
g = 3

# Brute-force up to 2^24 
max_attempts = 2**24
for x in tqdm(range(max_attempts)):
    if pow(g, x, n) == c:
        print(f"[+] FLAG found: {x}")
        # Try decoding to string
        flag_bytes = x.to_bytes((x.bit_length() + 7) // 8, 'big')
        try:
            print("Decoded flag:", flag_bytes.decode())
        except UnicodeDecodeError:
            print("Decoded flag (raw):", flag_bytes)
        break
else:
    print("[-] FLAG not found in range.")

