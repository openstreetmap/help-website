+++
type = "question"
title = "Temporary HGV destination road signs"
description = '''Hello, While editing the road network in OSM we have encountered a situation, which we are not sure how to tag. Temporary HGV destination road signs. Roads are being repaired and some of the town couincils refuse the HGV traffic to pass through their towns for the duration of the repairs.  We have f...'''
date = "2014-06-12T08:51:00Z"
lastmod = "2014-06-12T12:49:00Z"
weight = 33901
keywords = [ "hgv", "roads" ]
aliases = [ "/questions/33901" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Temporary HGV destination road signs](/questions/33901/temporary-hgv-destination-road-signs)

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
<span id="post-33901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, While editing the road network in OSM we have encountered a situation, which we are not sure how to tag.</p>
<p>Temporary HGV destination road signs.</p>
<p>Roads are being repaired and some of the town couincils refuse the HGV traffic to pass through their towns for the duration of the repairs.</p>
<p>We have found two ways to do it and we would like some guidance on which one to choose:</p>
<p>The goal of the tag is to express that only HGV who are supplying the road can enter and that it will in effect from date x to date y.</p>
<p>Option 1</p>
<pre><code>Temporary:hgv=destination
Temporary:date_on=20-10-2014
Temporary:date_off=28-11-2014</code></pre>
<p>Option 2</p>
<pre><code>hgv:conditional=destination @ (20.10.2014-28.11.2014)</code></pre>
<p>Which one is better to use? Thank you for all yout answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hgv" rel="tag" title="see questions tagged &#39;hgv&#39;">hgv</span> <span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/bbe97c3fa23d557d5cdaec1fef8e28db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomas%20Pajonk&#39;s gravatar image" />
<p><span>Tomas Pajonk</span><br />
<span class="score" title="191 reputation points">191</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomas Pajonk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33901" class="comments-container">
&#10;</div>
<div id="comment-tools-33901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33901-form-container" class="comment-form-container">
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

<span id="33911"></span>

<div id="answer-container-33911" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33911-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tomas Pajonk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should prefer using <a href="https://wiki.openstreetmap.org/wiki/Conditional_restriction">conditional access restrictions</a> instead of the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/temporary">temporary proposal</a>. It is more widely in use and more flexible.</p>
<p>However your date doesn't follow the specification. The time &amp; date in the <a href="https://wiki.openstreetmap.org/wiki/Conditional_restriction#Condition">condition</a> field should follow the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours:specification">specification</a> of the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> key which in turn is based on the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Time_domains">time domains</a> proposal. So if I'm not mistaken it has to be</p>
<pre><code>hgv:conditional=destination @ (2014 Oct 20-2014 Nov 28)</code></pre>
<p>But don't expect any software to handle this correctly at the moment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '14, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33911" class="comments-container">
<span id="33916"></span>
<div id="comment-33916" class="comment">
<div id="post-33916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-33916-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 12:49)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
</div>
<div id="comment-tools-33911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33911-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33902"></span>

<div id="answer-container-33902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33902-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-33902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Tomas, there have been questions like yours before, please read the links. And search with temporary for more. <a href="/questions/259/what-is-the-recommended-way-to-tag-temporary-road-works-and-traffic-situations">https://help.openstreetmap.org/questions/259/what-is-the-recommended-way-to-tag-temporary-road-works-and-traffic-situations</a> <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/temporary">https://wiki.openstreetmap.org/wiki/Proposed_features/temporary</a> And yes it’s possible to add the time of the construction, but it won’t disappear from OSM out of its self. You’ll have to remember as owner of the action to remove it afterwards. I would go for just one line option 1 ; hgv=no, temporary:period=3-4-2014 - 12-8-2014</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '14, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '14, 09:42</strong> </span></p>
</div>
</div>
<div id="comments-container-33902" class="comments-container">
<span id="33903"></span>
<div id="comment-33903" class="comment">
<div id="post-33903-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your <em>temporary</em> syntax is completely wrong, please re-read the proposal. The correct tags would be <em>temporary:hgv=destination</em>, <em>temporary:date_on=2014-10-20</em>, <em>temporary:date_off=2014-11-28</em>. But the <em>temporary</em> proposal is a bad idea anyway because it doesn't support multiple overlapping conditions. <a href="https://wiki.openstreetmap.org/wiki/Conditional_restriction">Conditional access restrictions</a> are more flexible.</p>
</div>
<div id="comment-33903-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 10:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33905"></span>
<div id="comment-33905" class="comment">
<div id="post-33905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is not HGV no. HGV can go there if it has a purpose. Ie. construction on the road closes the road, but vehicles cannot go through nearby village and completely ruin its one lane road (though if the vehicles must go to the village, they are allowed to enter)</p>
</div>
<div id="comment-33905-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 10:18)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="33906"></span>
<div id="comment-33906" class="comment">
<div id="post-33906-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the link.</p>
</div>
<div id="comment-33906-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 10:18)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="33909"></span>
<div id="comment-33909" class="comment">
<div id="post-33909-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh you are right, I changed it to <em>hgv=destination</em> :).</p>
</div>
<div id="comment-33909-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 10:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33902-form-container" class="comment-form-container">
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

