+++
type = "question"
title = "Missing Timestamp in osm2pgsql import"
description = '''I am importing data into PostgreSQL using osm2pgsql, and want to include the osm_timestamp data. I&#x27;ve updated my style file, and used the --extra-attributes and --hstore-all flags, which gives me timestamp data in my planet_osm_nodes and planet_osm_line` tables, but not in the polygon or points tabl...'''
date = "2018-07-30T19:41:00Z"
lastmod = "2018-07-31T23:27:00Z"
weight = 65029
keywords = [ "timestamps", "osm2pgsql" ]
aliases = [ "/questions/65029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing Timestamp in osm2pgsql import](/questions/65029/missing-timestamp-in-osm2pgsql-import)

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
<span id="post-65029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am importing data into PostgreSQL using osm2pgsql, and want to include the osm_timestamp data. I've updated my style file, and used the <code>--extra-attributes</code> and <code>--hstore-all</code> flags, which gives me timestamp data in my <code>planet_osm_nodes</code> and planet_osm_line` tables, but not in the polygon or points tables. How can I get the timestamp data to appear in those tables?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/5640c5ba887bd91e0e741412ec2064fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsoyka-radiant&#39;s gravatar image" />
<p><span>gsoyka-radiant</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsoyka-radiant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65029" class="comments-container">
<span id="65041"></span>
<div id="comment-65041" class="comment">
<div id="post-65041-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which version of osm2ogsql are you using?</p>
</div>
<div id="comment-65041-info" class="comment-info">
<span class="comment-age">(31 Jul '18, 18:06)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="65042"></span>
<div id="comment-65042" class="comment">
<div id="post-65042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm running <code>osm2pgsql SVN version 0.88.1</code></p>
</div>
<div id="comment-65042-info" class="comment-info">
<span class="comment-age">(31 Jul '18, 19:12)</span> <span class="comment-user userinfo">gsoyka-radiant</span>
</div>
</div>
</div>
<div id="comment-tools-65029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65029-form-container" class="comment-form-container">
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

<span id="65047"></span>

<div id="answer-container-65047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65047-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>0.88.1 is something like 3 years old. I haven't checked specifically for that version, but older osm2pgsql version only supported importing timestamps from XML format data and not from PBF files. More recent version use a third party OSM data parsing library and should support timestamps from PBF.</p>
<p>Note: the 0.9* version have changes in the database schema and you will have to re-import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '18, 23:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '18, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-65047" class="comments-container">
&#10;</div>
<div id="comment-tools-65047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65047-form-container" class="comment-form-container">
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

