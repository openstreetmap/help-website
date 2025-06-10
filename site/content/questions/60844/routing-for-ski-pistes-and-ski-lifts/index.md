+++
type = "question"
title = "Routing for Ski Pistes and Ski Lifts"
description = '''OpenStreetMap (OSM) includes data about ski pistes, however current routing engines, such as Open Source Routing Machine (OSRM), GraphHopper, Brouter etc., do not provide routes for pistes. I want to have routes for ski pistes and ski lifts for a ski resort in Chamrousse, France. Here is my scenario...'''
date = "2017-11-28T17:56:00Z"
lastmod = "2017-11-30T09:58:00Z"
weight = 60844
keywords = [ "development", "osrm", "ski", "routing", "graphhopper" ]
aliases = [ "/questions/60844" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing for Ski Pistes and Ski Lifts](/questions/60844/routing-for-ski-pistes-and-ski-lifts)

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
<span id="post-60844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60844-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OpenStreetMap (OSM) includes data about ski pistes, however current routing engines, such as Open Source Routing Machine (OSRM), GraphHopper, Brouter etc., do not provide routes for pistes.</p>
<p>I want to have routes for ski pistes and ski lifts for a ski resort in Chamrousse, France.</p>
<p>Here is my scenario: <em>A user will provide his current location and the destination point where he/she wants to go. Additionally, he/she will provide his/her level of expertise (e.g., difficulty of pistes), i.e., beginner, intermediate and expert. Subsequently, I should accordingly recommend multiple routes with novice, easy, intermediate or advanced pistes (based on the user's expertise), so that the user can choose one of the route he/she wants to take. <strong>It is important to note that I am only interested in routing for just one ski resort in Chamrousse, France.</strong></em></p>
<p>The problem is that to the best of my knowledge, none of the existing routing engines, such as OSRM, GraphHopper and Brouter provide this feature because they do not consider ski pistes data. Although <a href="http://www.opensnowmap.org/?zoom=15&amp;lat=45.1214&amp;lon=5.90133">OpenSnowMap</a> provides ski pistes routing functionality, but it is very basic one which does not meets my requirements.<br />
I am seeing two possiblities: (1) Modify existing open source routing engine (OSRM, GraphHopper or Brouter) and include the consideration of ski pistes and ski lifts based on my requirements or (2) Develop my own simple routing engine for ski pistes and ski lifts.</p>
<p>I want some suggestions, opinions and recommendations from experts. If modifying existing routing engine would be a better choice, then I will prefer to modify GraphHopper or Brouter (but I have no idea about them) because I am working in Java and these routing engines are also developed in Java. But if required, I can also switch to other programming language (e.g., C/C++ for OSRM).</p>
<p>I have good programming experience but I am very new to GIS and I only want this ski pistes and ski lifts routing functionality for Chamrousse ski resort in France. I would really appreciate if experts can also provide me some starting steps to start my development for option (1) or (2) which you will recommend. Many thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-ski" rel="tag" title="see questions tagged &#39;ski&#39;">ski</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '17, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9c57ef58dc4c0f205c99f8ab6b5d04c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yasir&#39;s gravatar image" />
<p><span>yasir</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yasir has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '17, 20:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-60844" class="comments-container">
<span id="60845"></span>
<div id="comment-60845" class="comment">
<div id="post-60845-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/263348/routing-for-ski-pistes-and-ski-lifts">https://gis.stackexchange.com/questions/263348/routing-for-ski-pistes-and-ski-lifts</a></p>
</div>
<div id="comment-60845-info" class="comment-info">
<span class="comment-age">(28 Nov '17, 18:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60844-form-container" class="comment-form-container">
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

<span id="60879"></span>

<div id="answer-container-60879" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the pistes are provided as ways it should be possible to configure any of the routers mentioned to route over piste+aerialway (aka lifts)+the normal stuff, however your will need to install one the engines yourself and change the setup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '17, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-60879" class="comments-container">
<span id="60884"></span>
<div id="comment-60884" class="comment">
<div id="post-60884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you want multiple weights on each arc of the graph for different skiing abilities, the Contraction Hierarchy routers are probably not appropriate (OSRM and Graphhopper with contraction hierarchies option). I'd probably try with Graphhopper and try adding pistes to something like the walker profile as a starting point.</p>
</div>
<div id="comment-60884-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 09:58)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60879-form-container" class="comment-form-container">
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

