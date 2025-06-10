+++
type = "question"
title = "OSM rendering with mapnik and Python script"
description = '''Hi, I&#x27;m struggling to render osm data in python, using mapnik. I have downloaded south-africa-and-lesotho-latest.osm.pbf, used imposm3 with provided mapping.json file, to load into postgis. For simple rendering, the following code snippet works - but I would like to render my maps using osm styles, ...'''
date = "2015-07-22T12:58:00Z"
lastmod = "2015-07-22T17:14:00Z"
weight = 44346
keywords = [ "python", "rendering", "style", "imposm", "mapnik" ]
aliases = [ "/questions/44346" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM rendering with mapnik and Python script](/questions/44346/osm-rendering-with-mapnik-and-python-script)

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
<span id="post-44346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm struggling to render osm data in python, using mapnik.</p>
<p>I have downloaded south-africa-and-lesotho-latest.osm.pbf, used imposm3 with provided mapping.json file, to load into postgis.</p>
<p>For simple rendering, the following code snippet works - but I would like to render my maps using osm styles, rather than simple lines, etc.</p>
<p>How would I tell mapnik to use a specific rendering style, and where can I get rendering style from?</p>
<p>I have looked at gravitystorm and standard_tile_layer, but can't work out how to implement them in python (below).</p>
<p>Thanks in advance,</p>
<p>Zoltan</p>
<p>#!/usr/bin/env python</p>
<p>import mapnik</p>
<p>m = mapnik.Map(7015,4961) # / <em>A4 LAndscape 600dpi</em> /</p>
<p>m.background = mapnik.Color('blue')</p>
<p>m.background = mapnik.Color('white')</p>
<p>s = mapnik.Style()</p>
<p>r = mapnik.Rule()</p>
<p>#polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('rgb(0,255,255)'))</p>
<p>#r.symbols.append(polygon_symbolizer)</p>
<p>line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(255,0,0)'),5)</p>
<p>r.symbols.append(line_symbolizer)</p>
<p>s.rules.append(r)</p>
<p>m.append_style('My Style',s)</p>
<p>lyr = mapnik.Layer('Geometry from PostGIS')</p>
<p>lyr.datasource = mapnik.PostGIS(host='192.168.0.91',user='osmgis',password='xxxx',dbname='gisdata',table='osm.osm_roads',srid=3857)</p>
<p>lyr.styles.append('My Style')</p>
<p>m.layers.append(lyr)</p>
<p>extent = mapnik.Box2d(2052835,-4039814,2056207,-4036860)</p>
<p>m.zoom_to_box(extent)</p>
<p>mapnik.render_to_file(m,'rsa_osm.png', 'png')</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '15, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/abaad5348154cc4e9e96bb22fe19cf3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoltan_Szecsei&#39;s gravatar image" />
<p><span>Zoltan_Szecsei</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoltan_Szecsei has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44346" class="comments-container">
&#10;</div>
<div id="comment-tools-44346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44346-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="44349"></span>

<div id="answer-container-44349" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the Python/mapnik part of the question take a look at nik4:</p>
<p><a href="https://github.com/Zverik/Nik4">https://github.com/Zverik/Nik4</a></p>
<p>(or maybe one of the other tools mentioned in the readme there)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '15, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-44349" class="comments-container">
<span id="44350"></span>
<div id="comment-44350" class="comment">
<div id="post-44350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cool. Will take a look at nik4 now.</p>
<p>Thanks &amp; regards, Zoltan</p>
</div>
<div id="comment-44350-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 13:56)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44356"></span>
<div id="comment-44356" class="comment">
<div id="post-44356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, thanks, but I can't see how nik4 will help, as I already have my data in postgis, and not in XML format. (am I getting muddled between osm data exported as XML, and styling XML files?</p>
<p>To rephrase my problem: I have OSM data, from PBF format, loaded into PostGIS (used imposm3 to get it into PostGIS)</p>
<p>I wish to (via a batch script/program) zoom into an arbitrary area, and render that area into a PNG file.</p>
<p>I don't want tiling or anything else. Just simply a rendered image, in osm style.</p>
<p>I've tried doing it with mapnik &amp; python (see script snippet in my forst post), but is my approach wrong? This must surely be the most standard thing anyone does with (downloaded) osm data.</p>
<p>TIA&lt; Zoltan</p>
</div>
<div id="comment-44356-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 14:58)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44363"></span>
<div id="comment-44363" class="comment">
<div id="post-44363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I think you are getting the XML types muddled. nik4.py itself doesn't care where the data is stored, it does the chore of passing the style XML and desired bounds/zoom into mapnik (so for example, the XML style file might have a connection to a PostGIS table).</p>
<p>In essence, I think you are probably working on building something very similar to what nik4 does.</p>
</div>
<div id="comment-44363-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:21)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-44349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44349-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44358"></span>

