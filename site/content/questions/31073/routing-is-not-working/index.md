+++
type = "question"
title = "Routing is not working"
description = '''Greetings, currently i am building an android indoor navigation app for my university. I am using osmdroid and osmbonuspack for routing. The problem is when i want to see the route path, it gives me straight line. I does not follow the road/path.   I follow exactly on how to draw indoor map from osm...'''
date = "2014-02-27T09:06:00Z"
lastmod = "2014-03-01T07:49:00Z"
weight = 31073
keywords = [ "josm", "android", "indoor", "osmdroid", "routing" ]
aliases = [ "/questions/31073" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Routing is not working](/questions/31073/routing-is-not-working)

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
<span id="post-31073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings, currently i am building an android indoor navigation app for my university. I am using <a href="https://code.google.com/p/osmdroid/">osmdroid</a> and <a href="https://code.google.com/p/osmbonuspack/">osmbonuspack</a> for routing. The problem is when i want to see the route path, it gives me straight line. I does not follow the road/path.</p>
<p><img src="http://help.openstreetmap.org/upfiles/Screenshot_2014-02-27-15-25-32.png" alt="alt text" /></p>
<p>I follow exactly on how to draw indoor map from <a href="http://wiki.openstreetmap.org/wiki/IndoorOSM">osm wiki for Indoor Mappping</a> Do I need to upload a routing layer from JOSM? Is there any possibility having error from the tiles that i downloaded from Mapnik? Do i need to have KML file? Do i need to include GPX ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '14, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/fa67c029cb445775d328af8be7e8ddcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firdaus%20shajahan&#39;s gravatar image" />
<p><span>firdaus shaj...</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firdaus shajahan has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-31073" class="comments-container">
&#10;</div>
<div id="comment-tools-31073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31073-form-container" class="comment-form-container">
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

<span id="31085"></span>

<div id="answer-container-31085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31085-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, your problem is still with the mapping initially. The question as to whether your routing engine will work is secondary. For a routing engine to work the mapping has to be correct.</p>
<p>As was stated to your previous question, (I now forget where that was posted) the linear ways/paths must be linked to the overall map, in a manner consistent with conventional mapping. I see that you have now added ways external to the building and thereby tried to join up the internal ways to the rest of the world. Unfortunately you mapping is not adequate. The circular path/roundabout and the four ways radiating from this have been duplicated, (one way added then another placed exactly on top of the first both with identical tags. This duplication will definitely foul up a routing engine <a href="http://tools.geofabrik.de/osmi/?view=routing&amp;lon=101.73041&amp;lat=3.25398&amp;zoom=18">please see here the problems to the date at foot of the page.</a></p>
<p>Once the mapping is corrected you could try this <a href="http://www.yournavigation.org/">routing page</a> which IMHO will test out your mapping as regards its routing capabilities. You can also see on this page that your ways are not connected to the rest of the map, because they are not yet accepted on the database as real ways.</p>
<p>Regards Bernard</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '14, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '14, 13:36</strong> </span></p>
</div>
</div>
<div id="comments-container-31085" class="comments-container">
<span id="31086"></span>
<div id="comment-31086" class="comment">
<div id="post-31086-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and one other thought to add to the answer above, perhaps you could try seeming if foot routing works in your app works somewhere else? Perhaps here, at little to the south in KL itself:</p>
<p><a href="http://tools.geofabrik.de/osmi/?view=routing&amp;lon=101.69480&amp;lat=3.14294&amp;zoom=18">http://tools.geofabrik.de/osmi/?view=routing&amp;lon=101.69480&amp;lat=3.14294&amp;zoom=18</a></p>
</div>
<div id="comment-31086-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 13:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="31089"></span>
<div id="comment-31089" class="comment">
<div id="post-31089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The question is about indoor mapping. The connection to the external world is secondary.</p>
</div>
<div id="comment-31089-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 14:18)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="31096"></span>
<div id="comment-31096" class="comment">
<div id="post-31096-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>South KL also not working.</p>
</div>
<div id="comment-31096-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 16:31)</span> <span class="comment-user userinfo">firdaus shaj...</span>
</div>
</div>
<span id="31098"></span>
<div id="comment-31098" class="comment">
<div id="post-31098-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have tried set different coordinate to check whether the Route engine really working or not. Found out that,it is not working. the route path still show straight line.</p>
</div>
<div id="comment-31098-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 16:33)</span> <span class="comment-user userinfo">firdaus shaj...</span>
</div>
</div>
<span id="31099"></span>
<div id="comment-31099" class="comment not_top_scorer">
<div id="post-31099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Pieren</span> Not if the used routing engine strips of all ways that are not reachable from the outside, which seems to be the case for OSRM.</p>
</div>
<div id="comment-31099-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 16:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31128"></span>
<div id="comment-31128" class="comment">
<div id="post-31128-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Having more time I have inspected your duplicated ways. Six of the eight ways (four ways duplicated equals eight), had either the start or end node unconnected.</p>
<p>I have removed the duplicates and joined up all ways.</p>
</div>
<div id="comment-31128-info" class="comment-info">
<span class="comment-age">(01 Mar '14, 07:49)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-31085" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-31085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31079"></span>

<div id="answer-container-31079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31079-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mapping seems okay. The problem is probably more on the routing engine (so your question is not really relevant for this help website). Anyway, check how osmbonuspack is working. A quick look reveals that the framework is calling third party OSM routing API's, either from MapquestOpen or OSRM. Your problem is probably that both engines are not supporting "pedestrians" routing (through "highway=footway" ways) but rather more for motor vehicules routing (through "highway=primary|secondary|tertiary|motorway|residential|etc" ways).</p>
<p>You should check if OSRM is eventually supporting other types of transportations (cars or bikes or pedestrians) and if yes, check how it can be specified in the OSRM API calls and ask or adapt the framework osmbonuspack accordingly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '14, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '14, 13:26</strong> </span></p>
</div>
</div>
<div id="comments-container-31079" class="comments-container">
&#10;</div>
<div id="comment-tools-31079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31079-form-container" class="comment-form-container">
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

