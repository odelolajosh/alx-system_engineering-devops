# Install nginx web server with puppet
exec { 'install nginx':
    provider => shell,
    path     => '/usr/bin:/bin',
    command  => 'sudo apt-get update; sudo apt-get install -y nginx; echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html; sudo sed -i "/server_name _;/a \\\n\tlocation /redirect_me {\n\t\treturn 301 https://github.com/odelolajosh;\n\t}" /etc/nginx/sites-available/default; sudo service nginx start'
}