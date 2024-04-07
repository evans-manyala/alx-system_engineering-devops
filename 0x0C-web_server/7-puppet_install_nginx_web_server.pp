# Puppet Config for installing and managing Nginx

# STEP 1: Install Nginx package
package { 'nginx':
  ensure => installed,
}

# CSETEP 2: Configuring the Nginx Server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
	    listen 80;
		listen [::]:80;
		
		server_name 54.172.62.80;

		root /var/www/html;
		index index.html index.htm index.nginx-debian.html;

		location / {
			return 200 'Hello World!';
		}

		location /redirect_me {
			return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
		}
	}
  ",
    notify => Exec['nginx_restart'],
}

# STEP 3: Enabling the default Nginx webpage
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# STEP 4: Ensuring Nginx service is always up
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# STEP 5: Executing restart Nginx service
exec { 'nginx_restart':
  command     => 'service nginx restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
