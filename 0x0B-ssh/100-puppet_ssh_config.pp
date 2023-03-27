# puppet ssh config file
$updates = '\nPasswordAuthentication no\nIdentityFile ~/.ssh/school\n'
$file = file('/etc/ssh/ssh_config')
$content = "${file}${updates}"
file { '/etc/ssh/ssh_config':
  content => $content
}

