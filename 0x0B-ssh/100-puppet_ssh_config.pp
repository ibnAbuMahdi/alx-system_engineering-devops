# puppet ssh config file
$updates = "PasswordAuthentication no \n IdentityFile ~/.ssh/school \n"
$file = file('/etc/ssh/ssh_config')
$content = "${file}${updates}"
file { '/etc/ssh/ssh_config':
  content => $content
}

