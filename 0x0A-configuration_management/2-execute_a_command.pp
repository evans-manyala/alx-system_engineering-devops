#Puppet exec resource to kill the process
exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/bin/bash:/bin',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow'
}

