+++
type = "question"
title = "How do you tag gates that are open most of the time?"
description = '''Richmond Park has (or is supposed to have, I think) a gate in every entrance. When closed the gates block all traffic so implied access=no is correct, in a way, and routing engines shouldn&#x27;t let you get in or out of the park. The opening times are very variable (PDF) but one could argue the gates ar...'''
date = "2010-07-18T20:31:00Z"
lastmod = "2010-07-22T13:35:00Z"
weight = 310
keywords = [ "access", "barrier", "tagging", "routing" ]
aliases = [ "/questions/310" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you tag gates that are open most of the time?](/questions/310/how-do-you-tag-gates-that-are-open-most-of-the-time)

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
<span id="post-310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-310-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://www.openstreetmap.org/?lat=51.4386&amp;lon=-0.2771&amp;zoom=14">Richmond Park</a> has (or is supposed to have, I think) a gate in every entrance. When closed the gates block all traffic so implied access=no is correct, in a way, and routing engines shouldn't let you get in or out of the park. The opening times are very variable (<a href="http://www.royalparks.org.uk/docs/richmondpark/Richmond%20Park%20opening%20times.pdf">PDF</a>) but one could argue the gates are always open for all practical purposes.</p>
<p>How should the gates be tagged to allow useful routing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '10, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e260236f98a32acdb3ce43cc9e1e01a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tko&#39;s gravatar image" />
<p><span>tko</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-310" class="comments-container">
&#10;</div>
<div id="comment-tools-310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-310-form-container" class="comment-form-container">
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

<span id="333"></span>

<div id="answer-container-333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-333-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>barrier=gate</li>
<li>access=yes</li>
</ul>
<p>I'd certainly be inclined to tag it access=yes or access=designated, to indicate the gate is normally open. Hopefully routing engines will understand this access tag.</p>
<p>Then the <a href="http://wiki.openstreetmap.org/wiki/Key:access#Access_time_restrictions">access time restrictions</a> tag docs would suggest something like...</p>
<ul>
<li>hour_on=22:00</li>
<li>hour_off=07:00</li>
</ul>
<p>I'm pretty sure there are no routing engines paying attention to that, but I guess it'll be a future possibility if we record the information:</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '10, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-333" class="comments-container">
&#10;</div>
<div id="comment-tools-333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-333-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="435"></span>

<div id="answer-container-435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-435-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My suggestion would be <strong>barrier=gate</strong> with <strong>access=permissive</strong>, since <a href="http://en.wikipedia.org/wiki/Royal_Parks_of_London">access to the Royal Parks</a> is by the grace and favour of the Crown (what a wonderful phrase!)</p>
<p>I'd suggest tagging the roads as permissive too, unless they're actual rights of way. Some research may be necessary...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '10, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-435" class="comments-container">
&#10;</div>
<div id="comment-tools-435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-435-form-container" class="comment-form-container">
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

