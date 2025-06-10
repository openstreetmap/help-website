+++
type = "question"
title = "PostGIS: Load Only OSM Lines and Polygons Using osm2pgsql"
description = '''I&#x27;m using OSM2PgSQL to load osm data into my PostGIS db. I am shortage of space and also do not need the entire data to be loaded. I only want to load osm_lines and osm_polygons. How can I configure this? Any other import tool which would help me accomplish this would do as well.'''
date = "2017-08-26T10:27:00Z"
lastmod = "2017-08-27T20:18:00Z"
weight = 58822
keywords = [ "osm2pgsql", "postgis" ]
aliases = [ "/questions/58822" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PostGIS: Load Only OSM Lines and Polygons Using osm2pgsql](/questions/58822/postgis-load-only-osm-lines-and-polygons-using-osm2pgsql)

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
<span id="post-58822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58822-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using OSM2PgSQL to load osm data into my PostGIS db. I am shortage of space and also do not need the entire data to be loaded. I only want to load osm_lines and osm_polygons. How can I configure this?</p>
<p>Any other import tool which would help me accomplish this would do as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '17, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/85d97df64f090abb5cfb29a669e37913?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ones%20Infinite&#39;s gravatar image" />
<p><span>Ones Infinite</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ones Infinite has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '17, 20:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-58822" class="comments-container">
&#10;</div>
<div id="comment-tools-58822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58822-form-container" class="comment-form-container">
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

<span id="58839"></span>

<div id="answer-container-58839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58839-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to edit the default.style file to only import what you are interested in and drop the slim mode tables once you've imported. In any case you will still be initially importing nodes because they are required for building the geometries (and given that most OSM nodes are actually way nodes it is going to be nearly all of them).</p>
<p>With other words at least temporarily you will need more space or lots of memory to be able to run osm2pgsql in non-slim mode.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '17, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '17, 20:19</strong> </span></p>
</div>
</div>
<div id="comments-container-58839" class="comments-container">
&#10;</div>
<div id="comment-tools-58839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58839-form-container" class="comment-form-container">
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

