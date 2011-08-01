from cStringIO import StringIO
import re
import sys


class ParseError:
    def __init__(self,line):
        self.line = line
    
    def __str__(self):
        return repr(self.line)

class AttributeParseError(ParseError):
    pass

class TempitaHamlTemplate:

    htmlElementRE = re.compile('[_:A-Za-z][-._:A-Za-z0-9]*')
    attrRE = re.compile(':([a-zA-Z]+)\s*=>\s*(.+)')

    def __init__(self):
        self.output = StringIO()
        self.indent_level = 0
        self.tag_stack = []
        self.indent_size = -1
    

    def convert(self,filename):
        f = open(filename)
        for line in f:
            self.parseLine(line)
        while self.tag_stack:            
            self.output.write("</{0}>".format(self.tag_stack.pop()))

        print self.output.getvalue()

    def parseLine(self,line):
        if len(line.strip()) == 0:
            return

        indent,line = self.parseIndent(line)
        if indent == self.indent_level - 1:
            self.closeTag()
        else:
            self.indent_level = indent
            if line[0] == '%':
                self.parseNamedTag(line[1:])

    
    
    """ 
    Parse a named tag '%div', push it on to our tag stack, and write 
    the resultant HTML to 'output'. If 

    """
    def parseNamedTag(self,line):
        match = TempitaHamlTemplate.htmlElementRE.match(line)
        if not match:
            raise InvalidFormatError("Missing identifer after %")
        tag = line[match.start():match.end()]
        self.tag_stack.append(tag)
        self.output.write("<{0} ".format(tag))
        remainder = line[match.end():]

        remainder = self.parseAttributes(remainder)
        self.output.write(">")
        remainder = self.parseValues(remainder)
        return  


    def parseValues(self,line):
        if line != None and len(line) > 0:
            self.output.write(line.strip())
        return 

    """
    Parse a set of HTML attributes, using either HAML's {:id => blah}
    format or the more HTML friendly (type='text/javascript') variety.

    Return the remainder of the line.

    """
    def parseAttributes(self,line):
        if line == None or len(line) == 0:
            return 
        if line[0] == '(':
            end = line.find(')')
            self.output.write("{0}".format(line[1:end]))
            return line[end+1:]
        if line[0] == '{':
            end = line.find('}')
            attrs = line[1:end]
            attrs = attrs.split(',')
            for attr in attrs:
                m = TempitaHamlTemplate.attrRE.match(attr)
                if not m:
                    raise AttributeParseError(attr)
                self.output.write(" {0}={1} ".format(attr[m.start(1):m.end(1)],attr[m.start(2):m.end(2)]))
            return line[end+1:]
        return line


    """
    Write the closing tag for the tag on the top of our stack

    """
    def closeTag(self):
        self.output.write("</{0}>".format(self.tag_stack.pop()))

    """
    Figure out how indented a given line is. Return a tuple
    containing the indentation level and the rest of the line.
    Raise IndentationError if the indentation doesn't make sense

    """
    def parseIndent(self,line):
        for (idx,val) in enumerate(line):
            if (val != ' '):
                if self.indent_size == -1:
                    if idx == 0: 
                        return (0,line)
                    self.indent_size = idx
                    return (1,line[idx:])
                elif idx % self.indent_size != 0:
                    raise IndentationError
                else:
                    indent = idx /self.indent_size
                    if indent > (self.indent_level +1):
                        raise IndentationError
                    return (idx /self.indent_size, line[idx:])

if __name__ == "__main__":
    t = TempitaHamlTemplate()
    t.convert(sys.argv[1])

  
