+++
type = "question"
title = "How to construct a GPS mobile app to calculate a new routing category?"
description = '''Hi there, I&#x27;m trying to develop a mobile application, like a GPS, but instead of only plan routes based on distance/traffic/etc , I also want to plan the best path based on my own routing type. I think I could do this with OSM services, but I don&#x27;t know how. Do you know what services should I use to...'''
date = "2014-07-26T18:13:00Z"
lastmod = "2014-07-30T00:13:00Z"
weight = 35219
keywords = [ "paths", "graph", "routing", "gps" ]
aliases = [ "/questions/35219" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How to construct a GPS mobile app to calculate a new routing category?](/questions/35219/how-to-construct-a-gps-mobile-app-to-calculate-a-new-routing-category)

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
<span id="post-35219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I'm trying to develop a mobile application, like a GPS, but instead of only plan routes based on distance/traffic/etc , I also want to plan the best path based on my own routing type. I think I could do this with OSM services, but I don't know how. Do you know what services should I use to? I think the best strategy is first - load the maps, second - convert it to a graph , third - apply weights , fourth - use routing algorithms. What do you think about it?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '14, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/b510761081a2e40ab8a7e6e398a14ec3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarlosPiedade&#39;s gravatar image" />
<p><span>CarlosPiedade</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarlosPiedade has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '14, 21:15</strong> </span></p>
</div>
</div>
<div id="comments-container-35219" class="comments-container">
&#10;</div>
<div id="comment-tools-35219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35219-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="35223"></span>

<div id="answer-container-35223" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35223-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CarlosPiedade has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if this is a question that is related to OSM. Usually I would point you to stackexchange or stackoverflow instead.</p>
<p>Anyway, first you need to specify your application on a module/component level. Here it seems to be:</p>
<ul>
<li>map rendering and interaction</li>
<li>routing strategies</li>
<li>online services (3rd party or self hosted) or offline</li>
<li>position providers</li>
</ul>
<p>Concering the <strong>routing</strong>, you should have a look at the <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">routers list</a> and pick the one who fits best. Otherwise you might try to work with an <a href="https://wiki.openstreetmap.org/wiki/Frameworks">offline framework</a> for your desired platform.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '14, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-35223" class="comments-container">
<span id="35242"></span>
<div id="comment-35242" class="comment">
<div id="post-35242-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Towards:<br />
</p>
<ol>
<li>I know that OpenRouteService supported "by safety" as criteria per routing profile<br />
</li>
<li>I don't know any routing service that publishes the routing graph -&gt; setup your own instance<br />
</li>
<li>Please see my links above<br />
</li>
<li>So you need to setup your own instance or use integrated solutions as Navit, ...</li>
</ol>
</div>
<div id="comment-35242-info" class="comment-info">
<span class="comment-age">(27 Jul '14, 15:09)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-35223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35244"></span>

<div id="answer-container-35244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35244-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO the most challenging part will be to merge the existing OSM data with the insurance data to have one common data model to work with (but please don't upload that data to OSM!). This depends quite a bit on the format you got from the insurance company (maybe you could provide some pointers to the format to get some more precise hints).</p>
<p>Usually you would start with a Geofabrik Extract of the region in question and then you need to figure out how to map the insurance data on existing OSM ways or nodes. Possibly you would add your own "safety tags" to your local OSM extract and use those artificial tags for routing decisions. Depending on your interpretation of your own tags, certain values could block a street altogether (compare to "access=no") or add a severe penalty to it (like "maxspeed=1"), so that a router will either completely ignore a way or use it with a much lower prio.</p>
<p>The rest is not really rocket science, iii already mentioned a number of pointers. OSRM, GraphHopper and BRouter come to mind, which are all fairly easily customizable to your requirements and can be made to accept your artificial tags for routing decisions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '14, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '14, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-35244" class="comments-container">
<span id="35290"></span>
<div id="comment-35290" class="comment">
<div id="post-35290-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Carlos, you’re asking allot besides OSM, a basic data scheme which enables you to build a map. If you want to go out and add accidents to a map based on OSM, please go ahead. Try to search in the hughe pile of maps based on OSM data collections, follow this link <a href="http://wiki.openstreetmap.org/wiki/List_of_OSM_based_Services">http://wiki.openstreetmap.org/wiki/List_of_OSM_based_Services</a> . Iii and mmd already pointed out some nice directions as well. To count the imported accidents you need some statistics and to import the insurance data onto your map a methode to translate it into a readable database. Did you consider to weight the accident rate by category as pedestrians and bicyclist ? And what about drunken drivers (colliding with obstacles, 1 motor vehicle only accidents) ?</p>
</div>
<div id="comment-35290-info" class="comment-info">
<span class="comment-age">(29 Jul '14, 13:36)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="35303"></span>
<div id="comment-35303" class="comment">
<div id="post-35303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Carlos, with a statistical program and a database and you’ll be able to visualize anything on a GIS related map. Add weight or minimize a group to show it. If you can’t think of any method or program follow Stephan’s advice. For instance follow this link <a href="http://karanik.webpages.auth.gr/main/images/papers/conferences/bulgaria2012.pdf">http://karanik.webpages.auth.gr/main/images/papers/conferences/bulgaria2012.pdf</a></p>
</div>
<div id="comment-35303-info" class="comment-info">
<span class="comment-age">(30 Jul '14, 00:13)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-35244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35244-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35258"></span>

<div id="answer-container-35258" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35258-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Carlos, a bit offtopic, some remarks for your your project; Pin pointing of accidents by the police isn’t perfect: The Insurance companies work with a data sheet made by civilians: Civilians even don’t know in which civil community the accident happened nor where: How do you want to reach a certain level of accuracy, based on such a database ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '14, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '14, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-35258" class="comments-container">
&#10;</div>
<div id="comment-tools-35258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35258-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35301"></span>

<div id="answer-container-35301" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35301-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you can try to visualize your basic data about accidents via <a href="http://cartodb.com">cartoDB</a>.</p>
<p>What I have seen so far, that webservice has really a lot of display features for all kinds of data on a map ... but no routing feature.</p>
<p>Did you ever had a look at <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">professional OSM service companies</a>? Maybe some of them can develop a solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '14, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-35301" class="comments-container">
&#10;</div>
<div id="comment-tools-35301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35301-form-container" class="comment-form-container">
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

