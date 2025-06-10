+++
type = "question"
title = "Tirex: Prefetching of next zoom level"
description = '''Consider a low-loaded tile server. The actions of the users might be to:   pan around zoom in at the current map position  One idea might be to put the tiles in the queue that are next to the current meta tile (8 pieces - but this case might be already covered by the meta-tile technique) and the met...'''
date = "2012-11-04T20:38:00Z"
lastmod = "2012-11-05T13:26:00Z"
weight = 17474
keywords = [ "rendering", "tirex", "tileserver" ]
aliases = [ "/questions/17474" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tirex: Prefetching of next zoom level](/questions/17474/tirex-prefetching-of-next-zoom-level)

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
<span id="post-17474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Consider a low-loaded tile server.</p>
<p>The actions of the users might be to:</p>
<ul>
<li>pan around</li>
<li>zoom in at the current map position</li>
</ul>
<p>One idea might be to put the tiles in the queue that are next to the current meta tile (8 pieces - but this case might be already covered by the meta-tile technique) and the meta tile in the next zoom level at the current map position.</p>
<p>What is the starting point to implement such kind of pre-rendering in Tirex?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '12, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '12, 20:38</strong> </span></p>
</div>
</div>
<div id="comments-container-17474" class="comments-container">
&#10;</div>
<div id="comment-tools-17474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17474-form-container" class="comment-form-container">
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

<span id="17485"></span>

<div id="answer-container-17485" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17485-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can not implement this in Tirex alone, because requests to existing tiles are handled by mod-tile and never reach Tirex. So you would have to change mod_tile. You could probably change mod-tile to send low priority rendering requests for the next zoom level in addition to the high priority request for the current zoom level.</p>
<p>But I think this is a bad idea. Chances are you'll do more harm than good. A typical scenario is this: User looks at zoom level n, your setup will calculate tiles for same position at n+1. User pans over a bit and zooms in. All renderers are now blocked with rendering what was requested before and can't render what the user actually wants to look at. Tirex promotes low-priority jobs if a high-priority job for the same tile comes in and it can reserve renderers for high-priority jobs, so maybe it can actually work. But there would still be contention for CPU, database access etc. so I don't believe it would be worth it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '12, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '12, 13:25</strong> </span></p>
</div>
</div>
<div id="comments-container-17485" class="comments-container">
<span id="17486"></span>
<div id="comment-17486" class="comment">
<div id="post-17486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Concerning the scenario: When the user zooms in, I was hoping that this new high-prio renderings are rendered before the queued low-prior renderings.</p>
</div>
<div id="comment-17486-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 08:24)</span> <span class="comment-user userinfo">Alex_AddisMap</span>
</div>
</div>
<span id="17487"></span>
<div id="comment-17487" class="comment">
<div id="post-17487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, if they are only queued. But if they have already started rendering, they keep rendering till they are finished. And your scenario only makes sense if they often start rendering immediately. If they end up sitting in the queue for a long time anyway, why bother with your scheme?</p>
</div>
<div id="comment-17487-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 08:55)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="17488"></span>
<div id="comment-17488" class="comment">
<div id="post-17488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It could work, but it'd need more smarts :</p>
<ul>
<li>Only schedule if a worker is otherwise idle.</li>
<li>Ability to promote the job from low priority to high.</li>
</ul>
<p>Maybe could be implemented with a low-priority, low-TTL queue ? Remove job from the low queue if it is added in the high queue. And make sure that you have a lot of workers. Not such a low-haging-fruit improvement, but worth experimenting with.</p>
</div>
<div id="comment-17488-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 11:01)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="17494"></span>
<div id="comment-17494" class="comment">
<div id="post-17494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I updated my answer based on the comment from Vincent de Phily, because Tirex can actually do the things he requests.</p>
</div>
<div id="comment-17494-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 13:26)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-17485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17485-form-container" class="comment-form-container">
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

