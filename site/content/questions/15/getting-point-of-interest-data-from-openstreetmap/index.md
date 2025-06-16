+++
type = "question"
title = "Getting point of interest data from OpenStreetMap"
description = '''Is it possible, say, for an independent developer to extract a list of &quot;landmarks&quot; (churches, museums, squares, ...) from OSM? (Question originally asked on IRC)'''
date = "2010-07-07T10:34:00Z"
lastmod = "2011-03-25T10:23:00Z"
weight = 15
keywords = [ "data", "poi" ]
aliases = [ "/questions/15" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting point of interest data from OpenStreetMap](/questions/15/getting-point-of-interest-data-from-openstreetmap)

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
<span id="post-15-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15-score" class="post-score" title="current number of votes">
15
</div>
<span id="post-15-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
5
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible, say, for an independent developer to extract a list of "landmarks" (churches, museums, squares, ...) from OSM? <em>(Question originally asked on IRC)</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '10, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-15" class="comments-container">
&#10;</div>
<div id="comment-tools-15" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15-form-container" class="comment-form-container">
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

<span id="16"></span>

<div id="answer-container-16" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16-score" class="post-score" title="current number of votes">
23
</div>
<span id="post-16-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Richard has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap has millions of points of interest which will serve you well for this. These are "nodes" (points) each tagged with a set of keywords that indicate what each point is. For example, you might have a node with latitude 51.398, longitude -1.082, and tags <code>amenity=place_of_worship</code>, <code>name=St Mary's Church</code>. This indicates that there's a church called St Mary's Church at that lat and long.</p>
<p>So you need to get this data out of OSM. The first step is to identify which tags you're interested in. You might want, for example, everything tagged as a church: in other words, everything with <code>amenity=place_of_worship</code>. (The first part of the tag is the 'key', the second the 'value'. You can see a long list of common OSM tags <a href="https://wiki.openstreetmap.org/wiki/Map_Features">on our wiki</a>.)</p>
<p>There are two ways you can get this data out of the OSM database.</p>
<p>One is by using <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass</a>, a separate API with a powerful query language which allows you to fetch data matching certain tags.</p>
<p>The second is to download the OpenStreetMap data dump and filter it according to your needs. The data dump is called <a href="https://wiki.openstreetmap.org/wiki/Planet">planet.osm</a>. You can either download the whole world (really huge), or just an extract covering one country or state.</p>
<p>Once you've downloaded it, you can use <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a> to extract the data for you, and output it into a file. Alternatively, you can load all the data into a local database with Osmosis or osm2pgsql, and then query the database for the features you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '10, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '20, 15:55</strong> </span></p>
</div>
</div>
<div id="comments-container-16" class="comments-container">
<span id="47"></span>
<div id="comment-47" class="comment">
<div id="post-47-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Especially in well-mapped parts of the world, points of interest may also be available as "areas" (closed sequences of nodes) instead of nodes. The tags are the same as you would find on nodes, but if you want a single latitude/longitude pair you need to calculate it from the area outline!</p>
</div>
<div id="comment-47-info" class="comment-info">
<span class="comment-age">(10 Jul '10, 13:19)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-16" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4066"></span>

<div id="answer-container-4066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4066-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I <a href="/questions/4065/getting-specific-poi-data-and-keeping-them-up-to-date">posted a follow-up question</a> that outlines the process of filtering specific data from a planet file. It may contain information useful to those interested in this topic. Also, I hope to get best practices on how to keep a POI database up-to-date once you have it set up, which is what my question is about.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '11, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4066" class="comments-container">
&#10;</div>
<div id="comment-tools-4066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4066-form-container" class="comment-form-container">
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

