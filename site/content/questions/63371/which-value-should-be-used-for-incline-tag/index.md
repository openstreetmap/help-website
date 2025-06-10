+++
type = "question"
title = "Which value should be used for incline tag?"
description = '''Hi, I&#x27;ve read the description of incline tag on wiki, but yet it&#x27;s a little confusing to me.  If I set an &quot;incline=up/down&quot; tag on a &quot;highway=steps&quot;, does it mean someone should not go down/up using that way (like oneway=yes)?  If the way is oneway, then it seems clear which value I should use for t...'''
date = "2018-05-07T17:28:00Z"
lastmod = "2018-05-07T23:13:00Z"
weight = 63371
keywords = [ "incline" ]
aliases = [ "/questions/63371" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Which value should be used for incline tag?](/questions/63371/which-value-should-be-used-for-incline-tag)

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
<span id="post-63371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've read the description of incline tag on wiki, but yet it's a little confusing to me.</p>
<p>If I set an "<a href="https://wiki.openstreetmap.org/wiki/Key:incline">incline</a>=up/down" tag on a "highway=<a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dsteps">steps</a>", does it mean someone should not go down/up using that way (like oneway=yes)?</p>
<p>If the way is oneway, then it seems clear which value I should use for the incline tag (up/down, negative/positive). But if a single way is not oneway how you decide which value to be used?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incline" rel="tag" title="see questions tagged &#39;incline&#39;">incline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '18, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5b2d680cd0c22a32517db07ed16eeaf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iriman&#39;s gravatar image" />
<p><span>iriman</span><br />
<span class="score" title="297 reputation points">297</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iriman has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-63371" class="comments-container">
&#10;</div>
<div id="comment-tools-63371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63371-form-container" class="comment-form-container">
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

<span id="63376"></span>

<div id="answer-container-63376" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63376-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iriman has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When used on <code>highway=steps</code>, the incline tag indicates whether following the direction of the way will take you up or down the steps. Without specifying this, data consumers wouldn't know which way the steps are inclined (there isn't a convention that says that the way's direction is always up or always down).</p>
<p>If walking in the direction of the way will take you up the steps, then it's <code>incline=up</code>. If walking in the direction of the way will take you down the steps, then it's <code>incline=down</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '18, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-63376" class="comments-container">
&#10;</div>
<div id="comment-tools-63376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63376-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63377"></span>

<div id="answer-container-63377" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63377-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All ways in the OSM database have a direction. Very often this is not related to anything in the real world - it is simply a convention. For example even ways used to outline buildings have a direction. Normally editors will show some kind of arrow to indicate the direction of a way.</p>
<p>This allows us to give a meaning to concepts such as left/right for any way. If a way is tagged as having a sidewalk on the left it means "on the left when following the direction of the way in the database".</p>
<p>Up/down works similarly. Imagine you follow the way in the same direction as the arrows in your editor. Would you go up or down? That is the tag to use. It in no way implies that the way can only be followed in that direction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '18, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-63377" class="comments-container">
<span id="63378"></span>
<div id="comment-63378" class="comment">
<div id="post-63378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like I was typing while alester was posting.</p>
</div>
<div id="comment-63378-info" class="comment-info">
<span class="comment-age">(07 May '18, 23:13)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-63377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63377-form-container" class="comment-form-container">
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

