+++
type = "question"
title = "pull out osm file from postgres database"
description = '''Hey, is it possible to pull out a .osm file from a postgres database. ive got osm data inputted inside a postgresql datbase on my linux server, is it now possible to pull that data out into an osm file Thanks in advance :)'''
date = "2021-01-27T13:02:00Z"
lastmod = "2021-01-28T09:40:00Z"
weight = 78541
keywords = [ "openstreetmap", "osm", "postgresql", "postgres", "linux" ]
aliases = [ "/questions/78541" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pull out osm file from postgres database](/questions/78541/pull-out-osm-file-from-postgres-database)

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
<span id="post-78541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, is it possible to pull out a .osm file from a postgres database. ive got osm data inputted inside a postgresql datbase on my linux server, is it now possible to pull that data out into an osm file Thanks in advance :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '21, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78541" class="comments-container">
&#10;</div>
<div id="comment-tools-78541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78541-form-container" class="comment-form-container">
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

<span id="78544"></span>

<div id="answer-container-78544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78544-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have imported with osm2pgsql or imposm then the answer is no, you can never go back to the original OSM file because metadata has been lost. You could possibly write code to generate a "pseudo" OpenSteetMap XML but how you would do that, and how useful it would be, depends on the data structure in your PostgreSQL and on what you want to do with the resulting OSM file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '21, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78544" class="comments-container">
<span id="78546"></span>
<div id="comment-78546" class="comment">
<div id="post-78546-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i have imported using osmosis API DB would it be possible with that</p>
</div>
<div id="comment-78546-info" class="comment-info">
<span class="comment-age">(27 Jan '21, 14:07)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
<span id="78548"></span>
<div id="comment-78548" class="comment">
<div id="post-78548-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>yes, it's just a reverse of the write to api-db <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48#--read-apidb-current_.28--rdcur.29">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48#--read-apidb-current_.28--rdcur.29</a></p>
</div>
<div id="comment-78548-info" class="comment-info">
<span class="comment-age">(27 Jan '21, 14:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="78563"></span>
<div id="comment-78563" class="comment">
<div id="post-78563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik for the insight, Also SK53 solution has allowed me to create an osm file from an API DB, for anyone who is looking for a command</p>
<blockquote>
<p>sudo osmosis --read-apidb-current host="localhost" database="openstreetmap" user="xxxx" password="xxx" validateSchemaVersion="no" --write-pbf file="file path of where you want it saved and the file type /home/export.osm.pbf"</p>
</blockquote>
</div>
<div id="comment-78563-info" class="comment-info">
<span class="comment-age">(28 Jan '21, 09:40)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
</div>
<div id="comment-tools-78544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78544-form-container" class="comment-form-container">
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

