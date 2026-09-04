#!/usr/bin/env ruby
message = ARGV[0]
from = message.match(/\[from:(.*?)\]/)[1]
to = message.match(/\[to:(.*?)\]/)[1]
flags = message.match(/\[flags:(.*?)\]/)[1]

puts "#{from},#{to},#{flags}"
