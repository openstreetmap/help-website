+++
type = "question"
title = "How to Mark a dead end or No Through Road"
description = '''Two year ago the community in agreement with the local Highways Department agreed to close a street to through traffic. Postcode CW11 1GN. 1st part of the street is public highway and a made up road, 2nd part is privately owned, and a dirt track. The high volume of traffic over the dirt track had ma...'''
date = "2023-05-07T00:19:00Z"
lastmod = "2023-05-08T14:35:00Z"
weight = 87230
keywords = [ "deadends" ]
aliases = [ "/questions/87230" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to Mark a dead end or No Through Road](/questions/87230/how-to-mark-a-dead-end-or-no-through-road)

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
<span id="post-87230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Two year ago the community in agreement with the local Highways Department agreed to close a street to through traffic. Postcode CW11 1GN. 1st part of the street is public highway and a made up road, 2nd part is privately owned, and a dirt track. The high volume of traffic over the dirt track had made it impassable for motor vehicles to pass as huge crators had developed. Successfully changed Google and TomTom maps only to find open street maps also needed to be changed.</p>
<p>So far I have Split Bradwall street ( 24441448/1168954855) shortend 1168954855 and added Bradwall Street Track ( 1168932723 ) and added a gate ( Way 1168929181, change set 135734602 )which is not open to vehicles on the track. Pedestrians and cyclists can pass around the gate but motor vehicles cannot get passed, No Entry signs also installed along with T dead end signs at each junction with the main road.</p>
<p>However if I ask how to get to a house on Bradwall St from the northern part of town the directions are telling me to turn into the track which is now blocked by a gate -</p>
<p>Can someone review what I've done and advise on how to correct the setup. Thanks John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deadends" rel="tag" title="see questions tagged &#39;deadends&#39;">deadends</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '23, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/14a8e821a42b96a4e185d5eaf036eb91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnKeane&#39;s gravatar image" />
<p><span>JohnKeane</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnKeane has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 May '23, 00:28</strong> </span></p>
</div>
</div>
<div id="comments-container-87230" class="comments-container">
<span id="87236"></span>
<div id="comment-87236" class="comment">
<div id="post-87236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even if unpaved and private I think this sounds like it is still a <code>highway=residential</code> road. You might want to tag it as having general <code>access=destination</code>, leaving the permissive food and cyclist tagging.</p>
</div>
<div id="comment-87236-info" class="comment-info">
<span class="comment-age">(07 May '23, 17:04)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-87230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87230-form-container" class="comment-form-container">
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

<span id="87232"></span>

<div id="answer-container-87232" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87232-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My suggestion would be to make the gate a node on the highway. Thus a physical barrier/restriction on the highway rather than a way drawn across the highway but not part of the highway. You would have to reconsider the tags on the highway and gate making them logically possible, (not locked and open 24/7).</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '23, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-87232" class="comments-container">
<span id="87237"></span>
<div id="comment-87237" class="comment">
<div id="post-87237-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just to add a note, even a barrier mapped as a way should normally share a node with the road it crosses to indicate the connection.</p>
</div>
<div id="comment-87237-info" class="comment-info">
<span class="comment-age">(07 May '23, 17:08)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-87232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87232-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87235"></span>

<div id="answer-container-87235" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87235-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>You probably want to read the <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">barrier</a> page on the osm wiki, it's well explained (about the node vs way approach). Sub-tags are interesting too.</p>
<p>Please check the <a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a> page. For example, the <code>access=no</code> tag on the "track" means it's forbidden for all.</p>
<p>On a side note, you shouldn't add "Track" in the name of the track part of the street, it should be inferred from the highway tag.</p>
<p>Speaking of which, <a href="https://wiki.openstreetmap.org/wiki/FR:Tag:highway=pedestrian">pedestrian</a> is usually meant for streets in cities.</p>
<p>Here I think I would tag as <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtrack"><code>highway=track</code></a> with <a href="https://wiki.openstreetmap.org/wiki/Key:smoothness"><code>smoothness=horrible</code></a> or something like that.</p>
<p>Please tell if you need more advice.</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '23, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-87235" class="comments-container">
&#10;</div>
<div id="comment-tools-87235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87238"></span>

<div id="answer-container-87238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that OSRM open source routing machine works now but Graphhopper does not yet. <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=53.14869%2C-2.36608%3B53.14815%2C-2.36708#map=17/53.14794/-2.36569">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=53.14869%2C-2.36608%3B53.14815%2C-2.36708#map=17/53.14794/-2.36569</a> Note although edits to OSM are instant the routers only seem to update their info from OSM every few days this could explain the delay...maybe?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '23, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '23, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-87238" class="comments-container">
<span id="87239"></span>
<div id="comment-87239" class="comment">
<div id="post-87239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the feedback, it would appear that the routing engines may take some time to gain access to the changes, thanks Andy_Mackey.</p>
<p>Considering the comments about the approach I have taken I'll do some more research before making any further changes, but further feedback is welcome. Key items to consider i) the 1st 200 meters of the roadway is public highway and maintained by the local authority ii) at the end of the tarmac road and pavement there is a privately owned track 70 meters in length, it is not permissable for the public to drive a vehicle along but it is open to the public to walk or cycle along it ( it is because the ownership and permissions of the highway and track are different that I split what had originally been mapped as a single unit into two ) iii) There is a gate across the track, permanently closed and locked to prevent vehicles from ignoring the access restriction, drivers are forced to turn around and retrace their steps</p>
<p>If I have been in the vicinity when vehicles ( usually delivery drivers using iPhones ) approach the barrier and have to then turn around I have been asking them what routing tool they have been using, so I will monitor this over the next few weeks and check if the change is effective across the various Apps.</p>
<p>One question I have is what is the typical timescale for a change like this to update onto remote devices ? I know TomTom was 3 months before the update was available.</p>
</div>
<div id="comment-87239-info" class="comment-info">
<span class="comment-age">(08 May '23, 13:19)</span> <span class="comment-user userinfo">JohnKeane</span>
</div>
</div>
<span id="87240"></span>
<div id="comment-87240" class="comment">
<div id="post-87240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/22989/johnkeane">@JohnKeane</a> The update frequency for devices is entirely up to the individual app maker. Changes go live in the database immediately, with <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/diffs#Minutely,_Hourly,_or_Daily_diffs">diffs</a> to the <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">planet file</a> published for use minutely if consumers so desire. Routing normally takes a fair amount of processing to convert OSM data into a usable format, which is probably why I'm not aware of a router that updates nearly this quickly. Apps that work offline might update once a month, online routers (especially speciality ones) may be quicker or may only update at a pace that their clients demand.</p>
</div>
<div id="comment-87240-info" class="comment-info">
<span class="comment-age">(08 May '23, 14:35)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-87238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87238-form-container" class="comment-form-container">
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

