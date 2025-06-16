+++
type = "question"
title = "how to combine .poly files?"
description = '''Hello - I am trying to combine 2 geofabrik .poly files into one file and do not know the &quot;technique&quot;.  I have tried pasting the data from the 2nd file to the bottom of the first (above the &quot;end, end&quot; lines) and then added the number &quot;2&quot; between the 2 sets of data. Neither approach worked because I d...'''
date = "2014-12-03T18:18:00Z"
lastmod = "2014-12-08T16:34:00Z"
weight = 39022
keywords = [ "polygon", "bounding-polygon" ]
aliases = [ "/questions/39022" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to combine .poly files?](/questions/39022/how-to-combine-poly-files)

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
<span id="post-39022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39022-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello -</p>
<p>I am trying to combine 2 geofabrik .poly files into one file and do not know the "technique". I have tried pasting the data from the 2nd file to the bottom of the first (above the "end, end" lines) and then added the number "2" between the 2 sets of data. Neither approach worked because I do not understand the file structure, besides that it uses sci notation. I am using phyghtmap to create contours from srtm data.</p>
<p>Thanks, pitney</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '14, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39022" class="comments-container">
&#10;</div>
<div id="comment-tools-39022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39022-form-container" class="comment-form-container">
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

<span id="39024"></span>

<div id="answer-container-39024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39024-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM might come in handy for this task: as a prerequisite you need to install poly and utilsplugin2 plugins.</p>
<ol>
<li>Open two intersecting poly files (I tried with France and Germany)</li>
<li>Combine the two of them into a single layer in the layers pane (combine one area with another area)</li>
<li>Select both poly lines</li>
<li>combine overlapping areas (shift-j)</li>
<li>save the result as poly file again.</li>
</ol>
<p>That's how my result looks like:</p>
<p><img src="/upfiles/france_germany.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '14, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '14, 20:41</strong> </span></p>
</div>
</div>
<div id="comments-container-39024" class="comments-container">
<span id="39104"></span>
<div id="comment-39104" class="comment">
<div id="post-39104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>mmd -</p>
<p>Thank you, this technique worked.</p>
<p>As a follow up Q, can JOSM also be used to split a .poly file?</p>
<p>Thanks, pitney</p>
</div>
<div id="comment-39104-info" class="comment-info">
<span class="comment-age">(06 Dec '14, 20:00)</span> <span class="comment-user userinfo">pitney</span>
</div>
</div>
<span id="39105"></span>
<div id="comment-39105" class="comment">
<div id="post-39105-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can split a polygon in JOSM by selecting 2 nodes (click while pressing ctrl-key) and then pressing alt-x. The result can be saved again as poly file.</p>
</div>
<div id="comment-39105-info" class="comment-info">
<span class="comment-age">(06 Dec '14, 20:08)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39024-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39141"></span>

<div id="answer-container-39141" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>as a final? update, if you need to add only an isolated area to an existing .poly file (ex. an island, say the Falklands to Argentina!) you can just add the data to the end of the file, before end,end.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '14, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39141" class="comments-container">
&#10;</div>
<div id="comment-tools-39141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39141-form-container" class="comment-form-container">
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

