+++
type = "question"
title = "Geographical coordinates conversion from one format to the other"
description = '''Dear All, I have my geographical coordinates in the following format: 3d44&#x27;42.838&quot;E 51d25&#x27;38.268&quot;N 44.443 3d45&#x27;9.935&quot;E 51d30&#x27;2.643&quot;N 44.330 3d44&#x27;54.911&quot;E 51d30&#x27;5.507&quot;N 44.328 How can I convert them into the decimal format. I also do not know the numbers after N such as 44.443 etc. '''
date = "2014-12-15T11:14:00Z"
lastmod = "2014-12-15T13:59:00Z"
weight = 39454
keywords = [ "algorithm", "degrees", "decimalformat", "coordinates" ]
aliases = [ "/questions/39454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Geographical coordinates conversion from one format to the other](/questions/39454/geographical-coordinates-conversion-from-one-format-to-the-other)

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
<span id="post-39454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear All,</p>
<p>I have my geographical coordinates in the following format:</p>
<p>3d44'42.838"E 51d25'38.268"N 44.443 3d45'9.935"E 51d30'2.643"N 44.330 3d44'54.911"E 51d30'5.507"N 44.328</p>
<p>How can I convert them into the decimal format. I also do not know the numbers after N such as 44.443 etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span> <span class="post-tag tag-link-degrees" rel="tag" title="see questions tagged &#39;degrees&#39;">degrees</span> <span class="post-tag tag-link-decimalformat" rel="tag" title="see questions tagged &#39;decimalformat&#39;">decimalformat</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '14, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/94b87aa7b3d83d8a5038f73f472a65a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebrahiem&#39;s gravatar image" />
<p><span>Ebrahiem</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebrahiem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>15 Dec '14, 13:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-39454" class="comments-container">
&#10;</div>
<div id="comment-tools-39454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39454-form-container" class="comment-form-container">
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

<span id="39483"></span>

<div id="answer-container-39483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is s programming problem. There are 60 minutes in one degree, and 60 seconds in one minute (i.e. 60×60 = 3600 seconds in one degree). <code>Xd Y ' Z.ZZZ" N</code> means there are X degrees, Y minutes and Z.ZZZ seconds. The forumula should be something like <code>X + Y/60 + Z.ZZZ/3600</code></p>
<p>I don't know what the <code>44.443</code> number is. Where did you get these coordinates?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '14, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-39483" class="comments-container">
<span id="39484"></span>
<div id="comment-39484" class="comment">
<div id="post-39484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I converted the coordinates from Amsterfoort RD to the conventional format and that is where I got that. Let me rephrase the question, can I just replace the d with the degree sign and make spaces in order to use these coordinates? many thanks in advance</p>
</div>
<div id="comment-39484-info" class="comment-info">
<span class="comment-age">(15 Dec '14, 12:14)</span> <span class="comment-user userinfo">Ebrahiem</span>
</div>
</div>
<span id="39494"></span>
<div id="comment-39494" class="comment">
<div id="post-39494-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No. <code>40d30'</code> is "40 degrees and 30 minutes". This is also <code>40.5 d</code>. So you can't just do a text replace. You need to do the calculation</p>
</div>
<div id="comment-39494-info" class="comment-info">
<span class="comment-age">(15 Dec '14, 13:27)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="39496"></span>
<div id="comment-39496" class="comment">
<div id="post-39496-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes a text replacement before a calculation</p>
</div>
<div id="comment-39496-info" class="comment-info">
<span class="comment-age">(15 Dec '14, 13:59)</span> <span class="comment-user userinfo">Ebrahiem</span>
</div>
</div>
</div>
<div id="comment-tools-39483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39483-form-container" class="comment-form-container">
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

