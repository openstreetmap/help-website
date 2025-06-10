+++
type = "question"
title = "How do I export a large area as PostScript?"
description = '''I want to export as postcript, and it is not working for me, is there any tip to follow? Also, I would like to have a big map of Buenos Aires City (200m/1000ft), but I can only export small sizes. I need to print this in a way that streets can be read. Is there a way to get the whole big map in post...'''
date = "2011-10-25T14:34:00Z"
lastmod = "2011-10-25T21:20:00Z"
weight = 8643
keywords = [ "mapnik", "postcript" ]
aliases = [ "/questions/8643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I export a large area as PostScript?](/questions/8643/how-do-i-export-a-large-area-as-postscript)

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
<span id="post-8643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8643-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to export as postcript, and it is not working for me, is there any tip to follow? Also, I would like to have a big map of Buenos Aires City (200m/1000ft), but I can only export small sizes. I need to print this in a way that streets can be read. Is there a way to get the whole big map in postcript format?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postcript" rel="tag" title="see questions tagged &#39;postcript&#39;">postcript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '11, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/faa1102d94c744d2e932ffeb61c7212c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="consu470&#39;s gravatar image" />
<p><span>consu470</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="consu470 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '11, 19:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8643" class="comments-container">
&#10;</div>
<div id="comment-tools-8643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8643-form-container" class="comment-form-container">
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

<span id="8647"></span>

<div id="answer-container-8647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8647-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Exporting requires individual rendering of the area. Large areas contains a lot of information and therefore takes a lot of time to render. Therefore this is disabled on the main server.</p>
<p>You can however use a tils stitching service such as <a href="http://openstreetmap.gryph.de/bigmap.cgi">BigMap</a> to stich together prerendered tiles to a bigger map. This limits the options you have like exact scale and output file type. You can use a image manipulation program or a "print to PostScript" option to convert the file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8647" class="comments-container">
&#10;</div>
<div id="comment-tools-8647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8647-form-container" class="comment-form-container">
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

