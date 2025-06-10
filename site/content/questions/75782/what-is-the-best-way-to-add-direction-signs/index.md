+++
type = "question"
title = "[closed] What is the best way to add direction signs?"
description = '''I want to add a few direction signs, so I looked at http://osm.mueschelsoft.de/destinationsign/example/index.htm to learn how to do it. What I found out that the data entries are often attached to an intersection node and not on the coordinates where the direction sign is physically situated.  Is th...'''
date = "2020-07-18T19:16:00Z"
lastmod = "2020-07-19T18:38:00Z"
weight = 75782
keywords = [ "direction_sign" ]
aliases = [ "/questions/75782" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] What is the best way to add direction signs?](/questions/75782/what-is-the-best-way-to-add-direction-signs)

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
<span id="post-75782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75782-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to add a few direction signs, so I looked at <a href="http://osm.mueschelsoft.de/destinationsign/example/index.htm">http://osm.mueschelsoft.de/destinationsign/example/index.htm</a> to learn how to do it.</p>
<p>What I found out that the data entries are often attached to an intersection node and not on the coordinates where the direction sign is physically situated.</p>
<p>Is this the correct way or should a new node be placed at the correct coordinates and the appropriate relationships added?</p>
<p>My own point of view is that OSM, being a map, should have the objects at the coordinates where they actually are situated!</p>
<p>Does anybody know of a renderer that displays direction_sign (s)? JOSM doesn't!</p>
<p>Please advise.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-direction_sign" rel="tag" title="see questions tagged &#39;direction_sign&#39;">direction_sign</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '20, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Jul '20, 18:40</strong> </span></p>
</div>
</div>
<div id="comments-container-75782" class="comments-container">
&#10;</div>
<div id="comment-tools-75782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75782-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by dcp 19 Jul '20, 18:40

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="75783"></span>

<div id="answer-container-75783" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While maps do frequently <a href="https://en.wikipedia.org/wiki/Cartographic_generalization#Displacement">displace</a> objects to aid legibility, OSM typically doesn't as that's a job for the renderer. OSM does however map many things where the effect takes place rather than where the sign is. See for example <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dstop"><code>highway=stop</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dgive_way">give way</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:maxspeed">speed limits</a> etc. In these instances the sign itself can be mapped with the <a href="https://wiki.openstreetmap.org/wiki/Key:traffic_sign"><code>traffic_sign=*</code></a> key when desired.</p>
<p>The most complete method for mapping destination signs is the <a href="https://wiki.openstreetmap.org/wiki/Relation:destination_sign">destination relation</a> which does have a role to identify node for the sign itself as well as the node for the intersection to which the sign refers. The sign node can itself be tagged as a traffic sign or a <a href="https://wiki.openstreetmap.org/wiki/Tag:information%3Dguidepost">guidepost</a> depending on its appearance. The latter is rendered by both JOSM and OSM carto.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '20, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-75783" class="comments-container">
<span id="75790"></span>
<div id="comment-75790" class="comment">
<div id="post-75790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That being said, relation:destination_sign is more often used on intersections, where different directions have different destinations.</p>
</div>
<div id="comment-75790-info" class="comment-info">
<span class="comment-age">(19 Jul '20, 10:52)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="75791"></span>
<div id="comment-75791" class="comment">
<div id="post-75791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While waiting for your useful comments I created my first direction_sign at node:</p>
<p>7727200367</p>
<p>based on <a href="https://www.mapillary.com/app/?lat=50.63313986923077&amp;lng=6.938710121678322&amp;z=17&amp;pKey=Clk3BJdpSmzGpfHkHqk33g&amp;focus=photo">https://www.mapillary.com/app/?lat=50.63313986923077&amp;lng=6.938710121678322&amp;z=17&amp;pKey=Clk3BJdpSmzGpfHkHqk33g&amp;focus=photo</a></p>
<p>The result can be seen here:</p>
<p><a href="http://osm.mueschelsoft.de/destinationsign/example/index.htm#node=7727200367&amp;namedroutes=1fromarrow=0&amp;include_sgn=1&amp;include_way=1&amp;country=">http://osm.mueschelsoft.de/destinationsign/example/index.htm#node=7727200367&amp;namedroutes=1fromarrow=0&amp;include_sgn=1&amp;include_way=1&amp;country=</a></p>
<p>I am not satisfied with the result, however, as the arrows are rendered to the compass angles and not to the direction sign itself; straight on, turn left, or turn right.</p>
<p>What I don't know: Am I doing something wrong or is mueschelsoft wrong in the rendering?</p>
<p>Incidently the node 7727200367 is not rendered in JOSM!</p>
</div>
<div id="comment-75791-info" class="comment-info">
<span class="comment-age">(19 Jul '20, 15:14)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="75792"></span>
<div id="comment-75792" class="comment">
<div id="post-75792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I install the traffic_signs_EUR_OC map paint style, and add the tag <code>traffic_sign=DE:434</code> it is rendered in JOSM (the closer suggestion DE:434-53 from <a href="https://de.wikipedia.org/wiki/Bildtafel_der_Verkehrszeichen_in_der_Bundesrepublik_Deutschland_von_2013_bis_2017">this</a> table doesn't appear to have an icon yet). The (new to me) Mueschelsoft site seems to take the departure way direction as the direction to show when ways are used in the relation, and the direction between <code>intersection</code>/<code>from</code> and <code>to</code> as the direction when nodes are used. The relation documentation allows multiple <code>sign</code> nodes for a single <code>intersection</code> and <code>to</code> so it would be very difficult to show instructions to turn left/right outside of an app giving directions.</p>
<p>I am no expert on these relations but I don't think the distances should be tagged on the relation if they are not shown on the sign. Ways are probably a little more 'stable' than node for the <code>to</code> element, but most software warns if you are about to break a relation by deleting something. Some of the relations that refer to 7727200367 also seem to define the intersection as from which seems a little odd.</p>
</div>
<div id="comment-75792-info" class="comment-info">
<span class="comment-age">(19 Jul '20, 17:41)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75793"></span>
<div id="comment-75793" class="comment">
<div id="post-75793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am coming to the conclusion that I will not add any of the directio_sign (s) at the moment. There does not seem to be a well-defined tagging verification and rendering concept at the moment.</p>
<p>Another oddity: mueschelsoft determines the direction for the arrow direction from the direction of the way and not from what is defined in the relation.</p>
<p>e.g. direction_northwest is ignored if the way direction is SE.</p>
<p>I am closing this discussion and thank you all for you knowledge!</p>
</div>
<div id="comment-75793-info" class="comment-info">
<span class="comment-age">(19 Jul '20, 18:38)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-75783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75783-form-container" class="comment-form-container">
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

