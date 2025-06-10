+++
type = "question"
title = "Having maps without data"
description = '''Using leaflet and OSM, to show some maps on my web application, I need to know if it is possible to have only roads map and remove data from the map which is shown on my page    L.tileLayer(&#x27;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#x27;, {  attribution: &#x27;&#x27;,  maxZoom: 19 }).addTo(map); '''
date = "2021-04-12T19:57:00Z"
lastmod = "2021-04-12T20:03:00Z"
weight = 79628
keywords = [ "openstreetmap", "leaflet" ]
aliases = [ "/questions/79628" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Having maps without data](/questions/79628/having-maps-without-data)

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
<span id="post-79628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using leaflet and OSM, to show some maps on my web application, I need to know if it is possible to have only roads map and remove data from the map which is shown on my page</p>
<p><img src="https://help.openstreetmap.org/upfiles/Untitled_uVfjvAJ.jpg" alt="alt text" /></p>
<pre><code> L.tileLayer(&#39;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
    attribution: &#39;&#39;,
    maxZoom: 19
}).addTo(map);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '21, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3b7a89ef361fa79a5bdaa01c87dc23d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ehsan_1362&#39;s gravatar image" />
<p><span>Ehsan_1362</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ehsan_1362 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79628" class="comments-container">
&#10;</div>
<div id="comment-tools-79628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79628-form-container" class="comment-form-container">
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

<span id="79629"></span>

<div id="answer-container-79629" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79629-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ehsan_1362 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible but you will have to set up your own tile server, and modify the map style to remove those elements you do not want. Setting up your own tile server is described on switch2osm.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '21, 20:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79629" class="comments-container">
&#10;</div>
<div id="comment-tools-79629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79629-form-container" class="comment-form-container">
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

