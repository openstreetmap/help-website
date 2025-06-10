+++
type = "question"
title = "Data import stuck at CREATE INDEX"
description = '''My machine has been importing North America data for the past 16 days now, which to me seems unusually slow. The output currently shows: ... CREATE INDEX CREATE INDEX CREATE INDEX  I checked what postgreSQL is doing by: postgres=# select * from pg_stat_activity; datid | datname | procpid | usesysid ...'''
date = "2013-10-28T18:13:00Z"
lastmod = "2013-10-31T04:32:00Z"
weight = 27587
keywords = [ "nominatim" ]
aliases = [ "/questions/27587" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Data import stuck at CREATE INDEX](/questions/27587/data-import-stuck-at-create-index)

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
<span id="post-27587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My machine has been importing North America data for the past 16 days now, which to me seems unusually slow. The output currently shows:</p>
<pre><code>...
CREATE INDEX
CREATE INDEX
CREATE INDEX</code></pre>
<p>I checked what postgreSQL is doing by:</p>
<pre><code>postgres=# select * from pg_stat_activity;
datid | datname  | procpid | usesysid | usename  | application_name | client_addr | client_hostname | client_port |         backend_start         |          xact_start           |          query_start          | waiting |          current_query
-------+----------+---------+----------+----------+------------------+-------------+-----------------+-------------+-------------------------------+-------------------------------+-------------------------------+---------+---------------------------------
12780 | postgres |   22028 |       10 | postgres | psql             |   |                 |          -1 | 2013-10-28 10:45:35.774566-07 | 2013-10-28 10:47:05.063072-07 | 2013-10-28 10:47:05.063072-07 | f       | select * from pg_stat_activity;
(1 row)</code></pre>
<p>Does that mean the machine is still indexing data? When can I expect the importing to finish? Thanks!</p>
<p><strong>EDIT:</strong> as one of the person answered below, I tried</p>
<pre><code>nominatim=# \d place
                Table &quot;public.place&quot;
    Column    |          Type           | Modifiers
--------------+-------------------------+-----------
 osm_type     | character(1)            | not null
 osm_id       | bigint                  | not null
 class        | text                    | not null
 type         | text                    | not null
 name         | hstore                  |
 admin_level  | integer                 |
 housenumber  | text                    |
 street       | text                    |
 addr_place   | text                    |
 isin         | text                    |
 postcode     | text                    |
 country_code | character varying(2)    |
 extratags    | hstore                  |
 geometry     | geometry(Geometry,4326) | not null
Indexes:
    &quot;idx_place_osm_unique&quot; UNIQUE, btree (osm_id, osm_type, class, type)
    &quot;place_id_idx&quot; btree (osm_type, osm_id)
Triggers:
    place_before_delete BEFORE DELETE ON place FOR EACH ROW EXECUTE PROCEDURE pl
ace_delete()
    place_before_insert BEFORE INSERT ON place FOR EACH ROW EXECUTE PROCEDURE pl
ace_insert()</code></pre>
<p>Does this mean my indexing is completed? If so, why does my pg_stat_activity still show recent timestamps?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '13, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '13, 22:40</strong> </span></p>
</div>
</div>
<div id="comments-container-27587" class="comments-container">
&#10;</div>
<div id="comment-tools-27587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27587-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="27601"></span>

<div id="answer-container-27601" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27601-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Index creation is the final step of the import and there is no explicit end-of-import message. If you don't see any activity in <code>pg_stat_activity</code> there is a good chance that you are done. The very last index to be created is <code>idx_place_osm_unique</code> on table <code>place</code>. If this index exists, the import is finished, feel free to abort the script.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '13, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27601" class="comments-container">
<span id="27602"></span>
<div id="comment-27602" class="comment">
<div id="post-27602-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How can I check the last created index?</p>
</div>
<div id="comment-27602-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 21:54)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="27604"></span>
<div id="comment-27604" class="comment">
<div id="post-27604-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Check the indexes on place by login into the database with <code>pgsql -d nominatim</code> and then listing the table with <code>\d place</code>.</p>
</div>
<div id="comment-27604-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 21:57)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="27617"></span>
<div id="comment-27617" class="comment">
<div id="post-27617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I am not confusing things, PostgreSQL will lump all the data and index creations into one transaction, therefore, logging into the database will not show anything until everything is done. In other words, no incomplete/partial data/indexes will be shown. (confirmed to be the case for the main APIDB database at least, I do not know for the nominatim operations)</p>
</div>
<div id="comment-27617-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 08:32)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="27645"></span>
<div id="comment-27645" class="comment not_top_scorer">
<div id="post-27645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I edited my question with an output. It's hard to tell if idx_place_osm_unique was actually created or not from that output.</p>
</div>
<div id="comment-27645-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 22:42)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="27646"></span>
<div id="comment-27646" class="comment">
<div id="post-27646-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can see that <code>idx_place_osm_unique</code> is listed in the Indexes section in your output. That means that the index is there. You can try your installation now by setting up the website and running a few test queries.</p>
</div>
<div id="comment-27646-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 23:06)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="27670"></span>
<div id="comment-27670" class="comment">
<div id="post-27670-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, turns out it was finished importing (or at least I think it's finished, judging by how I can query locations)</p>
</div>
<div id="comment-27670-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 22:05)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-27601" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-27601-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27589"></span>

<div id="answer-container-27589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are the hard drives lights active? CPU usage is high (PostgreSQL CPU usage is equivalent of 100% of one core)? If so, data is still being indexed. Based on my previous experience loading the whole world file, using a not so fast computer (i7 3770k, 32GB RAM, 6 independent SATA drives, each containing a tablespace of part of the full schema), the process takes a few weeks to complete.</p>
<p>However, if there is no drive activity, maybe something wrong happened. Again, in my case, there was one time that <a href="http://addictedtoosm.wordpress.com/2013/04/03/o-fim-de-uma-longa-pausa-e-outros-assuntos/">my cat</a> (in portuguese!) almost broke off one of the eSATA connectors. PostgreSQL did not crash, but drive speed plummeted to about 100kB/s. Had to interrupt the process, <a href="http://addictedtoosm.wordpress.com/2013/04/03/o-fim-de-uma-longa-pausa-e-outros-assuntos/">losing</a> (in portuguese!) <a href="http://addictedtoosm.wordpress.com/2012/10/02/frustracao/">weeks</a> of work, and restart.</p>
<p>So, in short, be very, very patient.</p>
<p>EDIT: Your "select * from pg_stat_activity" query is the only one showing in the query. If there was some index creation, there would be other lines in the result set. Repeat the query a few more times and see if anything else appears. If not, probably everything if fine, as noted by the other commenters.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '13, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '13, 01:06</strong> </span></p>
</div>
</div>
<div id="comments-container-27589" class="comments-container">
&#10;</div>
<div id="comment-tools-27589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27671"></span>

<div id="answer-container-27671" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't understand</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '13, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/df3f30604007d5822f9033b594df6733?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hainam1610&#39;s gravatar image" />
<p><span>hainam1610</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hainam1610 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27671" class="comments-container">
&#10;</div>
<div id="comment-tools-27671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27671-form-container" class="comment-form-container">
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

