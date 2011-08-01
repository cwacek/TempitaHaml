TempitaHaml - A Pure Python HAML template processor for Tempita
===============================================================

What
----
A pure python HAML preprocessor hook into the [tempita]: http://pythonpaste.org/tempita/ 'Tempita' templating engine.
Intended to allow use of HAML when writing small WSGI utilities that use Tempita.

Why
---
Sometimes I find myself creating very lightweight web applications - utilities more than anything else. 
Most recently I was using WSGI and Python (which by the way I quite like), and ran into the need to do
some HTML templating. There's nothing I hate more than writing out full HTML, and having used HAML when
working with RoR I fell in love. There are a couple of HAML preprocessors for Python, but they're all more
than I wanted or needed for the project.

TempitaHAML aims to extend the very simple but excellent Tempita templating engine to support HAML.

License
-------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

