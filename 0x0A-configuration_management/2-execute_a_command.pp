# kill process killmenow

package { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  return   => [0, 1]
}