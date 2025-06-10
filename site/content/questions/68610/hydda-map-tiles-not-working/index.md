+++
type = "question"
title = "hydda map tiles not working"
description = '''I have been using  https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png (chrome developer error &quot;GET https://c.tile.openstreetmap.se/hydda/full/7/35/51.png net::ERR_CERT_DATE_INVALID&quot;) as a tile layer for several months now, and it quit working. My other tile layers are working fine. Can som...'''
date = "2019-04-02T14:53:00Z"
lastmod = "2020-05-09T02:57:00Z"
weight = 68610
keywords = [ "water", "waterway", "sweden" ]
aliases = [ "/questions/68610" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [hydda map tiles not working](/questions/68610/hydda-map-tiles-not-working)

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
<span id="post-68610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68610-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png (chrome developer error "GET <a href="https://c.tile.openstreetmap.se/hydda/full/7/35/51.png">https://c.tile.openstreetmap.se/hydda/full/7/35/51.png</a> net::ERR_CERT_DATE_INVALID") as a tile layer for several months now, and it quit working. My other tile layers are working fine. Can someone point me in the correct direction on who I need to contact? These tiles seem to be based in Sweden, is there a contact person in Sweden, or do I contact someone here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-sweden" rel="tag" title="see questions tagged &#39;sweden&#39;">sweden</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '19, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f3f0630fa2fcba6cbbe5776cf4c252ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scottgeo&#39;s gravatar image" />
<p><span>scottgeo</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scottgeo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68610" class="comments-container">
<span id="68611"></span>
<div id="comment-68611" class="comment">
<div id="post-68611-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm facing the same issue, it looks like a problem with their certificate! Any solution? Our platform is broken.</p>
</div>
<div id="comment-68611-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 15:00)</span> <span class="comment-user userinfo">Rafael Berro</span>
</div>
</div>
<span id="68617"></span>
<div id="comment-68617" class="comment">
<div id="post-68617-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It was fixed! I'll keep using http for a few days before use https again.</p>
</div>
<div id="comment-68617-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 18:35)</span> <span class="comment-user userinfo">Rafael Berro</span>
</div>
</div>
</div>
<div id="comment-tools-68610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68610-form-container" class="comment-form-container">
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

<span id="74085"></span>

<div id="answer-container-74085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74085-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-74085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry all, we had a disk crash at openstreetmap.se. Due to easter this might take a few days. In wost case we'll have to reinstall the whole machine, that could take weeks.</p>
<p>As always we recommend installing your own tile server using our open stylesheet for your business critical solutions.</p>
<p><a href="https://github.com/karlwettin/carto-style-hydda">https://github.com/karlwettin/carto-style-hydda</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '20, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/94bbdf7692db409783b45d41cc065fd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karl%20Wettin&#39;s gravatar image" />
<p><span>Karl Wettin</span><br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karl Wettin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74085" class="comments-container">
<span id="74675"></span>
<div id="comment-74675" class="comment">
<div id="post-74675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any update on when the tile server will be fixed?</p>
</div>
<div id="comment-74675-info" class="comment-info">
<span class="comment-age">(09 May '20, 02:57)</span> <span class="comment-user userinfo">rohanmenon</span>
</div>
</div>
</div>
<div id="comment-tools-74085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68613"></span>

<div id="answer-container-68613" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68613-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll have to contact whoever it is that looks after openstreetmap.se. It's not in any way related to openstreetmap.org, so the admins of openstreetmap.org won't be able to help.</p>
<p>I've mentioned the problem in IRC; hopefully someone there knows someone who can fix it. <a href="http://openstreetmap.se/">http://openstreetmap.se/</a> has some contact information - you can try there too..</p>
<p>The site works just fine without https of course - you can change your tile layers to that temporarily if you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68613" class="comments-container">
<span id="68614"></span>
<div id="comment-68614" class="comment">
<div id="post-68614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like a temporary solution, I'll try to work without https until the problem is fixed, thank you so much!</p>
</div>
<div id="comment-68614-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 15:31)</span> <span class="comment-user userinfo">Rafael Berro</span>
</div>
</div>
<span id="74046"></span>
<div id="comment-74046" class="comment">
<div id="post-74046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello guys, all tiles from tile.openstreetmap.se/hydda/full/ are now returning 404 errors. Their server is not responding. Any idea who can we contact ?</p>
</div>
<div id="comment-74046-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 08:28)</span> <span class="comment-user userinfo">Benjamin</span>
</div>
</div>
<span id="74048"></span>
<div id="comment-74048" class="comment">
<div id="post-74048-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18165/benjamin">@Benjamin</a> - the answer that you commented on said "I've mentioned the problem in IRC; hopefully someone there knows someone who can fix it. <a href="http://openstreetmap.se/">http://openstreetmap.se/</a> has some contact information - you can try there too". Did you try either of those things?</p>
</div>
<div id="comment-74048-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 10:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74050"></span>
<div id="comment-74050" class="comment">
<div id="post-74050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, Thank you for your response. Unfortunately as their server is completely down, I can't find any contact information, that's why asked. I was wondering if you still had the corresponding irc channel name maybe?</p>
</div>
<div id="comment-74050-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 10:36)</span> <span class="comment-user userinfo">Benjamin</span>
</div>
</div>
<span id="74060"></span>
<div id="comment-74060" class="comment">
<div id="post-74060-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry if this leads like a "let me google that for you" response, but:</p>
<p>Although the server is down now it wasn't in the past, and therefore we can see what it last said at <a href="https://web.archive.org/web/20191009220737/https://openstreetmap.se/om">https://web.archive.org/web/20191009220737/https://openstreetmap.se/om</a> . That suggests talk-se, which has been <a href="https://lists.openstreetmap.org/pipermail/talk-se/2020-March/thread.html">active</a> this month. Similarly the IRC channel is still there and has a dozen or so people in it, although it is not very active.</p>
</div>
<div id="comment-74060-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 13:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68613-form-container" class="comment-form-container">
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

