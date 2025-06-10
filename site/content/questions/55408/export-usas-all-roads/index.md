+++
type = "question"
title = "Export USA&#x27;s all roads"
description = '''I was wondering how can I export all the roads (car drivable ones) of USA from OSM? To export it with the website I need to specify some boundaries, but I need only USA&#x27;s road (and obviously USA&#x27;s border is not a rectangle). The same is when I try to export it from QGIS&#x27;s using OpenLayers plugin and...'''
date = "2017-04-01T07:38:00Z"
lastmod = "2017-04-25T03:40:00Z"
weight = 55408
keywords = [ "export", "road", "usa" ]
aliases = [ "/questions/55408" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export USA's all roads](/questions/55408/export-usas-all-roads)

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
<span id="post-55408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55408-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was wondering how can I export all the roads (car drivable ones) of USA from OSM? To export it with the website I need to specify some boundaries, but I need only USA's road (and obviously USA's border is not a rectangle). The same is when I try to export it from QGIS's using OpenLayers plugin and also with overpass-turbo. My final goal is to import it into POSTGIS or QGIS. I am sure this is something trivial, but I am new to OSM and can't figure it out.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-usa" rel="tag" title="see questions tagged &#39;usa&#39;">usa</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '17, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b51e052c84a1cbfd9a233ff100cc8771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lianna94&#39;s gravatar image" />
<p><span>Lianna94</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lianna94 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55408" class="comments-container">
&#10;</div>
<div id="comment-tools-55408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55408-form-container" class="comment-form-container">
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

<span id="55415"></span>

<div id="answer-container-55415" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55415-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For such a large region you should download an extract and filter out the roads:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Regional_extract_sources">http://wiki.openstreetmap.org/wiki/Planet.osm#Regional_extract_sources</a></p>
<p>There are a variety of OSM specific tools that can do this filtering as they load data into a database:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs">http://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '17, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55415" class="comments-container">
<span id="55461"></span>
<div id="comment-55461" class="comment">
<div id="post-55461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and see <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> for its features.</p>
</div>
<div id="comment-55461-info" class="comment-info">
<span class="comment-age">(03 Apr '17, 21:08)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-55415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55533"></span>

<div id="answer-container-55533" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55533-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>You can download the Shape files from the following link and then extract only the roads.</p>
<p><a href="http://download.geofabrik.de/north-america.html">http://download.geofabrik.de/north-america.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '17, 07:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-55533" class="comments-container">
<span id="55841"></span>
<div id="comment-55841" class="comment">
<div id="post-55841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks mmahmud, but how can I merge them after? Or it doesn't make sense to merge them because of the size?</p>
</div>
<div id="comment-55841-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 01:38)</span> <span class="comment-user userinfo">Lianna94</span>
</div>
</div>
<span id="55844"></span>
<div id="comment-55844" class="comment">
<div id="post-55844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, merging with what? What is the ultimate goal here? And did the extraction work?</p>
</div>
<div id="comment-55844-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 03:40)</span> <span class="comment-user userinfo">mmahmud</span>
</div>
</div>
</div>
<div id="comment-tools-55533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55533-form-container" class="comment-form-container">
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

