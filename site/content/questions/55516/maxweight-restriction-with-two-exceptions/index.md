+++
type = "question"
title = "maxweight restriction, with two exceptions"
description = '''We need to map a series of maxweight restrictions. But with an exception for both destination traffic and agricultural vehicles. I suppose it would look something like this: maxweight=* maxweight:conditional=none @ (destination, agricultural) or maxweight=* maxweight:conditional=none @ destination; ...'''
date = "2017-04-07T09:07:00Z"
lastmod = "2017-04-07T17:08:00Z"
weight = 55516
keywords = [ "access", "conditional", "combine", "maxweight" ]
aliases = [ "/questions/55516" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [maxweight restriction, with two exceptions](/questions/55516/maxweight-restriction-with-two-exceptions)

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
<span id="post-55516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We need to map a series of maxweight restrictions. But with an exception for both destination traffic and agricultural vehicles. I suppose it would look something like this:</p>
<p><code>maxweight=* maxweight:conditional=none @ (destination, agricultural)</code></p>
<p>or</p>
<p><code>maxweight=* maxweight:conditional=none @ destination; none @ agricultural</code></p>
<p>Is this the best solution? Are both valid? Am I missing a wiki page where these kinds of combinations are explained?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-combine" rel="tag" title="see questions tagged &#39;combine&#39;">combine</span> <span class="post-tag tag-link-maxweight" rel="tag" title="see questions tagged &#39;maxweight&#39;">maxweight</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '17, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-55516" class="comments-container">
&#10;</div>
<div id="comment-tools-55516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55516-form-container" class="comment-form-container">
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

<span id="55517"></span>

<div id="answer-container-55517" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55517-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> scheme doesn't define how to combine several conditions. It defines an <em>AND</em> operator but we need an <em>OR</em> operator here. Therefore the only solution is to define multiple separate conditions as done in your second suggestion:</p>
<pre><code>maxweight=*
maxweight:conditional=none @ destination; none @ agricultural</code></pre>
<p>Note that <code>none @ agricultural</code> specifies the purpose of the highway use. It doesn't give a general permission for all agricultural vehicles. If you want to allow all agricultural vehicles (independent of their purpose) then you have to use <del><code>maxweight:agricultural:conditional=none</code></del> <code>maxweight:agricultural=no</code> instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '17, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '17, 13:28</strong> </span></p>
</div>
</div>
<div id="comments-container-55517" class="comments-container">
<span id="55519"></span>
<div id="comment-55519" class="comment">
<div id="post-55519-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the 5th example on the conditional restrictions page does something similar for busses , but uses maxweight:bus=none (so it does not repeat the :conditional). Should this be corrected then ?</p>
</div>
<div id="comment-55519-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 12:54)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="55520"></span>
<div id="comment-55520" class="comment">
<div id="post-55520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good question. Without the :conditional part would be the "old" (i.e. non-conditional) tagging style, in this case <code>maxweight:agricultural=no</code>. So I guess there are two possible tagging schemes for specifying no maxweight restriction for vehicle types (yay!). Preferring the old (and simpler) style seems to be a good idea. Thanks for the hint, I've updated my answer.</p>
</div>
<div id="comment-55520-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 13:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="55525"></span>
<div id="comment-55525" class="comment">
<div id="post-55525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, reading your clarification I understand we can make a difference between vehicles that are built to do something agricultural, and vehicles that happen to be doing something agricultural? So the maxweight:conditional=none @ destination; none @ agricultural means that agricultural vehicles are allowed, unless they aren't entering the area to do something agricultural. But of course, they are still allowed if they have to be there. Hmm, so remains to be seen what the Belgian lawmaker means with "landbouwvoertuigen": the purpose of the vehicle or the purpose of the trip...</p>
</div>
<div id="comment-55525-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 17:08)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-55517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55517-form-container" class="comment-form-container">
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

