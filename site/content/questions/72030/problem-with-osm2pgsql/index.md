+++
type = "question"
title = "problem with Osm2pgsql"
description = '''Hello everyone, i have this problem with Osm2pgsql,  i use linux mint 18.4 32bit with 3GB RAM, Processeur intel Centrino,  osm2pgsql -d gis --create --slim -G -hstore --tag-transform -script ~/src/openstreetmap-carto/openstreetmap-carto.lua -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/da...'''
date = "2019-12-07T11:00:00Z"
lastmod = "2020-05-27T12:35:00Z"
weight = 72030
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/72030" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [problem with Osm2pgsql](/questions/72030/problem-with-osm2pgsql)

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
<span id="post-72030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, i have this problem with Osm2pgsql, i use linux mint 18.4 32bit with 3GB RAM, Processeur intel Centrino,</p>
<h1 id="osm2pgsql--d-gis---create---slim--g--hstore---tag-transform--script-srcopenstreetmap-cartoopenstreetmap-carto.lua--s-srcopenstreetmap-cartoopenstreetmap-carto.style-datamadagascar-latest.osm.pbf">osm2pgsql -d gis --create --slim -G -hstore --tag-transform -script ~/src/openstreetmap-carto/openstreetmap-carto.lua -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/madagascar-latest.osm.pbf</h1>
<p>osm2pgsql SVN version 0.88.1 (64bit id space)</p>
<p>osm2pgsql: invalid option -- 't' Osm2pgsql failed due to ERROR: Usage error. For further information see: osm2pgsql -h|--help</p>
<p>how can i do? thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '19, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a4836e5906998e180a14732b5f5a87d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacquinot&#39;s gravatar image" />
<p><span>Jacquinot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacquinot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '19, 11:00</strong> </span></p>
</div>
</div>
<div id="comments-container-72030" class="comments-container">
&#10;</div>
<div id="comment-tools-72030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72030-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="72031"></span>

<div id="answer-container-72031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72031-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you have a space between "--tag-transform" and "-script" in your call? It should be "--tag-transform-script" without a space.</p>
<p>I also see that you are using a really old version and I'm not sure about the options offered in version 0.88.</p>
<p>I would advise to use a newer version from <a href="https://www.github.com/openstreetmap/osm2pgsql">https://www.github.com/openstreetmap/osm2pgsql</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '19, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '19, 13:41</strong> </span></p>
</div>
</div>
<div id="comments-container-72031" class="comments-container">
&#10;</div>
<div id="comment-tools-72031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72034"></span>

<div id="answer-container-72034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72034-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So it does look as if you are using options that are not provided in this old version of osm2pgsql. If you would do a "osm2pgsql -h" you would see the options available for version 0.88.</p>
<p>I strongly recommend to use a newer version (see my answer above) to have lua scripting included as well as hstore options.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '19, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72034" class="comments-container">
<span id="72035"></span>
<div id="comment-72035" class="comment">
<div id="post-72035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so i remove the old version of osm2pgsql and i install the new version !!</p>
</div>
<div id="comment-72035-info" class="comment-info">
<span class="comment-age">(07 Dec '19, 14:17)</span> <span class="comment-user userinfo">Jacquinot</span>
</div>
</div>
</div>
<div id="comment-tools-72034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72034-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72033"></span>

<div id="answer-container-72033" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>it haven't space in this script</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '19, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a4836e5906998e180a14732b5f5a87d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacquinot&#39;s gravatar image" />
<p><span>Jacquinot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacquinot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '19, 13:57</strong> </span></p>
</div>
</div>
<div id="comments-container-72033" class="comments-container">
&#10;</div>
<div id="comment-tools-72033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72033-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72036"></span>

<div id="answer-container-72036" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72036-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i have i new problem after installation:</p>
<p>osm2pgsql -d gis --create --slim -G -hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/madagascar-latest.osm.pbf bash: /usr/bin/osm2pgsql: No such file or directory</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '19, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a4836e5906998e180a14732b5f5a87d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacquinot&#39;s gravatar image" />
<p><span>Jacquinot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacquinot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72036" class="comments-container">
<span id="72037"></span>
<div id="comment-72037" class="comment">
<div id="post-72037-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds like osm2pgsql is not installed where they are expected. You do need some Linux knowledge to get this working.</p>
</div>
<div id="comment-72037-info" class="comment-info">
<span class="comment-age">(07 Dec '19, 21:11)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-72036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72036-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72066"></span>

<div id="answer-container-72066" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>now i have this:</p>
<p># osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/madagascar-latest.osm.pbf osm2pgsql version 1.2.0 (64 bit id space)</p>
<p>Allocating memory for sparse node cache Node-cache: cache=2500MB, maxblocks=40000*65536, allocation method=9 Mid: pgsql, cache=2500 Connection to database failed: could not connect to server: No such file or directory Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?</p>
<p>Connection to database failed: could not connect to server: No such file or directory Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?</p>
<p>DB writer thread failed due to ERROR: Connecting to database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '19, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a4836e5906998e180a14732b5f5a87d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacquinot&#39;s gravatar image" />
<p><span>Jacquinot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacquinot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72066" class="comments-container">
&#10;</div>
<div id="comment-tools-72066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72066-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75020"></span>

<div id="answer-container-75020" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Run this command to see what version(s) of PostgreSQL are running as well as their ports, statuses &amp; data directories:</p>
<p>$ pg_lsclusters</p>
<p>If you are running PostgreSQL on a port other than 5432, many of the commands you use require the option '-p &lt;port number=""&gt;'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '20, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/707d560964d2070ca4c3c23c09aed885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TimothyOnline&#39;s gravatar image" />
<p><span>TimothyOnline</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TimothyOnline has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75020" class="comments-container">
&#10;</div>
<div id="comment-tools-75020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75020-form-container" class="comment-form-container">
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

