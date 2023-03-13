import os

split_char = '-'

__dirname = os.getcwd()

__EXTENSION = '.mp4'


print(__dirname)


__MAXIMUM_NUMBER = -1;




for count, filename in enumerate(os.listdir(__dirname)) :
    file_extension = os.path.splitext(filename)
    if( file_extension[1] == __EXTENSION ) :
        fileNumber = int(file_extension[0].split(split_char)[0])
        #print(fileNumber)
        if( __MAXIMUM_NUMBER < fileNumber ) :
            __MAXIMUM_NUMBER = fileNumber



print( 'MAXIMUM LENGTH : ' , len(str(__MAXIMUM_NUMBER)) )


for count, filename in enumerate(os.listdir(__dirname)) :
    file_extension = os.path.splitext(filename)
    if( file_extension[1] == __EXTENSION ) :
        fileNumber = int(file_extension[0].split(split_char)[0])
        realFileName = file_extension[0].split(split_char)[1].strip()
        print(realFileName)
        #print('Length : ' , len(file_extension[0]) , file_extension ) 
        #print('0'*  ( len(str(__MAXIMUM_NUMBER)) - int(len(file_extension[0])) ) , file_extension  )
        #precedence = '0'*  ( len(str(__MAXIMUM_NUMBER)) - int(len(file_extension[0].split(split_char)[0])) )
        #print(precedence + file_extension[0] + file_extension[1]);
        source = filename
        #destination = precedence + "".join( file_extension[0].split(split_char) )  + file_extension[1]
        #os.rename(source, destination)
        destination = realFileName
        os.rename(source, destination)


print()
print()
#input("Press Any Key To Continue . . .")
