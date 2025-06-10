+++
type = "question"
title = "Import error: could not extend file"
description = '''So I ran the Nominatim setup script to import planet data into postgres with the following command: ./utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf --all --osm2pgsql-cache 18000  And after several hours, the script failed with the following error message: Proce...'''
date = "2013-10-01T19:24:00Z"
lastmod = "2013-12-08T10:25:00Z"
weight = 26900
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/26900" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Import error: could not extend file](/questions/26900/import-error-could-not-extend-file)

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
<span id="post-26900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26900-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I ran the Nominatim setup script to import planet data into postgres with the following command:</p>
<pre><code>./utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf --all --osm2pgsql-cache 18000</code></pre>
<p>And after several hours, the script failed with the following error message:</p>
<pre><code>Processing: Node(2027272k 226.0k/s) Way(197726k 11.57k/s) Relation(0 0.00/s)COPY_END for COPY planet_osm_ways FROM STDIN;
 failed: ERROR:  could not extend file &quot;base/18495/21039.22&quot;: wrote only 4096 of 8192 bytes at block 2954348
HINT:  Check free disk space.
CONTEXT:  COPY planet_osm_ways, line 156111299: &quot;192204006      {2027680220,2027680175,2027680161,2027680104,2027680021,2027679996,2027679945,2027679899,2...&quot;
&#10;Error occurred, cleaning up
osm2pgsql SVN version 0.81.0 (64bit id space)
&#10;ERROR: Error executing external command: /postgres/OpenStreetMaps/Nominatim-2.0.1/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 18000 -d nominatim /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf
Error executing external command: /postgres/OpenStreetMaps/Nominatim-2.0.1/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 18000 -d nominatim /postgres/OpenStreetMaps/planetfile/planet-latest.osm.pbf</code></pre>
<p>I'm not sure what's going on.. something about "free disk space"? I'm working on a machine with several TB of disk space. Any help would be appreciated, thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '13, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26900" class="comments-container">
&#10;</div>
<div id="comment-tools-26900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26900-form-container" class="comment-form-container">
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

<span id="26901"></span>

<div id="answer-container-26901" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26901-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your disk might be partitioned. Make sure that you actually have ~ 700 GB of disk space available at the location where your postgresql tries to save the data to. In a standard Ubuntu setup that would be /var/lib/postgresql, so you'd want to type</p>
<pre><code>df /var/lib/postgresql</code></pre>
<p>and check that the numbers in the "Available" column is larger than 700 million.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '13, 20:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26901" class="comments-container">
<span id="26902"></span>
<div id="comment-26902" class="comment">
<div id="post-26902-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks! apparently the postgres directory only had ~60GB of space.</p>
</div>
<div id="comment-26902-info" class="comment-info">
<span class="comment-age">(01 Oct '13, 22:09)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-26901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26901-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28887"></span>

<div id="answer-container-28887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have the same problem, the mount /var/lib/postgresql has only the capacity of 10 Gb and I dont have the admin rights to increase the size. But i have an another mount where IT has over 2TB of diskspace. How do I change the configuration of postgresql to use a different mount?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '13, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/576a9cbae52513a136aca47c4f0544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ironknight&#39;s gravatar image" />
<p><span>Ironknight</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ironknight has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28887" class="comments-container">
<span id="28909"></span>
<div id="comment-28909" class="comment">
<div id="post-28909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you ought to be able to add a new tablespace using CREATE TABLESPACE bla LOCATION mount-point. The directory needs to have +x persmission for the owner of the postgres database, usually postgres. You can then make the new tablespace the default tablespace for the database or explicitly allocate tables to that tablespace.</p>
</div>
<div id="comment-28909-info" class="comment-info">
<span class="comment-age">(08 Dec '13, 10:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28887-form-container" class="comment-form-container">
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

