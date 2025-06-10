+++
type = "question"
title = "Illegal turns: okay to map as crossing ways, or are turn restrictions necessary?"
description = '''Say two ways cross at an intersection, but it isn&#x27;t legal to turn from one into the other. (E.g. a footway crossing a cycleway, or a separated bus lane crossing another road.) Is it okay to map such intersections as crossing ways which don&#x27;t share a node, or is it better practice to add the crossing...'''
date = "2015-07-10T14:46:00Z"
lastmod = "2015-07-13T10:36:00Z"
weight = 44117
keywords = [ "crossing", "ways", "intersections", "turn_restrictions" ]
aliases = [ "/questions/44117" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Illegal turns: okay to map as crossing ways, or are turn restrictions necessary?](/questions/44117/illegal-turns-okay-to-map-as-crossing-ways-or-are-turn-restrictions-necessary)

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
<span id="post-44117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44117-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Say two ways cross at an intersection, but it isn't legal to turn from one into the other. (E.g. a footway crossing a cycleway, or a separated bus lane crossing another road.) Is it okay to map such intersections as crossing ways which don't share a node, or is it better practice to add the crossing node, and then add turn restrictions denoting that no turns can be made? The former seems much simpler, but unfortunately triggers false positives from quality assurance tools.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '15, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-44117" class="comments-container">
&#10;</div>
<div id="comment-tools-44117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44117-form-container" class="comment-form-container">
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

<span id="44118"></span>

<div id="answer-container-44118" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44118-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-44118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Paul_012 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>They should share a common node where they share a physical patch of asphalt (i.e. there's no bridges or tunnels).</p>
<p>For restricted use paths and roads, many turn restrictions are unnecessary. So in your example, if you have a path with bicycle=no, and a cycleway with foot=no, there's no need to add turn restrictions since the pedestrians aren't allowed on the cycleway and the bikes aren't allowed on the path.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '15, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-44118" class="comments-container">
&#10;</div>
<div id="comment-tools-44118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44118-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44146"></span>

<div id="answer-container-44146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44146-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Skipping the common node at the intersection will also prevent pedestrians from going from one road to the other. Moreover, various turn restrictions don't apply to emergency vehicles. Therefore you should always add a turn restriction instead of skipping the common node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '15, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44146" class="comments-container">
&#10;</div>
<div id="comment-tools-44146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44146-form-container" class="comment-form-container">
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

