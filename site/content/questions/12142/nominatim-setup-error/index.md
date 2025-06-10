+++
type = "question"
title = "Nominatim setup error"
description = '''Hello, I am getting this errors bellow when I run ./setup --index, or ./setup --all --osm-file ./panet.osm What is causing the problem? I have postgresql 9.1 and postgis 1.5.4 installed. Thank You index_placex: UPDATE failed: ERROR: operator does not exist: bigint[] @&amp;gt; integer[] LINE 1: select * ...'''
date = "2012-04-18T17:45:00Z"
lastmod = "2012-04-23T19:51:00Z"
weight = 12142
keywords = [ "index", "setup", "nominatim", "db", "error" ]
aliases = [ "/questions/12142" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim setup error](/questions/12142/nominatim-setup-error)

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
<span id="post-12142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12142-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am getting this errors bellow when I run ./setup --index, or ./setup --all --osm-file ./panet.osm What is causing the problem? I have postgresql 9.1 and postgis 1.5.4 installed. Thank You</p>
<pre><code>index_placex: UPDATE failed: ERROR:  operator does not exist: bigint[] @&gt; integer[]
LINE 1: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_i...
                                                  ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
QUERY:  select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_id::integer] and members @&gt; ARRAY[&#39;n&#39;||NEW.osm_id]
CONTEXT:  PL/pgSQL function &quot;placex_update&quot; line 133 at FOR over SELECT rows
index_placex: UPDATE failed: ERROR:  operator does not exist: bigint[] @&gt; integer[]
LINE 1: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_i...
                                                  ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
QUERY:  select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_id::integer] and members @&gt; ARRAY[&#39;n&#39;||NEW.osm_id]
CONTEXT:  PL/pgSQL function &quot;placex_update&quot; line 133 at FOR over SELECT rows
index_placex: UPDATE failed: ERROR:  operator does not exist: bigint[] @&gt; integer[]
LINE 1: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_i...</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-db" rel="tag" title="see questions tagged &#39;db&#39;">db</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '12, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/975421b0b4b0acab09fca4faae4e7c69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skypik&#39;s gravatar image" />
<p><span>skypik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skypik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12142" class="comments-container">
&#10;</div>
<div id="comment-tools-12142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12142-form-container" class="comment-form-container">
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

<span id="12306"></span>

<div id="answer-container-12306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12306-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is meant here is 64-bit id space which is currently not supported with Nominatim. Make sure that in osm2pgsql <code>#define OSMID64</code> is commented out in <code>osmtypes.h</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '12, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-12306" class="comments-container">
&#10;</div>
<div id="comment-tools-12306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12306-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12152"></span>

<div id="answer-container-12152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you compile osm2pgsql with 64bit support? I had the same error and switched to 32bit</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '12, 01:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e17c2bfaed82349f7a355866ff24e4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norm1&#39;s gravatar image" />
<p><span>Norm1</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norm1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12152" class="comments-container">
<span id="12161"></span>
<div id="comment-12161" class="comment">
<div id="post-12161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I did</p>
<p>file /usr/local/bin/osm2pgsql /usr/local/bin/osm2pgsql: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.18, not stripped</p>
</div>
<div id="comment-12161-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 08:09)</span> <span class="comment-user userinfo">skypik</span>
</div>
</div>
</div>
<div id="comment-tools-12152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12152-form-container" class="comment-form-container">
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

