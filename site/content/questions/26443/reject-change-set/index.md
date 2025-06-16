+++
type = "question"
title = "reject change set"
description = '''How can I reject my (still open) change set? Unfortunately something went terribly wrong. In particular JOSM moved a street away. Now I moved it (approximated) back by hand.'''
date = "2013-09-17T17:13:00Z"
lastmod = "2013-09-17T18:14:00Z"
weight = 26443
keywords = [ "josm", "changeset" ]
aliases = [ "/questions/26443" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [reject change set](/questions/26443/reject-change-set)

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
<span id="post-26443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26443-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I reject my (still open) <a href="https://www.openstreetmap.org/browse/changeset/17889112">change set</a>? Unfortunately something went terribly wrong. In particular JOSM moved a street away. Now I moved it (approximated) back by hand.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '13, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/4fbc313b19815699ce8e8a53cf8f8ad5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nobelium&#39;s gravatar image" />
<p><span>Nobelium</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nobelium has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26443" class="comments-container">
&#10;</div>
<div id="comment-tools-26443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26443-form-container" class="comment-form-container">
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

<span id="26444"></span>

<div id="answer-container-26444" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26444-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nobelium has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The changes you made in your changeset already are written to the OSM database¹. As far as I know there also isn't any way to reject a not closed changeset.<br />
The solution for your problem I would suggest:</p>
<ul>
<li>close the changeset</li>
<li>revert the changeset using the reverter plugin</li>
<li>select the previously misaligned way and upload only the selection</li>
<li>(in a new data layer: download the region anew and check if everything is fine)</li>
</ul>
<p>PS: Don't get too upset about your error. Only who does nothing does nothing wrong. Maybe it soothes your mind if you have a look at <a href="http://forum.openstreetmap.org/viewtopic.php?id=22014&amp;p=3">errors other people made</a>. :)</p>
<p>¹ <a href="https://www.openstreetmap.org/browse/changeset/17889112">here</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '13, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '13, 17:44</strong> </span></p>
</div>
</div>
<div id="comments-container-26444" class="comments-container">
<span id="26447"></span>
<div id="comment-26447" class="comment">
<div id="post-26447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your PS (and your answer). Now I'm happy again :-)</p>
</div>
<div id="comment-26447-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 18:01)</span> <span class="comment-user userinfo">Nobelium</span>
</div>
</div>
<span id="26450"></span>
<div id="comment-26450" class="comment">
<div id="post-26450-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Glad I could help and make you happy. (;</p>
</div>
<div id="comment-26450-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 18:14)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-26444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26444-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26445"></span>

<div id="answer-container-26445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26445-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that you have closed this changeset already, or that it closed automatically after a delay. Annoyingly there is no way to "cancel" a changeset that has already been partially uploaded. OSM changeset do not map to database transactions.</p>
<p>What you can do is "revert" a changeset, which actually involves creating another changeset that does the reverse of the original. The <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter">josm revert plugin</a> helps with that. You can even do a partial revert, but it can become tricky quickly. If you do not trust yourself with this operation, feel free to ask for a revert here or on <a href="https://wiki.openstreetmap.org/wiki/Contact#IRC">irc</a>.</p>
<p>In case you hadn't spoted it, josm has a changeset manager in the windows menu. Not quite what you are looking for, but still useful. And of course, one of josm's advantage is that you can take your time (even save your work localy and come back to it days later) to check a changeset before you upload it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '13, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-26445" class="comments-container">
<span id="26448"></span>
<div id="comment-26448" class="comment">
<div id="post-26448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you save your edits locally and try to upload them some days later it can happen that you first have to resolve conflicts when other mappers have worked in that region, too.</p>
</div>
<div id="comment-26448-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 18:02)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-26445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26445-form-container" class="comment-form-container">
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

