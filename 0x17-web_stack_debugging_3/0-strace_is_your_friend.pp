# puppet file that solves 500 error for web-stack-debugging 3

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('class-wp-local.phpp', 'class-wp-local.php'),
}

