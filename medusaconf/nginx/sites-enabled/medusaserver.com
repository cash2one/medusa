upstream medusaserver {
    server 127.0.0.1:8000 fail_timeout=3;
}

server {
    listen 80 default_server;
    server_name medusaserver.com;

    access_log /var/log/nginx/medusaserver.com-access.log format_combined;
    error_log /var/log/nginx/medusaserver.com-error.log;

    location /static {
        root /home/workspace/;
    }

    location / {
         proxy_pass http://medusaserver;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}