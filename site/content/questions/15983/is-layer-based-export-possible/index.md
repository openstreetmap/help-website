+++
type = "question"
title = "Is layer based export possible?"
description = '''While importing an area these is a restriction on the number of nodes. Not the all nodes are equally necessary for any specific mapping. By using ArcGIS Editor for OpenStreetmap, it is both so huge to load osm and so difficult to manage the complexity of datas.  Is there any way to extract map by se...'''
date = "2012-09-12T01:53:00Z"
lastmod = "2012-09-12T11:54:00Z"
weight = 15983
keywords = [ "arcgis", "layer", "import" ]
aliases = [ "/questions/15983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is layer based export possible?](/questions/15983/is-layer-based-export-possible)

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
<span id="post-15983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15983-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While importing an area these is a restriction on the number of nodes. Not the all nodes are equally necessary for any specific mapping. By using ArcGIS Editor for OpenStreetmap, it is both so huge to load osm and so difficult to manage the complexity of datas.</p>
<p>Is there any way to extract map by sellecting different the layers?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '12, 01:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f68589722472cc6f28a8973204fb104e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sinanf&#39;s gravatar image" />
<p><span>sinanf</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sinanf has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-15983" class="comments-container">
&#10;</div>
<div id="comment-tools-15983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15983-form-container" class="comment-form-container">
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

<span id="15989"></span>

<div id="answer-container-15989" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15989-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no concept of predefined layers within OpenStreetMap.</p>
<p>However, you can get for example the street grid related objects with a query like</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(node%5Bhighway%5D(bbox);way%5Bhighway%5D(bbox););(._;%3C;%3E;);out">http://overpass-api.de/api/interpreter?data=(node[highway](bbox);way[highway](bbox););(._;&lt;;&gt;;);out</a> meta;&amp;bbox=7.0,50.6,7.3,50.8</p>
<p>This is only one forth of the total data in this region. The region is specified with the bounding box</p>
<pre><code>bbox=7.0,50.6,7.3,50.8</code></pre>
<p>where 7.0 is the western border in degrees of longitude east (degrees of longitude west by negative values), 50.6 (degrees of latitude north) is the southern border, 7.3 is the eastern border and 50.8 the northern border.</p>
<p>If you want to download much larger areas, it will take much mor time. In this case you must tell the server that you expect a large download by providing the maximum timeout in seconds:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Btimeout:900%5D;(node%5Bhighway%5D(bbox);way%5Bhighway%5D(bbox););(._;%3C;%3E;);out">http://overpass-api.de/api/interpreter?data=[timeout:900];(node[highway](bbox);way[highway](bbox););(._;&lt;;&gt;;);out</a> meta;&amp;bbox=7.0,50.6,7.3,50.8</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '12, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-15989" class="comments-container">
<span id="15996"></span>
<div id="comment-15996" class="comment">
<div id="post-15996-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is great for viewing, but dangerous for editing. For example, the data you downloaded may be sharing nodes non-dowloaded data. Since OSM data is pretty much free-form, there is no garantee that a given area respects "reasonable constraints". So please do not work with partial data if you intend to contribute back to OSM.</p>
</div>
<div id="comment-15996-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 11:54)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15989-form-container" class="comment-form-container">
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

