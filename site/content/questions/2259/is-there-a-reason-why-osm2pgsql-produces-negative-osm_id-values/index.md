+++
type = "question"
title = "Is there a reason why osm2pgsql produces negative osm_id values?"
description = '''I am examining data imported into a PostGIS database with osm2pgsql and I have noticed some values in the osm_id (which I assume is unique) are negative. Is that ok?'''
date = "2011-01-18T13:28:00Z"
lastmod = "2013-09-29T05:58:00Z"
weight = 2259
keywords = [ "osm2pgsql", "osm_id" ]
aliases = [ "/questions/2259" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a reason why osm2pgsql produces negative osm_id values?](/questions/2259/is-there-a-reason-why-osm2pgsql-produces-negative-osm_id-values)

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
<span id="post-2259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2259-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am examining data imported into a PostGIS database with osm2pgsql and I have noticed some values in the osm_id (which I assume is unique) are negative. Is that ok?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '11, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/bbe97c3fa23d557d5cdaec1fef8e28db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomas%20Pajonk&#39;s gravatar image" />
<p><span>Tomas Pajonk</span><br />
<span class="score" title="191 reputation points">191</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomas Pajonk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '11, 09:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-2259" class="comments-container">
&#10;</div>
<div id="comment-tools-2259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2259-form-container" class="comment-form-container">
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

<span id="2260"></span>

<div id="answer-container-2260" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2260-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-2260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tomas Pajonk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm_id is only unique within element types in OSM database (but not in osm2pgsql schema, see the comment from pnorman below). So the same osm_id can apply to a node, a way and a relation. That's why osm2pgsql polygon table changes the sign of the relation id when it comes from relations and the original positive way id when it comes from simple closed ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '11, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '14, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-2260" class="comments-container">
<span id="2265"></span>
<div id="comment-2265" class="comment">
<div id="post-2265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-2265-info" class="comment-info">
<span class="comment-age">(18 Jan '11, 17:00)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="21130"></span>
<div id="comment-21130" class="comment">
<div id="post-21130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>More background Information is in Wiki <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema#Processed_Data">http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema#Processed_Data</a></p>
</div>
<div id="comment-21130-info" class="comment-info">
<span class="comment-age">(02 Apr '13, 14:13)</span> <span class="comment-user userinfo">geekQ</span>
</div>
</div>
<span id="26837"></span>
<div id="comment-26837" class="comment">
<div id="post-26837-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>osm_id is <strong>not</strong> unique in osm2pgsql's tables. Long ways are split by osm2pgsql into multiple rows with the same osm_id and multipolygons with distinct areas are also split into multiple rows.</p>
</div>
<div id="comment-26837-info" class="comment-info">
<span class="comment-age">(29 Sep '13, 05:58)</span> <span class="comment-user userinfo">pnorman</span>
</div>
</div>
</div>
<div id="comment-tools-2260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2260-form-container" class="comment-form-container">
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

