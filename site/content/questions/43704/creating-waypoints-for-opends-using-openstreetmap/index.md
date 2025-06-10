+++
type = "question"
title = "Creating Waypoints for OpenDS using OpenStreetMap"
description = '''How can I use OpenStreetMap to create WayPoints for a car to follow them in a driving scenario using OpenStreetMap in OpenDS simulator?'''
date = "2015-06-22T18:26:00Z"
lastmod = "2015-06-23T08:01:00Z"
weight = 43704
keywords = [ "openstreetmap", "map", "traffic", "waypoints", "waypoint" ]
aliases = [ "/questions/43704" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating Waypoints for OpenDS using OpenStreetMap](/questions/43704/creating-waypoints-for-opends-using-openstreetmap)

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
<span id="post-43704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I use OpenStreetMap to create WayPoints for a car to follow them in a driving scenario using OpenStreetMap in OpenDS simulator?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span> <span class="post-tag tag-link-waypoint" rel="tag" title="see questions tagged &#39;waypoint&#39;">waypoint</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '15, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/6f5cb245b7cf26607eb2bae7b6d69d83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lamiastella&#39;s gravatar image" />
<p><span>lamiastella</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lamiastella has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43704" class="comments-container">
<span id="43709"></span>
<div id="comment-43709" class="comment">
<div id="post-43709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please tell us first what data format is used by OpenDS when defining such waypoints from other sources. Then we can try to find a way for OSM based data to use in OpenDS simulator.</p>
</div>
<div id="comment-43709-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 19:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-43704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43704-form-container" class="comment-form-container">
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

<span id="43718"></span>

<div id="answer-container-43718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43718-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many OSM routing engines, e.g. <a href="http://map.project-osrm.org/,">http://map.project-osrm.org/,</a> will allow you to export a GPX file after you have planned a route. Perhaps that GPX file can be loaded into OpenDS. You can either use the online version of the routing engine, or download and install the software yourself if you want to compute many routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '15, 08:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43718" class="comments-container">
&#10;</div>
<div id="comment-tools-43718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43718-form-container" class="comment-form-container">
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

