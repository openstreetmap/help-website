+++
type = "question"
title = "What is correct: addr:postcode, postal_code or both?"
description = '''I&#x27;m numbering streets with iD editor. The menu have the following options to post code:   - addr: postcode;   - postal_code. What&#x27;s the correct tag: addr:postcode, postal_code or both?'''
date = "2015-09-18T13:59:00Z"
lastmod = "2015-09-18T16:28:00Z"
weight = 45369
keywords = [ "postal_code" ]
aliases = [ "/questions/45369" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is correct: addr:postcode, postal_code or both?](/questions/45369/what-is-correct-addrpostcode-postal_code-or-both)

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
<span id="post-45369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45369-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm numbering streets with iD editor. The menu have the following options to post code:   - addr: postcode;   - postal_code.</p>
<p>What's the correct tag: addr:postcode, postal_code or both?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '15, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/62b0db5708737186a53757d471a515ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seth&#39;s gravatar image" />
<p><span>seth</span><br />
<span class="score" title="201 reputation points">201</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '15, 14:01</strong> </span></p>
</div>
</div>
<div id="comments-container-45369" class="comments-container">
&#10;</div>
<div id="comment-tools-45369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45369-form-container" class="comment-form-container">
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

<span id="45370"></span>

<div id="answer-container-45370" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45370-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-45370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For something that has an address - e.g. a house - use <code>addr:postcode=1234</code>. For a post code boundary, use <code>boundary=postal_code</code>, <code>postal_code=1234</code>. For things that neither have an address nor are a post code boundary (e.g. streets or place nodes), don't add any postal code tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '15, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45370" class="comments-container">
<span id="45371"></span>
<div id="comment-45371" class="comment">
<div id="post-45371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am numbered with the tag addr:interpolation by adding at line ends the following information:   - addr: housenumber;   - addr: street;   - addr: postcode or postal_code (doubt is here).</p>
</div>
<div id="comment-45371-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 14:15)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="45373"></span>
<div id="comment-45373" class="comment">
<div id="post-45373-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10008/seth">@seth</a> the line ends of an addr:interpolation are something that "have an address", so addr:postcode</p>
</div>
<div id="comment-45373-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 14:23)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="45376"></span>
<div id="comment-45376" class="comment">
<div id="post-45376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5390/escada">@escada</a> thanks.</p>
</div>
<div id="comment-45376-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 16:28)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-45370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45370-form-container" class="comment-form-container">
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

