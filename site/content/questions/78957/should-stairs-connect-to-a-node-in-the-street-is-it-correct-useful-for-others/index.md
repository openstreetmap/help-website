+++
type = "question"
title = "Should stairs connect to a node in the street? Is it correct (=useful for others)?"
description = '''Hi, a newbie here. I was just &quot;randomly&quot; reviewing the map. But when I started seeing how it was made I started wondering: is it correct? Should I fix it or would I make a damage, on the long run? Here&#x27;s the situation: in my zone mapper have just put lines that share some nodes when it came to mappi...'''
date = "2021-02-20T15:59:00Z"
lastmod = "2021-02-21T07:37:00Z"
weight = 78957
keywords = [ "streets", "stairs", "shared_nodes" ]
aliases = [ "/questions/78957" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should stairs connect to a node in the street? Is it correct (=useful for others)?](/questions/78957/should-stairs-connect-to-a-node-in-the-street-is-it-correct-useful-for-others)

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
<span id="post-78957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78957-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, a newbie here. I was just "randomly" reviewing the map. But when I started seeing how it was made I started wondering: is it correct? Should I fix it or would I make a damage, on the long run? Here's the situation: in my zone mapper have just put lines that share some nodes when it came to mapping streets and stairs (there are a lot of stairs that flow into roads); they simply put a node in common between the street and the stairs. But, as obvious, this is a bit controversial and causes the real length of the stairs to not coincide with the satellite images and of course also reality of how things are put. I don't know much about online maps and how they are used to solve problems, but should I fix it? Is it worth it or am I just doing more damage than other?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-stairs" rel="tag" title="see questions tagged &#39;stairs&#39;">stairs</span> <span class="post-tag tag-link-shared_nodes" rel="tag" title="see questions tagged &#39;shared_nodes&#39;">shared_nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '21, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/06f5ee308b6d5fdf14a134086dc0fdaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonatoieri&#39;s gravatar image" />
<p><span>jonatoieri</span><br />
<span class="score" title="131 reputation points">131</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonatoieri has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78957" class="comments-container">
&#10;</div>
<div id="comment-tools-78957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78957-form-container" class="comment-form-container">
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

<span id="78959"></span>

<div id="answer-container-78959" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78959-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jonatoieri has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the stairs flow into the streets it is correct that they share a node. This is not specific to steps - it applies to all kinds of "highway" objects in OpenStreetMap. They all represent lines that people or vehicles can travel along. If they didn't connect, routing engines would not be able to calculate routes, and it would be hard for map viewers to work out how to travel from A to B. For many purposes knowing the connectivity of streets is more important than their exact physical dimensions. I was not aware this was controversial.</p>
<p>That said, some mappers do try to also reflect the physical size of streets. You have discovered the width tag, and some mappers use the area:highway tag. But these are in addition to the "connectivity" concept, they do not replace it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '21, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78959" class="comments-container">
<span id="78958"></span>
<div id="comment-78958" class="comment">
<div id="post-78958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay maybe if I just add the width to the intended streets it's easier and much faster to modify. Just realised.</p>
</div>
<div id="comment-78958-info" class="comment-info">
<span class="comment-age">(20 Feb '21, 17:36)</span> <span class="comment-user userinfo">jonatoieri</span>
</div>
</div>
<span id="78962"></span>
<div id="comment-78962" class="comment">
<div id="post-78962-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok thanks, I'll fix my mistakes. Anyway, no I didn't mean controversial in that sense, it was meant in my own sense. (I'm still learning some English words, sorry)</p>
</div>
<div id="comment-78962-info" class="comment-info">
<span class="comment-age">(20 Feb '21, 23:42)</span> <span class="comment-user userinfo">jonatoieri</span>
</div>
</div>
<span id="78963"></span>
<div id="comment-78963" class="comment">
<div id="post-78963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's usually recommended that <code>bridge=yes</code> is to be split to reflect the actual structure only, instead of connecting to roads on both sides directly. So I can understand why this question appears.</p>
</div>
<div id="comment-78963-info" class="comment-info">
<span class="comment-age">(21 Feb '21, 07:37)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-78959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78959-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78960"></span>

<div id="answer-container-78960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78960-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-78960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Changing a highway=steps so that this tag is only present on the actual part covered by stairs can be generally regarded as an example of stepwise refinement of the mapping.</p>
<p>The key information is that this route contains steps &amp; is therefore not accessible to wheelchair users &amp; others with limited mobility. It's usually a simple thing to split the way and retag the non-stair parts as highway=footway. (Even then you will have something marked as a footway crossing from the centre line of the road, but this is absolutely necessary to provide a networked model for routing).</p>
<p>There are plenty of other things which can then be added to the step section: count of number of steps (step_count), presence of handrails (handrail), surface etc). At the extreme end one might map each separate flight of stairs as a distinct way with each landing as a footway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '21, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78960" class="comments-container">
&#10;</div>
<div id="comment-tools-78960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78960-form-container" class="comment-form-container">
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

