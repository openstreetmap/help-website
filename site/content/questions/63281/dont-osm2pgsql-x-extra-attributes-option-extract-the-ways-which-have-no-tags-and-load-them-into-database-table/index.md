+++
type = "question"
title = "don&#x27;t osm2pgsql -x|--extra-attributes option extract the ways which have no tags and load them into database table?"
description = '''I am using osm2pgsql 0.92.0,in windows, to load the osm data from a pbf file into postgresql database. First time i have loaded the data without using &quot;--extra-attributes&quot; option, and i observed that the objects which have no tags attached to them are skipped. i.e., count of nodes in &quot;planet_osm_nod...'''
date = "2018-05-03T09:27:00Z"
lastmod = "2018-05-04T10:26:00Z"
weight = 63281
keywords = [ "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/63281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [don't osm2pgsql -x|--extra-attributes option extract the ways which have no tags and load them into database table?](/questions/63281/dont-osm2pgsql-x-extra-attributes-option-extract-the-ways-which-have-no-tags-and-load-them-into-database-table)

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
<span id="post-63281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63281-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osm2pgsql 0.92.0,in windows, to load the osm data from a pbf file into postgresql database. First time i have loaded the data without using "--extra-attributes" option, and i observed that the objects which have no tags attached to them are skipped. i.e., count of nodes in "planet_osm_nodes" slim table is greater than count of points in "planet_osm_point" database table. hstore column also don't have metadata like osm_user, osm_uid, osm_timestamp, osm_changeset etc.</p>
<p>Second time i have loaded the same pbf file into another database with "--extra-attributes" option, and also i have added osm_user and osm_uid to default style file. Here I observed that all the nodes are loaded into database point table irrespective of whether a node has tags attached to it or not. i.e., count of nodes in slim table "planet_osm_nodes" is equal to count of points in database table "planet_osm_point". Table columns for the nodes which have no tags are null except osm_user and osm_uid columns. Remaining metadata like osm_timestamp, osm_changeset etc are stored in hstore column.</p>
<p>So I supposed all the ways which have no tags attached to them also would get loaded same as nodes into "planet_osm_line" table irrespective of closed way or non-closed way. But observed that these ways are not loaded. Database tables "planet_osm_line" has the ways which have tags attached only, and osm_user and osm_uid columns got filled up and the remaining metadata is stored in hstore column for all. But this table doesn't have the ways which have no tags.</p>
<p>Can anyone, who has clear understanding of slim tables and database tables as in the osm2pgsql schema, please tell me "--extra-attributes" only work with the nodes or it should work with ways as well? if the --extra-attributes option extract all the metadata and treat the nodes which have no tags as legible to put in "planet_osm_point" table then why the line table is missing the ways which have no tags? has anyone experienced the same?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '18, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3bbb39efe1f2875e439ef6145dc83ce2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phanindra&#39;s gravatar image" />
<p><span>Phanindra</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phanindra has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '18, 07:35</strong> </span></p>
</div>
</div>
<div id="comments-container-63281" class="comments-container">
<span id="63288"></span>
<div id="comment-63288" class="comment">
<div id="post-63288-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please format your question so that it is legible (paragraphs and so on). Thank you.</p>
</div>
<div id="comment-63288-info" class="comment-info">
<span class="comment-age">(03 May '18, 18:45)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="63309"></span>
<div id="comment-63309" class="comment">
<div id="post-63309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>SimonPoole, I have formatted the question. I believe it is legible now. Thanks</p>
</div>
<div id="comment-63309-info" class="comment-info">
<span class="comment-age">(04 May '18, 07:41)</span> <span class="comment-user userinfo">Phanindra</span>
</div>
</div>
</div>
<div id="comment-tools-63281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63281-form-container" class="comment-form-container">
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

<span id="63310"></span>

<div id="answer-container-63310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63310-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have to admit that I've never tried with adding extra columns in the style file, but if you have hstore enabled, the values will be added to the tags in hstore.</p>
<p>The style file controls which OSM objects are imported at all, untagged ways will typically have to be a member of an imported relation type to be included. I don't believe that there is a direct way to include other untag ways (you could try with the * wildcard for the tag), or potentially use LUA transforms.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '18, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '18, 10:30</strong> </span></p>
</div>
</div>
<div id="comments-container-63310" class="comments-container">
&#10;</div>
<div id="comment-tools-63310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63310-form-container" class="comment-form-container">
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

