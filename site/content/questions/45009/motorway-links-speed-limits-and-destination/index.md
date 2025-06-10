+++
type = "question"
title = "Motorway links, speed limits and destination"
description = '''Hello, there. I recently came on the mapping of an interchange, on which the mapping of links was to be improved, as the junctions between the main highway and the links were made far before the effective road split. The problem is the motorway links, from where they begin to be painted, have differ...'''
date = "2015-09-01T10:11:00Z"
lastmod = "2015-09-01T14:42:00Z"
weight = 45009
keywords = [ "maxspeed", "link", "destination", "lanes", "highway" ]
aliases = [ "/questions/45009" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Motorway links, speed limits and destination](/questions/45009/motorway-links-speed-limits-and-destination)

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
<span id="post-45009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I recently came on the mapping of an interchange, on which the mapping of links was to be improved, as the junctions between the main highway and the links were made far before the effective road split. The problem is the motorway links, from where they begin to be painted, have different speed limits than the main motorway far before the effective pavement split, and remapping the junctions as it would lead to lose the speed limit data of the link before the effective split. Am I correct to assume I should use <code>maxspeed:lanes</code> to map the speed limit before the junction?</p>
<p>Another question regarding dests : when, before a junction, an overhead sign tells the destination of both the main highway and the upcoming, painted-but-not-yet-splitted link, am I correct to assume that I should use <code>destination:lanes</code> before the junction, <em>and</em> <code>destination</code> on the link after the junction? Or would <code>destination:lanes</code> before junction be enough? Either way, should I map <code>destination</code> on the main motorway <em>after</em> the junction or is it useful only before junctions?</p>
<p>Hoping you can help me,</p>
<p>Regards.</p>
<p>EDIT: the speed limit question concerns mainly <a href="https://www.openstreetmap.org/edit?#map=18/48.63200/6.18320">this zone</a>: the N-S direction of A 330 is connected by two links to the lower A 33, but the junctions are made prematurely and contain speed limit data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '15, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '15, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-45009" class="comments-container">
<span id="45010"></span>
<div id="comment-45010" class="comment">
<div id="post-45010-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd suggest adding a link to the area concerned.</p>
</div>
<div id="comment-45010-info" class="comment-info">
<span class="comment-age">(01 Sep '15, 10:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45012"></span>
<div id="comment-45012" class="comment">
<div id="post-45012-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Edited accordingly.</p>
</div>
<div id="comment-45012-info" class="comment-info">
<span class="comment-age">(01 Sep '15, 13:12)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-45009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45009-form-container" class="comment-form-container">
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

<span id="45013"></span>

<div id="answer-container-45013" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45013-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think it's correct to use maxspeed:lanes and destination:lanes as you describe. AFAIK, OsmAnd only uses destination tags and not destination:lanes. I would add both. Please consider adding <a href="http://wiki.openstreetmap.org/wiki/Key:turn:lanes">turn:lanes</a> and <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/change">change:lanes</a> as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '15, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-45013" class="comments-container">
&#10;</div>
<div id="comment-tools-45013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45013-form-container" class="comment-form-container">
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

