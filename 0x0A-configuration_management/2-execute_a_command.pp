# execute a kill command on process killmenow

exec { 'kill killmenow':
  command => '/usr/bin/pkill killmenow'
}
