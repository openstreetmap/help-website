+++
type = "question"
title = "Query Postgres DB for changeset comments"
description = '''I imported a metro extract from Mapzen to my DB with osm2pgsql. In the default.style I added the line:  node,waycomment text linear  and removed it from the deleted tags.  If I query now a table for the comments the following way: SELECT COUNT(*) FROM planet_osm_roads WHERE comment != &#x27;&#x27;  I get zero...'''
date = "2015-01-18T13:12:00Z"
lastmod = "2015-01-18T14:36:00Z"
weight = 40462
keywords = [ "changset", "postgresql", "tagging", "comments", "database" ]
aliases = [ "/questions/40462" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Query Postgres DB for changeset comments](/questions/40462/query-postgres-db-for-changeset-comments)

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
<span id="post-40462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40462-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported a metro extract from Mapzen to my DB with osm2pgsql. In the <code>default.style</code> I added the line:</p>
<pre><code> node,waycomment      text         linear</code></pre>
<p>and removed it from the deleted tags.</p>
<p>If I query now a table for the comments the following way:</p>
<pre><code>SELECT COUNT(*) FROM planet_osm_roads WHERE comment != &#39;&#39;</code></pre>
<p>I get zero rows:</p>
<pre><code> count 
-------
     0
(1 row)</code></pre>
<p>What do I have to do to get the rows that contain changset comments.</p>
<hr />
<p>I ultimately want to create a map that contain certain changes comment committed by me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changset" rel="tag" title="see questions tagged &#39;changset&#39;">changset</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-comments" rel="tag" title="see questions tagged &#39;comments&#39;">comments</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '15, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '15, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-40462" class="comments-container">
&#10;</div>
<div id="comment-tools-40462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40462-form-container" class="comment-form-container">
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

<span id="40465"></span>

<div id="answer-container-40465" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40465-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wasus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The generic comment tag (on objects) doesn't have anything to do with the same on changesets, nor does osm2pgsql know anything about changesets in the first place.</p>
<p>Likely the best current way to get changesets in to a database is <a href="https://github.com/ToeBee/ChangesetMD">https://github.com/ToeBee/ChangesetMD</a></p>
<p>Note that the metro extracts are unlikely to contain changesets to start with and that there is no real issue with simply using the full planet given that we are talking about a fairly small dataset. The latest full changeset dump can be obtained from <a href="http://planet.openstreetmap.org/planet/">http://planet.openstreetmap.org/planet/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '15, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '15, 15:26</strong> </span></p>
</div>
</div>
<div id="comments-container-40465" class="comments-container">
&#10;</div>
<div id="comment-tools-40465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40465-form-container" class="comment-form-container">
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

