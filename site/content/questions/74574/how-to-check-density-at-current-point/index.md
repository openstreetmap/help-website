+++
type = "question"
title = "How to check density at current point?"
description = '''I need to know the population or buildings density at current point. I see there is a tag &quot;population&quot; and osm-analytics.org, but how can I ask in js to get information about the density, say 1km2 around some chosen point? Thanks!'''
date = "2020-05-03T19:04:00Z"
lastmod = "2020-05-04T21:24:00Z"
weight = 74574
keywords = [ "analytics", "density" ]
aliases = [ "/questions/74574" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to check density at current point?](/questions/74574/how-to-check-density-at-current-point)

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
<span id="post-74574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to know the population or buildings density at current point. I see there is a tag "population" and osm-analytics.org, but how can I ask in js to get information about the density, say 1km2 around some chosen point? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-analytics" rel="tag" title="see questions tagged &#39;analytics&#39;">analytics</span> <span class="post-tag tag-link-density" rel="tag" title="see questions tagged &#39;density&#39;">density</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '20, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/b52d2a609c4afd95fff41c3ae8c812f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jujo0&#39;s gravatar image" />
<p><span>jujo0</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jujo0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74574" class="comments-container">
&#10;</div>
<div id="comment-tools-74574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74574-form-container" class="comment-form-container">
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

<span id="74583"></span>

<div id="answer-container-74583" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74583-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jujo0 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you want to read about the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>, for this kind of queries.</p>
<p>Please use <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">overpass turbo</a> to test your queries.</p>
<p>This <a href="https://overpass-turbo.eu/s/TAP">query</a> will return all the buildings in the viewing bbox. I leave you to calculate a fitting 1km bounding box around some point. Don't forget that in urban areas, it will mean a lot of data !</p>
<p>If you don't need the geometry of each building, <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Center">center</a> will help you, like in this <a href="https://overpass-turbo.eu/s/TAS">query</a>. Overpass is a very powerful language...</p>
<p>Some background in this <a href="https://gis.stackexchange.com/questions/239492/finding-residential-buildings-with-overpass-turbo">question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '20, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74583" class="comments-container">
<span id="74584"></span>
<div id="comment-74584" class="comment">
<div id="post-74584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-74584-info" class="comment-info">
<span class="comment-age">(03 May '20, 20:53)</span> <span class="comment-user userinfo">jujo0</span>
</div>
</div>
<span id="74587"></span>
<div id="comment-74587" class="comment">
<div id="post-74587-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem. Please mark the answer as accepted if it suits you.</p>
<p>Don't hesitate to ask more specific questions later.</p>
</div>
<div id="comment-74587-info" class="comment-info">
<span class="comment-age">(03 May '20, 22:08)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="74613"></span>
<div id="comment-74613" class="comment">
<div id="post-74613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to make a rectangle, +/-0.0018 deg (~200m) from some point, but poly keeps on being triangular. Is it a normal behaviour? My query looks like this (I must have changed dots to commas for the code to appear normally): <code>[out:json][timeout:25]; // gather results ( // query part for: “building” way["building"](poly:"52.209156623640474 18.2667298038213 52.245156623640476 18.2667298038213 52.209156623640474 18.230729803821298 52.209156623640474 18.2667298038213"); //relation["building"](poly:"52.22661090011143 18.259625256876017 52.22661090011143 18.25602525687602 52.22661090011143 18.259625256876017 52.23021090011144 18.259625256876017"); ); out center;</code></p>
</div>
<div id="comment-74613-info" class="comment-info">
<span class="comment-age">(04 May '20, 21:17)</span> <span class="comment-user userinfo">jujo0</span>
</div>
</div>
<span id="74614"></span>
<div id="comment-74614" class="comment">
<div id="post-74614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand your problem, I guess the code isn't complete. The simplest is to Share an url to overpass turbo IMHO.</p>
<p>But I would have computed the bounding box in JS, before creating the query.</p>
</div>
<div id="comment-74614-info" class="comment-info">
<span class="comment-age">(04 May '20, 21:24)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-74583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74583-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74577"></span>

<div id="answer-container-74577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74577-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>Short answer is, the information is not in OSM.</p>
<p>The tag population is mostly here to know how to sort the cities, to show the biggest ones' labels first. It's usually not really up-to-date or precise.</p>
<p>You could make an educated guess from the number (and size) of buildings, but you'll have to filter out non-residential buildings.</p>
<p>I'm afraid you'll have to turn to other sources for your query.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '20, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74577" class="comments-container">
<span id="74582"></span>
<div id="comment-74582" class="comment">
<div id="post-74582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could I somehow get the info about buildings including non-residential ones at some certain point, 1x1km square?</p>
</div>
<div id="comment-74582-info" class="comment-info">
<span class="comment-age">(03 May '20, 20:39)</span> <span class="comment-user userinfo">jujo0</span>
</div>
</div>
</div>
<div id="comment-tools-74577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74577-form-container" class="comment-form-container">
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

