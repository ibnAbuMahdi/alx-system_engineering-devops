# install and set up nginx server

exec { 'install nginx':
  command   => 'sudo apt-get -y install nginx'
}
exec { 'set up firewall':
  command  => "sudo ufw allow 'Nginx HTTP'"
}
exec { 'create index.html':
  command => 'sudo touch /var/www/html/index.html'
}
exec { 'change mode':
  command => 'sudo chmod 0777 /var/www/html/index.html'
}
exec { 'input text':
  command => "echo 'Hello World!'>/var/www/html/index.html"
}
exec { 'redirect: chmod':
  command => 'sudo chmod a+wrx /etc/nginx/sites-available'
}
exec { 'redirect: string':
  command => "new='server_name _;\n\t location \/redirect_me {\n\treturn 301 https\:\/\/www.google.com;\n\t}'"
}
exec { 'redirect: sed':
  command => "sed -i 's/server_name _;/${new}/' /etc/nginx/sites-available/default && sudo service nginx reload"
}
