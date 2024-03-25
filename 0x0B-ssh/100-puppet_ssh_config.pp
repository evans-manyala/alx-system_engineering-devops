# This puppet config script sets up your client SSH configuration
# file so that you can connect to a server without typing a password

exec {'Puppet Configuration':
  path    => '/usr/bin:/bin',
  command => 'echo -e "Host 52.207.70.238\n	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
}