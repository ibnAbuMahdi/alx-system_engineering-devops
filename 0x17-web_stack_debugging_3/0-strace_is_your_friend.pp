# puppet file that solves 500 error for web-stack-debugging 3

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => regsubst(file('/var/www/html/wp-settings.php'), 'class-wp-locale.phpp', 'class-wp-locale.php')
}
