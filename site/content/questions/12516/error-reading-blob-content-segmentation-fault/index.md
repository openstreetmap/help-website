+++
type = "question"
title = "error reading blob content Segmentation fault"
description = '''heyho while osm2pgsql I received the following error:  Processing: Node(96293k 17.2k/s) Way(1074k 0.03k/s) Relation(0 0.00/s)error reading blob content Segmentation fault  Is it possible that the error appeared because of a n error on my external HDD where I store my *.osm files or does this look li...'''
date = "2012-05-03T06:43:00Z"
lastmod = "2014-05-25T23:21:00Z"
weight = 12516
keywords = [ "segmentation", "osm2pgsql", "way", "error" ]
aliases = [ "/questions/12516" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error reading blob content Segmentation fault](/questions/12516/error-reading-blob-content-segmentation-fault)

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
<span id="post-12516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>heyho</p>
<p>while osm2pgsql I received the following error:</p>
<blockquote>
<p>Processing: Node(96293k 17.2k/s) Way(1074k 0.03k/s) Relation(0 0.00/s)error reading blob content Segmentation fault</p>
</blockquote>
<p>Is it possible that the error appeared because of a n error on my external HDD where I store my *.osm files or does this look like another reason?</p>
<p>It might be possible, that the external HDD got disconnected but I don't know if the error-message was there before.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segmentation" rel="tag" title="see questions tagged &#39;segmentation&#39;">segmentation</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '12, 06:43</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12516" class="comments-container">
&#10;</div>
<div id="comment-tools-12516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12516-form-container" class="comment-form-container">
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

<span id="12522"></span>

<div id="answer-container-12522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12522-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer - yes.</p>
<p>Longer answer - something spat "error reading blob content Segmentation fault" over the top of the normal output from osm2pgsql. A <a href="http://www.google.co.uk/search?q=%22error+reading+blob+content%22+&amp;btnG=Search&amp;oe=utf-8&amp;rls=org.mozilla%3Aen-GB%3Aofficial&amp;client=firefox-a">web search</a> shows the first part of that message in the PBF reader called by osm2pgsql, so yes, for some reason your external HDD became inaccessible and that caused the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '12, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12522" class="comments-container">
<span id="33469"></span>
<div id="comment-33469" class="comment">
<div id="post-33469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Someone on IRC has just mentioned another cause of this - a downloaded extract had somehow become truncated, which meant that osm2pgsql failed to understand the data, resulting in this same "error reading blob content" message.</p>
<p>If you're downloading extracts from somewhere like Geofabrik, there'll usually be a .md5 file available that you can compare the file you've downloaded against using "md5sum", to check that it hasn't got corrupted during the download process.</p>
</div>
<div id="comment-33469-info" class="comment-info">
<span class="comment-age">(25 May '14, 23:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12522-form-container" class="comment-form-container">
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

