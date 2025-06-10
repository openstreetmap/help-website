+++
type = "question"
title = "Nominatim - Tuning DB Results in &quot;Out of Disk Space&quot; Error?"
description = '''I built a Nominatim Server on GCP with 128 GB of RAM and 950 GB SSD. I finished the initial import of the pbf data, created all the indexes and search indices. Now I&#x27;m trying to tune the db, but it&#x27;s saying I don&#x27;t have enough disk space. How much more disk space do I need to re-calibrate the word f...'''
date = "2020-09-15T17:14:00Z"
lastmod = "2020-09-15T21:18:00Z"
weight = 76638
keywords = [ "openstreetmaps", "nominatim", "geocoding", "geoparsing" ]
aliases = [ "/questions/76638" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - Tuning DB Results in "Out of Disk Space" Error?](/questions/76638/nominatim-tuning-db-results-in-out-of-disk-space-error)

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
<span id="post-76638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I built a Nominatim Server on GCP with 128 GB of RAM and 950 GB SSD. I finished the initial import of the pbf data, created all the indexes and search indices. Now I'm trying to tune the db, but it's saying I don't have enough disk space. How much more disk space do I need to re-calibrate the word frequencies?</p>
<p>Command:</p>
<pre><code>sudo -u $USERNAME -H sh -c &quot;$BUILD_UTILS/update.php --recompute-word-counts&quot;</code></pre>
<p>Error:</p>
<pre><code>ERROR:  could not extend file &quot;base/16386/13231037.2&quot;: wrote only 4096 of 8192 bytes at block 302206
HINT:  Check free disk space.</code></pre>
<p>Update:</p>
<p>After allocating more disk space, I'm getting this error -</p>
<pre><code>ERROR:  could not write to file &quot;base/pgsql_tmp/pgsql_tmp3657.4&quot;: No space left on device</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmaps" rel="tag" title="see questions tagged &#39;openstreetmaps&#39;">openstreetmaps</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-geoparsing" rel="tag" title="see questions tagged &#39;geoparsing&#39;">geoparsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '20, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '20, 17:37</strong> </span></p>
</div>
</div>
<div id="comments-container-76638" class="comments-container">
&#10;</div>
<div id="comment-tools-76638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76638-form-container" class="comment-form-container">
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

<span id="76639"></span>

<div id="answer-container-76639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76639-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The output will be about 7GB, I don't know how much the temporary table during the processing will take. You can delete the planet.pbf file you imported, that's no longer needed, will free 65GB on the harddrive.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76639" class="comments-container">
<span id="76640"></span>
<div id="comment-76640" class="comment">
<div id="post-76640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the lightning fast response <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>.</p>
<p>I already deleted the planet.pbf file so I would like to think that I have more than enough space left.</p>
</div>
<div id="comment-76640-info" class="comment-info">
<span class="comment-age">(15 Sep '20, 17:25)</span> <span class="comment-user userinfo">rirhun</span>
</div>
</div>
</div>
<div id="comment-tools-76639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76639-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76646"></span>

<div id="answer-container-76646" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76646-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It was a partition issue. I had to resize the partition from the VM and it seems to be ok now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76646" class="comments-container">
&#10;</div>
<div id="comment-tools-76646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76646-form-container" class="comment-form-container">
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

