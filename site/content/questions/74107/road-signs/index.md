+++
type = "question"
title = "Road Signs"
description = '''Where do you put the road signs, mainly stop signs? Do you put them where the sign exists or next to the post on the road? For the stop sign, do you put the stop sign on the intersection even if the sign is a meter or two back?  ==========+=========== .....................| .....................!......'''
date = "2020-04-12T09:59:00Z"
lastmod = "2023-05-21T00:49:00Z"
weight = 74107
keywords = [ "stopsign", "road", "signs" ]
aliases = [ "/questions/74107" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Road Signs](/questions/74107/road-signs)

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
<span id="post-74107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74107-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Where do you put the road signs, mainly stop signs? Do you put them where the sign exists or next to the post on the road? For the stop sign, do you put the stop sign on the intersection even if the sign is a meter or two back?<br />
<br />
==========+===========<br />
.....................|<br />
.....................!.....◘<br />
.....................|<br />
.....................|<br />
.....................|<br />
KEY&gt; |-Side Road ==-Main Road ...-Nothing<br />
<br />
<br />
So, do you put it at "◘", "!," or "+," I'm sorry if the lines don't line up :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stopsign" rel="tag" title="see questions tagged &#39;stopsign&#39;">stopsign</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-signs" rel="tag" title="see questions tagged &#39;signs&#39;">signs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '20, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b5868b476e46281d48855dc281357d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timbot4x4&#39;s gravatar image" />
<p><span>Timbot4x4</span><br />
<span class="score" title="101 reputation points">101</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timbot4x4 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74107" class="comments-container">
&#10;</div>
<div id="comment-tools-74107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74107-form-container" class="comment-form-container">
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

<span id="74113"></span>

<div id="answer-container-74113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74113-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't usually map stop (or giveway) signs by themselves as signs by the side of the road. I guess that would be the good thing to do for completeness. But it adds no functionality: Routers and navigation apps will not find or process them and no renderer I know of will display them. Though I suppose some renderer somewhere might or might in the future.</p>
<p>What I do map is the effect of the sign on the road. I'll put a node on the way at the point where the driver is to stop or yield and tag it with both <code>highway=stop|giveway</code> and <code>direction=forward|backward</code>.</p>
<p>The reason for this is, in my opinion, the primary reason for mapping stop and giveway signs is for routing and driving directions.</p>
<p>Routers and navigation apps will not find or process signs that are place beside the road in OSM. They will, or at least should, find and process nodes with <code>highway=stop|giveway|traffic_signals</code> tagging on the ways. They can then use this information to better pick a route and/or give directions to a driver.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '20, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74113" class="comments-container">
<span id="87284"></span>
<div id="comment-87284" class="comment">
<div id="post-87284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd add that I find it acceptable to map 4-way stop signs at the intersection point itself (with <code>direction=both</code>) rather than putting four separate stop signs at each incoming way. Edit: I also see some areas that have the sign mapped on the side of the road in addition to the point on the way. This, however, violates the 'one feature, one element' principle.</p>
</div>
<div id="comment-87284-info" class="comment-info">
<span class="comment-age">(21 May '23, 00:49)</span> <span class="comment-user userinfo">ybungalobill</span>
</div>
</div>
</div>
<div id="comment-tools-74113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74113-form-container" class="comment-form-container">
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

