+++
type = "question"
title = "Use Bike layer openstreetMap javascript"
description = '''I would like to use the bike layer like this one: https://www.openstreetmap.org/#map=14/37.7874/-2.9519&amp;amp;layers=C But I don´t know which url to use. At the moment I have just the default one: var map = L.map(&#x27;map&#x27;); L.tileLayer(&#x27;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#x27;, {  attribution: ...'''
date = "2020-04-01T21:08:00Z"
lastmod = "2020-04-01T23:03:00Z"
weight = 73935
keywords = [ "openstreetmap", "layers", "javascript" ]
aliases = [ "/questions/73935" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use Bike layer openstreetMap javascript](/questions/73935/use-bike-layer-openstreetmap-javascript)

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
<span id="post-73935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73935-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to use the bike layer like this one:</p>
<p><a href="https://www.openstreetmap.org/#map=14/37.7874/-2.9519&amp;layers=C">https://www.openstreetmap.org/#map=14/37.7874/-2.9519&amp;layers=C</a></p>
<p>But I don´t know which url to use. At the moment I have just the default one:</p>
<pre><code>var map = L.map(&#39;map&#39;);
L.tileLayer(&#39;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
  attribution: &#39;Map data &amp;copy; &lt;a href=&quot;http://www.osm.org&quot;&gt;OpenStreetMap&lt;/a&gt;&#39;
}).addTo(map);</code></pre>
<p>Any ideas?</p>
<p>Code from: <a href="https://github.com/mpetazzoni/leaflet-gpx">https://github.com/mpetazzoni/leaflet-gpx</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '20, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/005c016b14d6c184014813b39d19e9a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cesp7&#39;s gravatar image" />
<p><span>Cesp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cesp7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73935" class="comments-container">
&#10;</div>
<div id="comment-tools-73935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73935-form-container" class="comment-form-container">
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

<span id="73937"></span>

<div id="answer-container-73937" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73937-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-73937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cesp7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That particular layer is provided by <a href="https://www.thunderforest.com/">Thunderforest</a> which ordinarily operates as a <a href="https://www.thunderforest.com/pricing/">subscription service</a> (there appears to be a free hobby tier).</p>
<p>Usage instructions are <a href="https://www.thunderforest.com/maps/opencyclemap/">here</a>, which links to further tutorials.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '20, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-73937" class="comments-container">
&#10;</div>
<div id="comment-tools-73937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73937-form-container" class="comment-form-container">
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

