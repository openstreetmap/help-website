+++
type = "question"
title = "How to download data bus stations with locations (POI)?"
description = '''Hi, thank you for any help. How do download bus stations with geolocation? I need list bus stations and to geolocations (POI).  For example:  Ginnheim, 50.1405127, 8.646109; Niddapark, 50.1438225, 8.6421729; Römerstadt, 50.1533931, 8.6381724; Nordwestzentrum, 50.1579072, 8.6347154; Heddernheimer Lan...'''
date = "2014-10-02T13:29:00Z"
lastmod = "2014-10-08T04:25:00Z"
weight = 37216
keywords = [ "geolocation", "station", "database", "location", "poi" ]
aliases = [ "/questions/37216" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to download data bus stations with locations (POI)?](/questions/37216/how-to-download-data-bus-stations-with-locations-poi)

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
<span id="post-37216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37216-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, thank you for any help. How do download bus stations with geolocation? I need list bus stations and to geolocations (POI).</p>
<p>For example: Ginnheim, 50.1405127, 8.646109; Niddapark, 50.1438225, 8.6421729; Römerstadt, 50.1533931, 8.6381724; Nordwestzentrum, 50.1579072, 8.6347154; Heddernheimer Landstraße, 50.1637958, 8.6348233; ...</p>
<p>This is done manually.</p>
<p>I need a list automatically. <a href="http://www.openstreetmap.org/relation/387071">http://www.openstreetmap.org/relation/387071</a></p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '14, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2b1482b234beb60ef035b76ccf842790?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="houmerope&#39;s gravatar image" />
<p><span>houmerope</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="houmerope has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Oct '14, 15:10</strong> </span></p>
</div>
</div>
<div id="comments-container-37216" class="comments-container">
&#10;</div>
<div id="comment-tools-37216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37216-form-container" class="comment-form-container">
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

<span id="37228"></span>

<div id="answer-container-37228" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37228-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="houmerope has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With this Overpass query <a href="http://overpass-turbo.eu/s/5ha">http://overpass-turbo.eu/s/5ha</a> , you can download all bus stops. I've tried to include both the old tagging scheme (highway=bus_stop) and the newer (public transport). Maybe you have to tweak the query a bit for your needs. The data can be downloaded in a number of formats.</p>
<p>I hope this helps</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '14, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-37228" class="comments-container">
<span id="37236"></span>
<div id="comment-37236" class="comment">
<div id="post-37236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great I need an advice. I entered... &lt;query type="node"&gt; &lt;has-kv k="railway" v="halt"/&gt; &lt;bbox-query {{bbox}}=""/&gt; &lt;/query&gt;</p>
<p>I wanted to find all U bahn stations, but the script found S-bahn stops too. Is there a script that lists only the session?</p>
<p>Session: U-Bahn Frankfurt (Main) (168034)</p>
</div>
<div id="comment-37236-info" class="comment-info">
<span class="comment-age">(02 Oct '14, 21:12)</span> <span class="comment-user userinfo">houmerope</span>
</div>
</div>
<span id="37245"></span>
<div id="comment-37245" class="comment">
<div id="post-37245-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Dear houmerope,</p>
<p>as you want to work with data from Germany, maybe you are also german speaking ...</p>
<p>in this case I would recommend to ask further more detailed questions about getting certain data via any api at the high-traffic German subforum at <a href="http://forum.openstreetmap.org">http://forum.openstreetmap.org</a> ... be welcome there!</p>
<p>Use your OSM account like on this FAQ site to log in there.</p>
</div>
<div id="comment-37245-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 08:41)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="37249"></span>
<div id="comment-37249" class="comment">
<div id="post-37249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is that correct? (rel(387071);&gt;&gt;)-&gt;.a;(node.a[highway=bus_stop]; node.a[railway=halt]; node.a[railway=tram_stop]; &gt;;); out meta; (rel(172258);&gt;&gt;)-&gt;.a;(node.a[highway=bus_stop]; node.a[railway=halt]; node.a[railway=tram_stop]; &gt;;); out meta; (rel(168034);&gt;&gt;)-&gt;.a;(node.a[highway=bus_stop]; node.a[railway=halt]; node.a[railway=tram_stop]; &gt;;); out meta;</p>
<p>what is node.a[public_transport~"^(stop_position|platform)$"] ?? Thanks</p>
</div>
<div id="comment-37249-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 08:59)</span> <span class="comment-user userinfo">houmerope</span>
</div>
</div>
<span id="37251"></span>
<div id="comment-37251" class="comment">
<div id="post-37251-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>all nodes that are either a tagged with public_transport=stop_position or public_transport=platform | stands for "or" ;<br />
"^" for start of the string; $ for end of the string</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/Public_transport">new tagging schema</a> for public transport does not use the highway=bus_stop notation.</p>
</div>
<div id="comment-37251-info" class="comment-info">
<span class="comment-age">(03 Oct '14, 09:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="37396"></span>
<div id="comment-37396" class="comment">
<div id="post-37396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a problem..</p>
<p>I need a lot of sessions and overpass turbo show me the error that there is much.</p>
<p>One relation - (rel(3335256);&gt;&gt;)-&gt;.a;(node.a[highway=bus_stop]; node.a[railway=halt]; node.a[railway=tram_stop]; node.a[railway=station];&gt;;); out meta;</p>
<p>How do I make multiple relations?</p>
<p>Problem is in <a href="http://wiki.openstreetmap.org/wiki/Finland:Helsinki/Joukkoliikenne">http://wiki.openstreetmap.org/wiki/Finland:Helsinki/Joukkoliikenne</a></p>
<p>Public transport in Helsinki has not one relation but very much. Do you know of any solutions ? Thank you</p>
</div>
<div id="comment-37396-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 18:09)</span> <span class="comment-user userinfo">houmerope</span>
</div>
</div>
<span id="37401"></span>
<div id="comment-37401" class="comment not_top_scorer">
<div id="post-37401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you need all public transport information without a city border, it might be better to search for all such items within the city in one query. I'm not sure about the syntax, but it is possible to search within an area</p>
</div>
<div id="comment-37401-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 04:25)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-37228" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-37228-form-container" class="comment-form-container">
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

