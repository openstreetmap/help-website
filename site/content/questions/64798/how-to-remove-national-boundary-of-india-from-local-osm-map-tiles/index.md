+++
type = "question"
title = "How to remove National boundary of India from local OSM Map tiles?"
description = '''I have set local OSM Map server for Map of India using mod tiles. I want to remove National Boundary from map. How to do it?'''
date = "2018-07-19T13:32:00Z"
lastmod = "2018-07-20T07:26:00Z"
weight = 64798
keywords = [ "national", "admin_boundary" ]
aliases = [ "/questions/64798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove National boundary of India from local OSM Map tiles?](/questions/64798/how-to-remove-national-boundary-of-india-from-local-osm-map-tiles)

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
<span id="post-64798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64798-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set local OSM Map server for Map of India using mod tiles. I want to remove National Boundary from map. How to do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national" rel="tag" title="see questions tagged &#39;national&#39;">national</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '18, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64798" class="comments-container">
&#10;</div>
<div id="comment-tools-64798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64798-form-container" class="comment-form-container">
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

<span id="64799"></span>

<div id="answer-container-64799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64799-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have several options:</p>
<ol>
<li>Identify the boundary in a LUA script which processes data as it is loaded into your database using osm2pgsql.</li>
<li>Use osmosis and a tag-transform to change one or more tags associated with the boundary, for instance remove or alter admin_level or boundary=administrative</li>
<li>If you wish to avoid reloading your database, it gets a bit trickier. One way would be to create a view on the polygon table to filter out the Indian boundary. The view would have to be named planet_osm_polygon, which in turn means that the base table names would all need changing which would likely make further incremental loads tricky if the renaming is not spot on. (I don't think it is possible with PostgreSQL to manage views owned by different users as one might do with Oracle - or at least when I've tried this I didn't get it to work, because of permissions on sys tables IIRC).</li>
<li>Change the SQL statement which downloads the boundaries in the Carto-CSS file to filter out the India boundary. You then need to recompile to raw mapnik.</li>
<li>Create a trigger on the planet_osm_polygon table which alters one or more of admin_level or boundary columns on INSERT and UPDATE.</li>
<li>Pre-filter your data with osmfilter, which requires pbf-&gt;o5m conversion with osmconvert.</li>
</ol>
<p>If you are content with a database reload I would use one of the first two, with a preference for the first. Of course you can do a manual intervention on the database table now as long as your update processes ensure that the polygon is ignored or not added as a national boundary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '18, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-64799" class="comments-container">
<span id="64810"></span>
<div id="comment-64810" class="comment">
<div id="post-64810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems to be difficult. Isn't there a simple way to do this?</p>
</div>
<div id="comment-64810-info" class="comment-info">
<span class="comment-age">(20 Jul '18, 07:26)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-64799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64799-form-container" class="comment-form-container">
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

