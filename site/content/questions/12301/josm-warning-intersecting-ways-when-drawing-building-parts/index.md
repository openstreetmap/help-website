+++
type = "question"
title = "JOSM-warning &#x27;intersecting ways&#x27; when drawing building parts"
description = '''Hello, I&#x27;m trying to map buildings with different parts in JOSM (version 5181). I use one closed way per building part (and tag it with &#x27;building:part=yes&#x27;) &amp;amp; then one closed way to mark the hole building (which I tag with &#x27;building=yes&#x27; and &#x27;building:parts=horizontal/vertical/mixed&#x27;). When I tr...'''
date = "2012-04-23T18:40:00Z"
lastmod = "2014-10-07T09:49:00Z"
weight = 12301
keywords = [ "building", "josm", "intersection" ]
aliases = [ "/questions/12301" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM-warning 'intersecting ways' when drawing building parts](/questions/12301/josm-warning-intersecting-ways-when-drawing-building-parts)

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
<span id="post-12301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12301-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to map buildings with different parts in JOSM (version 5181). I use one closed way per building part (and tag it with 'building:part=yes') &amp; then one closed way to mark the hole building (which I tag with 'building=yes' and 'building:parts=horizontal/vertical/mixed').</p>
<p>When I try to submit my changes I get a warning that the ways of my building parts are intersecting… Am I doing something wrong?</p>
<p>Thanks, Stefan.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '12, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f8a6b8b922bef3a95e2acce981b8a1a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stefan%20Nagy&#39;s gravatar image" />
<p><span>Stefan Nagy</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stefan Nagy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12301" class="comments-container">
<span id="37375"></span>
<div id="comment-37375" class="comment">
<div id="post-37375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might try updating JOSM to the current version of 7588. Your version 5181 is very old and a lot of improvements/alterations have since been made to JOSM and it's plug-ins. Regards</p>
</div>
<div id="comment-37375-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 09:05)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="37376"></span>
<div id="comment-37376" class="comment">
<div id="post-37376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wrote this more than two years ago, so that's why the mentioned version is very old ;) I'll try to reproduce this behavior by mapping a building with building parts (as described above) with the current version of JOSM as soon as possible. Thanks</p>
</div>
<div id="comment-37376-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 09:43)</span> <span class="comment-user userinfo">Stefan Nagy</span>
</div>
</div>
</div>
<div id="comment-tools-12301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12301-form-container" class="comment-form-container">
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

<span id="37361"></span>

<div id="answer-container-37361" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37361-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Stefan Nagy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The JOSM validator has several levels of notification.</p>
<p>Detected errors generally are unambiguously wrong.</p>
<p>Warnings are of suspicious looking items, it's generally a good idea to check these carefully to make sure you haven't made a mistake. If everything looks OK then you should be OK to upload.</p>
<p>In the case you mentioned I would think your edits are fine, I think the building:part=* tag isn't something the JOSM developers expected when they wrote the Validator.</p>
<p>More information on the validator can be found at the link below.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/JOSM/Validator">http://wiki.openstreetmap.org/wiki/JOSM/Validator</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '14, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-37361" class="comments-container">
<span id="37378"></span>
<div id="comment-37378" class="comment">
<div id="post-37378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I have to see if I can still reproduce this behavior in the current version of JOSM. However, would you suggest to file a bug report against JOSM in cases like this? Would it be helpful to the developers?</p>
</div>
<div id="comment-37378-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 09:49)</span> <span class="comment-user userinfo">Stefan Nagy</span>
</div>
</div>
</div>
<div id="comment-tools-37361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37361-form-container" class="comment-form-container">
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

