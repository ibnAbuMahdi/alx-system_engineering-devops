# install and set up nginx server

sh = "/usr/env/bash"
new="\"server_name _;\n\t location \/redirect_me {\n\treturn 301 https\:\/\/www.google.com;\n\t}\""
cntnt = "#!${sh} \nsudo apt-get -y update; sudo apt-get -y install nginx && sudo ufw allow 'Nginx HTTP'; sudo service nginx start; if [[ ! -d /var/www/html ]];then\n sudo ${sh}/mkdir /var/www/html\nfi\n sudo ${sh}/chmod 0666 /var/www/html; sudo ${sh}/touch /var/www/html/index.html && sudo ${sh}/chmod 0777 /var/www/html/index.html && ${sh}/echo 'Hello World!'>/var/www/html/index.html; sudo ${sh}/chmod a+wrx /etc/nginx/sites-available/ && sudo ${sh}/chmod a+wrx /etc/nginx/sites-available/default; sudo ${sh}/chmod a+wrx /etc/nginx/sites-enabled/default;  sed -i \"s/server_name _;/${new}/\" /etc/nginx/sites-available/default; sudo service nginx reload "
file { 'nginx_setup':
  path   => '~/',
  ensure => file,
  content => $cntnt,
  mode => '0777'
}
exec { 'setup_server':
  command  => "./root/nginx_setup"
}
