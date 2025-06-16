+++
type = "question"
title = "JOSM Routing - How to Establish Road Hierarchy"
description = '''I&#x27;ve built an OSM road dataset (from a shapefile to a .osm in JOSM), in which each unique feature has been assigned a &#x27;highway&#x27; tag. I&#x27;ve declared oneways and bridges in the proper syntax as well. This dataset is going to be used in a mobile routing application, which I am currently beta testing wit...'''
date = "2012-12-06T19:56:00Z"
lastmod = "2012-12-12T13:46:00Z"
weight = 18258
keywords = [ "hierarchy", "roads", "routing", "josm" ]
aliases = [ "/questions/18258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Routing - How to Establish Road Hierarchy](/questions/18258/josm-routing-how-to-establish-road-hierarchy)

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
<span id="post-18258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18258-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've built an OSM road dataset (from a shapefile to a .osm in JOSM), in which each unique feature has been assigned a <a href="https://wiki.openstreetmap.org/wiki/Key:highway">'highway' tag</a>. I've declared oneways and bridges in the proper syntax as well. This dataset is going to be used in a mobile routing application, which I am currently beta testing with a developer. The one-ways and the turn restrictions that I've already built are being recognized and followed in solving routes in this application currently, but I would like to build-in some kind of hierarchy as well so that a 'primary' road is given preference over an 'unclassified' when solving a route.</p>
<p>I had thought originally that the 'highway' tag would do this automatically, but that does not seem to be the case. What is it that I am missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '12, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/de57b64756fa6ff91b249fe3002d583c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jrand&#39;s gravatar image" />
<p><span>jrand</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jrand has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '12, 19:57</strong> </span></p>
</div>
</div>
<div id="comments-container-18258" class="comments-container">
<span id="18316"></span>
<div id="comment-18316" class="comment">
<div id="post-18316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question seems to be not an FAQ but mote a topic that would be beter placed to one of the OSM mailing lists, maybe the one about Routing or developing ... see <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">https://wiki.openstreetmap.org/wiki/Mailing_lists</a></p>
</div>
<div id="comment-18316-info" class="comment-info">
<span class="comment-age">(09 Dec '12, 21:01)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="18370"></span>
<div id="comment-18370" class="comment">
<div id="post-18370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What do you mean with "given preference"?</p>
<p>When you develop a router, you need a method that calculates the weight for every part of the road. This can happen based on a lot of tags s.a. the highway tag, maxspeed, No of lanes ...</p>
<p>For OSM data, tags are only key-value pairs. The data user needs to give a meaning on it.</p>
</div>
<div id="comment-18370-info" class="comment-info">
<span class="comment-age">(11 Dec '12, 15:11)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18258-form-container" class="comment-form-container">
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

<span id="18398"></span>

<div id="answer-container-18398" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18398-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is true that the "<a href="https://wiki.openstreetmap.org/wiki/Key:highway">highway</a>" tag is defining the road importance in the traffic. But nothing is "automatic". Your software will have to translate a "highway" value into a speed/importance factor. For instance, a "highway=primary" will be prefered to a "highway=track". JOSM editor will not help you in this matter. You have to know that "primary" is more important than "secondary" which is more important than "tertiary" then "unclassified", etc... See for instance how <a href="https://github.com/DennisOSRM/Project-OSRM/blob/master/profiles/car.lua">OSRM is defining a speed profile for highway values</a>. As hint, you should notice that the wiki table about "highway" is already sorted by importance (Starting with "motorway" and finishing with "service"/"track"). Some values can be considered as equivalent.</p>
<p>But more importantly, your software will have to check if the "highway" is accessible for your vehicles (cars ? motorbikes ? trucks ?) by checking the highway value (e.g. the "highway=cycleway" is not allowed for cars) combined with the "<a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a>" tags.</p>
<p>For instance, an "access=no" or "access=private" is not allowed for cars but ("access=no" + "motorcar=yes") or ("access=no" + "motor_vehicle=yes") or "access=motorocar" or "access=motor_vehicle" is allowed. Or "access=destination" is allowed but only if the concerned street is the route final destination... Sometimes, the "access" tag may allow motorcars where it is presumed forbidden, e.g. a combination of "highway=path" + "motorcar=yes" is bit exotic tagging since we assume that "path" is normally not open for 4 wheels vehicles but if a contributor specified explicitely "motorcar=yes", the access tag is more important than the "highway" value (but what is tolerated for "path" might be considered as a tagging error for other values e.g. if you combine "highway=footway" + "motorcar=yes").</p>
<p>You might also have to check if some nodes on your ways contain the tag "barrier" which is most probably blocking your vehicle again (for cars, it's quite easy : all "barrier" values shall stop you excepted perhaps the improbable "barrier=no"; for bicycles, it's more difficult since barriers might be passable or not depending on the value).</p>
<p>So, as you see, creating a routing software with OSM data requires a good knowledge of OSM tags and also current practices. You can study the wiki for that and also check the data itself and the different combinations. You also have to accept that contributors can do mistakes. If you route is wrong, it can be your algorithm ignoring a specific tag but it can be the data itself as well (tags and/or geometry). In case of doubts, you can ask the community here or on the <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">mailing lists</a>. You should also start with a limited amount of tags and simply admit publicly that you are only handling the most usual and simple cases at start ;-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '12, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '12, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-18398" class="comments-container">
&#10;</div>
<div id="comment-tools-18398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18398-form-container" class="comment-form-container">
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

