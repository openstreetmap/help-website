+++
type = "question"
title = "How to tag Mountain Bike Single Track"
description = '''I&#x27;ve been using highway=path, bicycle=yes. If a dedicated MTB track, then also foot=no. But I&#x27;ve also seen highway=cycleway, cycleway=track, bicycle=yes used. I know that cycleway=track, bicycle=yes is redundant, but I can see that highway=cycleway is more explicit to dentote that it is mainly or ex...'''
date = "2011-01-04T14:19:00Z"
lastmod = "2011-10-11T00:46:00Z"
weight = 2020
keywords = [ "mtb", "singletrack" ]
aliases = [ "/questions/2020" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag Mountain Bike Single Track](/questions/2020/how-to-tag-mountain-bike-single-track)

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
<span id="post-2020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2020-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been using highway=path, bicycle=yes. If a dedicated MTB track, then also foot=no.</p>
<p>But I've also seen highway=cycleway, cycleway=track, bicycle=yes used. I know that cycleway=track, bicycle=yes is redundant, but I can see that highway=cycleway is more explicit to dentote that it is mainly or exclusively for bicycles. However cycleway to me evokes a paved track in an urban setting. Perhaps highway=cycleway, surface=unpaved.</p>
<p>I haven't been able to find a definitive ruling on the Wiki which is a bit odd as there is a lot of MTB single track out there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mtb" rel="tag" title="see questions tagged &#39;mtb&#39;">mtb</span> <span class="post-tag tag-link-singletrack" rel="tag" title="see questions tagged &#39;singletrack&#39;">singletrack</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '11, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d495461cf85d79a58788d70d776a0256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewfr&#39;s gravatar image" />
<p><span>andrewfr</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewfr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2020" class="comments-container">
&#10;</div>
<div id="comment-tools-2020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2020-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="2023"></span>

<div id="answer-container-2023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2023-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no "definitive ruling", and there's unlikely to ever be. Also, don't try to infer any meaning from the words "path" or "cycleway" outside the context of OpenStreetMap - there's nothing inherently paved or urban about either of them.</p>
<p>There are two options for mapping paths:</p>
<ol>
<li>Use highway=path and other tags to say what is permitted</li>
<li>Use highway=footway or highway=cycleway or highway=bridleway or ... as appropriate</li>
</ol>
<p>Neither approach is particularly right or wrong, but the existence of two alternatives is just something we need to live with. Don't worry about it too much.</p>
<p>P.S. You said "I know that cycleway=track, bicycle=yes is redundant", but you're misunderstanding something somewhere. The two tags describe separate things:</p>
<ul>
<li>cycleway=track means that a road (e.g. highway=secondary) has a cycle track running parallel and separated by a kerb. Don't use cycleway=track on highway=cycleway or highway=path.</li>
<li>bicycle=yes means you are legally permitted to ride your bike on the feature (e.g. highway=secondary)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-2023" class="comments-container">
&#10;</div>
<div id="comment-tools-2023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2023-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2028"></span>

<div id="answer-container-2028" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2028-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also use the tags for <a href="http://wiki.openstreetmap.org/wiki/Key:mtb:scale">mtb:scale</a> to specify the difficulty of mountain bike trails. That should make it clear that its not just a paved urban cycleway, and it may have a poor surface or obstacles etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2028" class="comments-container">
&#10;</div>
<div id="comment-tools-2028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2028-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8391"></span>

<div id="answer-container-8391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm starting to think we may need to be bold enough to actually propose something different. Singletrack is singletrack, and is not just (always) just a footpath that happens to be mountain bikeable. A track that is purpose built for mountain biking should, in my very humble opinion, have a real tag like highway=mtb.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '11, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/75f5707160697b2164444fc3f5054084?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stevage&#39;s gravatar image" />
<p><span>Stevage</span><br />
<span class="score" title="254 reputation points">254</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stevage has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8391" class="comments-container">
&#10;</div>
<div id="comment-tools-8391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8391-form-container" class="comment-form-container">
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

