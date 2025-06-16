+++
type = "question"
title = "Exporting shapefiles from OpenStreetMap on QGis"
description = '''Hello, I&#x27;m a student working on a thesis of traffic optimization. I&#x27;m getting desperate: I need a shapefile out of a little portion of a city (Milan, in my case). I achieved that by downloading the portion of the map in &quot;.osm&quot;, installing the OpenStreetMap plugin on QGis, and exported in shapefiles....'''
date = "2013-09-16T14:54:00Z"
lastmod = "2013-09-19T15:41:00Z"
weight = 26383
keywords = [ "shapefile", "gis", "osm", "traffic_signals" ]
aliases = [ "/questions/26383" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting shapefiles from OpenStreetMap on QGis](/questions/26383/exporting-shapefiles-from-openstreetmap-on-qgis)

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
<span id="post-26383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26383-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm a student working on a thesis of traffic optimization. I'm getting desperate: I need a shapefile out of a little portion of a city (Milan, in my case). I achieved that by downloading the portion of the map in ".osm", installing the OpenStreetMap plugin on QGis, and exported in shapefiles. The main problem I found is that during this operation I lose a lot of data (my main problem is that I lose traffic lights information). I can clearly see that the traffic light is handled as a point in QGis and OSM but as I export as a shapefile and import it back in QGis I lose all the traffic ligths I had when I imported the portion of the map from OSM. I don't really know if I expalained myself well, my brain is actually dried out after all the searches I did on google and relatives. I'd gladly appreciate any tip or advice on how to get a shapefile with informations on traffic lights in it. Thanks in advance.</p>
<p>P.S. I need the map in shapefile format because I've to load it on Repast Simphony</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '13, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/218091ef6c8ffad55923d77a99713432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MassimoUNIMIB&#39;s gravatar image" />
<p><span>MassimoUNIMIB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MassimoUNIMIB has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '13, 14:55</strong> </span></p>
</div>
</div>
<div id="comments-container-26383" class="comments-container">
<span id="26400"></span>
<div id="comment-26400" class="comment">
<div id="post-26400-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>two hint for you:</p>
<p>Be sure that the OSM-import-plugin of QGIS can work with all you data: There is currently a problem with object id numbers szored in 64-bit data:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/64-bit_Identifiers">https://wiki.openstreetmap.org/wiki/64-bit_Identifiers</a></p>
<p>and:</p>
<p>all about OSM2Shapefile should be collected at <a href="https://wiki.openstreetmap.org/wiki/Shapefile">https://wiki.openstreetmap.org/wiki/Shapefile</a></p>
</div>
<div id="comment-26400-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 17:08)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26403"></span>
<div id="comment-26403" class="comment">
<div id="post-26403-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>one more idea: you can use ogr2ogr (<a href="http://www.gdal.org/ogr/index.html)">http://www.gdal.org/ogr/index.html)</a> to read the .osm file, then produce a shapefile from it. Once the data is in shapefile format, the 64-bit data isn't an issue.</p>
</div>
<div id="comment-26403-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 17:28)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="26418"></span>
<div id="comment-26418" class="comment">
<div id="post-26418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello everyone, thanks for the quick answers! My data is still pretty small, a little square located here: <a href="https://www.openstreetmap.org/#map=16/45.5012/9.2365">https://www.openstreetmap.org/#map=16/45.5012/9.2365</a> . I'm now triyng the ogr2ogr's way but I'm encountering new problems: it seems the driver doesn't like the geometry type "Geometry Collection" saying that shapefiles don't support that kind of geometry(Error6). I've tried to bypass (with skipfailures) it but it gives Error 1 "Non increasing node id. Use OSM_USE_CUSTOM_INDEXING=ON. I'm feeling a bit lost, probably because I can't find proper documentation anywhere!Can you point me to it?</p>
</div>
<div id="comment-26418-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 08:53)</span> <span class="comment-user userinfo">MassimoUNIMIB</span>
</div>
</div>
<span id="26438"></span>
<div id="comment-26438" class="comment">
<div id="post-26438-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>to extract points try something like this:</p>
<p>ogr2ogr -where "OGR_GEOMETRY='Point'" -lco SHPT=POINT outfile.shp infile.osm</p>
<p>Also, make sure you're using GDAL 1.10</p>
</div>
<div id="comment-26438-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 16:01)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="26493"></span>
<div id="comment-26493" class="comment">
<div id="post-26493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I tried that but it still gives me the same error: Non increasing node id. Use etc...". I found a temporary solution by downloading arcGis for desktop and converting the .osm maps with it. It still has some problems (it doubles some points and lines, but I guess I'll fix them with my software). Thanks for replying anyway! Bye.</p>
</div>
<div id="comment-26493-info" class="comment-info">
<span class="comment-age">(19 Sep '13, 09:51)</span> <span class="comment-user userinfo">MassimoUNIMIB</span>
</div>
</div>
</div>
<div id="comment-tools-26383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26383-form-container" class="comment-form-container">
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

<span id="26495"></span>

<div id="answer-container-26495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26495-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I find that far &amp; away the simplest way to get shapefiles from OSM data out of QGIS is to use osm2pgsql to import the data to a PostGIS database and then pull the data into QGIS that way.</p>
<p>A couple of things are necessary: use the hstore option to get all the tags; and create a view on the standard tables loaded by osm2pgsql to shorten all column names to &lt;= 10 characters if you need those with long names, such as <code>addr:housenumber</code> (otherwise QGIS gets stroppy, saving the data as a Shape file).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '13, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-26495" class="comments-container">
&#10;</div>
<div id="comment-tools-26495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26495-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26504"></span>

<div id="answer-container-26504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26504-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could take your OSM file, use OSMConvert to convert it to a CSV and then import that into qgis.</p>
<p>Also, you could use osmfilter to only keep relevant data.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files">https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '13, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-26504" class="comments-container">
&#10;</div>
<div id="comment-tools-26504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26504-form-container" class="comment-form-container">
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

