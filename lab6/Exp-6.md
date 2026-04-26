"# 🧪 Experiment 6: Docker Run vs Docker Compose

---

## 🎯 Aim

To compare Docker Run and Docker Compose and deploy applications using both methods.

---

# 🔹 PART A: Single Container (Nginx)

## Step 1: Run using Docker Run

```bash
docker run -d -p 8081:80 --name mynginx nginx:alpine
```

📸 Screenshot
![Docker Run Output](images_lab-6/step10_compose_browser.png.png)

---

## Step 2: Verify

```bash
docker ps
```

📸 Screenshot
![Docker PS](images_lab-6/step9_compose_ps.png.png)

---

## Step 3: Stop Container

```bash
docker stop mynginx
docker rm mynginx
```

📸 Screenshot
![Stop Container](images_lab-6/step11_compose_down.png.png)

---

# 🔹 PART B: Using Docker Compose (Nginx)

## Step 1: Create docker-compose.yml

📸 Screenshot
![Compose File](images_lab-6/step7_compose_yaml.png.png)

---

## Step 2: Run

```bash
docker compose up -d
```

📸 Screenshot
![Compose Up](images_lab-6/step8_compose_up.png.png)

---

## Step 3: Verify

```bash
docker compose ps
```

📸 Screenshot
![Compose PS](images_lab-6/step9_compose_ps.png.png)

---

## Step 4: Browser Output

📸 Screenshot
![Browser Output](images_lab-6/step10_compose_browser.png.png)

---

## Step 5: Stop

```bash
docker compose down
```

📸 Screenshot
![Compose Down](images_lab-6/step11_compose_down.png.png)

---

# 🔹 PART C: WordPress + MySQL (Docker Compose)

## Step 1: Create Compose File

📸 Screenshot
![Create File](images_lab-6/step12_wp_create_file.png.png)

---

## Step 2: WordPress YAML

📸 Screenshot
![WordPress YAML](images_lab-6/step13_wp_yaml.png.png)

---

## Step 3: Run Containers

```bash
docker compose up -d
```

📸 Screenshot
![WP Compose Up](images_lab-6/step14_wp_up.png.png)

---

## Step 4: Verify

```bash
docker ps
```

📸 Screenshot
![WP PS](images_lab-6/step15_wp_ps.png.png)

---

## Step 5: WordPress Setup Page

📸 Screenshot
![WP Setup](images_lab-6/step16_wp_browser.png.png)

---

## Step 6: WordPress Dashboard

📸 Screenshot
![WP Dashboard](images_lab-6/final_wordpress_dashboard.png.png)

---

## Step 7: Volumes

```bash
docker volume ls
```

📸 Screenshot
![Volumes](images_lab-6/volumes_list.png.png)

---

# 🧾 Result

The experiment was successfully completed. Docker Run and Docker Compose were used to deploy both single-container and multi-container applications.

---

# 🧾 Conclusion

Docker Compose is more efficient and easier to manage than Docker Run, especially for multi-container applications like WordPress with MySQL.

---
