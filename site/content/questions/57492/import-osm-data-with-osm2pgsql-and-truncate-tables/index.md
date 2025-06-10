+++
type = "question"
title = "import osm data with osm2pgsql and truncate tables"
description = '''I am importing north-america osm data using osm2pgsql in slim mode. i am only importing roads data. after import the total size of the db around 45gb. most of the space is occupied by planet_osm_nodes and planet_osm_ways. I know i can use --drop option and the size will dramatically increase but tha...'''
date = "2017-08-07T14:29:00Z"
lastmod = "2017-08-07T17:56:00Z"
weight = 57492
keywords = [ "ways", "diffs", "nodes", "updates", "osm2pgsql" ]
aliases = [ "/questions/57492" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [import osm data with osm2pgsql and truncate tables](/questions/57492/import-osm-data-with-osm2pgsql-and-truncate-tables)

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
<span id="post-57492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am importing north-america osm data using osm2pgsql in slim mode. i am only importing roads data. after import the total size of the db around 45gb. most of the space is occupied by <code>planet_osm_nodes</code> and <code>planet_osm_ways</code>. I know i can use <code>--drop</code> option and the size will dramatically increase but that would not allow updating the database. Will I be able to update the database if i truncate these tables after update? i see that the updates run just fine but I think i might be missing something as i am new to the whole osm thing.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '17, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57492" class="comments-container">
&#10;</div>
<div id="comment-tools-57492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57492-form-container" class="comment-form-container">
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

<span id="57494"></span>

<div id="answer-container-57494" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57494-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aitizazk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Truncating the tables is unlikely to work.</p>
<p>What osm2pgsql does when importing is to build the geometry for the roads by going through the list of nodes in a way and building a linestring from the coordinates stored in the nodes. If the geometry of a way changes the linestring is rebuilt, this implies that osm2pgsql needs access to all the original nodes of the way and not just the ones that changed in the diff.</p>
<p>You might be able to save a bit of space by using the --flat-nodes option which stores nodes in a file instead of a database table (see <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/usage.md">https://github.com/openstreetmap/osm2pgsql/blob/master/docs/usage.md</a> ),</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '17, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '17, 18:03</strong> </span></p>
</div>
</div>
<div id="comments-container-57494" class="comments-container">
&#10;</div>
<div id="comment-tools-57494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57494-form-container" class="comment-form-container">
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

