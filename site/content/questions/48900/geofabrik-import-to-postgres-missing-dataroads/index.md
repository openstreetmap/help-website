+++
type = "question"
title = "GEOFABRIK Import to Postgres Missing Data/Roads"
description = '''I&#x27;ll first start by saying that I&#x27;m new to the GIS world. I apologize if this has been posted before but I tried searching a lot and couldn&#x27;t find the answer. Maybe I&#x27;m searching the wrong terms. I am playing around with visualizing some traffic information. I&#x27;ve been using GEOFABRIK to download lar...'''
date = "2016-03-29T15:33:00Z"
lastmod = "2016-03-31T22:45:00Z"
weight = 48900
keywords = [ "import", "geofabrik", "missing" ]
aliases = [ "/questions/48900" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [GEOFABRIK Import to Postgres Missing Data/Roads](/questions/48900/geofabrik-import-to-postgres-missing-dataroads)

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
<span id="post-48900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48900-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'll first start by saying that I'm new to the GIS world. I apologize if this has been posted before but I tried searching a lot and couldn't find the answer. Maybe I'm searching the wrong terms.</p>
<p>I am playing around with visualizing some traffic information. I've been using GEOFABRIK to download large data sets for OSM (which I believe is the suggested way of doing it). So I'll download an entire state in the US (like Michigan) in the .osm.pbf format. Next, I use a standard osm2pgsql command to import all the data into a postgres gis db.</p>
<pre><code>osm2pgsql --create --latlong --slim --drop  -U myusername -d gis wisconsin-latest.osm.pbf</code></pre>
<p>All this seems to go fine. Imports run well. I am now trying to run some select statements to check on the data that has been loaded. It seems to me that many of the smaller side streets are missing from this data but are present in the OSM main site. For example, the way/road with Way: Ontario Road (21447015) (<a href="http://www.openstreetmap.org/way/21447015">http://www.openstreetmap.org/way/21447015</a>)</p>
<p>But a query of:</p>
<pre><code>select * from planet_osm_roads where osm_id=21447015;</code></pre>
<p>results in 0 rows.</p>
<p>I feel like I'm just missing something. Does anyone have any guidance? I seem to be missing a lot of these side roads (which seem to exist on the OSM site). Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '16, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '16, 15:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-48900" class="comments-container">
&#10;</div>
<div id="comment-tools-48900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48900-form-container" class="comment-form-container">
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

<span id="48901"></span>

<div id="answer-container-48901" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48901-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sbryfcz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "roads" table is a misnomer and should really be called "stuff we likely draw on lower zoom levels". <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/tagtransform.cpp#L38-L54">https://github.com/openstreetmap/osm2pgsql/blob/master/tagtransform.cpp#L38-L54</a> determines what gets stored in the roads table - residential roads aren't! You will find them in <code>planet_osm_line</code>. (The roads table is a subset of the line table.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '16, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48901" class="comments-container">
<span id="48982"></span>
<div id="comment-48982" class="comment">
<div id="post-48982-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks a ton. Changed that 1 table name and everything worked perfect.</p>
</div>
<div id="comment-48982-info" class="comment-info">
<span class="comment-age">(31 Mar '16, 22:45)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
</div>
<div id="comment-tools-48901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48901-form-container" class="comment-form-container">
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

