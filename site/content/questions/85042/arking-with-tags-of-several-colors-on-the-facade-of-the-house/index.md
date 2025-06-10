+++
type = "question"
title = "Мarking with tags of several colors on the facade of the house"
description = '''Hi! I am trying to find a way to specify several colors on the facade of houses, but I do not know how to do it. There are cases when the main color of the house, for example, is white, but the brightest, for example, is yellow. In this case, I would like to be able to add two tags to the building -...'''
date = "2022-07-12T13:44:00Z"
lastmod = "2022-07-13T10:12:00Z"
weight = 85042
keywords = [ "building", "buildings", "colour" ]
aliases = [ "/questions/85042" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Мarking with tags of several colors on the facade of the house](/questions/85042/arking-with-tags-of-several-colors-on-the-facade-of-the-house)

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
<span id="post-85042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am trying to find a way to specify <strong>several colors on the facade of houses</strong>, but I do not know how to do it. There are cases when the main color of the house, for example, is white, but the brightest, for example, is yellow. In this case, I would like to be able to add two tags to the building - the predominant color of the facade (in my example, white) and the characteristic color of the facade (in the example, yellow). Help (:</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-colour" rel="tag" title="see questions tagged &#39;colour&#39;">colour</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '22, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/605d3e34a079dc4fd2c75629afaf6a58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1ghtmare&#39;s gravatar image" />
<p><span>1ghtmare</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1ghtmare has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85042" class="comments-container">
<span id="85049"></span>
<div id="comment-85049" class="comment">
<div id="post-85049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For comparison, <code>type=destination_sign</code> uses <code>colour:back=</code> for the sign's background color.</p>
</div>
<div id="comment-85049-info" class="comment-info">
<span class="comment-age">(13 Jul '22, 10:12)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-85042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85042-form-container" class="comment-form-container">
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

<span id="85045"></span>

<div id="answer-container-85045" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85045-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the colours of the building are painted in rectangular shapes, you could use <a href="https://wiki.openstreetmap.org/wiki/Key:building:part">building:part</a> to split up the building into multiple parts and assign a colour to each one. If this is not the case, you can only use multiple values for the tag, so in your example <code>building:colour=white;yellow</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '22, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ec46821d791b304a5c3c9380ab661d11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discostu36&#39;s gravatar image" />
<p><span>Discostu36</span><br />
<span class="score" title="236 reputation points">236</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discostu36 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '22, 08:06</strong> </span></p>
</div>
</div>
<div id="comments-container-85045" class="comments-container">
<span id="85048"></span>
<div id="comment-85048" class="comment">
<div id="post-85048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, the brightest color should be implied by it having yellow. Although, this doesn't explicitly show white is predominant, only that it is some majority, can even be equal.</p>
</div>
<div id="comment-85048-info" class="comment-info">
<span class="comment-age">(13 Jul '22, 10:06)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-85045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85045-form-container" class="comment-form-container">
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

