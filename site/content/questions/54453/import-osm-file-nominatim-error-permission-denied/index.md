+++
type = "question"
title = "Import osm-file nominatim error - Permission denied"
description = '''Hi, I hope I have installed nominatim successfully. But when I try to import the osm.pbf data, it gives the following error nominatim@byk-ubuntu:~/Nominatim/build$ ./utils/setup.php --osm-file /home/ybalasubramanian/Documents/germany-latest.osm.pbf --all 2&amp;gt;&amp;amp;1 | tee setup.log WARNING: resettin...'''
date = "2017-02-04T10:29:00Z"
lastmod = "2019-07-17T14:20:00Z"
weight = 54453
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/54453" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import osm-file nominatim error - Permission denied](/questions/54453/import-osm-file-nominatim-error-permission-denied)

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
<span id="post-54453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54453-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I hope I have installed nominatim successfully. But when I try to import the osm.pbf data, it gives the following error</p>
<pre><code>nominatim@byk-ubuntu:~/Nominatim/build$ ./utils/setup.php --osm-file /home/ybalasubramanian/Documents/germany-latest.osm.pbf --all 2&gt;&amp;1 | tee setup.log
WARNING: resetting threads to 1
Create DB
Setup DB
Postgres version found: 9.5
CREATE EXTENSION
CREATE EXTENSION
Postgis version found: 2.2
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
COPY 250
CREATE INDEX
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
COPY 229
CREATE INDEX
CREATE INDEX
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
COPY 25477
CREATE INDEX
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
WARNING: external UK postcode table not found.
SET
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
COPY 32387
CREATE TABLE
CREATE TYPE
Import
sh: 1: /srv/nominatim/Nominatim/build/osm2pgsql: Permission denied
ERROR: Error executing external command: /srv/nominatim/Nominatim/build/osm2pgsql -lsc -O gazetteer --hstore --number-processes 1 -C 2676 -P 5432 -d nominatim /home/ybalasubramanian/Documents/germany-latest.osm.pbf
Error executing external command: /srv/nominatim/Nominatim/build/osm2pgsql -lsc -O gazetteer --hstore --number-processes 1 -C 2676 -P 5432 -d nominatim /home/ybalasubramanian/Documents/germany-latest.osm.pbf</code></pre>
<p>I am running as the nominatim user as per the documentation. All the files inside the above folder has rights with nominatim user. I have no idea why the permission is denied</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '17, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2a95229b87eba17c63a633a8fe609aa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3yK&#39;s gravatar image" />
<p><span>3yK</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3yK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '17, 13:37</strong> </span></p>
</div>
</div>
<div id="comments-container-54453" class="comments-container">
<span id="54524"></span>
<div id="comment-54524" class="comment">
<div id="post-54524-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Discussion moved to <a href="https://github.com/twain47/Nominatim/issues/625">https://github.com/twain47/Nominatim/issues/625</a></p>
</div>
<div id="comment-54524-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 20:42)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-54453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54453-form-container" class="comment-form-container">
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

<span id="70118"></span>

<div id="answer-container-70118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi, i had the same problem on ubuntu 18.04 try fist create db nominatim via ./utils/setup.php ended with error</p>
<p>then "append" created db with data like this</p>
<pre><code>/srv/nominatim/Nominatim/build/osm2pgsql/osm2pgsql -S /srv/nominatim/Nominatim/settings/import-full.style -lsc -O gazetteer --hstore --number-processes 1 -C 2676 -P 5432 -d nominatim /home/ybalasubramanian/Documents/germany-latest.osm.pbf</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '19, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/db39bb18141038c7185abe643529b6c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdvjdv82&#39;s gravatar image" />
<p><span>jdvjdv82</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdvjdv82 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70118" class="comments-container">
&#10;</div>
<div id="comment-tools-70118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70118-form-container" class="comment-form-container">
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

