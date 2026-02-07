# Experiment 1: Comparison of Virtual Machine and Container

## Aim
To study and compare **Virtual Machines (VMs)** and **Containers** by setting up a Virtual Machine using **Vagrant** and running a web server (**Nginx**) inside it, then analyzing the differences between VM-based and container-based virtualization.

---

## Objectives
- To understand the concept of virtualization using Virtual Machines
- To learn the basics of containerization
- To deploy and test a web server inside a VM
- To compare VM and Container based architectures

---

## Software / Tools Required
- Host OS: Windows 10 / 11  
- Virtualization Tool: VirtualBox  
- VM Provisioning Tool: Vagrant  
- Guest OS: Ubuntu  
- Web Server: Nginx  
- Browser: Google Chrome / Edge  

---

## Theory

### Virtual Machine (VM)
A Virtual Machine is a software-based emulation of a physical computer. Each VM runs its own **guest operating system**, along with applications and required libraries. VMs are managed by a **hypervisor**.

**Features of VM:**
- Full OS isolation
- Higher resource usage
- Strong security
- Slower startup time

---

### Container
A container is a lightweight virtualization method that packages an application and its dependencies but **shares the host OS kernel**. Containers are faster and more efficient than VMs.

**Features of Containers:**
- Lightweight and fast
- No separate guest OS
- Lower resource consumption
- Faster startup time

---

## Procedure
## Screenshots

### Nginx Running Inside Virtual Machine
![Nginx Status](screenshot/Screenshot%202026-01-21%20093039.png)

### Starting Nginx Service
![Starting Nginx](screenshot/Screenshot%202026-01-21%20093257.png)

### Output on Browser (localhost:8080)
![Nginx Welcome Page](screenshot/Screenshot%202026-01-28%20084243.png)

### Running Nginx Using Docker Container
![Docker Nginx Commands](screenshot/Screenshot%202026-01-28%200848xx.png)


### Step 1: Initialize Vagrant Virtual Machine
```bash
vagrant init
vagrant up
vagrant ssh
# Containerization-and-Devops
