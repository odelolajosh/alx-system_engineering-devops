# configure passwordless ssh login to the remote host
exec { 'echo':
    path    => '/usr/bin:/bin',
    command => 'echo \tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no >> /etc/ssh/ssh_config',
    returns => [0, 1]
}