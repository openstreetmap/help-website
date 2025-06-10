+++
type = "question"
title = "Anybody know about this error?- osm solar"
description = '''I have installed osm2pgsql, postgresql, postgis, tilestache etc what i need thing for OSM Solar. And download osm file from geofabrik and put them into postgresql. however, when i run the &#x27;tilestache-server.py&#x27; i saw this messages  127.0.0.1 - - [11/Dec/2013 02:26:18] &quot;GET /solar-light/1/1/1.png HTT...'''
date = "2013-12-11T10:28:00Z"
lastmod = "2013-12-12T01:59:00Z"
weight = 28988
keywords = [ "osm", "solar" ]
aliases = [ "/questions/28988" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Anybody know about this error?- osm solar](/questions/28988/anybody-know-about-this-error-osm-solar)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed osm2pgsql, postgresql, postgis, tilestache etc what i need thing for <a href="https://github.com/migurski/OSM-Solar">OSM Solar</a>.</p>
<p>And download osm file from geofabrik and put them into postgresql.</p>
<p>however, when i run the 'tilestache-server.py' i saw this messages</p>
<pre><code>127.0.0.1 - - [11/Dec/2013 02:26:18] &quot;GET /solar-light/1/1/1.png HTTP/1.1&quot; 500 -
Error on request:
Traceback (most recent call last):
  File &quot;/usr/local/lib/python2.7/dist-packages/Werkzeug-0.9.4-py2.7.egg/werkzeug/serving.py&quot;, line 177, in run_wsgi
    execute(self.server.app)
  File &quot;/usr/local/lib/python2.7/dist-packages/Werkzeug-0.9.4-py2.7.egg/werkzeug/serving.py&quot;, line 165, in execute
    application_iter = app(environ, start_response)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/__init__.py&quot;, line 379, in __call__
    status_code, headers, content = requestHandler2(self.config, path_info, query_string, script_name)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/__init__.py&quot;, line 255, in requestHandler2
    status_code, headers, content = layer.getTileResponse(coord, extension)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Core.py&quot;, line 414, in getTileResponse
    tile = self.render(coord, format)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Core.py&quot;, line 495, in render
    tile = provider.renderArea(width, height, srs, xmin, ymin, xmax, ymax, coord.zoom)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Mapnik.py&quot;, line 115, in renderArea
    self.mapnik = get_mapnikMap(self.mapfile)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Mapnik.py&quot;, line 399, in get_mapnikMap
    mapnik.load_map(mmap, str(mapfile))
RuntimeError: Failed to parse expression: &quot;name&quot; in rule &#39;rule 367&#39; in style &#39;text style 106 (name)&#39; in TextSymbolizer at line 1704 of &#39;/home/lee/TileStache-1.49.8/scripts/tile-style.xml&#39;
127.0.0.1 - - [11/Dec/2013 02:26:18] &quot;GET /solar-light/1/1/0.png HTTP/1.1&quot; 500 -
Error on request:
Traceback (most recent call last):
  File &quot;/usr/local/lib/python2.7/dist-packages/Werkzeug-0.9.4-py2.7.egg/werkzeug/serving.py&quot;, line 177, in run_wsgi
    execute(self.server.app)
  File &quot;/usr/local/lib/python2.7/dist-packages/Werkzeug-0.9.4-py2.7.egg/werkzeug/serving.py&quot;, line 165, in execute
    application_iter = app(environ, start_response)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/__init__.py&quot;, line 379, in __call__
    status_code, headers, content = requestHandler2(self.config, path_info, query_string, script_name)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/__init__.py&quot;, line 255, in requestHandler2
    status_code, headers, content = layer.getTileResponse(coord, extension)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Core.py&quot;, line 414, in getTileResponse
    tile = self.render(coord, format)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Core.py&quot;, line 495, in render
    tile = provider.renderArea(width, height, srs, xmin, ymin, xmax, ymax, coord.zoom)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Mapnik.py&quot;, line 115, in renderArea
    self.mapnik = get_mapnikMap(self.mapfile)
  File &quot;/usr/local/lib/python2.7/dist-packages/TileStache/Mapnik.py&quot;, line 399, in get_mapnikMap
    mapnik.load_map(mmap, str(mapfile))
RuntimeError: Failed to parse expression: &quot;name&quot; in rule &#39;rule 367&#39; in style &#39;text style 106 (name)&#39; in TextSymbolizer at line 1704 of &#39;/home/lee/TileStache-1.49.8/scripts/tile-style.xml&#39;
127.0.0.1 - - [11/Dec/2013 02:26:18] &quot;GET /solar-light/null HTTP/1.1&quot; 400 -</code></pre>
<p>everthing is alright(I think), I don't know why is it not working :-</p>
<p>anybody knows about this??</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-solar" rel="tag" title="see questions tagged &#39;solar&#39;">solar</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '13, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/8f333adfbe89cd2ea897e0dbf1f46f01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leeoh&#39;s gravatar image" />
<p><span>leeoh</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leeoh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '13, 10:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-28988" class="comments-container">
<span id="28996"></span>
<div id="comment-28996" class="comment">
<div id="post-28996-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not experienced with all details of the rendering stack, but looks like an conflict between the mapnik map style and the available mapnik version?<br />
Which tutorial did you follow to setup the stack? <a href="http://www.switch2osm.org">http://www.switch2osm.org</a>?</p>
</div>
<div id="comment-28996-info" class="comment-info">
<span class="comment-age">(11 Dec '13, 18:12)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="28997"></span>
<div id="comment-28997" class="comment">
<div id="post-28997-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What versions of everything are you using and on what platform? I'm not in any way familar with TileStache, but perhaps the OSM Solar mapnik style (which based on the stuff in Github, looks quite old) depends on an older version of Mapnik than what you're using?</p>
</div>
<div id="comment-28997-info" class="comment-info">
<span class="comment-age">(11 Dec '13, 18:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28999"></span>
<div id="comment-28999" class="comment">
<div id="post-28999-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have installed my self mapnik and etc</p>
<p>My Mapnik version is 2.2.0, Postgresql is 9.1.11 and others are followed OSM Solar.</p>
</div>
<div id="comment-28999-info" class="comment-info">
<span class="comment-age">(12 Dec '13, 01:59)</span> <span class="comment-user userinfo">leeoh</span>
</div>
</div>
</div>
<div id="comment-tools-28988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28988-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

