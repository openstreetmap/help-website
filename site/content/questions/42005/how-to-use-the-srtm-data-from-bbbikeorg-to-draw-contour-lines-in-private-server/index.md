+++
type = "question"
title = "How to use the SRTM data from bbbike.org to draw contour lines in private server?"
description = '''I would like to create a tile server in order to bulk download map tiles for personal use. I have followed the switch2osm guide and I managed to setup an OSM tile server with a small regional DB that works nicely. However, I would also like to get contour lines on my tiles. I have already read the i...'''
date = "2015-03-29T23:49:00Z"
lastmod = "2015-04-04T00:56:00Z"
weight = 42005
keywords = [ "bbbike.org", "switch2osm", "contours", "srtm" ]
aliases = [ "/questions/42005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use the SRTM data from bbbike.org to draw contour lines in private server?](/questions/42005/how-to-use-the-srtm-data-from-bbbikeorg-to-draw-contour-lines-in-private-server)

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
<span id="post-42005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42005-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to create a tile server in order to bulk download map tiles for personal use. I have followed the switch2osm guide and I managed to setup an OSM tile server with a small regional DB that works nicely.</p>
<p>However, I would also like to get contour lines on my tiles.</p>
<p>I have already read the information about SRTM, the contour lines and hill shading in the wiki, but it looks like an overly complicated process.</p>
<p>After looking around, I found that bbbike.org allows to extract regions of the map, and one of the options allows the extraction of SRTM data: <a href="http://extract.bbbike.org/">http://extract.bbbike.org/</a></p>
<p><a href="http://download.bbbike.org/osm/planet/srtm/">Here</a> actually, they even have the entire planet SRTM pbf file available for download.</p>
<p>Can someone please explain how these data could be properly imported in the postgres database? Also, is there any further configuration that needs to be done in Mapnik or any other component?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbbike.org" rel="tag" title="see questions tagged &#39;bbbike.org&#39;">bbbike.org</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span> <span class="post-tag tag-link-srtm" rel="tag" title="see questions tagged &#39;srtm&#39;">srtm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '15, 23:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d5625c6ca5fca65ee63be21d3980a55e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyberang3l&#39;s gravatar image" />
<p><span>cyberang3l</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyberang3l has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '15, 14:19</strong> </span></p>
</div>
</div>
<div id="comments-container-42005" class="comments-container">
&#10;</div>
<div id="comment-tools-42005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42005-form-container" class="comment-form-container">
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

<span id="42052"></span>

<div id="answer-container-42052" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42052-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I managed to import the data and configure them to appear on my map.</p>
<p>Steps I followed:</p>
<ol>
<li>This tutorial in order to setup a tile server: <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></li>
<li>On the "import map data" step, I extracted the part of the map I was interested from <a href="http://extract.bbbike.org/">http://extract.bbbike.org/</a> (choose the format OSM -&gt; Protocolbuffer (PBF)) and used this file for my database.</li>
<li>At this point you should test that you have a working tile server, that is able to serve tiles if you visit <a href="http://ip.of.your.server/osm/0/0/0.png">http://ip.of.your.server/osm/0/0/0.png</a></li>
<li>Now it is time to add the SRTM data. Go again to the website <a href="http://extract.bbbike.org/">http://extract.bbbike.org/</a> and choose the same part of the map that chose when you extracted the database that you used on step 2. This time, choose the format "SRTM Europe PBF (25m)" if your extract is located in Europe, or "SRTM World PBF (40m)" if your extract is located anywhere else in the world. Download this file.</li>
<li>Add the following lines at the end of the files <code>/usr/share/osm2pgsql/default.style</code> and <code>/usr/share/osm2pgsql/osm2pgsql/default.style</code>. These lines will force osm2pgsql in the next step to generate three additional table columns in the database, that are needed for the SRTM data. (probably you don't need to add the lines to both of the files, but I don't know which is the correct file so I added the lines to both of them and it worked)</li>
</ol>
<pre><code>     # Contour lines
     node,way    contour                 text    linear
     way         contour_ext             text    linear
     way         ele                     text    linear
 </code></pre>
<ol>
<li><p>Append the SRTM data into the database with the command <code>osm2pgsql --append --slim -d gis srtm-data.pbf</code></p></li>
<li><p>Add the following XML text in the file <code>/etc/mapnik-osm-carto-data/osm.xml</code>, after the <code>landcover-line</code> Layer (around line 720 in the file).</p>
<p>&lt;layer name="srtm-minor" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a></a></a> +wktext +no_defs +over"&gt; &lt;stylename&gt;contours-minor&lt;/stylename&gt; &lt;datasource&gt; &lt;parameter name="type"&gt;&lt;![CDATA[postgis]]&gt;&lt;/parameter&gt; &lt;parameter name="table"&gt;&lt;![CDATA[(SELECT way,ele,ele as name FROM planet_osm_line WHERE contour_ext = 'elevation_minor') AS "contours-minor"]]&gt;&lt;/parameter&gt; &lt;parameter name="dbname"&gt;&lt;![CDATA[gis]]&gt;&lt;/parameter&gt; &lt;/datasource&gt; &lt;/layer&gt; &lt;layer name="srtm-medium" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a></a></a> +wktext +no_defs +over"&gt; &lt;stylename&gt;contours-medium&lt;/stylename&gt; &lt;stylename&gt;contours-medium-text&lt;/stylename&gt; &lt;datasource&gt; &lt;parameter name="type"&gt;&lt;![CDATA[postgis]]&gt;&lt;/parameter&gt; &lt;parameter name="table"&gt;&lt;![CDATA[(SELECT way,ele,ele as name FROM planet_osm_line WHERE contour_ext = 'elevation_medium') AS "contours-medium"]]&gt;&lt;/parameter&gt; &lt;parameter name="dbname"&gt;&lt;![CDATA[gis]]&gt;&lt;/parameter&gt; &lt;/datasource&gt; &lt;/layer&gt; &lt;layer name="srtm-major" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer"></a><a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a></a></a> +wktext +no_defs +over"&gt; &lt;stylename&gt;contours-major&lt;/stylename&gt; &lt;stylename&gt;contours-major-text&lt;/stylename&gt; &lt;datasource&gt; &lt;parameter name="type"&gt;&lt;![CDATA[postgis]]&gt;&lt;/parameter&gt; &lt;parameter name="table"&gt;&lt;![CDATA[(SELECT way,ele,ele as name FROM planet_osm_line WHERE contour_ext = 'elevation_major') AS "contours-major"]]&gt;&lt;/parameter&gt; &lt;parameter name="dbname"&gt;&lt;![CDATA[gis]]&gt;&lt;/parameter&gt; &lt;/datasource&gt; &lt;/layer&gt;</p>
<p>&lt;style name="contours-minor"&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;70000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;2000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#9cb197" stroke-width="0.3"/&gt; &lt;/rule&gt; &lt;/style&gt; &lt;style name="contours-medium"&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;300000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;70000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#9cb197" stroke-width="0.5"/&gt; &lt;/rule&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;70000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;2000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#747b90" stroke-width="0.5"/&gt; &lt;/rule&gt; &lt;/style&gt; &lt;style name="contours-major"&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;600000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;300000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#9cb197" stroke-width="0.7"/&gt; &lt;/rule&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;300000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;70000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#747b90" stroke-width="0.7"/&gt; &lt;/rule&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;70000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;2000&lt;/minscaledenominator&gt; &lt;linesymbolizer stroke="#855d62" stroke-width="0.7"/&gt; &lt;/rule&gt; &lt;/style&gt; &lt;style name="contours-medium-text"&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;70000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;2000&lt;/minscaledenominator&gt; &lt;textsymbolizer size="10" fill="#9c9" fontset-name="fontset-1" halo-radius="1" wrap-width="14"&gt;&lt;![CDATA[[name]]]&gt;&lt;/textsymbolizer&gt; &lt;textsymbolizer fontset-name="fontset-0" size="10" fill="#747b90" halo-radius="1" placement="line"&gt;&lt;![CDATA[[ele]]]&gt;&lt;/textsymbolizer&gt; &lt;/rule&gt; &lt;/style&gt; &lt;style name="contours-major-text"&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;300000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;70000&lt;/minscaledenominator&gt; &lt;textsymbolizer fontset-name="fontset-1" size="10" fill="#747b90" halo-radius="1" placement="line"&gt;&lt;![CDATA[[ele]]]&gt;&lt;/textsymbolizer&gt; &lt;/rule&gt; &lt;rule&gt; &lt;maxscaledenominator&gt;70000&lt;/maxscaledenominator&gt; &lt;minscaledenominator&gt;2000&lt;/minscaledenominator&gt; &lt;textsymbolizer fontset-name="fontset-1" size="10" fill="#855d62" halo-radius="1" placement="line"&gt;&lt;![CDATA[[ele]]]&gt;&lt;/textsymbolizer&gt; &lt;/rule&gt; &lt;/style&gt;</p></li>
<li><p>Restart renderd, and you should have the contour lines shown on the map. Probably you will need to tune the <code>osm.xml</code> file, because I noticed that it gets bloated with the contour lines and the default style provided by osm.xml that already shows too many things on the map.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '15, 02:04</strong></p>
<img src="https://secure.gravatar.com/avatar/d5625c6ca5fca65ee63be21d3980a55e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyberang3l&#39;s gravatar image" />
<p><span>cyberang3l</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyberang3l has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>31 Mar '15, 15:06</strong> </span></p>
</div>
</div>
<div id="comments-container-42052" class="comments-container">
<span id="42053"></span>
<div id="comment-42053" class="comment">
<div id="post-42053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does anyone know how to insert XML code properly in an answer?</p>
</div>
<div id="comment-42053-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 02:05)</span> <span class="comment-user userinfo">cyberang3l</span>
</div>
</div>
<span id="42054"></span>
<div id="comment-42054" class="comment">
<div id="post-42054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, how can I continue the list numbering after a code block? In the preview is was shown correctly, but now that I see the answer posted, after each code block the ordered lists start counting from 1 again.</p>
</div>
<div id="comment-42054-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 02:08)</span> <span class="comment-user userinfo">cyberang3l</span>
</div>
</div>
<span id="42070"></span>
<div id="comment-42070" class="comment">
<div id="post-42070-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nice answer. Welcome to markdown :-(</p>
</div>
<div id="comment-42070-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 14:17)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="42072"></span>
<div id="comment-42072" class="comment">
<div id="post-42072-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Alternatively you could present your solution in a blog entry via your OSM user account.</p>
</div>
<div id="comment-42072-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 14:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42073"></span>
<div id="comment-42073" class="comment not_top_scorer">
<div id="post-42073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>: … where there is also Markdown, isn't it?</p>
<p><a href="https://help.openstreetmap.org/users/10746/cyberang3l">@cyberang3l</a>: the "preview" does work partly. Use <a href="http://daringfireball.net/projects/markdown/dingus">http://daringfireball.net/projects/markdown/dingus</a> instead for previewing "complex" stuff. And <a href="http://daringfireball.net/projects/markdown/syntax">http://daringfireball.net/projects/markdown/syntax</a> should explain the formatting … however, I did not get the XML block to work, too.</p>
</div>
<div id="comment-42073-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 15:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42122"></span>
<div id="comment-42122" class="comment">
<div id="post-42122-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For anyone interested, I collected a few different map styles and I made a script for easy installation in one go. One of the map styles is the OSM Bright map that includes contour lines. I didn't use the XML code above, but I incorporated the change in the CartoCSS.</p>
<p>You can check it out here: <a href="https://github.com/cyberang3l/osm-maps">https://github.com/cyberang3l/osm-maps</a></p>
</div>
<div id="comment-42122-info" class="comment-info">
<span class="comment-age">(04 Apr '15, 00:56)</span> <span class="comment-user userinfo">cyberang3l</span>
</div>
</div>
</div>
<div id="comment-tools-42052" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42052-form-container" class="comment-form-container">
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

