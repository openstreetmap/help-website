+++
type = "question"
title = "Highway turn restriction and relations"
description = '''Reference node ID 1349143672 I was recently using the OSMAND app to navigate and it directed me to make an illegal U-Turn. (I know it is illegal because my wife was stopped by the cops for doing it. Nothing to do with OSM.) Anyway, I thought I would look at the OSM data and try to fix this. The situ...'''
date = "2019-12-17T17:27:00Z"
lastmod = "2019-12-17T18:27:00Z"
weight = 72139
keywords = [ "turn_restrictions", "relations" ]
aliases = [ "/questions/72139" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Highway turn restriction and relations](/questions/72139/highway-turn-restriction-and-relations)

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
<span id="post-72139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Reference node ID 1349143672</p>
<p>I was recently using the OSMAND app to navigate and it directed me to make an illegal U-Turn. (I know it is illegal because my wife was stopped by the cops for doing it. Nothing to do with OSM.)</p>
<p>Anyway, I thought I would look at the OSM data and try to fix this. The situation is where a dual carrigeway ends and becomes a two way road. The restriction is that a U-Turn back to the other side of the dual carrigeway is prohibited. There is currently a no_U_Turn restriction in the OSM data but I don't think that is correct. No U Turn means one is not allowed to go back on the same path. I think the restriction should be No_Left_Turn back to the other lane of the dual carrigeway.</p>
<p>I tried to make this change in JOSM, but the validator complained that this restriction needs to be part of a relation. That is where I am stuck. I find this business of relations to be quite difficult and have gotten into serious difficulty messing with them in the past, so I thought it best to seek some guidance on this occasion.</p>
<p>Cheers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '19, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3ce1f997a6c008a7b6a34c380f5d54d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dougcb68&#39;s gravatar image" />
<p><span>dougcb68</span><br />
<span class="score" title="101 reputation points">101</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dougcb68 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72139" class="comments-container">
&#10;</div>
<div id="comment-tools-72139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72139-form-container" class="comment-form-container">
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

<span id="72141"></span>

<div id="answer-container-72141" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72141-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dougcb68 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/relation/1650531#map=17/21.54260/-105.27883">This relation looks close</a> but needs the node where you can't turn back to the other side added as a "via" node - especially in this instance where it looks like the ways join at both ends (can you do a U-turn at the other end - that would need to be a second relation with a different via node and the from and to roles swapped).</p>
<p>Edit: if the roadsign says no u turn then that is the restriction type to use. In practice no u turn or no left turn in this instance with the same from and to ways and via node should work the same for routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '19, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '19, 17:56</strong> </span></p>
</div>
</div>
<div id="comments-container-72141" class="comments-container">
<span id="72142"></span>
<div id="comment-72142" class="comment">
<div id="post-72142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good! That is what I was missing. I didn't realize the node was also needed as "via" in the relationship. This passed the validator. Thanks.</p>
</div>
<div id="comment-72142-info" class="comment-info">
<span class="comment-age">(17 Dec '19, 18:27)</span> <span class="comment-user userinfo">dougcb68</span>
</div>
</div>
</div>
<div id="comment-tools-72141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72141-form-container" class="comment-form-container">
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

