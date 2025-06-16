+++
type = "question"
title = "Extract single points of interest from OSM when described both as nodes and ways"
description = '''I extracted both nodes and ways from OpenStreetMap in PostgreSQL with Osmosis. I&#x27;m looking for all restaurants in a given area. The issue is that some of them are coded in OSM as nodes and others as ways. How is it possible to have only one point when it is represented both as a node and a way? The ...'''
date = "2014-04-14T17:14:00Z"
lastmod = "2014-04-17T13:33:00Z"
weight = 32366
keywords = [ "centroid", "postgresql", "osmosis" ]
aliases = [ "/questions/32366" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extract single points of interest from OSM when described both as nodes and ways](/questions/32366/extract-single-points-of-interest-from-osm-when-described-both-as-nodes-and-ways)

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
<span id="post-32366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32366-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I extracted both nodes and ways from <a href="http://openstreetmap.org/">OpenStreetMap</a> in PostgreSQL with <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>. I'm looking for all restaurants in a given area. The issue is that some of them are coded in OSM as nodes and others as ways.</p>
<p>How is it possible to have only one point when it is represented both as a node and a way?</p>
<p>The intuitive answer is to intersect the ways with the nodes. If a node is inside a way, they will both count as one. Otherwise, if there is only a node or only a way without nodes inside, it's fine.</p>
<p>The 'geometry' column in the 'ways' table does not contain information (it has something like a geometry, but all values are similar). Or maybe it is possible to use the 'nodes' table?</p>
<p>The fundamental question is: How is it possible to have a proper geometry column in PostgreSQL with Osmosis?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centroid" rel="tag" title="see questions tagged &#39;centroid&#39;">centroid</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '14, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/65da3e87020b1932ba6fc144a74394f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antonind&#39;s gravatar image" />
<p><span>antonind</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antonind has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 18:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-32366" class="comments-container">
&#10;</div>
<div id="comment-tools-32366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32366-form-container" class="comment-form-container">
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

<span id="32371"></span>

<div id="answer-container-32371" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32371-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-32371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="antonind has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alternatively, use osm2pgsql which builds geometries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '14, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32371" class="comments-container">
<span id="32378"></span>
<div id="comment-32378" class="comment">
<div id="post-32378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do you do tag-filtering with osm2pgsql? I guess via a style file. If I'm not interested in some key, I just delete them from the style file?</p>
</div>
<div id="comment-32378-info" class="comment-info">
<span class="comment-age">(15 Apr '14, 10:02)</span> <span class="comment-user userinfo">antonind</span>
</div>
</div>
<span id="32379"></span>
<div id="comment-32379" class="comment">
<div id="post-32379-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should be able to do that with <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/README_lua.md">lua tag transformations</a>.</p>
</div>
<div id="comment-32379-info" class="comment-info">
<span class="comment-age">(15 Apr '14, 10:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32380"></span>
<div id="comment-32380" class="comment">
<div id="post-32380-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But just deleting lines in the style file wouldn't do the thing?</p>
</div>
<div id="comment-32380-info" class="comment-info">
<span class="comment-age">(15 Apr '14, 10:38)</span> <span class="comment-user userinfo">antonind</span>
</div>
</div>
<span id="32393"></span>
<div id="comment-32393" class="comment">
<div id="post-32393-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes it would work; the only thing you can't do in the style file is saying "I want highway=A but not highway=B". You can only say that you want, or don't want, highway.</p>
</div>
<div id="comment-32393-info" class="comment-info">
<span class="comment-age">(16 Apr '14, 21:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="32409"></span>
<div id="comment-32409" class="comment">
<div id="post-32409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It worked perfectly by just removing some lines in the style file and using 'osm2pgsql -S default.style --host=something.com --username myUsername --password --database myDB switzerland-latest.osm.pbf</p>
</div>
<div id="comment-32409-info" class="comment-info">
<span class="comment-age">(17 Apr '14, 13:33)</span> <span class="comment-user userinfo">antonind</span>
</div>
</div>
</div>
<div id="comment-tools-32371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32371-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32368"></span>

<div id="answer-container-32368" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32368-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The general understand is already ok.</p>
<p>For the postprocessing you might want to derive a own table/db as it's a custom procedure that depends on your own needs:</p>
<ul>
<li>you want just the node holding all (maybe merged) metainformation</li>
<li>you might want to be able to determine the original OSM object (might be nessary for updates etc)</li>
</ul>
<p>I guess you can do the processing just using PGSQL, but I would recommend e.g. a python script that:</p>
<ol>
<li>Creates a new table</li>
<li>Add all nodes as lat/lon point geoms, maybe with additional fields for address, www, ...</li>
<li>Find all restaurant closed ways (any maybe just building=*)
<ol>
<li>Check if existing lat/lon points lay within this shape -&gt; Flag shape as "processed"</li>
<li>if not, calculate centeroid of that shape and add it in your point table</li>
</ol></li>
</ol>
<p>Sorry, I can't provide code, but maybe this will be helpful if you decide to do it the Python way: <a href="http://conference.scipy.org/scipy2013/tutorial_detail.php?id=110">http://conference.scipy.org/scipy2013/tutorial_detail.php?id=110</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '14, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-32368" class="comments-container">
&#10;</div>
<div id="comment-tools-32368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32368-form-container" class="comment-form-container">
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

