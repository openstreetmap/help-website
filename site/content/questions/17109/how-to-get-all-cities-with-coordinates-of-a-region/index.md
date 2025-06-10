+++
type = "question"
title = "how to get all cities with coordinates of a region?"
description = '''Hi I imported the ism file into posture/PostGIS database. Please guide me how can I get all cities and towns of a region with coordinates (Only I need Lat &amp;amp; lon). Also How can I get all hamlet of a city or town with coordinates too. Many thanks for all people working on this great project.'''
date = "2012-10-22T19:09:00Z"
lastmod = "2012-10-22T19:42:00Z"
weight = 17109
keywords = [ "city", "postgresql", "postgis", "hamlet" ]
aliases = [ "/questions/17109" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to get all cities with coordinates of a region?](/questions/17109/how-to-get-all-cities-with-coordinates-of-a-region)

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
<span id="post-17109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I imported the ism file into posture/PostGIS database. Please guide me how can I get all cities and towns of a region with coordinates (Only I need Lat &amp; lon). Also How can I get all hamlet of a city or town with coordinates too.</p>
<p>Many thanks for all people working on this great project.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '12, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/7766d12c36b38d1bc645b33ff065142b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="usef&#39;s gravatar image" />
<p><span>usef</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="usef has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17109" class="comments-container">
&#10;</div>
<div id="comment-tools-17109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17109-form-container" class="comment-form-container">
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

<span id="17112"></span>

<div id="answer-container-17112" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17112-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="usef has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A simple approach would be (assuming you used osm2pgsql without the -l (ell) option for importing):</p>
<pre><code> select st_astext(st_transform(way, 4326)),name 
 from planet_osm_point where place=&#39;city&#39;;</code></pre>
<p>You can add a condition to limit the area, like</p>
<pre><code> ... and way &amp;&amp; st_transform(st_makebox2d(st_point(x1,y1), st_point(x2,y2)),900913):</code></pre>
<p>where x1,x2,y1,y2 are two corners of your bounding rectangle. If you want to find all suburbs within a city named "Mycity" you could do</p>
<pre><code> select st_astext(st_transform(way, 4326)),name 
 from planet_osm_point 
 where place=&#39;suburb&#39; 
 and way &amp;&amp; (select way from planet_osm_polygon 
     where boundary=&#39;administrative&#39; 
     and admin_level=&#39;8&#39; and name=&#39;Mycity&#39;);</code></pre>
<p>however this only works if the specified city boundary exists and is unique. Use `st_contains`` instead of the &amp;&amp; operator to achieve real polygon operations insead of just bounding boxes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17112" class="comments-container">
&#10;</div>
<div id="comment-tools-17112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17112-form-container" class="comment-form-container">
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

