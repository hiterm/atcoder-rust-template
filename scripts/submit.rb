#!/usr/bin/env ruby

require 'open3'

if ARGV.length == 0
  puts 'usage: atcoder-submit problem'
  puts 'problem is required'
  exit
end

problem = ARGV[0]

# detect debug prints
file = "src/bin/#{problem}.rs"
output = ''
Open3.pipeline_r(['grep', '-e', 'eprintln!', '-e', 'dbg!', file], ['grep', '-v', '^ *//']) do |r|
  output = r.read
end

unless output.empty?
  puts '!!!!Please remove debug prints!!!!'
  puts output
  exit
end

system("rustup run stable cargo atcoder submit --bin #{problem}")
