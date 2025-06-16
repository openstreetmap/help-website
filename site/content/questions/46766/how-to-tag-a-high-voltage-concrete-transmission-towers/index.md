+++
type = "question"
title = "How to tag a high voltage concrete transmission towers?"
description = '''How to tag a high voltage concrete transmission towers like this (220 kV) and this (110 kV) : power=tower or power=pole?'''
date = "2015-11-21T17:43:00Z"
lastmod = "2016-02-18T22:07:00Z"
weight = 46766
keywords = [ "pole", "tagging", "power", "tower" ]
aliases = [ "/questions/46766" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a high voltage concrete transmission towers?](/questions/46766/how-to-tag-a-high-voltage-concrete-transmission-towers)

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
<span id="post-46766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46766-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to tag a high voltage concrete transmission towers like this (220 kV)<img src="/upfiles/6Nqt_a1LDrk_kqN7RSD.jpg" alt="alt text" /></p>
<p>and this (110 kV)</p>
<p>:<img src="/upfiles/x_a60c1126_q3AMtZ7.jpg" alt="alt text" /></p>
<p>power=tower or power=pole?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pole" rel="tag" title="see questions tagged &#39;pole&#39;">pole</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span> <span class="post-tag tag-link-tower" rel="tag" title="see questions tagged &#39;tower&#39;">tower</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '15, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/61bec032cd24528a8253e204895d3c78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pokakukam&#39;s gravatar image" />
<p><span>pokakukam</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pokakukam has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '15, 19:36</strong> </span></p>
</div>
</div>
<div id="comments-container-46766" class="comments-container">
<span id="46767"></span>
<div id="comment-46767" class="comment">
<div id="post-46767-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><del>did you mean <code>power=tower</code> instead of <code>power=pylon</code> (check <a href="http://taginfo.openstreetmap.org/keys/power#values">taginfo</a>)?</del></p>
</div>
<div id="comment-46767-info" class="comment-info">
<span class="comment-age">(21 Nov '15, 19:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46766-form-container" class="comment-form-container">
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

<span id="48213"></span>

<div id="answer-container-48213" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48213-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general <a href="https://wiki.openstreetmap.org/wiki/Tag:power%3Dpole">power=pole</a> is used to mark smaller masts, while <a href="https://wiki.openstreetmap.org/wiki/Tag:power%3Dtower">power=tower</a> is reserved for bigger structures. This makes it for example easier for data consumers to judge the importance of the support with regards to the landscape. In practice this approach means that the differentiation between pole &amp; tower is relatively closely tied to the voltage of the line carried by a structure. Most of the time lines of triple-digit voltage are suppported on towers, in the range of 50-100 kV I'd say it can get a little bit fuzzy and below that it's mostly poles. But as always there are exceptions...</p>
<p>So what does that mean in your case? Well, although your first picture is missing an obvious reference to estimate the height of the tower, comparing its insulators to those in your other picture, I think it's quite clear that it's at least as high if not higher. Now the second image definitely shows a big tower, that stands out between all those trees and buildings and of course the voltages you mention are another hint. So this is how I would tag them:</p>
<ul>
<li>power=tower</li>
<li>material=concrete</li>
<li>(probably structure=solid , not 100% sure if such a pole-like concrete tower can be hollow; in that case the value would be tubular, I think)</li>
<li>design=asymmetric/barrel (1./2. tower)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '16, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a7a266361ac17107a1c0d0ecf6cae19b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TOGA&#39;s gravatar image" />
<p><span>TOGA</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TOGA has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-48213" class="comments-container">
&#10;</div>
<div id="comment-tools-48213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48213-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46768"></span>

<div id="answer-container-46768" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46768-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi pokakukam, take a look here <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Power_networks/France,">https://wiki.openstreetmap.org/wiki/WikiProject_Power_networks/France,</a> its Francois Lacombes as far as I remember work and he’s specialized in power lines. So if you can’t work it out yourself ask him directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '15, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-46768" class="comments-container">
&#10;</div>
<div id="comment-tools-46768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46768-form-container" class="comment-form-container">
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

