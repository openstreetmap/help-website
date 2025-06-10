+++
type = "question"
title = "Fix Osmose &quot;Broken highway level continuity&quot; issue"
description = '''I want to fix some Osmose issues, and don&#x27;t know how to deal with this ones: http://osmose.openstreetmap.fr/en/map/#zoom=16&amp;amp;lat=-27.26658&amp;amp;lon=-65.35282&amp;amp;item=1120&amp;amp;level=1%2C2%2C3&amp;amp;tags=&amp;amp;fixable= They are corners that connect residential highways with secondary ones. The seconda...'''
date = "2020-04-03T05:47:00Z"
lastmod = "2020-04-04T21:01:00Z"
weight = 73976
keywords = [ "qa", "osmose", "issue" ]
aliases = [ "/questions/73976" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fix Osmose "Broken highway level continuity" issue](/questions/73976/fix-osmose-broken-highway-level-continuity-issue)

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
<span id="post-73976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73976-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to fix some Osmose issues, and don't know how to deal with this ones: <a href="http://osmose.openstreetmap.fr/en/map/#zoom=16&amp;lat=-27.26658&amp;lon=-65.35282&amp;item=1120&amp;level=1%2C2%2C3&amp;tags=&amp;fixable=">http://osmose.openstreetmap.fr/en/map/#zoom=16&amp;lat=-27.26658&amp;lon=-65.35282&amp;item=1120&amp;level=1%2C2%2C3&amp;tags=&amp;fixable=</a></p>
<p>They are corners that connect residential highways with secondary ones. The secondary ones are so by their use, but they do not have a great constructive difference with respect to the residential ones.</p>
<p>I am not finding the correct way to indicate that a residential highway connects directly to a secondary one. I know that the issue is marked as low, but I want to fix it if possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qa" rel="tag" title="see questions tagged &#39;qa&#39;">qa</span> <span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span> <span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '20, 05:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a1b4ab9425e43b01f9930ab25d8a503c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gabriel%20De%20Luca&#39;s gravatar image" />
<p><span>Gabriel De Luca</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gabriel De Luca has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Apr '20, 05:50</strong> </span></p>
</div>
</div>
<div id="comments-container-73976" class="comments-container">
&#10;</div>
<div id="comment-tools-73976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73976-form-container" class="comment-form-container">
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

<span id="74007"></span>

<div id="answer-container-74007" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fixed it by improving the level of some residential roads, raising them to tertiary since it is the level that corresponds to them according to their use in our local formal classification, giving continuity from secondary to tertiary and from tertiary to residential levels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '20, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a1b4ab9425e43b01f9930ab25d8a503c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gabriel%20De%20Luca&#39;s gravatar image" />
<p><span>Gabriel De Luca</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gabriel De Luca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74007" class="comments-container">
&#10;</div>
<div id="comment-tools-74007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74007-form-container" class="comment-form-container">
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

