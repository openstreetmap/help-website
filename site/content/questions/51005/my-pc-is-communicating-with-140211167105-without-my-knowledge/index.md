+++
type = "question"
title = "My PC is communicating with 140.211.167.105 without my knowledge"
description = '''My PC is communicating with 140.211.167.105 without my knowledge. I just found this today and traced the IP address to stormfly-02.osm.osuosl.org. I can&#x27;t find the software on my PC that is doing this.  How do I stop this communication? Please email me an answer ASAP to gbugh@yahoo.com I don&#x27;t want ...'''
date = "2016-07-20T22:59:00Z"
lastmod = "2016-07-21T13:19:00Z"
weight = 51005
keywords = [ "help" ]
aliases = [ "/questions/51005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [My PC is communicating with 140.211.167.105 without my knowledge](/questions/51005/my-pc-is-communicating-with-140211167105-without-my-knowledge)

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
<span id="post-51005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51005-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My PC is communicating with 140.211.167.105 without my knowledge. I just found this today and traced the IP address to stormfly-02.osm.osuosl.org. I can't find the software on my PC that is doing this.</p>
<p>How do I stop this communication? Please email me an answer ASAP to gbugh@yahoo.com</p>
<p>I don't want to signup on this webpage because I don't even know what this is but I had to to ask this question.</p>
<p>Thanks, George Bugh</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '16, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/71b729171dcb17d066d74038421dcf23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gbugh&#39;s gravatar image" />
<p><span>gbugh</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gbugh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51005" class="comments-container">
<span id="51018"></span>
<div id="comment-51018" class="comment">
<div id="post-51018-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What software are you using on your PC which displays a map?</p>
</div>
<div id="comment-51018-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 11:10)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="51029"></span>
<div id="comment-51029" class="comment">
<div id="post-51029-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok thanks!!!</p>
<p>I was going to: <a href="https://db-ip.com">https://db-ip.com</a> and they were drawing maps on the webpage.</p>
<p>Yesterday I thought I saw svchost.exe going to that IP address but this morning I see only firefox.exe going there so I guess that's all it was.</p>
</div>
<div id="comment-51029-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 13:19)</span> <span class="comment-user userinfo">gbugh</span>
</div>
</div>
</div>
<div id="comment-tools-51005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51005-form-container" class="comment-form-container">
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

<span id="51011"></span>

<div id="answer-container-51011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51011-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://hardware.openstreetmap.org/servers/stormfly-02.openstreetmap.org/">hardware.openstreetmap.org</a> stormfly-02.osm.osuosl.org is a tile cache server. That means it is responsible for caching and delivering of <a href="https://wiki.openstreetmap.org/wiki/Tiles">tiles</a>, the images that are used for drawing the map.</p>
<p>It is very likely that this server gets accessed while you browse the map at openstreetmap.org or any other site that displays an OSM map and is using one of OSM's official tile servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51011" class="comments-container">
<span id="51013"></span>
<div id="comment-51013" class="comment">
<div id="post-51013-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Furthermore, OSUOSL is the Oregon State University Open Source Laboratory, which is basically this decade's sunsite...</p>
</div>
<div id="comment-51013-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 08:40)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-51011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51011-form-container" class="comment-form-container">
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

