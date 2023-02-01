#!/usr/bin/env ruby
# text me :(^(\w+)$|((\+?\d{1,3})?^\d{10,10}$)#

s = ARGV[0].scan(/\[[^\]]*from:(\w+|((\+?\d{1,3})?\d{10,10}))\]/)[0]
puts s[0]
