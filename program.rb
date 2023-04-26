def sort_words(my_str: String) -> String
  # breakdown the string into a list of words
  words = my_str.downcase.split

  # sort the list
  words.sort!

  # display the sorted words
  puts "The sorted words are:"
  words.each do |word|
    puts word
  end
end

sort_words("Have a nice day.")