import sys
from xml.etree import ElementTree as et

class XMLCombiner(object):
    def __init__(self, filenames):
        assert len(filenames) > 0, 'No filenames!'
        # save all the roots, in order, to be processed later
        self.roots = [et.parse(f).getroot() for f in filenames]

    def combine(self):
        dest = self.roots[0].find('glyf')
        new = self.roots[1].find('glyf')
        self.combine_glyphs(dest, new)
        dest = self.roots[0].find('cmap')
        new = self.roots[1].find('cmap')
        self.combine_cmap(dest, new)
        print '<?xml version="1.0" encoding="UTF-8"?>'
        print et.tostring(self.roots[0], encoding='utf-8')

    def combine_glyphs(self, one, other):
        for upd in other:
            found = False
            for src in one:
                if src.attrib["name"] == upd.attrib["name"]:
                    one.remove(src)
                    one.append(upd)
                    found = True
            if found == False:
                one.append(upd)
                
    def combine_cmap(self, one, other):
        for upd in other:
            one.append(upd)
        

if __name__ == '__main__':
    r = XMLCombiner(sys.argv[1:]).combine()
    