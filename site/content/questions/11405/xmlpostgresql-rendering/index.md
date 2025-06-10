+++
type = "question"
title = "XML/Postgresql Rendering"
description = '''Heyho! I try to render my map from a Postgresql/PostGIS Database. I use a simple XML-Stylesheet. Can somebody please tell me, what this error-message means and how I can fix it? That would be really kind! The error-massage is quoted at the end of this post. If needed, I can quote/upload my code as w...'''
date = "2012-03-22T08:19:00Z"
lastmod = "2012-03-23T07:41:00Z"
weight = 11405
keywords = [ "xml", "geometry", "postgresql", "postgis", "database" ]
aliases = [ "/questions/11405" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [XML/Postgresql Rendering](/questions/11405/xmlpostgresql-rendering)

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
<span id="post-11405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Heyho!</p>
<p>I try to render my map from a Postgresql/PostGIS Database. I use a simple XML-Stylesheet.</p>
<p>Can somebody please tell me, what this error-message means and how I can fix it? That would be really kind!</p>
<p>The error-massage is quoted at the end of this post. If needed, I can quote/upload my code as well.</p>
<p>Greetings Matze</p>
<hr />
<pre><code>Traceback (most recent call last):
  File &quot;C:/0A/run_python&quot;, line 3, in &lt;module&gt;
    execfile(r&quot;C:\0A\7\schwentine.py&quot;)
  File &quot;C:\0A\7\schwentine.py&quot;, line 57, in &lt;module&gt;
    render_image()
  File &quot;C:\0A\7\schwentine.py&quot;, line 21, in render_image
    mapnik.load_map(m,r&quot;C:\0A\7\schwentine.xml&quot;)
RuntimeError: Postgis Plugin: PSQL error:
ERROR:  syntax error at or near &quot;planet_osm_line&quot;
LINE 1: ... srid FROM geometry_columns WHERE f_table_name=&#39; &#39;planet_osm...
                                                             ^
Full sql was: &#39;SELECT f_geometry_column, srid FROM geometry_columns WHERE f_table_name=&#39; &#39;planet_osm_line&#39; &#39;&#39;
 (encountered during parsing of layer &#39;tutorial&#39; in map &#39;C:\0A\7\schwentine.xml&#39;)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '12, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11405" class="comments-container">
&#10;</div>
<div id="comment-tools-11405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11405-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11457"></span>

<div id="answer-container-11457" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11457-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MHein has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is the last line of your inc/settings.xml.inc file? If you are running the default setup it should be &lt;!ENTITY prefix "planet_osm"&gt;</p>
<p>It looks like you might have put in extra quotes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '12, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-11457" class="comments-container">
<span id="11458"></span>
<div id="comment-11458" class="comment">
<div id="post-11458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is my XML-Stylesheet:</p>
<hr />
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;!DOCTYPE Map
[
       &lt;!ENTITY world_boundaries_dir   &quot;/home/foo/mapnik/world_boundaries/&quot;&gt;
       &lt;!ENTITY dbtype &quot;postgis&quot;&gt;
       &lt;!ENTITY dbhost &quot;localhost&quot;&gt;
       &lt;!ENTITY dbuser &quot;Hein&quot;&gt;
       &lt;!ENTITY dbname &quot;gis_schwentine&quot;&gt;
       &lt;!ENTITY dbprefix &quot;planet_osm&quot;&gt;
       &lt;!ENTITY tutorial-casing SYSTEM &quot;/home/foo/spreadnik/tutorial-casing.sty&quot;&gt;
]&gt;
&lt;Map bgcolor=&quot;#b5d0d0&quot; &gt;
&amp;lt;Style name=&quot;world&quot;&amp;gt;&amp;lt;/Style&amp;gt;
&amp;lt;Style name=&quot;coast-poly&quot;&amp;gt;&amp;lt;/Style&amp;gt;
&amp;lt;Style name=&quot;builtup&quot;&amp;gt;&amp;lt;/Style&amp;gt;
&#10;&amp;lt;Layer name=&quot;world&quot;&amp;gt;&amp;lt;/Layer&amp;gt;
&amp;lt;Layer name=&quot;coast-poly&quot;&amp;gt;&amp;lt;/Layer&amp;gt;
&amp;lt;Layer name=&quot;builtup&quot;&amp;gt;&amp;lt;/Layer&amp;gt;
&#10;&amp;lt;Layer name=&quot;tutorial&quot;&amp;gt;
&amp;lt;StyleName&amp;gt;tutorial-fill&amp;lt;/StyleName&amp;gt;
    &amp;lt;Datasource&amp;gt;
        &amp;lt;Parameter name=&quot;type&quot;&amp;gt;&amp;amp;dbtype;&amp;lt;/Parameter&amp;gt;
        &amp;lt;Parameter name=&quot;user&quot;&amp;gt;&amp;amp;dbuser;&amp;lt;/Parameter&amp;gt;
        &amp;lt;Parameter name=&quot;dbname&quot;&amp;gt;&amp;amp;dbname;&amp;lt;/Parameter&amp;gt;
        &amp;lt;Parameter name=&quot;table&quot;&amp;gt; &#39;planet_osm_points&#39; &amp;lt;/Parameter&amp;gt;
        &amp;lt;Parameter name=&quot;estimate_extent&quot;&amp;gt;false&amp;lt;/Parameter&amp;gt;
        &amp;lt;Parameter name=&quot;extent&quot;&amp;gt;-20037508,-19929239,20037508,19929239&amp;lt;/Parameter&amp;gt;
    &amp;lt;/Datasource&amp;gt;
&amp;lt;/Layer&amp;gt;</code></pre>
</code>
<p><code>&lt;/Map&gt; </code></p>
</pre>
</div>
<div id="comment-11458-info" class="comment-info">
<span class="comment-age">(23 Mar '12, 06:53)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="11459"></span>
<div id="comment-11459" class="comment">
<div id="post-11459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is my Python-file</p>
<hr />
<pre><code>    #!/usr/bin/python
import mapnik 
from mapnik import Layer, PostGIS
import sys, os
def render_image():
ll = (-180.0,-90.0, 180.0,90.0)
prj = mapnik.Projection(&quot;+proj=utm +zone=32U +ellps=GRS80 +datum=WGS84 +units=m +no_defs&quot;)
#prj = mapnik.Projection(&quot;+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.999601 +x_0=400000 +y_0=-100000 +ellps=airy  +units=m +towgs84=446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894 +units=m +nodefs&quot;)
#prj = mapnik.Projection(&quot;+proj=latlong +datum=WGS84&quot;)
c0 = prj.forward(mapnik.Coord(ll[0],ll[1]))
c1 = prj.forward(mapnik.Coord(ll[2],ll[3]))
&#10;z = 3
imgx = 336 * z
imgy = 450 * z
&#10;m = mapnik.Map(imgx,imgy)
mapnik.load_map(m,r&quot;C:\0A\7\schwentine.xml&quot;)
&#10;db_params = dict(
  dbname = &#39;gis_schwentine&#39;,
  user = &#39;Hein&#39;,
  password = &#39;1234&#39;,
  host = &#39;localhost&#39;,
  port = 5432,
  estimate_extent = False,
  extent = &quot;3390650.221286806, -3163145.87245787, 3609898.596229789, -2956043.104540316&quot;
)
&#10;lyr = Layer(&#39;points&#39;,&quot;+init=epsg:900913&quot;)
db_params[&#39;table&#39;] = (planet_osm_point)
lyr.datasource = PostGIS(**db_params)
lyr.styles.append(&#39;points&#39;)
m.layers.append(lyr)
&#10;if hasattr(mapnik,&#39;mapnik_version&#39;) and mapnik.mapnik_version() &amp;gt;= 800:
    bbox = mapnik.Box2d(c0.x,c0.y,c1.x,c1.y)
else:
    bbox = mapnik.Envelope(c0.x,c0.y,c1.x,c1.y)
m.zoom_to_box(bbox)
im = mapnik.Image(imgx,imgy)
mapnik.render(m, im)
view = im.view(0,0,imgx,imgy) # x,y,width,height
view.save(&quot;schwentine.png&quot;,&#39;png&#39;)</code></pre>
</code>
<p><code>if </code><strong><code>name</code></strong><code> == "</code><strong><code>main</code></strong><code>": render_image() </code></p>
</pre>
</div>
<div id="comment-11459-info" class="comment-info">
<span class="comment-age">(23 Mar '12, 07:41)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-11457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11457-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

