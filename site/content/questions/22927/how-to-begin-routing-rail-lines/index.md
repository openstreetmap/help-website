+++
type = "question"
title = "How to begin routing rail lines?"
description = '''I&#x27;d like to be able to plot routes between rail stations (non-commuter, primarily transportation lines). However, I don&#x27;t understand enough about the OpenStreetMap stack to know where to begin. I&#x27;ve read that the rail lines are stored as GPX data, and that it&#x27;s available in raw format to those who w...'''
date = "2013-05-31T16:57:00Z"
lastmod = "2013-06-04T14:08:00Z"
weight = 22927
keywords = [ "railway", "gpx", "routing", "rails" ]
aliases = [ "/questions/22927" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to begin routing rail lines?](/questions/22927/how-to-begin-routing-rail-lines)

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
<span id="post-22927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22927-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to be able to plot routes between rail stations (non-commuter, primarily transportation lines). However, I don't understand enough about the OpenStreetMap stack to know where to begin. I've read that the rail lines are stored as GPX data, and that it's available in raw format to those who wish to do something with them. So my questions are:</p>
<p>1.) Is it currently possible to route between rail stations on rail lines in OpenStreetMap without third party tools (I assume this is not the case). 2.) Is the rail line data available as GPX data, and if not, what format? 3.) Is there a well known or generally accepted way to route between rail stations, or is there a third party tool that uses/integrates with OpenStreetMap?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '13, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/bb5982f667c0ae8f60bc1b512363f33b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sparticus&#39;s gravatar image" />
<p><span>sparticus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sparticus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22927" class="comments-container">
&#10;</div>
<div id="comment-tools-22927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22927-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="22930"></span>

<div id="answer-container-22930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22930-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could try creating a "railway" config for one of the existing osm routing engine like <a href="http://project-osrm.org/">OSRM</a>, but that doesn't deal with the train schedules, wether they're direct or omnibus, etc. If you use the train schedule data (which isn't something provided by OSM), you'd probably need an approach quite different from a routing engine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 17:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-22930" class="comments-container">
<span id="22950"></span>
<div id="comment-22950" class="comment">
<div id="post-22950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OP's request for "non-commuter, primarily transportation lines" suggests that he's less interested in schedules, however.</p>
</div>
<div id="comment-22950-info" class="comment-info">
<span class="comment-age">(02 Jun '13, 08:54)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22930-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22931"></span>

<div id="answer-container-22931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22931-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data is usually not in GPX format but in a <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">own XML format</a>. You can <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">downloaded OSM data in various ways</a>. It is also possible to download smaller <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extracts</a> or only specific data using for example the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. In your case you are interested in <a href="https://wiki.openstreetmap.org/wiki/Elements">elements</a> with <a href="https://wiki.openstreetmap.org/wiki/Railways">railroad related tags</a>, especially the <a href="https://wiki.openstreetmap.org/wiki/Key:railway">railway key</a>. For routing there a several <a href="https://wiki.openstreetmap.org/wiki/Routing">online and offline routers</a> available. You will have to modify them if you want to route on railways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22931" class="comments-container">
<span id="22948"></span>
<div id="comment-22948" class="comment">
<div id="post-22948-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>While quite a hack, it is possible to get by without modifying the routing engine - by modifying the data. Get an extract of all railway lines, and re-write the tags so that they look like roads, then feed them to a router.</p>
</div>
<div id="comment-22948-info" class="comment-info">
<span class="comment-age">(01 Jun '13, 23:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="22991"></span>
<div id="comment-22991" class="comment">
<div id="post-22991-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... with an extra turn restriction at every set of points (switches) I suspect :-)</p>
</div>
<div id="comment-22991-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 17:18)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="22998"></span>
<div id="comment-22998" class="comment">
<div id="post-22998-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To be honest, if you're using OSRM, it's easier to modify the routing engine - by supplying a new lua profile - than to hack the data. OSRM actively encourages you to do that. Andy's point about turn restrictions can be trivially achieved by modifying the turn_function to return very high penalties for turns over (say) 45°.</p>
</div>
<div id="comment-22998-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 21:43)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22931-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23004"></span>

<div id="answer-container-23004" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23004-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you for instance look for tram line "1" in Vienna, you could get all the objects necessary to draw it via <a href="http://overpass-turbo.eu/s/ic">this overpass query</a>.</p>
<p>Is this what you are looking for?</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '13, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-23004" class="comments-container">
&#10;</div>
<div id="comment-tools-23004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23004-form-container" class="comment-form-container">
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

