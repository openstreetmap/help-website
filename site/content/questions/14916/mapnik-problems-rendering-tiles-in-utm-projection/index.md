+++
type = "question"
title = "Mapnik: Problems rendering tiles in UTM projection"
description = '''Hello all, I am using mapnik to generate slippy maps, which are then used within my software. This works fine for the &#x27;normal&#x27; projections, such as 900913.  But when rendering tiles in UTM, I face strange behaviors: some tiles seem to be shifted. I have already searched and found the description of ...'''
date = "2012-08-09T08:11:00Z"
lastmod = "2012-08-10T13:04:00Z"
weight = 14916
keywords = [ "map", "rendering", "slippy", "mapnik", "utm" ]
aliases = [ "/questions/14916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik: Problems rendering tiles in UTM projection](/questions/14916/mapnik-problems-rendering-tiles-in-utm-projection)

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
<span id="post-14916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14916-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,<br />
I am using mapnik to generate slippy maps, which are then used within my software. This works fine for the 'normal' projections, such as 900913.<br />
But when rendering tiles in UTM, I face strange behaviors: some tiles seem to be shifted. I have already searched and found the <a href="http://old.nabble.com/Problems-with-some-Mapnik-projections-td28751475.html">description of similar problems</a> for UTM rendering, but following the instructions (setting the extent paramter) did not really help.<br />
These errors only occur when rendering tiles (using the generate_tiles.py script); generating a single image for the same region (generate_image.py) works fine...<br />
Am I missing the point?<br />
</p>
<p>This is what I did:<br />
</p>
<ol>
<li>setup under windows: complete from the scratch, incl. PostgreSQL 9.1, PostGIS 1.5, Python 2.7, proj4</li>
<li>Mapnik: installed version 2.0.1.RC0, mapnik python from <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">http://svn.openstreetmap.org/applications/rendering/mapnik/</a></li>
<li>Data loaded into DB using osm2pgsql with the <strong>-E 2157</strong> option (UTM zone for Ireland)</li>
<li>Changes in configuration:
<ol>
<li><p>osm.xml, changed to (the string was provided by <a href="http://spatialreference.org/ref/epsg/2157/">http://spatialreference.org/ref/epsg/2157/</a>):</p>
<pre><code>&lt;Map background-color=&quot;#b5d0d0&quot; srs=&quot;+proj=tmerc +lat_0=53.5 +lon_0=-8 +k=0.99982 +x_0=600000 +y_0=750000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs&quot; minimum-version=&quot;2.0.0&quot;&gt;</code></pre></li>
<li><p>datasource-settings.xml.inc: Projected Bounds from website -&gt;</p>
<pre><code>&lt;Parameter name=&quot;extent&quot;&gt;418829.9650, 511786.6808, 786046.9273, 964701.5937&lt;/Parameter&gt;</code></pre></li>
<li><p>settings.xml: changed the referenced osm2pgsql_projection:</p>
<pre><code>&lt;!ENTITY osm2pgsql_projection &quot;+proj=tmerc +lat_0=53.5 +lon_0=-8 +k=0.99982 +x_0=600000 +y_0=750000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs&quot;&gt;</code></pre></li>
<li><p>generate_tiles.py:</p>
<pre><code>bbox = (-10.6000, 51.3300, -5.3300, 55.4000)</code></pre></li>
</ol></li>
</ol>
<br />
This little error troubles me now for some days; it is really frustrating, has anyone an idea of how to proceed? Is the patch mentioned in <a href="http://old.nabble.com/Re%3A-Problems-with-some-Mapnik-projections-p28777331.html">this message</a> already part of mapnik_2.0.1.RC0?<br />
A sample snapshot from the generated slippy map can be viewed at <a href="http://old.nabble.com/Problems-rendering-tiles-in-UTM-projection-p34134479.html">original post on mapnik forum</a><br />
<br />
Kind regards, Dieter
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-slippy" rel="tag" title="see questions tagged &#39;slippy&#39;">slippy</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '12, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d516615e19cde7dba2a7e95b4299b079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="19melo00&#39;s gravatar image" />
<p><span>19melo00</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="19melo00 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-14916" class="comments-container">
&#10;</div>
<div id="comment-tools-14916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14916-form-container" class="comment-form-container">
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

<span id="14920"></span>

<div id="answer-container-14920" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14920-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>generate_tiles.py uses spherical mercartor for calculating how big the tiles should be. And generate_image.py overrides the projection used in the style. You need to tweak these programs a bit to work with other projections.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '12, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-14920" class="comments-container">
<span id="14945"></span>
<div id="comment-14945" class="comment">
<div id="post-14945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gnonthgol, thanks for your answer. As I understand you, the problem might be due to the transformations between my map's srs and the class GoogleProjection used to calculate the tiles? I have checked the srs used within the map (and passed to the generate_tiles.py), that's excactly the one I intented to use (UTM 2157 with the settings above).</p>
<p>I have no idea how this 'bug' happens, but I can nail it down to the allignment of tiles. The error is more than one pixel, so simple rounding errors seem not to be the case. Can you give me some additional hints for the tweaking?</p>
<p>Thanks so far!</p>
</div>
<div id="comment-14945-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 13:04)</span> <span class="comment-user userinfo">19melo00</span>
</div>
</div>
</div>
<div id="comment-tools-14920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14920-form-container" class="comment-form-container">
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

