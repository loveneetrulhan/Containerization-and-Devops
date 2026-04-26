**Name:** Loveneet Rulhan 
**SAP ID:** 500123392
**Batch:** B3 (CCVT)

# 🧪 Experiment 4: Docker Essentials

## 🎯 Aim

To understand Docker basics including Dockerfile, images, containers, multi-stage builds, and Docker Hub.

---

## 🔹 Step 1: Create Project Directory

```bash
mkdir flask-app
cd flask-app
```

![Step 1](images_lab-4/step1_create_project.png.png)

---

## 🔹 Step 2: Create Flask Application

```bash
nano app.py
```

![Step 2](images_lab-4/step2_app_py.png.png)

---

## 🔹 Step 3: Create requirements.txt

```bash
nano requirements.txt
```

![Step 3](images_lab-4/step3_requirements.png.png)

---

## 🔹 Step 4: Create Dockerfile

```bash
nano Dockerfile
```

![Step 4](images_lab-4/step4_dockerfile.png.png)

---

## 🔹 Step 5: Verify Files

```bash
ls
```

![Step 5](images_lab-4/step5_project_files.png.png)

---

## 🔹 Step 6: Build Docker Image

```bash
docker build -t flask-app .
```

![Step 6](images_lab-4/step6_docker_build.png.png)

---

## 🔹 Step 7: Run Container

```bash
docker run -p 5000:5000 flask-app
```

![Step 7](images_lab-4/step7_container_running.png.png)

---

## 🔹 Step 8: Output

![Step 8](images_lab-4/step8_browser_output.png.png.png)

---

## 🔹 Step 9: Create .dockerignore

```bash
nano .dockerignore
```

![Step 9](images_lab-4/step9_dockerignore.png.png)

---

## 🔹 Step 10: Docker Images

```bash
docker images
```

![Step 10](images_lab-4/step10_docker_images.png.png)

---

## 🔹 Step 11: Tag Image

```bash
docker tag flask-app <your-username>/flask-app:1.0
```

![Step 11](images_lab-4/step11_tagging.png.png)

---

## 🔹 Step 12: Inspect Image

```bash
docker inspect flask-app
```

![Step 12](images_lab-4/step12_inspect.png.png)

---

## 🔹 Step 13: Run in Background

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

![Step 13](images_lab-4/step13_background_run.png.png)

---

## 🔹 Step 14: Running Containers

```bash
docker ps
```

![Step 14](images_lab-4/step14_docker_ps.png.png)

---

## 🔹 Step 15: Logs

```bash
docker logs flask-container
```

![Step 15](images_lab-4/step15_logs.png.png)

---

## 🔹 Step 16: Stop Container

```bash
docker stop flask-container
```

![Step 16](images_lab-4/step16_stop.png.png)

---

## 🔹 Step 17: Multi-stage Dockerfile

![Step 17](images_lab-4/step17_multistage_file.png.png)

---

## 🔹 Step 18: Build Multi-stage

```bash
docker build -f Dockerfile.multi -t flask-multi .
```

![Step 18](images_lab-4/step18_multistage_build.png.png)

---

## 🔹 Step 19: Compare Images

```bash
docker images
```

![Step 19](images_lab-4/step19_image_compare.png.png)

---

## 🔹 Step 20: Login

```bash
docker login
```

![Step 20](images_lab-4/step20_login.png.png)

---

## 🔹 Step 21: Tag for Hub

```bash
docker tag flask-app <your-username>/flask-app:latest
```

![Step 21](images_lab-4/step21_tag.png.png)

---

## 🔹 Step 22: Push Image

```bash
docker push <your-username>/flask-app:latest
```

![Step 22](images_lab-4/step22_push.png.png)

---

## 🧾 Result

The experiment was successfully completed. Docker images were created, containers were run, and images were pushed to Docker Hub.

---

## 🧾 Conclusion

Docker simplifies deployment and improves portability and scalability.
