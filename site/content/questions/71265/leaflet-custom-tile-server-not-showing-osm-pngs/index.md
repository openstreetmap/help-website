+++
type = "question"
title = "Leaflet custom tile server not showing osm .pngs"
description = '''Hello All, I am working in a Windows environment. In an .aspx web form L.tileLayer(&#x27;http://tile.osm.org/{z}/{x}/{y}.png&#x27;, { }).addTo(map); will show the correct OSM tile.  I also have some custom tiles on MyOwnCustomServer.  If I type http://MyOwnCustomServer/7/19/43.png into my web browser, it will...'''
date = "2019-10-22T21:52:00Z"
lastmod = "2019-10-22T23:37:00Z"
weight = 71265
keywords = [ "leaflet", "tile", "custom", "osm", "server" ]
aliases = [ "/questions/71265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Leaflet custom tile server not showing osm .pngs](/questions/71265/leaflet-custom-tile-server-not-showing-osm-pngs)

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
<span id="post-71265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello All, I am working in a Windows environment. In an .aspx web form</p>
<p>L.tileLayer('http://tile.osm.org/{z}/{x}/{y}.png', { }).addTo(map);</p>
<p>will show the correct OSM tile.</p>
<p>I also have some custom tiles on MyOwnCustomServer.</p>
<p>If I type <a href="http://MyOwnCustomServer/7/19/43.png">http://MyOwnCustomServer/7/19/43.png</a> into my web browser, it will show the correct tile.</p>
<p>However,</p>
<p>L.tileLayer('http://MyOwnCustomServer/7/19/43.png', { }).addTo(map);</p>
<p>AND</p>
<p>L.tileLayer('http://MyOwnCustomServer/{z}/{x}/{y}.png', { }).addTo(map);</p>
<p>do not show any OSM tiles.</p>
<p>Does anyone know what I need to do to get this to work? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '19, 21:52</strong></p>
<img src="https://secure.gravatar.com/avatar/41a7fedf2793f657dcef6efefeb10b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeattleHeather&#39;s gravatar image" />
<p><span>SeattleHeather</span><br />
<span class="score" title="220 reputation points">220</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeattleHeather has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '19, 22:06</strong> </span></p>
</div>
</div>
<div id="comments-container-71265" class="comments-container">
&#10;</div>
<div id="comment-tools-71265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71265-form-container" class="comment-form-container">
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

<span id="71266"></span>

<div id="answer-container-71266" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71266-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured out the answer. My browser wasn't clearing the cache. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '19, 23:37</strong></p>
<img src="https://secure.gravatar.com/avatar/41a7fedf2793f657dcef6efefeb10b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeattleHeather&#39;s gravatar image" />
<p><span>SeattleHeather</span><br />
<span class="score" title="220 reputation points">220</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeattleHeather has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71266" class="comments-container">
&#10;</div>
<div id="comment-tools-71266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71266-form-container" class="comment-form-container">
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

