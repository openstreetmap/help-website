+++
type = "question"
title = "How do I study POI density in OSM?"
description = '''Given the question: Which location has the most of a specific POI mapped in OSM per area? If I load OSM data into PostgreSQL, can it answer that type of query? A more specific example would be &quot;Where in the US does OSM contain the most park benches per square mile?&quot;'''
date = "2014-12-07T03:27:00Z"
lastmod = "2014-12-07T21:20:00Z"
weight = 39110
keywords = [ "density", "poi" ]
aliases = [ "/questions/39110" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I study POI density in OSM?](/questions/39110/how-do-i-study-poi-density-in-osm)

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
<span id="post-39110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39110-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given the question: Which location has the most of a specific POI mapped in OSM per area? If I load OSM data into PostgreSQL, can it answer that type of query?</p>
<p>A more specific example would be "Where in the US does OSM contain the most park benches per square mile?"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-density" rel="tag" title="see questions tagged &#39;density&#39;">density</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '14, 03:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-39110" class="comments-container">
<span id="39123"></span>
<div id="comment-39123" class="comment">
<div id="post-39123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you try <a href="http://osmatrix.uni-hd.de/">http://osmatrix.uni-hd.de/</a> ?</p>
</div>
<div id="comment-39123-info" class="comment-info">
<span class="comment-age">(07 Dec '14, 20:33)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-39110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39110-form-container" class="comment-form-container">
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

<span id="39124"></span>

<div id="answer-container-39124" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39124-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mike N has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That kind of question is generally answered with a "heat map" or "hot spot" analysis in GIS (Geographical Information System) terminology.</p>
<p>QGIS or ArcGIS can do that for you, once you have the data in some kind of GIS ready format (database or shapefile):</p>
<p><strong>QGIS - Heat Map plugin:</strong> <a href="http://docs.qgis.org/2.0/en/docs/user_manual/plugins/plugins_heatmap.html">http://docs.qgis.org/2.0/en/docs/user_manual/plugins/plugins_heatmap.html</a></p>
<p><strong>ArcGIS - Optimized Hot Spot Analysis (Spatial Statistics):</strong> <a href="http://resources.arcgis.com/en/help/main/10.2/index.html#//005p00000058000000">http://resources.arcgis.com/en/help/main/10.2/index.html#//005p00000058000000</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '14, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-39124" class="comments-container">
&#10;</div>
<div id="comment-tools-39124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39124-form-container" class="comment-form-container">
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

