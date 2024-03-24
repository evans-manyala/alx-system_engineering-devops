# Exec resource to kill the process
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
