# This puppet config script sets up your client SSH configuration
# file so that you can connect to a server without typing a password

$conf = "IdentityFile ~/.ssh/school
PubKeyAuthentication yes
PasswordAuthentication no
"

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => $conf,
}