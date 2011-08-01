from cStringIO import StringIO
import re




class TempitaHamlTemplate:

    htmlElementRE = re.compile('[_:A-Za-z][-._:A-Za-z0-9]*')

    def __init__(self):
        self.output = StringIO()
        self.indent_level = 0
        self.tag_stack = ()
        self.indent_size = -1
    


    def parseLine(self,line):
        if len(line.strip()) == 0:
            return

        indent,line = ParseIndent(line)
        if indent == self.indent_level:
            closeTag(self)
        else:
            if line[0] == '%':
                self.parseNamedTag(line[1:])
    
    
    """ 
    Parse a named tag '%div', push it on to our tag stack, and write 
    the resultant HTML to 'output'. If 

    """
    def parseNamedTag(self,line):
        match = htmlElementRE.match(line)
        if not match:
            raise InvalidFormatError("Missing identifer after %")
        tag = line[match.start(),match.end()]
        self.indent_level += 1
        self.tag_stack.append(tag)
        self.output.write("<{0} ".format(tag))
        parseAttributes(self,line[match.end():])

    def parseAttributes(self,line):

    """
    Write the closing tag for the tag on the top of our stack

    """
    def closeTag(self):
        self.output.write("</{0}>".format(tag_stack.pop()))

    """
    Figure out how indented a given line is. Return a tuple
    containing the indentation level and the rest of the line.
    Raise IndentationError if the indentation doesn't make sense

    """
    def parseIndent(line):
        for (idx,val) in enumerate(ints):
            if (val != ' '):
                if self.indent_size == -1:
                    self.indent_size = idx
                    return (0,line[idx:])
                elif idx % self.indent_size != 0:
                    raise IndentationError
                else:
                    indent = idx /self.indent_size
                    if indent > (self.indent_level +1):
                        raise IndentationError
                    return (idx /self.indent_size, line[idx:])

    
