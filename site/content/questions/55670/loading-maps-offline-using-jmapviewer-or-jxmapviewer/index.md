+++
type = "question"
title = "Loading maps offline using JMapViewer or JXMapViewer"
description = '''Hi, I&#x27;m new to openstreetmap and working with maps overall. I&#x27;m a developer and I&#x27;m trying to figure out what is the best way to load map on my Java application using either JMapViewer or JXMapViewer. Someone did created some java classes to allow JMapViewer to load tiles offline and render them, bu...'''
date = "2017-04-18T03:48:00Z"
lastmod = "2017-04-19T00:50:00Z"
weight = 55670
keywords = [ "map", "offline", "vector" ]
aliases = [ "/questions/55670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Loading maps offline using JMapViewer or JXMapViewer](/questions/55670/loading-maps-offline-using-jmapviewer-or-jxmapviewer)

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
<span id="post-55670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm new to openstreetmap and working with maps overall. I'm a developer and I'm trying to figure out what is the best way to load map on my Java application using either JMapViewer or JXMapViewer. Someone did created some java classes to allow JMapViewer to load tiles offline and render them, but I'm not sure exactly how to get the "tiles". I'm still learning about the difference between raster and vectors. I would rather use vectors than raster, but I can't seem to be able to figure out how to load vectors files offline to JMapViewer or JXMapViewer. I thought about setting up my own tile server like tile.openstreetmap.org and only load the countries I want to use at a time. Then use JXMapViewer to connect to my tile server and get the maps I want. But I can't find any sources on how to setup a tile server. All I want to do is to be able to load a map, zoom in and out and add marker points on the map all offline. Any thoughts?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '17, 03:48</strong></p>
<img src="https://secure.gravatar.com/avatar/edbf10029172f8204f531c279a931c83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David2047&#39;s gravatar image" />
<p><span>David2047</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David2047 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '17, 03:49</strong> </span></p>
</div>
</div>
<div id="comments-container-55670" class="comments-container">
&#10;</div>
<div id="comment-tools-55670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55670-form-container" class="comment-form-container">
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

<span id="55671"></span>

<div id="answer-container-55671" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not a programmer but a little Java app called GPS Prune that is open source does something very similar. It may help you see how they do it. <a href="https://activityworkshop.net/software/gpsprune/">https://activityworkshop.net/software/gpsprune/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '17, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '17, 07:00</strong> </span></p>
</div>
</div>
<div id="comments-container-55671" class="comments-container">
<span id="55688"></span>
<div id="comment-55688" class="comment">
<div id="post-55688-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Andy, unfortunately this is not what I'm looking for. GPS Prune is connecting to other tile server which provide the OSM tiles to render a map. What I'm looking for is to get some instructions on how to setup my own tile server that I can use with JMapViewer or JXMapViewer. Another way I'm looking for is how to load tiles from a file into JXMapViewer. But I just don't know where I can get tiles that I can use with JXMapViewer or how to setup a tile server for that matter. Thanks for the help though!</p>
</div>
<div id="comment-55688-info" class="comment-info">
<span class="comment-age">(19 Apr '17, 00:50)</span> <span class="comment-user userinfo">David2047</span>
</div>
</div>
</div>
<div id="comment-tools-55671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55671-form-container" class="comment-form-container">
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

