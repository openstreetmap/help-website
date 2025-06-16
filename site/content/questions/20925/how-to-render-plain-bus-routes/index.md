+++
type = "question"
title = "How to render plain bus routes?"
description = '''I already rendered tram and rail lines, but i have problem render bus routes. I use this script to render rail lines: #!/usr/bin/env python import mapnik stylesheet = &#x27;schema.xml&#x27; image = &#x27;output.png&#x27; m = mapnik.Map(4000,2671) mapnik.load_map(m, stylesheet) m.zoom_all()  mapnik.render_to_file(m, ima...'''
date = "2013-03-22T23:54:00Z"
lastmod = "2013-03-23T19:44:00Z"
weight = 20925
keywords = [ "bus", "route", "osm", "mapnik", "rendering" ]
aliases = [ "/questions/20925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to render plain bus routes?](/questions/20925/how-to-render-plain-bus-routes)

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
<span id="post-20925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20925-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I already rendered tram and rail lines, but i have problem render bus routes. I use this script to render rail lines:</p>
<p><code>#!/usr/bin/env python import mapnik stylesheet = 'schema.xml' image = 'output.png' m = mapnik.Map(4000,2671) mapnik.load_map(m, stylesheet) m.zoom_all() mapnik.render_to_file(m, image)</code></p>
<p>and this scheme:</p>
<p><code>&lt;?xml version="1.0" encoding="utf-8"?&gt; &lt;Map background-color="white" srs="+proj=latlong +datum=WGS84"&gt; &lt;Style name="rail"&gt; &lt;Rule&gt; &lt;Filter&gt;[railway] = 'rail' &lt;/Filter&gt; &lt;LineSymbolizer stroke="black" stroke-width="1"/&gt; &lt;/Rule&gt; &lt;/Style&gt; &lt;Layer name="rails" status="on" srs="+proj=latlong +datum=WGS84"&gt; &lt;StyleName&gt;rail &lt;/StyleName&gt; &lt;Datasource&gt; &lt;Parameter name="type"&gt;osm &lt;/Parameter&gt; &lt;Parameter name="file"&gt;map.osm &lt;/Parameter&gt; &lt;/Datasource&gt; &lt;/Layer&gt; &lt;/Map&gt;</code></p>
<p>To render tram lines I only changed filter to [railway] = 'tram'. I tried different filters to render bus routes, but nothing worked. I want only black lines 1pixel wide on white background. How can I do it?</p>
<p><strong>Edit:</strong> I have rendered bus routes from postgis database. I imported the map.osm using osm2pgsl. And changed Datasource in schema.xml. The problem is different aspect ratio. This happen when i overlap the images <span>(clipped overlaping images)</span>. Red - tram, azur - bus. Bus image has white border on left and right side.</p>
<p><strong>Edit2:</strong> Ratio problem solved, I have bad srs projection in layer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '13, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/3c86ff28dd11badc03a1e53a7edb8973?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lived&#39;s gravatar image" />
<p><span>lived</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lived has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '13, 13:23</strong> </span></p>
</div>
</div>
<div id="comments-container-20925" class="comments-container">
&#10;</div>
<div id="comment-tools-20925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20925-form-container" class="comment-form-container">
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

<span id="20940"></span>

<div id="answer-container-20940" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20940-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lived has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In a standard osm2pgsql-created database, bus routes will not be in the database - the roads making up the bus routes certainly are, but the information which bus route, if any, they belong to, isn't. There was a <a href="http://lists.openstreetmap.org/pipermail/talk/2013-March/066521.html">question about route relations</a> on the "talk" mailing list recently where a similar question was asked.</p>
<p>Showing the bus routes is much more difficult than showing the railways or trams in your case because you're doing something conceptually different. In your example you are not showing railway or tram <em>lines</em>, you are showing railway or tram <em>tracks</em> - these are easy to match. If you wanted to show tram <em>lines</em> (as in "tram #15 uses this piece of track") then you'd be looking at the same problem that you have with bus routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '13, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20940" class="comments-container">
&#10;</div>
<div id="comment-tools-20940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20940-form-container" class="comment-form-container">
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

