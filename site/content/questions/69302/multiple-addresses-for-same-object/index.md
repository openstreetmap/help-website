+++
type = "question"
title = "Multiple addresses for same object"
description = '''How do I assign multiple addresses to same object (e.g. a building)?'''
date = "2019-05-25T20:30:00Z"
lastmod = "2019-05-26T03:52:00Z"
weight = 69302
keywords = [ "address" ]
aliases = [ "/questions/69302" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Multiple addresses for same object](/questions/69302/multiple-addresses-for-same-object)

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
<span id="post-69302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69302-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I assign multiple addresses to same object (e.g. a building)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '19, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e93bc6a14fd87851cd36f33d15677d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ateny&#39;s gravatar image" />
<p><span>ateny</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ateny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '19, 20:30</strong> </span></p>
</div>
</div>
<div id="comments-container-69302" class="comments-container">
&#10;</div>
<div id="comment-tools-69302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69302-form-container" class="comment-form-container">
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

<span id="69310"></span>

<div id="answer-container-69310" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69310-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ateny has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simplest way: Don't add any <code>addr:*</code> tags to the building itself. Instead, create nodes inside the building perimeter (preferably near the entrances that corresponds to each address) and add the <code>addr:*</code> tags to those nodes. The addresses can be entirely different -- different housenumber, different street.</p>
<p>More complicated: Similar, but instead of address nodes inside the building's perimeter, put entrance nodes directly <em>on</em> the building's perimeter. Tag these with the <code>addr:*</code> info plus add <code>entrance=main</code> or <code>entrance=yes</code>. Possible difficulty -- you might not consider every address to be a true "entrance" to the building. (If it's just the address of a shop on the ground floor of a large building, should that be considered an entrance to the building? Opinions differ on this.)</p>
<p>There are other approaches too, depending on the circumstances. If you show the exact situation I can tell you what <em>I</em> would do ... but ultimately it depends on local consensus. Examine nearby areas that are well mapped, and see how similar situations have been handled. Don't be shy about contacting the local mappers who dealt with these same problems in the past -- sometimes they're long gone, but often they're happy to advise &amp; help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '19, 03:15</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-69310" class="comments-container">
&#10;</div>
<div id="comment-tools-69310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69310-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69303"></span>

<div id="answer-container-69303" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There’s an article in the wiki on this topic: <a href="https://wiki.openstreetmap.org/wiki/Addresses">https://wiki.openstreetmap.org/wiki/Addresses</a> Scroll down to the headline “Buildings with multiple house numbers” According to this there is currently no global consensus on this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '19, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/daf22b4dd344ab47d2f026759821a535?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mofte105&#39;s gravatar image" />
<p><span>Mofte105</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mofte105 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69303" class="comments-container">
<span id="69309"></span>
<div id="comment-69309" class="comment">
<div id="post-69309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I had read that section and I thought it talked only about house numbers, which I assumed was about different numbers for same address. The scenario I am proposing is when addresses are different. I was not able to use tags e.g. addr:street multiple times, and there are no alternate address tags such as there are for names, e.g. alt:street:alt_name.</p>
</div>
<div id="comment-69309-info" class="comment-info">
<span class="comment-age">(25 May '19, 23:46)</span> <span class="comment-user userinfo">ateny</span>
</div>
</div>
<span id="69312"></span>
<div id="comment-69312" class="comment">
<div id="post-69312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah well, multiple house numbers was the scenario I was thinking of, sorry. Without knowing any further detail I‘d go with umsonst‘s first proposal.</p>
</div>
<div id="comment-69312-info" class="comment-info">
<span class="comment-age">(26 May '19, 03:52)</span> <span class="comment-user userinfo">Mofte105</span>
</div>
</div>
</div>
<div id="comment-tools-69303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69303-form-container" class="comment-form-container">
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

