+++
type = "question"
title = "How to link the residential buildings and residential in osm?"
description = '''In osm. I can map building with tag building = residential also can map Residential way with tag landuse = residential but how to map The building belongs to residential? I thought of a way map the building with operator = &#x27;xxxx&#x27;. But it does not seem right'''
date = "2017-06-07T07:30:00Z"
lastmod = "2017-06-08T04:07:00Z"
weight = 56490
keywords = [ "residential" ]
aliases = [ "/questions/56490" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to link the residential buildings and residential in osm?](/questions/56490/how-to-link-the-residential-buildings-and-residential-in-osm)

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
<span id="post-56490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56490-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In osm. I can map building with tag building = residential also can map Residential way with tag landuse = residential but how to map The building belongs to residential? I thought of a way map the building with operator = 'xxxx'. But it does not seem right</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '17, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/80e0c523c689ca888ae4e7f17a4b0618?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suze8793686&#39;s gravatar image" />
<p><span>suze8793686</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suze8793686 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56490" class="comments-container">
<span id="56491"></span>
<div id="comment-56491" class="comment">
<div id="post-56491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-post: <a href="https://gis.stackexchange.com/questions/243039/how-to-link-the-residential-buildings-and-residential-in-osm">https://gis.stackexchange.com/questions/243039/how-to-link-the-residential-buildings-and-residential-in-osm</a></p>
</div>
<div id="comment-56491-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 07:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56494"></span>
<div id="comment-56494" class="comment">
<div id="post-56494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-post here too: <a href="https://forum.openstreetmap.org/viewtopic.php?id=58663">https://forum.openstreetmap.org/viewtopic.php?id=58663</a></p>
</div>
<div id="comment-56494-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 10:51)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-56490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56490-form-container" class="comment-form-container">
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

<span id="56503"></span>

<div id="answer-container-56503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A residential way (or street/road) is never mapped as landuse=residential, a street is mapped with the highway key. While many residential roads will be mapped with highway=residential, other values such as living_street are also likely. But in many cases, such roads can also be primary or secondary roads in the road network.</p>
<p>A residential building can also be mapped as building=house, apartments, etc. See <a href="https://wiki.openstreetmap.org/wiki/Key:building#Accommodation">wiki page on buildings</a>.</p>
<p>I'm not sure what you mean with "Building belongs to residential". A street will (in the Western world) have an name. The building (or just a node inside the building) will have an addr:street tag. This "connects" the two. Is this what you want ?</p>
<p>If you want to "connect" the building with the landuse=residential (i.e. an area in which most buildings are for living), this is accomplished by the spatial relationship (building inside the landuse), so you do not need another construct for this.</p>
<p>Some people use the associatedStreet or street relations to connect buildings with streets, but others find this a bad things to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 04:07</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-56503" class="comments-container">
&#10;</div>
<div id="comment-tools-56503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56503-form-container" class="comment-form-container">
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

