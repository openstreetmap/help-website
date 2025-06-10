+++
type = "question"
title = "nominatim - error (my bad) with import. What now?"
description = '''Hello there, happy new year. During update (I manually update every 6-12 months) my disk was full so import failed. My postgres nominatim-db is fine (?). How should I continue? It is a problem if I re-import from geofabrik and index? (To gain space I used compression in btrfs. 100GiB free out of 0by...'''
date = "2017-12-30T21:04:00Z"
lastmod = "2018-01-04T21:08:00Z"
weight = 61422
keywords = [ "import", "nominatim", "geofabrik" ]
aliases = [ "/questions/61422" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nominatim - error (my bad) with import. What now?](/questions/61422/nominatim-error-my-bad-with-import-what-now)

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
<span id="post-61422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61422-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there, happy new year.</p>
<p>During update (I manually update every 6-12 months) my disk was full so import failed.</p>
<p>My postgres nominatim-db is fine (?). How should I continue? It is a problem if I re-import from geofabrik and index?</p>
<p>(To gain space I used compression in btrfs. 100GiB free out of 0bytes free! Some optimization is missing from postgres?)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '17, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f24afa65ec173a0eda40f0ad1e6733e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RandomGreekTracker&#39;s gravatar image" />
<p><span>RandomGreekT...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RandomGreekTracker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61422" class="comments-container">
&#10;</div>
<div id="comment-tools-61422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61422-form-container" class="comment-form-container">
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

<span id="61459"></span>

<div id="answer-container-61459" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61459-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RandomGreekTracker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As long as the database is not corrupted, you can simply restart the updates and they will pick up where they errored the last time. Check the Postgres log files for errors.</p>
<p>However, if you really only update once every 6-12 months, I strongly recommend that you simply drop the database and reimport from scratch every time. The database will remain much smaller (updates tend to bloat the database), you can update to newer versions of Nominatim (recent versions create a much smaller database), and you can use the <code>--drop</code> option during import which frees a lot of space on your disk once the import is finished.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '18, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-61459" class="comments-container">
<span id="61487"></span>
<div id="comment-61487" class="comment">
<div id="post-61487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I don't see any fatal messages in /var/log/postgreslq-X.log but I am newbie in postgresql.</p>
<p>In that case I have to build a second database, switch to second db and then delete the first. Maybe too complicated to my project, unless the gains are too high. Do you know (approx.) the difference in speed and size?</p>
<p>Currently I use compression with btrfs and it seems fine.</p>
<pre><code>compsize /db-eu-9.5/
Processed 8177 files, 7262783 regular extents (9635308 refs), 19 inline.
Type       Perc     Disk Usage   Uncompressed Referenced
Data        42%      142G         334G         292G
none       100%       56G          56G          54G
zlib        30%       86G         278G         237G
&#10;du -hs /db-eu-9.5/ 
293G    /db-eu-9.5/</code></pre>
<p>Here we have a compression party</p>
<pre><code>compsize /flat-nodes-eu 
Type       Perc     Disk Usage   Uncompressed Referenced  
Data        48%      1.6G         3.3G         2.4G       
none       100%      1.4G         1.4G         1.4G       
zlib         9%      181M         1.8G         981M
&#10;ls -lh /flat-nodes-eu 
-rw------- 1 postgres postgres 39G Ιαν   4 23:06 /flat-nodes-eu</code></pre>
</div>
<div id="comment-61487-info" class="comment-info">
<span class="comment-age">(04 Jan '18, 21:08)</span> <span class="comment-user userinfo">RandomGreekT...</span>
</div>
</div>
</div>
<div id="comment-tools-61459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61459-form-container" class="comment-form-container">
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

