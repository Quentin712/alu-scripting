#!/usr/bin/env ruby

text = ARGV[0].to_s
matches = text.scan(/School/)
puts matches.join
