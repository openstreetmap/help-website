+++
type = "question"
title = "Got error while setup North America data in Nominatim"
description = '''hi everyone  i got the follwing error while i setuping North America data in Nominatim in ubuntu.   when i check for Disk Space it shows Available disk space on my system Filesystem Type Size Used Avail Use% Mounted on /dev/sda1 ext3 92G 58G 30G 67% / udev devtmpfs 3.9G 4.0K 3.9G 1% /dev tmpfs tmpfs...'''
date = "2014-01-31T06:36:00Z"
lastmod = "2014-01-31T09:48:00Z"
weight = 30346
keywords = [ "nominatim", "ubuntu" ]
aliases = [ "/questions/30346" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Got error while setup North America data in Nominatim](/questions/30346/got-error-while-setup-north-america-data-in-nominatim)

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
<span id="post-30346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi everyone</p>
<pre><code>                i got the follwing error while i setuping North America data in Nominatim in ubuntu.</code></pre>
<p><img src="http://help.openstreetmap.org/upfiles/Screenshot_from_2014-01-31_08-07-21-png.jpg" alt="alt text" /></p>
<p>when i check for Disk Space it shows</p>
<p>Available disk space on my system</p>
<p>Filesystem Type Size Used Avail Use% Mounted on</p>
<p>/dev/sda1 ext3 92G 58G 30G 67% /</p>
<p>udev devtmpfs 3.9G 4.0K 3.9G 1% /dev</p>
<p>tmpfs tmpfs 1.6G 1.1M 1.6G 1% /run</p>
<p>none tmpfs 5.0M 0 5.0M 0% /run/lock</p>
<p>none tmpfs 3.9G 312K 3.9G 1% /run/shm</p>
<p>/dev/sda3 ext3 353G 22G 313G 7% /home</p>
<p>if its a space problem means 30GB more data to process.</p>
<p>then i check total data occupied by nominatim in psql it show 49 GB.</p>
<p>Anybody help me get out of this issue.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '14, 06:36</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '14, 06:43</strong> </span></p>
</div>
</div>
<div id="comments-container-30346" class="comments-container">
&#10;</div>
<div id="comment-tools-30346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30346-form-container" class="comment-form-container">
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

<span id="30348"></span>

<div id="answer-container-30348" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30348-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arun kmp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A Nominatim import of North America will need about 150-200 GB of PostgreSQL storage. Your disk is too small for this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '14, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30348" class="comments-container">
<span id="30352"></span>
<div id="comment-30352" class="comment">
<div id="post-30352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you #Frederik Ramm</p>
</div>
<div id="comment-30352-info" class="comment-info">
<span class="comment-age">(31 Jan '14, 09:48)</span> <span class="comment-user userinfo">Arun kmp</span>
</div>
</div>
</div>
<div id="comment-tools-30348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30348-form-container" class="comment-form-container">
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

