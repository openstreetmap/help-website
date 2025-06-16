+++
type = "question"
title = "Specs for building a OSM tile server"
description = '''I haves successfully built my tile server using the following link for UK. Now I need the my server to have the data of the entire planet. I was wondering how much memory would the database need?  Also, I saw that the .pfb file for the entire planet is around 50-60GB then why is the disk space requi...'''
date = "2018-10-17T20:55:00Z"
lastmod = "2018-10-17T22:53:00Z"
weight = 66372
keywords = [ "disk_usage", "osm", "tileserver" ]
aliases = [ "/questions/66372" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Specs for building a OSM tile server](/questions/66372/specs-for-building-a-osm-tile-server)

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
<span id="post-66372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I haves successfully built my tile server using the following <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">link</a> for UK. Now I need the my server to have the data of the entire planet. I was wondering how much memory would the database need?</p>
<p>Also, I saw that the .pfb file for the entire planet is around 50-60GB then why is the disk space required mentioned over 1TB in this <a href="/questions/11949/server-spec-for-running-osm">answer</a> ?</p>
<p>And how often is it advised to update the server from the OSM server? I see that there are daily, minutely and hourly difference updates. But if I update it once a week would it cost me more(in terms of time and disk space)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '18, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/153d30d9d12370c8532371eaaa3593b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishy91&#39;s gravatar image" />
<p><span>vishy91</span><br />
<span class="score" title="66 reputation points">66</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishy91 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Oct '18, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-66372" class="comments-container">
&#10;</div>
<div id="comment-tools-66372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66372-form-container" class="comment-form-container">
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

<span id="66373"></span>

<div id="answer-container-66373" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66373-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vishy91 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends on what kind of performance you expect. For worry-free operations I suggest 64 GB of RAM but you can make do with 48 or even 32 if you absolutely have to. As for the database usage, I suggest that you simply look at how big your database currently is, compare that to the size of the UK data file you have imported, and then extrapolate that to the size of the planet file. My guess is you'll end up at around 600 GB. Add 20% to that for index/table bloat and the necessary working space to rebuild indexes from time to time; and don't forget that OSM data also grows by about 10% per year.</p>
<p>Updating once a week would mean that the update takes a long time; perhaps up to one day. During this time your server will be slower than usual since it is very busy doing updates. If your server usage is such that you have low-use periods every day (e.g. during the night) then it could be a good idea to run daily updates because you could nicely fit them into the low-activity window.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '18, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66373" class="comments-container">
&#10;</div>
<div id="comment-tools-66373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66373-form-container" class="comment-form-container">
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

