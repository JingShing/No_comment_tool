# No_comment_tool
This tool can help you to get rid of code comment

## How to use
Argument: ```file_path method``` 
* ```file_path``` is a path to your file
* method can be: ```c```, ```py``` or ```custom```
* if choose custom you need to input the block comment prefix, profix and one line comment prefix

activate this script and input the file you want to de-comment. It will kill comments to make code more clear ~~or help you to make code more difficult to read~~.

It will detect your file format. Now it can kill c or py format comments. And if it can not tell what file format it is. It will ask you use which method or format to kill comments.

After processing codes. It will generate a new file with ```no_comment_``` prefix 

## Log
### Ver 0.1
* Only can accept one line commeand in c and python
* can only read ```.c``` and ```.py``` file format
### Ver 0.2
* Add block comment function
* now has one line comment function and block comment function to kill comment
### Ver 0.3
* Add Argument in file input, you can add method in it
* Add custom method. You can use custom prefix, profix in block comment and one line comment.

### up to do
- [X] block comment
- [X] more language comment no no
- [ ] comment  may in function or quote error
