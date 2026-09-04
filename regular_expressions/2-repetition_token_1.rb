#!/usr/bin/env ruby

text = ARGV[0].to_s
matches = text.scan(/hbt?n/)
puts matches.join
