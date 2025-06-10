+++
type = "question"
title = "Rendering images/maps from Postgresql/PostGIS Database"
description = '''Hi everyone! I convert .osm - data into pgsql-database. When I try to render images from these databases/tables. I use Python version 2.7.2 with Mapnik-2.0.1rc0. My .py:  #!/usr/bin/python  import mapnik from mapnik import Layer, PostGIS from datetime import datetime, timedelta import sys, os  def r...'''
date = "2012-03-20T12:52:00Z"
lastmod = "2012-03-20T12:52:00Z"
weight = 11357
keywords = [ "python", "rendering", "postgresql", "mapnik", "postgis" ]
aliases = [ "/questions/11357" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering images/maps from Postgresql/PostGIS Database](/questions/11357/rendering-imagesmaps-from-postgresqlpostgis-database)

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
<span id="post-11357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I convert .osm - data into pgsql-database.</p>
<p>When I try to render images from these databases/tables.</p>
<p>I use Python version 2.7.2 with Mapnik-2.0.1rc0.</p>
<p>My .py:</p>
<hr />
<pre><code>#!/usr/bin/python
&#10;import mapnik
from mapnik import Layer, PostGIS
from datetime import datetime, timedelta
import sys, os
&#10;def render_image(start_time,end_time):
&#10;    ll = (30.708,-27.414,32.179,-25.652)
    prj = mapnik.Projection(&quot;+proj=latlong +datum=WGS84&quot;)
    c0 = prj.forward(mapnik.Coord(ll[0],ll[1]))
    c1 = prj.forward(mapnik.Coord(ll[2],ll[3]))
&#10;z = 3
imgx = 336 * z
imgy = 450 * z
&#10;m = mapnik.Map(imgx,imgy)
#mapnik.load_map(m,&quot;some_kind_of_stylesheet.xml&quot;)
&#10;db_params = dict(
  dbname = &#39;gis&#39;,
  user = &#39;Hein&#39;,
  password = &#39;1234&#39;,
  host = &#39;localhost&#39;,
  port = 5432,
  estimate_extent = False,
  extent = &quot;3390650.221286806, -3163145.87245787, 3609898.596229789, -2956043.104540316&quot;
)
&#10;lyr = Layer(&#39;points&#39;,&quot;+init=epsg:900913&quot;)
###db_params[&#39;table&#39;] = &#39;(planet_osm_line,planet_osm_point,planet_osm_polygon,planet_osm_roads)&#39;
db_params[&#39;table&#39;] = &#39;planet_osm_point&#39;
lyr.datasource = PostGIS(**db_params)
lyr.styles.append(&#39;points&#39;)
m.layers.append(lyr)
&#10;if hasattr(mapnik,&#39;mapnik_version&#39;) and mapnik.mapnik_version() &gt;= 800:
    bbox = mapnik.Box2d(c0.x,c0.y,c1.x,c1.y)
else:
    bbox = mapnik.Envelope(c0.x,c0.y,c1.x,c1.y)
m.zoom_to_box(bbox)
im = mapnik.Image(imgx,imgy)
mapnik.render(m, im)
view = im.view(0,0,imgx,imgy) # x,y,width,height
view.save(&quot;map.png&quot;,&#39;png&#39;)
&#10;if __name__ == &quot;__main__&quot;:
    cur_time = datetime(2010,8,10,0,0,0)
    end_time = datetime(2010,12,6,23,59,59)
    delta = timedelta(minutes=+30)
    while cur_time &lt; end_time:
        render_image(cur_time.isoformat(), (cur_time+delta).isoformat())
        cur_time = cur_time + delta</code></pre>
<hr />
<p>I got this file from example-code and modified it. But there are some lines, where I don't know, what they mean and if they are useful.</p>
<p>What kind of XML-stylesheet must I use? Where can I get sample XML-code, that I can use?</p>
<p>I would be very happy if anyone could help me. Thank you!</p>
<p>Greets, Matze</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '12, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Mar '12, 13:03</strong> </span></p>
</div>
</div>
<div id="comments-container-11357" class="comments-container">
&#10;</div>
<div id="comment-tools-11357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

