import fanstatic
import js.jquery

library = fanstatic.Library('flot', 'resources')

excanvas = fanstatic.Resource(library, 'excanvas.js',
    minified='excanvas.min.js')

flot = fanstatic.Resource(library, 'jquery.flot.js',
    minified='jquery.flot.min.js',
    depends=[js.jquery.jquery, excanvas])
