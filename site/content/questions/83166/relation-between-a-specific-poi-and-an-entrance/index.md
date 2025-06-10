+++
type = "question"
title = "Relation between a specific POI and an entrance?"
description = '''Hello, is there a specific relation for entrance=* and a POI in form of area or point? For example, there is a case of a building (area) of a swimming pool. There is a gym from the back and a cinema above the swimming pool with an entrance from one corner. Is there any way how to bind a specific ent...'''
date = "2022-01-23T16:48:00Z"
lastmod = "2022-01-25T12:26:00Z"
weight = 83166
keywords = [ "provides_feature", "entrance", "associated_entrance", "relations", "poi" ]
aliases = [ "/questions/83166" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Relation between a specific POI and an entrance?](/questions/83166/relation-between-a-specific-poi-and-an-entrance)

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
<span id="post-83166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83166-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, is there a specific relation for <code>entrance=*</code> and a POI in form of area or point? For example, there is a case of a building (area) of a swimming pool. There is a gym from the back and a cinema above the swimming pool with an entrance from one corner. Is there any way how to bind a specific entrance to a specific POI, or is it always done only the way that the main entrance is for the building itself, and other POIs (points) have to be located somewhere at their entry point, no matter if they are physically located (through the corridors) elsewhere in the building?</p>
<p>I found these two relation proposals <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Associated_Entrance">type=associated<strong>_</strong>_entrance</a> and <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Provides_feature">type=provides<strong><em>_</em></strong>_feature</a>, but neither seems to be approved.</p>
<p>I hope my question is a bit clear...</p>
<p>Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-provides_feature" rel="tag" title="see questions tagged &#39;provides_feature&#39;">provides_feature</span> <span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span> <span class="post-tag tag-link-associated_entrance" rel="tag" title="see questions tagged &#39;associated_entrance&#39;">associated_entrance</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '22, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/4660eafc9d705be1c65dd6f06577b999?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KingCZE&#39;s gravatar image" />
<p><span>KingCZE</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KingCZE has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83166" class="comments-container">
&#10;</div>
<div id="comment-tools-83166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83166-form-container" class="comment-form-container">
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

<span id="83187"></span>

<div id="answer-container-83187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83187-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Very thoroughly researched! I was aware of the proposed associated_entrance relation (and I've used it myself) but not of the proposed provides_feature relation, which, it appears, is a bit more popular.</p>
<p>I would have suggested associated_entrance, but knowing now that there are two competing proposals -- and best I know, neither has gained enough traction to be implemented in end-user software -- it's hard to know which relation to pick. Certainly doing both seems wrong.</p>
<p>In the situation you describe, I'd be satisfied (for now) with adding the POI nodes near the most useful entrance for each POI, rather than locating them near their interior coordinates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '22, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-83187" class="comments-container">
&#10;</div>
<div id="comment-tools-83187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83187-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83189"></span>

<div id="answer-container-83189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>type=site</code> is less unpopular so to speak. It is used when areas can't describe the feature fully. Although, <code>type=provides_feature</code> author disagree <a href="https://wiki.openstreetmap.org/wiki/Talk:Relations/Proposed/Provides_feature">https://wiki.openstreetmap.org/wiki/Talk:Relations/Proposed/Provides_feature</a> without elaboration a decade ago, this has already been used in <code>site=parking</code> widely, with exactly the same usage to relate the <code>=parking_entrance</code> to the <code>=parking</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '22, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83189" class="comments-container">
&#10;</div>
<div id="comment-tools-83189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83189-form-container" class="comment-form-container">
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

