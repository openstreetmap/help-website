+++
type = "question"
title = "Orphan Nodes and Ways"
description = '''Hello, all. I recently downloaded and audited an OSM data file for an area of Northern California. In it I found 44 orphan nodes and 25 orphan ways (untagged nodes not part of any way or relation, untagged ways not part of any relation). What is the best way to help clear these from the OSM database...'''
date = "2016-06-14T23:59:00Z"
lastmod = "2016-06-15T06:34:00Z"
weight = 50206
keywords = [ "errors", "orphan-nodes" ]
aliases = [ "/questions/50206" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Orphan Nodes and Ways](/questions/50206/orphan-nodes-and-ways)

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
<span id="post-50206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50206-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, all. I recently downloaded and audited an OSM data file for an area of Northern California. In it I found 44 orphan nodes and 25 orphan ways (untagged nodes not part of any way or relation, untagged ways not part of any relation). What is the best way to help clear these from the OSM database? Thanks. Roke Whitson</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-orphan-nodes" rel="tag" title="see questions tagged &#39;orphan-nodes&#39;">orphan-nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '16, 23:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5287d5caf8fe235df3006923c87f88b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RokeW&#39;s gravatar image" />
<p><span>RokeW</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RokeW has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50206" class="comments-container">
&#10;</div>
<div id="comment-tools-50206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50206-form-container" class="comment-form-container">
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

<span id="50209"></span>

<div id="answer-container-50209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50209-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-50209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should try to understand the history of the objects (<a href="https://wiki.openstreetmap.org/wiki/Quality_assurance">see</a> object history, whodidit, OSMHV, attic, …). Were these objects not orphaned when they were created? Were they created as orphans? Was it just a single orphan object in a big changeset or were there many? Are the objects arranged in some special shape? Are there gps traces? Any recognizable from our aerial imagery?</p>
<p>Sometimes</p>
<ul>
<li>you can find newbies needing help,</li>
<li>just the tags are missing and the creating user forgot to add them (mail the user),</li>
<li>you can find other problems in the related changeset,</li>
<li>(in year 2012, but maybe still today) that could be a surviving left-over from the <a href="/questions/15482/orphan-nodes-by-redaction-bot">redaction bot</a> (license change) which may be an indicator that there is some feature missing (could be seen in aerial imagery sometimes).</li>
</ul>
<p>At the end you may</p>
<ul>
<li>contact the creator/modifying user (see escada's answer) and</li>
<li>add relevant tags, delete the object or leave a fixme tag with some already collected info for fellow mappers who might know the location better than you.</li>
</ul>
<p>It would not be beneficial to just delete these objects. That could remove a valuable hint for other mappers that there is something (of importance) missing.</p>
<p>If you are still quite new to OSM then this might not be the right task to start with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '16, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jun '16, 06:39</strong> </span></p>
</div>
</div>
<div id="comments-container-50209" class="comments-container">
&#10;</div>
<div id="comment-tools-50209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50208"></span>

<div id="answer-container-50208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50208-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Contact the mapper that created them via a changeset comment or private message in (of course) a friendly way. Wait a couple of days to give them the time to react. This way you give them the possibility to learn. In case they do not react, or when you see they have not been contributing in a long time, you can remove them yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '16, 04:25</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-50208" class="comments-container">
&#10;</div>
<div id="comment-tools-50208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50208-form-container" class="comment-form-container">
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

