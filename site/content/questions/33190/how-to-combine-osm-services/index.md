+++
type = "question"
title = "How to combine OSM Services"
description = '''Hello all, As mentioned in my previous question I am currently trying to set my own OSM-Server instance including website, API and Tile Server. In this context I also want to set up an own Overpass and Nominatim, which hopefully be done tomorrow. My problem is that I don&#x27;t have a clear idea of how t...'''
date = "2014-05-15T02:21:00Z"
lastmod = "2014-05-15T07:35:00Z"
weight = 33190
keywords = [ "mapserver", "api", "combine", "tileserver" ]
aliases = [ "/questions/33190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to combine OSM Services](/questions/33190/how-to-combine-osm-services)

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
<span id="post-33190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33190-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,<br />
As mentioned in <a href="/questions/33178/accessing-data-by-using-own-instance-of-osm-api-06">my previous question</a> I am currently trying to set my own OSM-Server instance including website, API and Tile Server. In this context I also want to set up an own Overpass and Nominatim, which hopefully be done tomorrow. My problem is that I don't have a clear idea of how to combine those services to "one application". Up to now the website is up and running and I also have a working Tile-Server machine including the dataset and the database with my relevant data. In my case the data for the Tile server cover only one city but this is enough for my use case.<br />
</p>
<p>Now my questions are:<br />
1.) How can I combine both services (the website rails port and Tile-Server)? I would like to be able to query data using the API on my local server. As mentioned in the answer of my <a href="/questions/33178/accessing-data-by-using-own-instance-of-osm-api-06">my previous question</a> it's necessary to have a own database so the local port of the API can access the data.<br />
2.) Apart from querying the data using the API, how can I change the map source to my Tile-Sever. I've checked the source code, but I did not find the right line, where I could change it.</p>
<p>Thanks for your input!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-combine" rel="tag" title="see questions tagged &#39;combine&#39;">combine</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '14, 02:21</strong></p>
<img src="https://secure.gravatar.com/avatar/6fc6f0ce6b15926034073d61c76482fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schlomm&#39;s gravatar image" />
<p><span>schlomm</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schlomm has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33190" class="comments-container">
&#10;</div>
<div id="comment-tools-33190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33190-form-container" class="comment-form-container">
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

<span id="33193"></span>

<div id="answer-container-33193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33193-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>1.) You have to dump your API database into a "planet file" using Osmosis, and then load that file into a different PostGIS database with osm2pgsql, and run your tile server off of that database. If your data set is very small then you can make a complete dump and re-import any time you change something, or else set up a "diff" mechanism that only dumps and processes changes.</p>
<p>2.) The tile layers are defined in <code>vendor/assets/leaflet/leaflet.osm.js</code> - you can simply add your own to the list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '14, 07:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33193" class="comments-container">
&#10;</div>
<div id="comment-tools-33193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33193-form-container" class="comment-form-container">
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