<div id="answer-container-44358" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am using this:</p>
<pre><code>m = mapnik.Map(image_width,image_height)
mapnik.load_map(m, v[&#39;style&#39;])
bbox=mapnik.Envelope( left, top, right, bottom )
m.zoom_to_box(bbox)
mapnik.render_to_file(m, v[&#39;out&#39;],&#39;jpeg&#39;)</code></pre>
<p>Where v['style'] points to a mapnik XML style sheet. This is the older way to style mapnik, the newer being to use a CSS file that, I think, is used to generate mapnik XML. Some information to get you started is here: <a href="https://github.com/mapnik/mapnik/wiki/XMLConfigReference">https://github.com/mapnik/mapnik/wiki/XMLConfigReference</a></p>
<p>The mapnik XML is not as well documented as I'd like and you need to be sure that the tags your style(s) need are actually inserted into the Postgresql database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '15, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-44358" class="comments-container">
<span id="44359"></span>
<div id="comment-44359" class="comment">
<div id="post-44359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, OSM data can be downloaded as XML or PBF. In your v'style' example, that style sheet also has the map geometry in it, does it not? If not, what do you use to load your geometry? Thanks, Zoltan</p>
</div>
<div id="comment-44359-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 15:47)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44360"></span>
<div id="comment-44360" class="comment">
<div id="post-44360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>edit: I can't get the code to format properly, so posting new answer to your comment.</p>
<p>No, the mapnik style has no geometry in it. For each type of thing to be rendered there are two parts, one specifics how to get the data (from database with query, from XML, from other file, etc.) and one that specifies how it is to be rendered.</p>
</div>
<div id="comment-44360-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:02)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-44358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44358-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44361"></span>

<div id="answer-container-44361" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44361-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is the script I use to get OSM data and to load it into my database. The "style" file for osm2pgsql is actually in a column format listing the tagging on the objects that are to be loaded.</p>
<pre><code>#! /bin/bash
  # Define defaults
  state_file=&quot;california-latest.osm.pbf&quot;
  state_server=&quot;http://download.geofabrik.de/north-america/us/&quot;
  cache_dir=&quot;osm/&quot;
  osm_style=&quot;${cache_dir}osm2pgsql.style&quot;
  if [ -e &quot;${cache_dir}${state_file}&quot; ] ; then
    mv -f &quot;${cache_dir}${state_file}&quot; &quot;${cache_dir}${state_file}.bak&quot;
  fi
  wget -O &quot;${cache_dir}${state_file}&quot; &quot;${state_server}${state_file}&quot;
  echo &quot;Filling PostGIS database&quot;
  cmd=&quot;osm2pgsql --verbose --create --multi-geometry --database osm --style ${osm_style} --hstore ${cache_dir}${state_file}&quot;
  echo ${cmd}
  ${cmd}
  echo &#39;CREATE INDEX idx_planet_osm_point_tags ON planet_osm_point USING gist(tags);&#39; &gt; pgsql osm
  echo &#39;CREATE INDEX idx_planet_osm_polygon_tags ON planet_osm_polygon USING gist(tags);&#39; &gt; pgsql osm
  echo &#39;CREATE INDEX idx_planet_osm_line_tags ON planet_osm_line USING gist(tags);&#39; &gt; pgsql osm</code></pre>
<p>For rendering, the mapnik XML has one part that lists what and how to render another part that gets the data. Here is how I render buildings and fences:</p>
<pre><code>    &lt;Style name=&quot;buildings&quot;&gt;
    &lt;Rule&gt;
        &lt;Filter&gt;[building] != &#39;&#39;&lt;/Filter&gt;
            &lt;PolygonSymbolizer fill=&quot;rgb(0,0,0)&quot; /&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&#10;&lt;Style name=&quot;fences&quot;&gt;
    &lt;Rule&gt;
        &lt;Filter&gt;
            ([barrier] != &#39;&#39;)
        &lt;/Filter&gt;
        &lt;LineSymbolizer
            stroke=&quot;rgb(0,0,0)&quot;
            stroke-width=&quot;&amp;pt_size_0_5;&quot;
            stroke-dasharray=&quot;&amp;pt_size_0_5;,&amp;pt_size_0_5;&quot;
        /&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&#10;&lt;Layer name=&quot;buildings&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;buildings&lt;/StyleName&gt;
    &lt;Datasource&gt;
        &lt;Parameter name=&quot;type&quot;&gt;postgis&lt;/Parameter&gt;
        &lt;Parameter name=&quot;host&quot;&gt;localhost&lt;/Parameter&gt;
        &lt;Parameter name=&quot;dbname&quot;&gt;osm&lt;/Parameter&gt;
        &lt;Parameter name=&quot;user&quot;&gt;&lt;/Parameter&gt;
        &lt;Parameter name=&quot;password&quot;&gt;&lt;/Parameter&gt;
        &lt;Parameter name=&quot;table&quot;&gt;
            (SELECT way, building
            from planet_osm_polygon where building is not null) as foo
        &lt;/Parameter&gt;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&#10;&lt;Layer name=&quot;fences&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;fences&lt;/StyleName&gt;
    &lt;Datasource&gt;
        &lt;Parameter name=&quot;type&quot;&gt;postgis&lt;/Parameter&gt;
        &lt;Parameter name=&quot;host&quot;&gt;localhost&lt;/Parameter&gt;
        &lt;Parameter name=&quot;dbname&quot;&gt;osm&lt;/Parameter&gt;
        &lt;Parameter name=&quot;user&quot;&gt;&lt;/Parameter&gt;
        &lt;Parameter name=&quot;password&quot;&gt;&lt;/Parameter&gt;
        &lt;Parameter name=&quot;table&quot;&gt;
            (SELECT way, barrier
            from planet_osm_line where (barrier = &#39;fence&#39;) or (barrier = &#39;gate&#39;)) as foo
        &lt;/Parameter&gt;
    &lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '15, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '15, 16:09</strong> </span></p>
</div>
</div>
<div id="comments-container-44361" class="comments-container">
<span id="44362"></span>
<div id="comment-44362" class="comment">
<div id="post-44362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ugh! Why does this site lose the \n?????</p>
<p>I'm deciphering above now......</p>
</div>
<div id="comment-44362-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:09)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44365"></span>
<div id="comment-44365" class="comment">
<div id="post-44365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So your mapnik XML file (above file with &lt;style name="buildings"&gt; etc) is called style, and that;s how you point to it with your rendering script, using:</p>
<p>m = mapnik.Map(image_width,image_height)</p>
<p>mapnik.load_map(m, v['style']) ??</p>
</div>
<div id="comment-44365-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:38)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44367"></span>
<div id="comment-44367" class="comment">
<div id="post-44367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically yes. In actuality the file called out by v['style'] is a XML file that defines some entities and then includes files like the one I posted above. That way I can do different maps with different things displayed pretty easily.</p>
</div>
<div id="comment-44367-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:46)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="44368"></span>
<div id="comment-44368" class="comment">
<div id="post-44368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And that is exactly the (default) style file I am looking to download and use. Is it available somewhere?</p>
</div>
<div id="comment-44368-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 16:51)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
<span id="44369"></span>
<div id="comment-44369" class="comment">
<div id="post-44369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, no: All the style sheets I have I created myself and my organization is unique to me.</p>
<p>The default rendering used to be directly by mapnik xml but is now through CartoCSS. The current carto CSS stuff is at <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
<p>And a link there to the old stuff points to <a href="https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik#inc">https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik#inc</a></p>
<p>But I haven't worked my way through that to verify everything is there. Looks like a lot of scripts and Python stuff are there in addition to style information.</p>
<p>If you want to use the current techniques then you probably want to be working off of the cartoCSS stuff rather than directly writing the mapnik XML. I got started before cartoCSS was released and haven't bothered to update as what I have works for me.</p>
</div>
<div id="comment-44369-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 17:05)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="44370"></span>
<div id="comment-44370" class="comment not_top_scorer">
<div id="post-44370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ugh. OK - will take a longer look at building something with cartoCSS. If I have to learn, might as well start with 'current' than 'old'.</p>
<p>Big thanks for your input. Regards, Zoltan</p>
</div>
<div id="comment-44370-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 17:14)</span> <span class="comment-user userinfo">Zoltan_Szecsei</span>
</div>
</div>
</div>
<div id="comment-tools-44361" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44361-form-container" class="comment-form-container">
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

