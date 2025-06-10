+++
type = "question"
title = "How to find the distance values in osm file?"
description = '''I am designing the android mobile application project using java. I downloaded the map from http://downloads.cloudmade.com/ . I got infromation (lat &amp;amp; lon) of each node but there is no information about distance value. I am facing the problem to calculate the shortest path. These day I found the...'''
date = "2012-03-19T08:16:00Z"
lastmod = "2018-05-23T17:41:00Z"
weight = 11313
keywords = [ "distance", "android" ]
aliases = [ "/questions/11313" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to find the distance values in osm file?](/questions/11313/how-to-find-the-distance-values-in-osm-file)

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
<span id="post-11313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am designing the android mobile application project using java. I downloaded the map from <a href="http://downloads.cloudmade.com/">http://downloads.cloudmade.com/</a> . I got infromation (lat &amp; lon) of each node but there is no information about distance value. I am facing the problem to calculate the shortest path. These day I found the possible solution but it is still confused.</p>
<p>Here is the website seems to be useful: <a href="http://wiki.openstreetmap.org/wiki/Distance_maps#Checking_routing_connectivity_of_an_OSM_file">http://wiki.openstreetmap.org/wiki/Distance_maps#Checking_routing_connectivity_of_an_OSM_file</a> . But I cannot find the ROUTE.OSM from the cloudmade.com</p>
<p>As I know, the well-known method is Dijkstra's algorithm. Is there any existing method to get the shortest path between nodes under android development environment ?</p>
<p>Many Thanks!!!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0b422a6f9fbd98c28ce45107ad89a604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yenyip&#39;s gravatar image" />
<p><span>yenyip</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yenyip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '12, 08:32</strong> </span></p>
</div>
</div>
<div id="comments-container-11313" class="comments-container">
<span id="11396"></span>
<div id="comment-11396" class="comment">
<div id="post-11396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please elaborate. What exactly do you want to compute?</p>
<ul>
<li>The shortest path between two variable nodes</li>
<li>The shortest path between one fixed and one variable node?</li>
<li>The shortest path between one fixed and “all” points?</li>
</ul>
</div>
<div id="comment-11396-info" class="comment-info">
<span class="comment-age">(21 Mar '12, 20:35)</span> <span class="comment-user userinfo">hfs</span>
</div>
</div>
<span id="11453"></span>
<div id="comment-11453" class="comment">
<div id="post-11453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The shortest path between two variable nodes. The application receives the input (starting point and destination) from the user and calculates the path by Dijkstra's algorithm</p>
</div>
<div id="comment-11453-info" class="comment-info">
<span class="comment-age">(23 Mar '12, 03:50)</span> <span class="comment-user userinfo">yenyip</span>
</div>
</div>
<span id="63656"></span>
<div id="comment-63656" class="comment">
<div id="post-63656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please how did you get infromation (lat &amp; lon) of each node??</p>
</div>
<div id="comment-63656-info" class="comment-info">
<span class="comment-age">(23 May '18, 17:41)</span> <span class="comment-user userinfo">yhsafa</span>
</div>
</div>
</div>
<div id="comment-tools-11313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11313-form-container" class="comment-form-container">
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

<span id="11442"></span>

<div id="answer-container-11442" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11442-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you ever had a look at the OSM wiki, the endless source of knowledge?</p>
<p>At <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a> you get an overview about routing with OSM data.</p>
<p>Or go to the <a href="http://wiki.openstreetmap.org/wiki/Android">Android</a> section and search for apps that are opensource and have routing features.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '12, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-11442" class="comments-container">
<span id="11452"></span>
<div id="comment-11452" class="comment">
<div id="post-11452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks stephan75. Actually I have tried to use the apps listed in Android section. I have read the OSM wiki but still cannot get the distance values. Normally, which method should be used ?</p>
</div>
<div id="comment-11452-info" class="comment-info">
<span class="comment-age">(23 Mar '12, 03:47)</span> <span class="comment-user userinfo">yenyip</span>
</div>
</div>
</div>
<div id="comment-tools-11442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11442-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11569"></span>

<div id="answer-container-11569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11569-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, apart from the useful advices, you are still missing the answer to your question: how to calculate the distance on the WGS'84 sphere between two points defined by P1(Lat1,Lon1) and P2(Lat2,Lon2)?</p>
<p>If you don't minde, try this:</p>
<p>X1=cos(C x Lat1) x cos(C x Lon1); X2=cos(C x Lat2) x cos(C x Lon2);</p>
<p>Y1=cos(C x Lat1) x sin(C x Lon1); Y2=cos(C x Lat2) x sin(C x Lon2);</p>
<p>Z1=sin(C x Lat1); Z2=sin(C x Lat2);</p>
<p>(main-circle)distance(P1,P2)=R x acos(X1 x X2 + Y1 x Y2 + Z1 x Z2);</p>
<p>Where R=6378137 and C=PI/180=0.0174532925 and distance in meters.</p>
<p>Assumed, latitude and longitude are given in decimal degrees (if in radians, take C=1).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 17:39</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '12, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-11569" class="comments-container">
&#10;</div>
<div id="comment-tools-11569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11569-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11455"></span>

<div id="answer-container-11455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11455-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand you right you want to make a routing engine for android. For the first this have been done <a href="http://wiki.openstreetmap.org/wiki/Android">before</a> and you might be better of using one of those open source implementations.</p>
<p>The first thing you have to learn is how the osm data is. There are a lot of tags that describe who can travel where and how fast and so forth. In the end you want to create a weighted graph of this data that you can store. Then you can run dijkstras algorithm on that graph. When you finaly have a route you can calculate the distance from point to point and add them up.</p>
<p>As you might imagine this is quite the task and it will take a lot of development to get the routing engine fast enough that you can use it. My recomendations is that you take a look at some of the open source applications for android that supports offline routing, and try to reuse their code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '12, 04:23</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11455" class="comments-container">
&#10;</div>
<div id="comment-tools-11455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11455-form-container" class="comment-form-container">
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

