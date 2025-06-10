+++
type = "question"
title = "Map layer &quot;standard&quot; always grey"
description = '''Hi, Url where you can find the map : https://beta.montreal.ca/en/requests311/report-pothole/location All images downloaded from https://c.tile.openstreetmap.fr/hot/* are grey Like : https://c.tile.openstreetmap.fr/hot/17/38754/46886.png, https://b.tile.openstreetmap.fr/hot/17/38754/46888.png'''
date = "2021-05-27T16:42:00Z"
lastmod = "2021-05-27T21:36:00Z"
weight = 80328
keywords = [ "website", "tiles" ]
aliases = [ "/questions/80328" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Map layer "standard" always grey](/questions/80328/map-layer-standard-always-grey)

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
<span id="post-80328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Url where you can find the map : <a href="https://beta.montreal.ca/en/requests311/report-pothole/location">https://beta.montreal.ca/en/requests311/report-pothole/location</a> All images downloaded from <a href="https://c.tile.openstreetmap.fr/hot/*">https://c.tile.openstreetmap.fr/hot/*</a> are grey</p>
<p>Like : <a href="https://c.tile.openstreetmap.fr/hot/17/38754/46886.png,">https://c.tile.openstreetmap.fr/hot/17/38754/46886.png,</a> <a href="https://b.tile.openstreetmap.fr/hot/17/38754/46888.png">https://b.tile.openstreetmap.fr/hot/17/38754/46888.png</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '21, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/3112f22632f63d8e4841594803823e7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olivier%20Albertini&#39;s gravatar image" />
<p><span>Olivier Albe...</span><br />
<span class="score" title="13 reputation points">13</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olivier Albertini has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80328" class="comments-container">
&#10;</div>
<div id="comment-tools-80328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80328-form-container" class="comment-form-container">
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

<span id="80329"></span>

<div id="answer-container-80329" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80329-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Olivier Albertini has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not the standard tile layer, it's the <a href="https://wiki.openstreetmap.org/wiki/Humanitarian_map_style">humanitarian</a> one. If I unzoom till level 12 it starts working.</p>
<p>Same problem happens on <a href="https://www.openstreetmap.org/search?query=montr%C3%A9al#map=14/45.4980/-73.5490&amp;layers=H">openstreetmap.org</a> in the montréal area. In Paris I have problems at zoom level 17.</p>
<p>The infrastructure behind this layer is managed in this <a href="https://github.com/osm-fr/infrastructure/issues">repository</a>. The "gray tiles" issue has been happening several times this last year, but it should be resolved. You can open a new issue to describe your problem.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '21, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80329" class="comments-container">
<span id="80331"></span>
<div id="comment-80331" class="comment">
<div id="post-80331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is what we found during the investigation too. Thanks for your help! Do you know if the standard tile layer is more stable ?</p>
</div>
<div id="comment-80331-info" class="comment-info">
<span class="comment-age">(27 May '21, 19:09)</span> <span class="comment-user userinfo">Olivier Albe...</span>
</div>
</div>
<span id="80332"></span>
<div id="comment-80332" class="comment">
<div id="post-80332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The infrastructure is way bigger. But for garanteed reliability, you'll have to go to either paid services, self-hosting or at least tile caching.</p>
<p>Regards.</p>
</div>
<div id="comment-80332-info" class="comment-info">
<span class="comment-age">(27 May '21, 21:36)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-80329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80329-form-container" class="comment-form-container">
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

