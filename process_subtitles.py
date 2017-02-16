"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.
filename = "small_subtitles.srt"
filename = "pirates_of_silicon_valley.srt"
"""
filename = "pirates_of_silicon_valley.srt"
my_file = open(filename)
out = open('output.js', 'w')
out.write('var Subtitles = [ \n')
comma = ","
for line in my_file:
  line = line.strip()
  if "-->" in line:
      line_duration = 'duration: ' + '"%s"'%line + comma
      line1 = '"%s"'%next(my_file).strip() + comma
    #   if next(my_file) == None:
    #     Print('end of file');
      line2 = '"%s"'%next(my_file).strip() + comma
      if line2 == '"",':
          line1, line2 = line2, line1
      print(line_duration)
      print('line1: ' + line1)
      print('line2: ' + line2)
      out.write('{ \n')
      out.write(line_duration + "\n")
      out.write('line1: ' + line1 + "\n")
      out.write('line2: ' + line2 + "\n")
      out.write('} \n')

out.write('];')
out.close()
