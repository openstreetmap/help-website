+++
type = "question"
title = "Finding the distance between two coordinates (longitudes/latitudes) which are not found as nodes in OSM"
description = '''I intend to make my own OSM Router, and I do not want to use third party OSM routers. WHAT I HAVE DONE: I have downloaded OSM data in XML format and applied different algorithms to find the shortest path between two nodes in map using their coordinates (longitude/latitude). Everything is working fin...'''
date = "2019-09-19T17:27:00Z"
lastmod = "2019-09-20T08:18:00Z"
weight = 70849
keywords = [ "latitude", "geolocation", "geocoding", "routing", "longitude" ]
aliases = [ "/questions/70849" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding the distance between two coordinates (longitudes/latitudes) which are not found as nodes in OSM](/questions/70849/finding-the-distance-between-two-coordinates-longitudeslatitudes-which-are-not-found-as-nodes-in-osm)

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
<span id="post-70849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70849-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I intend to make my own OSM Router, and I do not want to use third party OSM routers.</p>
<p><strong><em>WHAT I HAVE DONE:</em></strong> I have downloaded OSM data in XML format and applied different algorithms to find the shortest path between two nodes in map using their coordinates (longitude/latitude). Everything is working fine.</p>
<p><strong><em>THE PROBLEM:</em></strong> The only problem is OSM XML data has only limited number of coordinates (longitude/latitude). I want to find the distance between two coordinates (longitudes/latitudes) which are not found as nodes in OSM. I could not find any thing related to this on internet.</p>
<p><strong><em>FOR INSTANCE,</em></strong> I have a random longitude/latitude for point A, and random I have a random longitude/latitude for point B. These longitudes and latitudes are not available in OSM XML data. How can I find the distance between these two points?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '19, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/5553a8c343cd8eed83e66bbb023f0a3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hk_hamzakhalid&#39;s gravatar image" />
<p><span>hk_hamzakhalid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hk_hamzakhalid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70849" class="comments-container">
&#10;</div>
<div id="comment-tools-70849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70849-form-container" class="comment-form-container">
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

<span id="70851"></span>

<div id="answer-container-70851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70851-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use your favourite search engine to search for the words "Haversine Formula", or you might also find libraries that already implement this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '19, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70851" class="comments-container">
<span id="70856"></span>
<div id="comment-70856" class="comment">
<div id="post-70856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the feeling hk was rather looking for a way to find the closest node in the routing graph and base the distance calculation on the OSM network he has already used for routing.</p>
</div>
<div id="comment-70856-info" class="comment-info">
<span class="comment-age">(20 Sep '19, 08:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-70851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70851-form-container" class="comment-form-container">
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

