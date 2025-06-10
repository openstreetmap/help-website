+++
type = "question"
title = "..resume import process after &quot;no space left&quot; error"
description = '''Please.. tell me that ther&#x27;is a way to resume.. please Rank30 returned error at ETA 0.135401 and it is: ERROR: It is not possible to extend file &quot;base/16386/5101187: No space left on device&quot; ERROR: pgsql returned eith error code (3) Please guys.. it runs since 18/10... I have 410 gb written (by nomi...'''
date = "2015-11-22T16:02:00Z"
lastmod = "2015-11-24T16:32:00Z"
weight = 46770
keywords = [ "nominatim" ]
aliases = [ "/questions/46770" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [..resume import process after "no space left" error](/questions/46770/resume-import-process-after-no-space-left-error)

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
<span id="post-46770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please.. tell me that ther'is a way to resume.. please</p>
<p>Rank30 returned error at ETA 0.135401 and it is:</p>
<p>ERROR: It is not possible to extend file "base/16386/5101187: No space left on device" ERROR: pgsql returned eith error code (3)</p>
<p>Please guys.. it runs since 18/10... I have 410 gb written (by nominatim) and 7.8 gb free on my disk.. People says me that it need 350/400 gb..</p>
<p>No way to resume..?? And if it is possible can I remove the european_map file (16gb) to get more space on disk?? Or the process still need it even at this point?? My life is on your hands..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '15, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '15, 17:05</strong> </span></p>
</div>
</div>
<div id="comments-container-46770" class="comments-container">
<span id="46775"></span>
<div id="comment-46775" class="comment">
<div id="post-46775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the wiki doc I have read that it can be done but I prefer your suggestion because I can't waste 32 days of work..</p>
</div>
<div id="comment-46775-info" class="comment-info">
<span class="comment-age">(22 Nov '15, 18:03)</span> <span class="comment-user userinfo">giacomo-keybiz</span>
</div>
</div>
</div>
<div id="comment-tools-46770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46770-form-container" class="comment-form-container">
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

<span id="46776"></span>

<div id="answer-container-46776" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46776-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The pbf file is not needed any more at this point.</p>
<p>You should be able to re-run <code>utils/update.php</code> with the flags <code>--index --create-search-indices</code> to restart indexing where it left off. If you do not plan to update your data then I am pretty sure you can, at this point, already drop some tables, most likely everything called planet_osm_something as well as "place" but please wait until someone else confirms that before running with it. If you <em>do</em> plan to run updates - which is going to be near impossible given that you'd be looking at catching up a full month - then you might need to find other ways of saving space.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '15, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46776" class="comments-container">
<span id="46777"></span>
<div id="comment-46777" class="comment">
<div id="post-46777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot man, you give me back some hope. Removing map I earn 16 gb, I hope this is enough. Thanks a lot</p>
</div>
<div id="comment-46777-info" class="comment-info">
<span class="comment-age">(22 Nov '15, 19:00)</span> <span class="comment-user userinfo">giacomo-keybiz</span>
</div>
</div>
<span id="46824"></span>
<div id="comment-46824" class="comment">
<div id="post-46824-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can drop the planet_osm_<em>, place and search_name_</em> tables if you do not intent to update but only <em>after</em> --index has finished. It is safe to do it before running --create-search-indices.</p>
</div>
<div id="comment-46824-info" class="comment-info">
<span class="comment-age">(24 Nov '15, 16:32)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-46776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46776-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46791"></span>

<div id="answer-container-46791" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46791-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi guys.. I made a merge of your istruction and others provided by "the official page". And than I shot:</p>
<pre><code>nohup ./utils/setup.php --index --create-search-indices --index-noanalyse 2&gt;&gt;resumeErr.log 1&gt;&gt;resumeSetup.log &amp;</code></pre>
<p>Now I see an output like this:</p>
<pre><code>Starting rank 17
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 18
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 19
 Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 20
 Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 21
 Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 22</code></pre>
<p>Tell me this is ok... please.. Thanks a lot.. you should have a part of my salary.. Giacomo</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '15, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46791" class="comments-container">
<span id="46798"></span>
<div id="comment-46798" class="comment">
<div id="post-46798-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://donate.osm.org/">http://donate.osm.org/</a></p>
<p>:)</p>
</div>
<div id="comment-46798-info" class="comment-info">
<span class="comment-age">(23 Nov '15, 16:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46791-form-container" class="comment-form-container">
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

