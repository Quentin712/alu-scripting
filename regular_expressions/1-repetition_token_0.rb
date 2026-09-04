#!/usr/bin/env ruby

text = ARGV[0].to_s
matches = text.scan(/hbt{2,5}n/)
puts matches.join

