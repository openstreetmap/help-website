+++
type = "question"
title = "Getting the longitude and latitude from local Nominatim server."
description = '''Hello, I have setup a local Nominatim server using the instructions found on this site: https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/. I have tested the server using Luxembourg and it works.  I was wondering if I could use this Nominatim server to extract the longitude lat...'''
date = "2018-01-29T14:25:00Z"
lastmod = "2018-01-29T15:22:00Z"
weight = 61883
keywords = [ "nominatim" ]
aliases = [ "/questions/61883" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting the longitude and latitude from local Nominatim server.](/questions/61883/getting-the-longitude-and-latitude-from-local-nominatim-server)

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
<span id="post-61883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61883-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have setup a local Nominatim server using the instructions found on this site: <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/.">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/.</a> I have tested the server using Luxembourg and it works.</p>
<p>I was wondering if I could use this Nominatim server to extract the longitude latitude coordinates being called from outside like an API call. I already have tiles made from my mapnik server and I would like to highlights the points of the search from the user by getting the longitude and latitude from the nominatim server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '18, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/206bbb2d3464a897f0b828361911ef31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ujjawal&#39;s gravatar image" />
<p><span>Ujjawal</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ujjawal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61883" class="comments-container">
&#10;</div>
<div id="comment-tools-61883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61883-form-container" class="comment-form-container">
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

<span id="61884"></span>

<div id="answer-container-61884" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61884-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ujjawal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim has multiple output formats.</p>
<p>This is HTML <a href="https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=html,">https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=html,</a> this is JSON <a href="https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=jsonv2</a> and XML <a href="https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=xml">https://nominatim.openstreetmap.org/search.php?q=paris&amp;format=xml</a></p>
<p>The various parameters are explained on <a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a></p>
<p>On your own installation you might need to use <a href="http://IPADDRESS/nominatim/search.php">http://IPADDRESS/nominatim/search.php</a> instead of <a href="http://IPADDRESS/search.php">http://IPADDRESS/search.php</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '18, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-61884" class="comments-container">
<span id="61885"></span>
<div id="comment-61885" class="comment">
<div id="post-61885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks!! This is what I needed.</p>
</div>
<div id="comment-61885-info" class="comment-info">
<span class="comment-age">(29 Jan '18, 15:22)</span> <span class="comment-user userinfo">Ujjawal</span>
</div>
</div>
</div>
<div id="comment-tools-61884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61884-form-container" class="comment-form-container">
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

