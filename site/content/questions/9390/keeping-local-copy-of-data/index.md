+++
type = "question"
title = "Keeping local copy of data?"
description = '''In JOSM one can save the data layer and load it later, it also has the ability to update the map. Seems like a good idea - download once, than only update, saves my time downloading, saves server time sending, I can work offline and later somehow merge the edits if needed.  What is bothering me is t...'''
date = "2011-12-08T23:13:00Z"
lastmod = "2011-12-09T10:41:00Z"
weight = 9390
keywords = [ "josm", "local-copy" ]
aliases = [ "/questions/9390" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Keeping local copy of data?](/questions/9390/keeping-local-copy-of-data)

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
<span id="post-9390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9390-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM one can save the data layer and load it later, it also has the ability to update the map. Seems like a good idea - download once, than only update, saves my time downloading, saves server time sending, I can work offline and later somehow merge the edits if needed.<br />
What is bothering me is that the updating looks very similar (same) as fresh download. Working on a big (city) are stops being so smooth and convenient.<br />
</p>
<p>Does it have any meaning to have local copy of data and update it compared to fresh downloads for each edit? Any advantages I did not mention? Any hidden drawbacks?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-local-copy" rel="tag" title="see questions tagged &#39;local-copy&#39;">local-copy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '11, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-9390" class="comments-container">
&#10;</div>
<div id="comment-tools-9390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9390-form-container" class="comment-form-container">
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

<span id="9394"></span>

<div id="answer-container-9394" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9394-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do not have any pending edits, I'd recommend, starting from scratch with a fresh download.</p>
<p><em>Update data</em> is a shortcut for the following actions:</p>
<ul>
<li>Downloading all the bounding boxes of the current data layer. (This is <strong>not</strong> faster than the initial download. In fact, it is the same API request.)</li>
<li>Merging the fresh data with your (modified) old data. (Similar to merging two data layers.)</li>
</ul>
<p>Update can be useful when you like to check for conflicts. Also, it's handy, if you have many small boxes and you want the most recent data, but downloading the boxes one by one would be too cumbersome.</p>
<p>Note that <em>Update selection</em> and <em>Update modified</em> work differently: The bounding boxes do not matter; JOSM will request only data for the selected / modified objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '11, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/766400faa78a96dce84422cdb20779d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bastik&#39;s gravatar image" />
<p><span>bastik</span><br />
<span class="score" title="651 reputation points">651</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bastik has 5 accepted answers">41%</span></p>
</div>
</div>
<div id="comments-container-9394" class="comments-container">
&#10;</div>
<div id="comment-tools-9394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9394-form-container" class="comment-form-container">
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

