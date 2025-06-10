+++
type = "question"
title = "What is the proper way to show a route and a point using OSM"
description = '''In my MS-Windows application (which could embed a browser window) I wish to show a route across the UK and a point along this route. Back ground info: 1: The application is a commercial tool that we develop for a third party 2: I am happy to convert the raw lat, long and time to any format 3: The ro...'''
date = "2012-09-20T16:34:00Z"
lastmod = "2012-09-21T01:17:00Z"
weight = 16280
keywords = [ "track", "marker", "overlay" ]
aliases = [ "/questions/16280" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the proper way to show a route and a point using OSM](/questions/16280/what-is-the-proper-way-to-show-a-route-and-a-point-using-osm)

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
<span id="post-16280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16280-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my MS-Windows application (which could embed a browser window) I wish to show a route across the UK and a point along this route.</p>
<p>Back ground info: 1: The application is a commercial tool that we develop for a third party 2: I am happy to convert the raw lat, long and time to any format 3: The route might be 500 miles along - including going over itself one or more times 4: I'd like to be able to draw a marker to represent the 'current' point 5: I'd like to be able to move/redraw the marker at another location as the user uses our application 6: This mapping feature might be used 50 times per 8 hour working day</p>
<p>What is the PROPER legal way I should proceed?</p>
<p>Many thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '12, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e29e3254127b162143163d7c152fc167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ReadiesCards&#39;s gravatar image" />
<p><span>ReadiesCards</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ReadiesCards has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16280" class="comments-container">
&#10;</div>
<div id="comment-tools-16280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16280-form-container" class="comment-form-container">
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

<span id="16295"></span>

<div id="answer-container-16295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you want some sort of service to display a map background behind a route that you plot, and possibly calculate the route as well.</p>
<p>If so, it's worth taking a step back. OSM is essentially <a href="http://help.openstreetmap.org/questions/8869/how-to-display-an-osm-map-in-a-piece-of-software/8887">just lots and lots of data</a>. It's possible to do all sorts of things with that data (e.g. <a href="http://project-osrm.org/">calculate and display routes</a>) but it's not something that you'll find hosted on the OSM website, although you will find a list of <a href="http://wiki.openstreetmap.org/wiki/List_of_OSM_based_Services">OSM-based services</a> (some free to use, some not) in the wiki.<br />
</p>
<p>OSM's servers that render the tiles that you see on maps on the OSM site have a <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">usage policy</a> designed to prevent abuse, as does the <a href="http://wiki.openstreetmap.org/wiki/API_usage_policy">API</a> that can be used to extra map data on the file.</p>
<p>You can, of course, download the data (or an <a href="http://wiki.openstreetmap.org/wiki/Extract">extract</a> of it) and do what you want with it subject to the <a href="http://www.openstreetmap.org/copyright">licence</a>, such as <a href="http://switch2osm.org/serving-tiles/">serve your own map tiles</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '12, 01:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-16295" class="comments-container">
&#10;</div>
<div id="comment-tools-16295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16295-form-container" class="comment-form-container">
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

