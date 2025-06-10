+++
type = "question"
title = "tagging of surface."
description = '''Hello. I&#x27;m new on openstreetmap, so I&#x27;m not sure about how to answer certain quest given by StreetComplete. For example, in this instance (in the middle of https://www.openstreetmap.org/way/636409055), there is only one way for the stairs, and one way for the footway. Should I tag the footway with s...'''
date = "2020-06-05T18:55:00Z"
lastmod = "2020-06-05T21:15:00Z"
weight = 75153
keywords = [ "surface" ]
aliases = [ "/questions/75153" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tagging of surface.](/questions/75153/tagging-of-surface)

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
<span id="post-75153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75153-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I'm new on openstreetmap, so I'm not sure about how to answer certain quest given by StreetComplete.</p>
<p>For example, in this instance (in the middle of <a href="https://www.openstreetmap.org/way/636409055">https://www.openstreetmap.org/way/636409055</a>), there is only one way for the stairs, and one way for the footway. Should I tag the footway with surface=concrete and stop there, or should I split the footway and the stairs in order to be more precise ? <img src="https://help.openstreetmap.org/upfiles/croisement.jpeg" alt="alt text" /></p>
<p>In another case, there is a space between two part of the stairs. Should I tag surface=asphalt, or once again break in different part to tag more accurately ? <img src="https://help.openstreetmap.org/upfiles/stairs.jpeg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '20, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/72b40fd3b80d7f68272943ede468c85a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miggaz%20elquez&#39;s gravatar image" />
<p><span>miggaz elquez</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miggaz elquez has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-75153" class="comments-container">
&#10;</div>
<div id="comment-tools-75153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75153-form-container" class="comment-form-container">
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

<span id="75156"></span>

<div id="answer-container-75156" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75156-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-75156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="miggaz elquez has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This decision is very much a personal one at this stage, and to a certain extent will depend if you have particular use-cases which might benefit from the more detailed mapping.</p>
<p>Most people choose your first option, ignoring small sections of paths with variant surfaces. In general people do not do this because to do it consistently would limit mapping things which might be considered more important.</p>
<p>Areas where such information might be more immediately useful will typically be places such as university campuses where additional information for people with limited mobility or sight might benefit.</p>
<p>There is no harm in trying this out in a limited area to gain experience, and perhaps have concrete examples to show to others. I presume we will be seeing a lot of micromapping (as it is termed) as mappers constrained by where they can travel add information in their local patch.</p>
<p>Looking at the pictures and thinking about the things I find important, I would want to add the following information:</p>
<ul>
<li>step_count: Number of steps (it can be useful to split the steps into 2 flights, just as you might for the surface).</li>
<li>handrail: Absence of handrail. This can make even short flights of steps harder for some people.</li>
<li>tactile_paving: Absence of tactile paving. Navigating this area may be harder for a blind person because this is lacking. However the change of surface may be anticipated to provide the same effect.</li>
<li>lit=yes: the stairs are lit (at least I assume I see lamp posts in the images)</li>
</ul>
<p>As you can see once one starts considering the detail they may be even more. Only you can make the judgement as to what is appropriate right now. Ultimately these details will eventually appear in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '20, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-75156" class="comments-container">
<span id="75157"></span>
<div id="comment-75157" class="comment">
<div id="post-75157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this help me a lot !</p>
</div>
<div id="comment-75157-info" class="comment-info">
<span class="comment-age">(05 Jun '20, 21:15)</span> <span class="comment-user userinfo">miggaz elquez</span>
</div>
</div>
</div>
<div id="comment-tools-75156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75156-form-container" class="comment-form-container">
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

