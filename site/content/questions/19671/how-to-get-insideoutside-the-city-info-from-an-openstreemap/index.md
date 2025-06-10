+++
type = "question"
title = "How to get inside/outside the city info from an OpenStreeMap?"
description = '''Hello,  Is there a way to get information about the current zone from OpenStreetMap shapefile ? I mean, I need info whether I am inside the city or outside the city. Is there an attribute that I could use for that ?'''
date = "2013-02-07T11:11:00Z"
lastmod = "2013-02-07T22:43:00Z"
weight = 19671
keywords = [ "shapefile" ]
aliases = [ "/questions/19671" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get inside/outside the city info from an OpenStreeMap?](/questions/19671/how-to-get-insideoutside-the-city-info-from-an-openstreemap)

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
<span id="post-19671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, Is there a way to get information about the current zone from OpenStreetMap shapefile ? I mean, I need info whether I am inside the city or outside the city. Is there an attribute that I could use for that ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '13, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a61464568d94365860d078ae876156ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LukaszP&#39;s gravatar image" />
<p><span>LukaszP</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LukaszP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19671" class="comments-container">
<span id="19672"></span>
<div id="comment-19672" class="comment">
<div id="post-19672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>LukaszP, could you tell more about this question ? What do you mean by the city limits, administration borders or other limits ? And secondly what the apparatus youre using ? Greetz</p>
</div>
<div id="comment-19672-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 11:33)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-19671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19671-form-container" class="comment-form-container">
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

<span id="19678"></span>

<div id="answer-container-19678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the gheofabrik shapefiles (assuming you use geofabrik shapes) there is no easy way, as they don't contain admin boundaries.</p>
<p>If you had a shapefile with each city as a polygon you could use standard GIS Software (e.g. QGis, ArcGIS) or command line OGR tools (don't know which, though) to determine if your point is inside the "city" polygon.</p>
<p>What's your application/use for the information? Maybe there is a better way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-19678" class="comments-container">
<span id="19679"></span>
<div id="comment-19679" class="comment">
<div id="post-19679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>city limits : e.g. rural or urban, it's something like administration borders</p>
<p>I've found Tag:boundary=administrative, does it mean that when the value of admin_level = 8 then i'm inside the city, and &lt;&gt; 8 means outside ?</p>
<p>I am using <a href="http://downloads.cloudmade.com/">http://downloads.cloudmade.com/</a> to get shapefiles. One shapefile per country, not per city.</p>
</div>
<div id="comment-19679-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 12:40)</span> <span class="comment-user userinfo">LukaszP</span>
</div>
</div>
<span id="19717"></span>
<div id="comment-19717" class="comment">
<div id="post-19717-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Lukasz, just a hint: data downloads from cloudmade.com seem to be very outdated, from December 2011!</p>
<p>Have a look at <a href="http://geofabrik.de">http://geofabrik.de</a> ... they offer up-to-date data files.</p>
</div>
<div id="comment-19717-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 22:43)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-19678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19678-form-container" class="comment-form-container">
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

