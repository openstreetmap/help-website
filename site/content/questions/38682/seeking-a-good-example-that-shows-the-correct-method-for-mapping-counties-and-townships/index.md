+++
type = "question"
title = "seeking a good example that shows the correct method for mapping counties and townships"
description = '''Most of the counties in Ohio are missing the townships. I&#x27;d like to begin by adding the townships that exist in my county, and I&#x27;ve been reading everything I can find about relations, boundaries, etc. (I&#x27;m a newbie).  It would be really helpful to have a good example where this is done correctly so ...'''
date = "2014-11-20T14:07:00Z"
lastmod = "2014-11-26T05:55:00Z"
weight = 38682
keywords = [ "boundaries", "county", "townships", "relations" ]
aliases = [ "/questions/38682" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [seeking a good example that shows the correct method for mapping counties and townships](/questions/38682/seeking-a-good-example-that-shows-the-correct-method-for-mapping-counties-and-townships)

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
<span id="post-38682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38682-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Most of the counties in Ohio are missing the townships. I'd like to begin by adding the townships that exist in my county, and I've been reading everything I can find about relations, boundaries, etc. (I'm a newbie).</p>
<p>It would be really helpful to have a good example where this is done correctly so that I can examine how the shared boundaries are tagged...and any other info that would help would be greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-county" rel="tag" title="see questions tagged &#39;county&#39;">county</span> <span class="post-tag tag-link-townships" rel="tag" title="see questions tagged &#39;townships&#39;">townships</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '14, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/4d1fe4bbbb52dc0195ee00d38ec5a792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unigami&#39;s gravatar image" />
<p><span>unigami</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unigami has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38682" class="comments-container">
&#10;</div>
<div id="comment-tools-38682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38682-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="38686"></span>

<div id="answer-container-38686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38686-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="http://wiki.openstreetmap.org/wiki/Admin_level#10_admin_level_values_for_specific_countries,">http://wiki.openstreetmap.org/wiki/Admin_level#10_admin_level_values_for_specific_countries,</a> townships should be admin_level=7 in most of the US.</p>
<p>I would highly recommend using type=boundary, boundary=administrative relations for these. Then those boundary ways can be reused for multiple townships/cities/counties/etc. Here's an example of a township done with relation: <a href="http://www.openstreetmap.org/relation/2342528">http://www.openstreetmap.org/relation/2342528</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '14, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-38686" class="comments-container">
<span id="38688"></span>
<div id="comment-38688" class="comment">
<div id="post-38688-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-38688-info" class="comment-info">
<span class="comment-age">(20 Nov '14, 18:14)</span> <span class="comment-user userinfo">unigami</span>
</div>
</div>
</div>
<div id="comment-tools-38686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38686-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38783"></span>

<div id="answer-container-38783" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38783-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at Ireland. In Ireland, we're adding <code>admin_level=10</code>'s (which we call townlands). The ways that make them up are shared with the higher level admin boundaries (like <code>admin_level=9/6/etc.</code>)</p>
<p>e.g. <a href="http://www.openstreetmap.org/relation/4118986">http://www.openstreetmap.org/relation/4118986</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '14, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-38783" class="comments-container">
&#10;</div>
<div id="comment-tools-38783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38783-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38833"></span>

<div id="answer-container-38833" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38833-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've been doing the same in Pennsylvania and have Clarion, Butler, Armstrong, and Greene Counties completed. You can take a look at <a href="http://www.openstreetmap.org/user/vinlendingur/history">some of my more recent edits</a> to see how I've done these township relationships. The only difference you would have is admin_level... PA has incorporated townships, so their level is 8, while OH would use level 7.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '14, 05:55</strong></p>
<img src="https://secure.gravatar.com/avatar/52597735f1dab413ec921690d96a0603?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vinlendingur&#39;s gravatar image" />
<p><span>vinlendingur</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vinlendingur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38833" class="comments-container">
&#10;</div>
<div id="comment-tools-38833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38833-form-container" class="comment-form-container">
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

