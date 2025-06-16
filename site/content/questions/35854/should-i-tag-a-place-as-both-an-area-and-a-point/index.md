+++
type = "question"
title = "Should I tag a place as both an area and a point?"
description = '''It seems like the answer should be obvious but I guess I&#x27;m still getting my bearings on OSM. Once I come across an individual structure, should I outline that and mark it as a (e.g.) residential building and then also put a point that is the residence as well? If it&#x27;s a simple house, it seems like t...'''
date = "2014-08-15T03:25:00Z"
lastmod = "2014-08-15T08:10:00Z"
weight = 35854
keywords = [ "points", "mapping", "areas" ]
aliases = [ "/questions/35854" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Should I tag a place as both an area and a point?](/questions/35854/should-i-tag-a-place-as-both-an-area-and-a-point)

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
<span id="post-35854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35854-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems like the answer should be obvious but I guess I'm still getting my bearings on OSM. Once I come across an individual structure, should I outline that and mark it as a (e.g.) residential building and then also put a point that is the residence as well? If it's a simple house, it seems like that might be overkill but that also marks out which portions of the map are structures and which aren't. Alternately, an apartment complex may have many addresses in one structure. Or a single structure may have storefronts on the first floor and housing above them (this is common in holder buildings in my city).</p>
<p>If we <em>only</em> use points, then it won't be clear for a machine what is a building and what is not a building. If I <em>only</em> use areas, there are certain tags that don't appear available with ID in-browser editing and it would be impossible to mark some points as one address and some as another address.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '14, 03:25</strong></p>
<img src="https://secure.gravatar.com/avatar/f936a6af8335f7f14b9ea53ff536b921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin_-koavf-&#39;s gravatar image" />
<p><span>Justin_-koavf-</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin_-koavf- has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35854" class="comments-container">
&#10;</div>
<div id="comment-tools-35854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35854-form-container" class="comment-form-container">
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

<span id="35855"></span>

<div id="answer-container-35855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I try to use one feature (node or way) to describe what I see if at all possible.</p>
<p>So for single family detached houses, I tag the address information on the way (area) that shows the building outline.</p>
<p>For a building housing multiple businesses or families, I use one way (area) for the building and then nodes for the individual businesses or addresses.</p>
<p>But take care on addresses: Sometimes the building has one address for multiple tenants. If that is the case, I generally tag the address on the building and put the other information on the node tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '14, 05:25</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-35855" class="comments-container">
&#10;</div>
<div id="comment-tools-35855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35857"></span>

<div id="answer-container-35857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35857-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi consider the building as it is and tag it accordingly, with function and any characteristics you noticed, the address to the address node, because a building could be on different streets as well. Where is the border between the Streets, most of the time there is not any border. The operator just makes a building with business or garages at street level and houses or offices on top. Take a look at the different solutions used in OSM. <a href="https://www.openstreetmap.org/#map=19/51.83937/6.62174">https://www.openstreetmap.org/#map=19/51.83937/6.62174</a> DE <a href="https://www.openstreetmap.org/#map=19/51.58758/-0.22628">https://www.openstreetmap.org/#map=19/51.58758/-0.22628</a> UK <a href="https://www.openstreetmap.org/#map=19/49.50766/0.12585">https://www.openstreetmap.org/#map=19/49.50766/0.12585</a> Fr <a href="https://www.openstreetmap.org/#map=19/51.33799/3.82648">https://www.openstreetmap.org/#map=19/51.33799/3.82648</a> Nl</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '14, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-35857" class="comments-container">
&#10;</div>
<div id="comment-tools-35857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35857-form-container" class="comment-form-container">
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

