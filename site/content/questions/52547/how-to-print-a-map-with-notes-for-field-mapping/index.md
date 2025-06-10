+++
type = "question"
title = "How to print a map with notes for field mapping?"
description = '''A nearby village has accumulated about 10 justified notes. I would like to make a bicycle trip there and check or verify the notes on the ground. Is there a way to print a map, like Field Papers, but additionally with the unresolved notes? Ideally the printout would consist of the map plus markers A...'''
date = "2016-10-14T11:03:00Z"
lastmod = "2016-10-14T12:40:00Z"
weight = 52547
keywords = [ "field", "notes", "printing", "survey" ]
aliases = [ "/questions/52547" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to print a map with notes for field mapping?](/questions/52547/how-to-print-a-map-with-notes-for-field-mapping)

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
<span id="post-52547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52547-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A nearby village has accumulated about 10 justified notes. I would like to make a bicycle trip there and check or verify the notes on the ground. Is there a way to print a map, like <a href="http://www.fieldpapers.org/">Field Papers</a>, but additionally with the unresolved notes?</p>
<p>Ideally the printout would consist of the map plus markers A, B, C for the notes and a second page where the note text and comments are listed.</p>
<p>Alternatively, is there a way to export all open notes in a given bounding box in some text format for printout?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span> <span class="post-tag tag-link-survey" rel="tag" title="see questions tagged &#39;survey&#39;">survey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '16, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-52547" class="comments-container">
&#10;</div>
<div id="comment-tools-52547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52547-form-container" class="comment-form-container">
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

<span id="52548"></span>

<div id="answer-container-52548" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52548-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hfs has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API">notes API</a> to download <a href="http://api.openstreetmap.org/api/0.6/notes?bbox=-0.65094,51.312159,0.374908,51.669148&amp;closed=0#">all open notes in a bbox</a> in xml format. You'll probably want to trim the output to keep only the interesting bits. Then print the map from osm.org with the notes layer activated, and write the note numbers on the printed paper to match with the note descriptions. Not very elegant or streamlined, but for a 10-notes one-off it should do the trick ?</p>
<p>Alternatively, if you have a smartphone, you can install <a href="https://wiki.openstreetmap.org/wiki/Vespucci">vespucci</a> on it and download the area (including the notes) before you go, to have them available during your survey. Other apps like <a href="https://wiki.openstreetmap.org/wiki/Osmand">osmand</a> can do that too, but might require you to have a data connection during the survey.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '16, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-52548" class="comments-container">
<span id="52549"></span>
<div id="comment-52549" class="comment">
<div id="post-52549-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Great tips! I went with the notes API way using JSON output, which I found a bit friendlier to edit (after using an online pretty printer). It’s workable for a one-time job.</p>
</div>
<div id="comment-52549-info" class="comment-info">
<span class="comment-age">(14 Oct '16, 12:40)</span> <span class="comment-user userinfo">hfs</span>
</div>
</div>
</div>
<div id="comment-tools-52548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52548-form-container" class="comment-form-container">
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

