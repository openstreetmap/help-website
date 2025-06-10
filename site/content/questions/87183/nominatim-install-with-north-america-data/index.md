+++
type = "question"
title = "Nominatim Install with North America Data"
description = '''Hello all, Trying to setup a local nominatim server with north america dataset. I will be using this server to normalize some adress stating strings and get full adress (especially city,state,country) data. I have limited disk space and installation got cancelled because of lack of space on disk. So...'''
date = "2023-04-28T11:45:00Z"
lastmod = "2023-05-01T20:00:00Z"
weight = 87183
keywords = [ "nominatim", "installation", "northamerica" ]
aliases = [ "/questions/87183" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Install with North America Data](/questions/87183/nominatim-install-with-north-america-data)

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
<span id="post-87183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>Trying to setup a local nominatim server with north america dataset. I will be using this server to normalize some adress stating strings and get full adress (especially city,state,country) data. I have limited disk space and installation got cancelled because of lack of space on disk. So, I'm looking for ways to reduce size. I used --no-updates tag also. Appreciate any suggestions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-northamerica" rel="tag" title="see questions tagged &#39;northamerica&#39;">northamerica</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '23, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/97f4f7e9bed9ce0816f30b24a7788421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gorkemsanal&#39;s gravatar image" />
<p><span>Gorkemsanal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gorkemsanal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87183" class="comments-container">
&#10;</div>
<div id="comment-tools-87183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87183-form-container" class="comment-form-container">
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

<span id="87184"></span>

<div id="answer-container-87184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There aren't many changes you can to, it's just a lot of data. Nominatim imports everything into 3 database tables first (or 2 tables plus the flatnode file), then convert everything into the final search tables. With --no-updates the 3 tables get deleted but during the index stage they're needed and consume most.</p>
<p>Use the flatnode file <a href="https://nominatim.org/release-docs/latest/admin/Import/#flatnode-files">https://nominatim.org/release-docs/latest/admin/Import/#flatnode-files</a></p>
<p>Maybe import USA only <a href="https://download.geofabrik.de/north-america.html">https://download.geofabrik.de/north-america.html</a> and then <a href="https://nominatim.org/release-docs/latest/admin/Advanced-Installations/">https://nominatim.org/release-docs/latest/admin/Advanced-Installations/</a> how to add Mexico and Canada later. That could also work if you import one US state after the other but I'm not sure how streets crossing state borders are treated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '23, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-87184" class="comments-container">
<span id="87191"></span>
<div id="comment-87191" class="comment">
<div id="post-87191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I've created a flatnode file right now installation goes on. However, "Processing: Node(1682145k 654.3k/s) Way(53345k 0.29k/s) Relation(0 0.0/s)" as you can see "Way" has this speed is it too slow or normal?</p>
</div>
<div id="comment-87191-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 17:53)</span> <span class="comment-user userinfo">Gorkemsanal</span>
</div>
</div>
<span id="87203"></span>
<div id="comment-87203" class="comment">
<div id="post-87203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That seems slow but I know nothing about the hardware you use. The database tuning parameter will have an effect <a href="https://nominatim.org/release-docs/latest/admin/Installation/#tuning-the-postgresql-database">https://nominatim.org/release-docs/latest/admin/Installation/#tuning-the-postgresql-database</a> but so does raw processor speed and how fast the discs are.</p>
</div>
<div id="comment-87203-info" class="comment-info">
<span class="comment-age">(01 May '23, 20:00)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-87184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87184-form-container" class="comment-form-container">
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

