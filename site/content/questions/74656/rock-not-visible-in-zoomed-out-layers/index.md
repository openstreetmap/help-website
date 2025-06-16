+++
type = "question"
title = "Rock not visible in zoomed out layers"
description = '''Hi, Rock is not visible fis zoomed out layers https://www.openstreetmap.org/node/5744002460 It&#x27;s nice plase with postglacial rocks and bigges one is in the center. Is is possible to make it more visible? Telling the truth i found it only by google map thanks to my friend. in Osmand app when i was in...'''
date = "2020-05-07T20:57:00Z"
lastmod = "2020-05-07T21:38:00Z"
weight = 74656
keywords = [ "stones" ]
aliases = [ "/questions/74656" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rock not visible in zoomed out layers](/questions/74656/rock-not-visible-in-zoomed-out-layers)

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
<span id="post-74656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74656-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Rock is not visible fis zoomed out layers <a href="https://www.openstreetmap.org/node/5744002460">https://www.openstreetmap.org/node/5744002460</a></p>
<p>It's nice plase with postglacial rocks and bigges one is in the center. Is is possible to make it more visible? Telling the truth i found it only by google map thanks to my friend. in Osmand app when i was in the forest it was not possible to find it. Maybe stone/rock shall be marked with other tag to make it more visible? Thanks</p>
<p>My own pic<span>link text</span></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stones" rel="tag" title="see questions tagged &#39;stones&#39;">stones</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '20, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/474daa10f74e86ba7084e8a112b4c8b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbvndonh&#39;s gravatar image" />
<p><span>rbvndonh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbvndonh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74656" class="comments-container">
<span id="74657"></span>
<div id="comment-74657" class="comment">
<div id="post-74657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Small forest table is visible when you zoom in and zoom out <a href="https://www.openstreetmap.org/search?whereami=1&amp;query=52.15821%2C15.68062#map=19/52.15821/15.68062">https://www.openstreetmap.org/search?whereami=1&amp;query=52.15821%2C15.68062#map=19/52.15821/15.68062</a></p>
<p>but giant stone not..</p>
</div>
<div id="comment-74657-info" class="comment-info">
<span class="comment-age">(07 May '20, 21:04)</span> <span class="comment-user userinfo">rbvndonh</span>
</div>
</div>
</div>
<div id="comment-tools-74656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74656-form-container" class="comment-form-container">
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

<span id="74658"></span>

<div id="answer-container-74658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74658-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The rock is tagged as natural=stone. This is not currently rendered in the standard OpenStreetMap layer. There is an open issue to address this: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3628">https://github.com/gravitystorm/openstreetmap-carto/issues/3628</a> . I don't think there is anything you can do to change this, the tagging as it stands appears correct.</p>
<p>Note that each renderer is independent, so even if this does eventually get rendered in the standard layer, that doesn't mean it will appear in other layers or in apps such as Osmand. If you wish to see natural=stone in Osmand you'd need to raise it with the developer of that app.</p>
<p>There are two things mapped at the other location you point to: a building mapped as an area (shown as a greyish rectangle in the standard layer), and a shelter mapped as a node (which has a specific icon in the standard layer). It's hard to make out what is actually there from the imagery - if it is actually only a small table as you say, then maybe the tagging is wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '20, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 May '20, 21:39</strong> </span></p>
</div>
</div>
<div id="comments-container-74658" class="comments-container">
&#10;</div>
<div id="comment-tools-74658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74658-form-container" class="comment-form-container">
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

