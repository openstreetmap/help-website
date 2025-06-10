+++
type = "question"
title = "Non optimal OSRM route - yet all attributes appear correct."
description = '''Hi, When routing from 51.78981, 0.15966 to 51.79049, 0.15968 (basically from one side of a roundabout to the other) the routing is not navigating through the roundabout but taking a large detour. I work for a company that uses OSM for routing taxi journeys (hence I am by not that familiar with OSM)....'''
date = "2022-03-23T13:12:00Z"
lastmod = "2022-03-23T13:41:00Z"
weight = 83987
keywords = [ "attributes", "routingerror" ]
aliases = [ "/questions/83987" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Non optimal OSRM route - yet all attributes appear correct.](/questions/83987/non-optimal-osrm-route-yet-all-attributes-appear-correct)

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
<span id="post-83987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83987-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When routing from 51.78981, 0.15966 to 51.79049, 0.15968 (basically from one side of a roundabout to the other) the routing is not navigating through the roundabout but taking a large detour. I work for a company that uses OSM for routing taxi journeys (hence I am by not that familiar with OSM). I have looked at the features and attributes and cant find any reason why OSM will not route using the roundabout. Any help would be appreciated as to which features/attributes are incorrect and what needs to change.</p>
<p>Regards,</p>
<p>Steve.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '22, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/aa604be467d765143ba6dc671e30714d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve%20P&#39;s gravatar image" />
<p><span>Steve P</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve P has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83987" class="comments-container">
&#10;</div>
<div id="comment-tools-83987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83987-form-container" class="comment-form-container">
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

<span id="83988"></span>

<div id="answer-container-83988" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83988-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-83988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Steve P has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the route in question: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=51.78952%2C0.15936%3B51.79030%2C0.16035#map=17/51.79066/0.16278">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=51.78952%2C0.15936%3B51.79030%2C0.16035#map=17/51.79066/0.16278</a></p>
<p>Ways <a href="https://www.openstreetmap.org/way/1028499848">https://www.openstreetmap.org/way/1028499848</a> and <a href="https://www.openstreetmap.org/way/1029414075">https://www.openstreetmap.org/way/1029414075</a> still have <code>construction=primary</code> set. I guess this makes OSRM ignore these ways (in contrast to GraphHopper which uses them for routing, probably because they also have <code>highway=secondary</code> set).</p>
<p>Remove this tag if construction is finished. Wait a few days for the data to get updated in the routing engines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '22, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '22, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-83988" class="comments-container">
&#10;</div>
<div id="comment-tools-83988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83988-form-container" class="comment-form-container">
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

