# puppet file that solves 500 error for web-stack-debugging 3

file { '/path/to/wp-settings.php':
  ensure  => file,
  content => file('/path/to/wp-settings.php').content.gsub('class-wp-local.phpp', 'class-wp-local.php'),
}

