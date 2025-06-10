+++
type = "question"
title = "[closed] Extratags not being returned in reverse geocoding request"
description = '''I have a private Nominatim installation. If I pass extratags=1 as a part of my reverse geocoding query nothing is returned. I have checked that the values exist in the placex table and they are being returned on the details.php page. Any further troubleshooting suggestions would be much appreciated....'''
date = "2016-10-15T00:54:00Z"
lastmod = "2016-10-18T21:15:00Z"
weight = 52551
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/52551" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Extratags not being returned in reverse geocoding request](/questions/52551/extratags-not-being-returned-in-reverse-geocoding-request)

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
<span id="post-52551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a private Nominatim installation. If I pass <code>extratags=1</code> as a part of my reverse geocoding query nothing is returned. I have checked that the values exist in the placex table and they are being returned on the details.php page. Any further troubleshooting suggestions would be much appreciated. Thanks.</p>
<p>I'm running postgres v9.3 and Nominatim v2.5.1</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '16, 00:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d2e7eae60626279a0687656a0d82a4c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cswrsinc&#39;s gravatar image" />
<p><span>cswrsinc</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cswrsinc has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>15 Oct '16, 12:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52551" class="comments-container">
&#10;</div>
<div id="comment-tools-52551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52551-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic (unrelated problem of non-GIS software further down in the stack)" by aseerel4c26 15 Oct '16, 12:31

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52553"></span>

<div id="answer-container-52553" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52553-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured it out, it was a problem with the Apache VirtualHost actually pointing to the old site. After enabling NameVirtualHost all is well, thanks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '16, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d2e7eae60626279a0687656a0d82a4c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cswrsinc&#39;s gravatar image" />
<p><span>cswrsinc</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cswrsinc has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-52553" class="comments-container">
<span id="52556"></span>
<div id="comment-52556" class="comment">
<div id="post-52556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the feedback. So it was not a Nominatim-related problem at all, right? Is it like this: You were essentially querying the wrong Nominatim instance?</p>
</div>
<div id="comment-52556-info" class="comment-info">
<span class="comment-age">(15 Oct '16, 12:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52593"></span>
<div id="comment-52593" class="comment">
<div id="post-52593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No it wasn't...correct, I was still hitting 2.4.0.</p>
</div>
<div id="comment-52593-info" class="comment-info">
<span class="comment-age">(18 Oct '16, 20:26)</span> <span class="comment-user userinfo">cswrsinc</span>
</div>
</div>
<span id="52595"></span>
<div id="comment-52595" class="comment">
<div id="post-52595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>for the interested people some background: Ah, I see, "extratags" <a href="https://github.com/twain47/Nominatim/blob/master/ChangeLog">is</a> a new (2.4 to current version 2.5) feature ("new namedetails and extratags parameters that expose the name and extratags fields of the placex table") of Nominatim.</p>
</div>
<div id="comment-52595-info" class="comment-info">
<span class="comment-age">(18 Oct '16, 21:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52553-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52552"></span>

<div id="answer-container-52552" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hmm, it should work like this <a href="http://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=51&amp;lon=11&amp;extratags=1">http://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=51&amp;lon=11&amp;extratags=1</a></p>
<p>Can you share the request URL and the response you get returned? Of course strip your domain name or any other personal information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '16, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52552" class="comments-container">
&#10;</div>
<div id="comment-tools-52552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52552-form-container" class="comment-form-container">
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

