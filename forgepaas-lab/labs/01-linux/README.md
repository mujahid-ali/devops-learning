# Lab 01 — Linux operations on disposable VMs

Use the free RHEL-compatible virtual machines for this lab. Do not perform LVM, RAID, SELinux, routing or firewall changes on the macOS host. Snapshot a VM before each storage exercise.

## Competency map

| Exercise | Topics and required evidence |
|---|---|
| 01.1 Runaway worker | processes, scheduler, signals, CPU/memory inspection; capture `ps`, `top`/`pidstat`, then stop gracefully before escalation |
| 01.2 Failed daemon | systemd unit, dependencies, journal, exit code and restart policy; repair a deliberately invalid `ExecStart` |
| 01.3 Memory pressure | virtual memory, OOM signals, limits and cgroups; compare host process and constrained container behavior |
| 01.4 Full filesystem | ext4/XFS, inode versus block exhaustion, mount options and safe cleanup; grow a test filesystem only after proving the cause |
| 01.5 Expand data safely | LVM PV/VG/LV inspection, extension, filesystem grow and rollback plan using an attached disposable disk |
| 01.6 Degraded redundancy | RAID status, simulated member failure, rebuild observation and service impact statement |
| 01.7 SELinux denial | enforcing/permissive state, labels, audit log and a least-privilege repair with `semanage` or a policy—not global disablement |
| 01.8 Isolation anatomy | cgroups and namespaces from a running container; map PID, mount and network namespaces back to the host |
| 01.9 Slow service | `uptime`, `vmstat`, `iostat`, `ss`, `sar`/`pidstat` and a measured performance-tuning hypothesis |
| 01.10 Remote access | SSH key permissions, host verification, agent forwarding risk, `sshd` logs and package-manager recovery |

## Break/fix 01.1 — A service starts manually but fails under systemd

**Inject:** Create a test unit whose `ExecStart` uses a relative path or an inaccessible configuration file.

**Investigate:** `systemctl status`, `journalctl -u`, unit effective configuration, executable ownership/mode and SELinux context.

**Repair:** Use an absolute executable path, a dedicated service account, a valid working directory and the least required permissions. Enable and restart the unit.

**Done when:** The service survives a restart and its logs identify the startup configuration.

## Break/fix 01.2 — Port 8080 is unreachable only in enforcing mode

**Inject:** Bind a test service to a nonstandard port on a RHEL-compatible VM under SELinux enforcing mode.

**Investigate:** `getenforce`, `ss -lntp`, `firewall-cmd`, `ausearch -m AVC`, and port labelling.

**Repair:** Apply the narrow port/type or file-label change required by the service. Do not disable SELinux or open broad firewall rules.

**Done when:** The service remains reachable after reboot with SELinux enforcing and evidence explains the exact policy cause.

## Break/fix 01.3 — Filesystem full during a deployment

**Inject:** Fill a dedicated test filesystem or consume its inodes with tiny files.

**Investigate:** Distinguish blocks from inodes using `df -h` and `df -i`; find ownership using `du`, `lsof +L1`, and service logs.

**Repair:** Clean only the identified data, then expand the test LVM volume if capacity planning supports it.

**Done when:** The service recovers, the root cause is measured, and a monitoring threshold is proposed.
