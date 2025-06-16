+++
type = "question"
title = "Setting PostGIS as a datasource"
description = '''Hi there,  I am following tutorials to learn about OSM and how to make some maps.  Currently I am using this one, https://github.com/mapnik/mapnik/wiki/GettingStartedInPython but in the instructions it uses shapefiles as a datasource just in a normal file directory. I don’t want to do that, I want t...'''
date = "2012-02-20T13:09:00Z"
lastmod = "2012-03-01T10:12:00Z"
weight = 10677
keywords = [ "mapnik", "postgresql", "postgres", "postgis", "osm2pgsql" ]
aliases = [ "/questions/10677" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Setting PostGIS as a datasource](/questions/10677/setting-postgis-as-a-datasource)

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
<span id="post-10677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10677-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I am following tutorials to learn about OSM and how to make some maps. Currently I am using this one, <a href="https://github.com/mapnik/mapnik/wiki/GettingStartedInPython">https://github.com/mapnik/mapnik/wiki/GettingStartedInPython</a> but in the instructions it uses shapefiles as a datasource just in a normal file directory. I don’t want to do that, I want the file source to be from my database in PostGIS, where I have stored my OSM data. What do I need to do to make it do that? I tried:</p>
<p>lyr = Layer('Geometry from PostGIS') lyr.datasource = PostGIS(host='localhost',user='postgres',password='',dbname='your_postgis_database',table='your_table')</p>
<p>which I copied off one of the wiki pages. Obviously I amended details as appropriate, but it just said layer not recognised. I wondered if there way something I had to do or tell it to do to get into the database?</p>
<p>In the literature I have read, it says that using PostGIS is one of the most common ways of doing what I want to do, but I cannot seem to find any code to use! Thanks in Advance, Tracey</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '12, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/5e0670aa9ef7ddb00b17215e77fb9132?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lgxtlm&#39;s gravatar image" />
<p><span>lgxtlm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lgxtlm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10677" class="comments-container">
<span id="10899"></span>
<div id="comment-10899" class="comment">
<div id="post-10899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have solve your problem?</p>
</div>
<div id="comment-10899-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 10:12)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-10677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10677-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="10834"></span>

<div id="answer-container-10834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10834-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please, give us more of your code. Here is one of my script that was working with mapnik two years ago:</p>
<pre><code>def addLayer(m, name, dbname, table, symbolizer):
  # style creation
  s = mapnik.Style()
  r = mapnik.Rule()
  r.symbols.append(symbolizer)
  s.rules.append(r)
  m.append_style(name,s)
  # layer creation
  layer = mapnik.Layer(name, &quot;+proj=latlong +datum=WGS84&quot;)
  layer.datasource = mapnik.PostGIS(host=&#39;localhost&#39;,port=&#39;5434&#39;,user=&#39;mapnik&#39;,password=&#39;mapnik&#39;,dbname=dbname,table=table)
  layer.styles.append(name)
  m.layers.append(layer)
  return layer
# usage sample
m = mapnik.Map(1000,1500)
m.background = mapnik.Color(&#39;white&#39;)
projection = &quot;+proj=latlong +datum=WGS84&quot;
addLayer(m, name=&#39;data&#39;, dbname=&#39;osm&#39;,
  table=&#39;(select way from planet_osm_line) as roads&#39;,
  symbolizer=mapnik.LineSymbolizer(mapnik.Color(&#39;rgb(0,0,0)&#39;),2))</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '12, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10834" class="comments-container">
&#10;</div>
<div id="comment-tools-10834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10834-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10842"></span>

<div id="answer-container-10842" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10842-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An important choice you're also faced with initially is... Do you want to get the default OpenStreetMap stylesheets working with Mapnik? We have a lot of documentation about how to do this. Unfortunately it's a little more fiddly than some of the basic "Getting started" Mapnik tutorials, and you are more restricted as to which Mapnik version you work with and what your data source types are.</p>
<p>To get the OSM <em>default</em> stylesheet running you <em>must</em> work with PostGIS (as well as some shapefiles for zoomed out world boundaries and coastline), and you <em>must</em> populate the database using osm2pgsql which is also governed by a matching style configuration file. Hopefully a good guide to all this is the <a href="https://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a> wiki page. Having done the database loading, there's some python scripts provided: <a href="http://generate_image.py"><code>generate_image.py</code></a> and <a href="http://generate_tiles.py"><code>generate_tiles.py</code></a> Playing around with these, you'll get some control within python, but it's not quite the same as the from-scratch tutorial you link to.</p>
<p>...but maybe there's a better half-way-house tutorial involving osm2pgsql and building style rules in python. (Anyone know?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '12, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '12, 16:00</strong> </span></p>
</div>
</div>
<div id="comments-container-10842" class="comments-container">
&#10;</div>
<div id="comment-tools-10842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10842-form-container" class="comment-form-container">
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

</div>

</div>

