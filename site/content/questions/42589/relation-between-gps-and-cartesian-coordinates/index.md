+++
type = "question"
title = "Relation between GPS and cartesian coordinates"
description = '''Hi,  I&#x27;m trying to create a layer with nodes representing a route. This occurs indoor so there&#x27;s no GPS info along the way. I have a starting point with its GPS coordinates in OSM. That point corresponds to a cartesian point, say, (0,0). At a few points I calculate the variation of the cartesian coo...'''
date = "2015-04-25T14:06:00Z"
lastmod = "2015-04-26T15:58:00Z"
weight = 42589
keywords = [ "coordinates", "gps" ]
aliases = [ "/questions/42589" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Relation between GPS and cartesian coordinates](/questions/42589/relation-between-gps-and-cartesian-coordinates)

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
<span id="post-42589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42589-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to create a layer with nodes representing a route. This occurs indoor so there's no GPS info along the way. I have a starting point with its GPS coordinates in OSM. That point corresponds to a cartesian point, say, (0,0). At a few points I calculate the variation of the cartesian coordinates having then several (x1,y1), (x2,y2), etc. points in meters. I'd like to calculate the GPS coordinates of that points knowing that the initial point (0,0) is the initial GPS coordinate.</p>
<p>I've read about <a href="http://rosettacode.org/wiki/Haversine_formula">haversine formula</a> about how to calculate distances between two GPS coordinates but I don't know how to do the inverse action.</p>
<p>Can anyone shed some light?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '15, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/35cb8824414102c741aa42fa33d29376?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viper_scull&#39;s gravatar image" />
<p><span>Viper_scull</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viper_scull has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '15, 18:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42589" class="comments-container">
&#10;</div>
<div id="comment-tools-42589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42589-form-container" class="comment-form-container">
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

<span id="42600"></span>

<div id="answer-container-42600" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42600-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well the basic problem is that the world isn't flat.</p>
<p>You need to <a href="http://en.wikipedia.org/wiki/Map_projection">project</a> your <a href="http://en.wikipedia.org/wiki/World_Geodetic_System">coodinates on a spheroid</a> on to a plane. There are multiple ways to do this as the wikipedia article points out, but I suspect what you would want to use is the <a href="http://en.wikipedia.org/wiki/Mercator_projection">mercator projection</a>, likely scaled to whatever you are using as a local grid.</p>
<p>To get the WGS84 (GPS) coordinates back from your cartesian coordinates you have to naturally do the inverse.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '15, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '15, 16:25</strong> </span></p>
</div>
</div>
<div id="comments-container-42600" class="comments-container">
<span id="42603"></span>
<div id="comment-42603" class="comment">
<div id="post-42603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For indoor mapping of this kind I would find a local co-ordinate system suitable for calculations in Cartesian geometry (such as OSGB (EPSG:27700 for UK) or CH-1903 or CH-1903+(for CH)). This is effectively what <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> is suggesting.</p>
</div>
<div id="comment-42603-info" class="comment-info">
<span class="comment-age">(26 Apr '15, 15:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="42604"></span>
<div id="comment-42604" class="comment">
<div id="post-42604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> I suspect this maybe simply an arbitrary grid laid over the floor plan (or screen coordinates for what it is worth).</p>
</div>
<div id="comment-42604-info" class="comment-info">
<span class="comment-age">(26 Apr '15, 15:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42600" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42600-form-container" class="comment-form-container">
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

