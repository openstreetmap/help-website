+++
type = "question"
title = "Resuming failed Nominatim setup (due to no osmosis)"
description = '''On my CentOS 6 machine, I ran the command: ./Nominatim-2.0.1/utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf --all --osm2pgsql-cache 18000  to set up Nominatim, and after waiting for 3 days, it failed with the following log: Osm2pgsql took 238253s overall . .   a...'''
date = "2013-10-07T19:26:00Z"
lastmod = "2013-10-08T01:58:00Z"
weight = 26997
keywords = [ "nominatim", "osmosis" ]
aliases = [ "/questions/26997" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Resuming failed Nominatim setup (due to no osmosis)](/questions/26997/resuming-failed-nominatim-setup-due-to-no-osmosis)

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
<span id="post-26997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On my CentOS 6 machine, I ran the command:</p>
<pre><code>./Nominatim-2.0.1/utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf --all --osm2pgsql-cache 18000</code></pre>
<p>to set up Nominatim, and after waiting for 3 days, it failed with the following log:</p>
<pre><code>Osm2pgsql took 238253s overall
.
.
&#10;                         addgeometrycolumn
-------------------------------------------------------------------
 public.location_road_230.geometry SRID:4326 TYPE:GEOMETRY DIMS:2
(1 row)
&#10;CREATE INDEX
&#10;.
.
Reanalysing database...
NOTICE:   no notnull values, invalid stats
NOTICE:   no notnull values, invalid stats
ANALYZE
ERROR: please download osmosis
please download osmosis</code></pre>
<p>I had no idea that osmosis was a dependency. After I download and install osmosis, is there a way I can resume the setup process without having to start from the beginning? I'm assuming I don't have to import to postgres database anymore, because the setup failed after the output "Osm2pgsql took 238253s overall". If possible, what would the command be? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '13, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26997" class="comments-container">
&#10;</div>
<div id="comment-tools-26997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26997-form-container" class="comment-form-container">
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

<span id="27005"></span>

<div id="answer-container-27005" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27005-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can continue by using:</p>
<pre><code>./Nominatim-2.0.1/utils/setup.php --index</code></pre>
<p>However you should be aware that 2.1 (which includes a fix for this problem) has now been released. It would be recommended to do a new install using that since no more fixes or updates to 2.0.1 will be released.</p>
<p>Also, if osm2pgsql by itself took 3 days it is likely that it will take a very, very long time to index the data. You may want to look at upgrading your server with an ssd drive or seeing if you can manage with just an extract rather than the full plant.</p>
<p>Also, we always recommend doing a test install with a small extract first before trying a full plant import to check everything is installed and working.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '13, 00:05</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27005" class="comments-container">
<span id="27006"></span>
<div id="comment-27006" class="comment">
<div id="post-27006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I installed Nominatim 2.1, and now I'm having other issues. Very frustrating :/</p>
</div>
<div id="comment-27006-info" class="comment-info">
<span class="comment-age">(08 Oct '13, 01:58)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-27005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27005-form-container" class="comment-form-container">
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

