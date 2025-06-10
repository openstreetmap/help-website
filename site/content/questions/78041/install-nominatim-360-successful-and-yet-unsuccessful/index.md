+++
type = "question"
title = "Install nominatim 3.6.0 successful and yet unsuccessful"
description = '''Hi, just installed nominatim 3.6.0 on my machine (40 cores, 256GB RAM, 3TB Disk) with full planet.  The end of the logging on the setup.php are below: ======== WARNING: Done 147447047/147447047 in 79915 @ 1845.030 per second - FINISHED rank 30 2020-12-20 18:31:09 == Index postcodes 2020-12-20 19:33:...'''
date = "2020-12-21T14:39:00Z"
lastmod = "2020-12-21T15:10:00Z"
weight = 78041
keywords = [ "place", "nominatim", "installation", "check", "install" ]
aliases = [ "/questions/78041" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Install nominatim 3.6.0 successful and yet unsuccessful](/questions/78041/install-nominatim-360-successful-and-yet-unsuccessful)

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
<span id="post-78041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78041-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, just installed nominatim 3.6.0 on my machine (40 cores, 256GB RAM, 3TB Disk) with full planet. The end of the logging on the setup.php are below: ======== WARNING: Done 147447047/147447047 in 79915 @ 1845.030 per second - FINISHED rank 30</p>
<p>2020-12-20 18:31:09 == Index postcodes 2020-12-20 19:33:25 == Drop tables only required for updates 2020-12-20 19:33:34 == Create Search indices 2020-12-21 00:45:39 == Create search index for default country names getorcreate_country</p>
<hr />
<pre><code>        67840656</code></pre>
<p>(1 row)</p>
<h2 id="getorcreate_country">getorcreate_country</h2>
<pre><code>        67838726</code></pre>
<p>(1 row)</p>
<h2 id="count">count</h2>
<p>251 (1 row)</p>
<h2 id="count-1">count</h2>
<p>250 (1 row)</p>
<h2 id="count-2">count</h2>
<p>43100 (1 row)</p>
<p>2020-12-21 00:45:55 == /home/nominatim/build/settings/settings-frontend.php has been set up successfully Summary of warnings:</p>
<h1 id="setup-finished.">2020-12-21 00:45:55 == Setup finished.</h1>
<h1 id="as-indicated-in-the-documentation-i-run-check_import_finished.php-which-says">as indicated in the documentation, I run check_import_finished.php, which says:</h1>
<p>Checking database got created ... OK Checking nominatim.so module installed ... OK Checking place table ... Failed * The import didn't finish. Hints: * Check the output of the utils/setup.php you ran. Usually the osm2pgsql step failed. Check for errors related to * the file you imported not containing any places * harddrive full * out of memory (RAM) * osm2pgsql killed by other scripts, for consuming to much memory ========</p>
<h1 id="indeed-at-the-beginning-of-setup-we-see">Indeed, at the beginning of setup we see</h1>
<p>2020-12-18 10:24:18 == Import data 2020-12-18 11:24:18 osm2pgsql version 1.4.0 2020-12-18 11:24:18 Database version: 11.10 2020-12-18 11:24:18 Node-cache: cache=56000MB, maxblocks=896000*65536, allocation method=11 2020-12-18 11:24:18 Parsing gazetteer style file '/home/nominatim/Nominatim-3.6.0/settings/import-extratags.style'. NOTICE: table "place" does not exist, skipping</p>
<p>======== But that has not been an issue before. What might be the issue? How can I resolve the issue?</p>
<p>thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Dec '20, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9eec58c4605b0c0c76cfd1d2cb31ad80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hupa&#39;s gravatar image" />
<p><span>Hupa</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hupa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78041" class="comments-container">
&#10;</div>
<div id="comment-tools-78041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78041-form-container" class="comment-form-container">
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

<span id="78042"></span>

<div id="answer-container-78042" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you run the <code>setup.php</code> with <code>--drop</code> <a href="https://nominatim.org/release-docs/3.6.0/admin/Import/#dropping-data-required-for-dynamic-updates">https://nominatim.org/release-docs/3.6.0/admin/Import/#dropping-data-required-for-dynamic-updates</a> ? In that case the place table got deleted ("Drop tables only required for updates") and expected. The issue then is <code>utils/check_import_finished.php</code> script reporting a warning when it shouldn't. Can be ignored.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '20, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-78042" class="comments-container">
<span id="78043"></span>
<div id="comment-78043" class="comment">
<div id="post-78043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I created <a href="https://github.com/osm-search/Nominatim/issues/2117">https://github.com/osm-search/Nominatim/issues/2117</a></p>
</div>
<div id="comment-78043-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 15:10)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-78042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78042-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

