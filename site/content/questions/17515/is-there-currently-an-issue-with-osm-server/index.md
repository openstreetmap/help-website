+++
type = "question"
title = "Is there currently an issue with OSM server ?"
description = '''In particular api.openstreetmap.org (redirects to main site with a browser) ? I am finding JOSM fails when trying to download a map section. &quot;GET http://api.openstreetmap.org/api/capabilities...&quot;.  I also note while starting JOSM failed to load a image from a .com site ? Thats interesting too ! &quot;Fai...'''
date = "2012-11-06T05:27:00Z"
lastmod = "2012-11-06T23:23:00Z"
weight = 17515
keywords = [ "josm", "failed" ]
aliases = [ "/questions/17515" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there currently an issue with OSM server ?](/questions/17515/is-there-currently-an-issue-with-osm-server)

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
<span id="post-17515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In particular api.openstreetmap.org (redirects to main site with a browser) ?</p>
<p>I am finding JOSM fails when trying to download a map section. "GET <a href="http://api.openstreetmap.org/api/capabilities...">http://api.openstreetmap.org/api/capabilities...".</a></p>
<p>I also note while starting JOSM failed to load a image from a .com site ? Thats interesting too ! "Failed to load <a href="http://o.aolcdn.com/os/mapquest/marketing/MQ_Icon/Tiny/MQ_Icon_Tiny.png,">http://o.aolcdn.com/os/mapquest/marketing/MQ_Icon/Tiny/MQ_Icon_Tiny.png,</a> use cached file and retry next time."</p>
<p>I have recently updated my Ubuntu OS so it could be a java problem but strace does not spot anything obvious.</p>
<p>David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '12, 05:27</strong></p>
<img src="https://secure.gravatar.com/avatar/85e1d5d2a4825f5251297994741cd33b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davo&#39;s gravatar image" />
<p><span>Davo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17515" class="comments-container">
&#10;</div>
<div id="comment-tools-17515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17515-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="17516"></span>

<div id="answer-container-17516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the <a href="http://wiki.openstreetmap.org/wiki/Platform_Status">Platform Status</a> there is no problem with the API. Downloading data with JOSM succeeds here. Does it work for you meanwhile? If not it might be a problem of your local network.</p>
<p><a href="http://api.openstreetmap.org/api/capabilities...">http://api.openstreetmap.org/api/capabilities...</a> redirecting to a HTML page is completely normal, the dots aren't part of the URL. <a href="http://api.openstreetmap.org/api/capabilities">http://api.openstreetmap.org/api/capabilities</a> instead should return with a XML file which is then parsed by JOSM in order to get information about the current API version, various restrictions and so on.</p>
<p>And the MapQuest icon seems to have changed it's location. This shouldn't be a problem for you and should get fixed with the next JOSM update.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '12, 06:40</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17516" class="comments-container">
<span id="17517"></span>
<div id="comment-17517" class="comment">
<div id="post-17517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks Scai, so, an hour or so later, yep, the image is now downloading from MapQuest fine. Both in JOSM and a browser.</p>
<p>However, the real problem remains in JOSM. I select a small area of the map to download and it eventually fails. Indications are that its still failing at the "GET <a href="http://api.openstreetmap.org/api/capabilities...">http://api.openstreetmap.org/api/capabilities..."</a> but, as you state, I don't get to see what it really is down loading, just a truncated version of it. Java ! If I knew what was hidden behind the "..." I could try it myself.</p>
<p>I do see a message box saying "Failed to upload data to or download data from 'http://api.openstreetmap.org/api/' due to a problem with transferring data. Details (untranslated): connect timed out"</p>
<p>Still don't see any reason to suspect my Java install but I am starting to assume that is the case.</p>
<p>Thanks for your help, especially confirming its working fine there.</p>
<p>David</p>
</div>
<div id="comment-17517-info" class="comment-info">
<span class="comment-age">(06 Nov '12, 07:51)</span> <span class="comment-user userinfo">Davo</span>
</div>
</div>
<span id="17518"></span>
<div id="comment-17518" class="comment">
<div id="post-17518-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is nothing hidden behind the "...", for downloading actual data JOSM will call <a href="http://api.openstreetmap.org/api/0.6/map?bbox=...">http://api.openstreetmap.org/api/0.6/map?bbox=...</a> per default.</p>
<p>If you get a timeout try downloading a smaller area or try it again later. I had some timeouts in the last few days myself, I think this is a known problem. Otherwise try contacting someone on <a href="http://wiki.openstreetmap.org/wiki/IRC">IRC</a>, this help site is not really suited for such problems.</p>
</div>
<div id="comment-17518-info" class="comment-info">
<span class="comment-age">(06 Nov '12, 08:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17516-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17534"></span>

<div id="answer-container-17534" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17534-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the record, I am now convinced that this problem is external, most likely local network problems but further testing will be needed to be quite sure.</p>
<p>To be clear, your browser should be able to return a bit of simple xml when pointed to <a href="http://api.openstreetmap.org/api/capabilities">http://api.openstreetmap.org/api/capabilities</a></p>
<p>I can 'sometimes'....</p>
<p>David</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '12, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/85e1d5d2a4825f5251297994741cd33b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davo&#39;s gravatar image" />
<p><span>Davo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17534" class="comments-container">
&#10;</div>
<div id="comment-tools-17534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17534-form-container" class="comment-form-container">
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

