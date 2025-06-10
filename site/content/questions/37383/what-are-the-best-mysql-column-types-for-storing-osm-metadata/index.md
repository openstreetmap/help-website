+++
type = "question"
title = "What are the best mysql column types for storing OSM metadata?"
description = '''I am writing a script to sync points from a site and amenity=recycling tags in OSM so I need to store OSM id, version and type in local database. What are the best column types? UNSIGNED BIGINT, UNSIGNED INT and SET? Bonus points for other metadata fields info. Extra bonus points for PostgreSQL info...'''
date = "2014-10-07T13:38:00Z"
lastmod = "2014-10-08T13:04:00Z"
weight = 37383
keywords = [ "metadata", "mysql" ]
aliases = [ "/questions/37383" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What are the best mysql column types for storing OSM metadata?](/questions/37383/what-are-the-best-mysql-column-types-for-storing-osm-metadata)

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
<span id="post-37383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37383-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am writing a script to sync points from a site and amenity=recycling tags in OSM so I need to store OSM <code>id</code>, <code>version</code> and <code>type</code> in local database. What are the best column types? <code>UNSIGNED BIGINT</code>, <code>UNSIGNED INT</code> and <code>SET</code>?</p>
<p>Bonus points for other metadata fields info.</p>
<p>Extra bonus points for PostgreSQL info.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-metadata" rel="tag" title="see questions tagged &#39;metadata&#39;">metadata</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '14, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/1aaaf77e89ed1b496cefd433400ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="int_ua&#39;s gravatar image" />
<p><span>int_ua</span><br />
<span class="score" title="275 reputation points">275</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="int_ua has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '14, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-37383" class="comments-container">
&#10;</div>
<div id="comment-tools-37383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37383-form-container" class="comment-form-container">
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

<span id="37389"></span>

<div id="answer-container-37389" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37389-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="int_ua has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unsigned bigint and smallint for the id and version. Note sure what "type" is in your case. If it's types of recycling amenities, you probably want text. If it's about way/node/relation, set looks like what you want, but it might be better to use three different tables instead.</p>
<p>The OSM community usually uses postgres instead of mysql, so you're probably better off with PG (there are many non-osm-related reasons you should do that anyway, but let's keep this to the point). The answers for pg types are pretty much the same as for mysql.</p>
<p>There are <a href="http://wiki.openstreetmap.org/wiki/Category:OSM_processing">a few tools</a> that import osm data into postgres which might interest you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '14, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '14, 16:15</strong> </span></p>
</div>
</div>
<div id="comments-container-37389" class="comments-container">
<span id="37422"></span>
<div id="comment-37422" class="comment">
<div id="post-37422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>way/node, yes.</p>
</div>
<div id="comment-37422-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 13:04)</span> <span class="comment-user userinfo">int_ua</span>
</div>
</div>
</div>
<div id="comment-tools-37389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37389-form-container" class="comment-form-container">
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

