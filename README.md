
Plaintext

```
  __              _      _
 / _|___  ___  ___ (_) ___| |_ _   _
| |_/ __|/ _ \/ __|| |/ _ \ __| | | |
|  _\__ \ (_) \__ \| |  __/ |_| |_| |
|_| |___/\___/|___/|_|\___|\__|\__, |
                               |___/

```

> **"Control is an illusion."**
> 
> The **Fsociety Protocol** is a Python-based terminal environment designed for reconnaissance, asset tracing, and secure communication. We are finally free.

----------

## 💀 SYSTEM STATUS

## ⚡ DEPLOYMENT

### 1. clone_repo.sh

Download the protocol to your local machine.

Bash

```
https://github.com/Gh0sttakhs/Fsociety.git
cd Fsociety

```

### 2. initiate.py

No external libraries required. Pure Python standard library.

Bash

```
python3 fsociety.py

```

### 3. authentication

The system is locked. You need the master key.

Plaintext

```
[!] AUTHENTICATION REQUIRED
hint: Who is the leader?
```

----------

## 🛠 COMMAND PROTOCOL

Once inside the shell (`root@fsociety:~$`), use the following tools:

| COMMAND | ARGUMENT | DESCRIPTION |
| :--- | :--- | :--- |
| `trap` | `N/A` | **[HONEYPOT]** Starts a local HTTP server to log victim IP/User-Agent. |
| `scan` | `<ip/domain>` | **[RECON]** Scans target for open ports (FTP, SSH, HTTP, etc). |
| `trace` | `<ip>` | **[GEO-OSINT]** Triangulates the physical location of an IP address. |
| `mask` | `<url>` | **[OBSCURE]** Masks a malicious URL using TinyURL API. |
| `encrypt` | `<text>` | **[SECURE]** Encodes message to Base64. |
| `decrypt` | `<code>` | **[REVEAL]** Decodes Base64 message. |
| `check` | `<password>` | **[AUDIT]** Verifies password strength/complexity. |
| `quote` | `N/A` | **[WISDOM]** Dispenses fsociety philosophy. |
| `exit` | `N/A` | **[LOGOUT]** Terminates the session. |
----------

## 🕸 HONEYTRAP USAGE

To expose the local `trap` server to the public internet (WAN) and catch targets outside your network:

1.  Type `trap` in the console.
    
2.  Open a **new terminal session**.
    
3.  Run the following SSH tunneling command:
    
    Bash
    
    ```
    ssh -R 80:localhost:8080 nokey@localhost.run
    
    ```
    
4.  Send the generated `https://...` link to the target.
    
5.  Watch the main terminal for hits.
    

----------

## ⚠️ DISCLAIMER

Diff

```
- [!] WARNING:
- THIS TOOL IS FOR EDUCATIONAL PURPOSES AND CTF SIMULATIONS ONLY.
- THE CREATOR IS NOT RESPONSIBLE FOR ANY ILLEGAL ACTS COMMITTED.
- DO NOT SCAN OR ATTACK TARGETS YOU DO NOT OWN.

```

> **"We are fsociety. We are finally free. We are finally awake."**
