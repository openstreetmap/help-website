+++
type = "question"
title = "Unable to view the bus routes that I created"
description = '''I have created a bus route using the following steps  1. Check if the bus stop is present  2. At the end in the relation field, add a new relation as bus route and under &quot;ref&quot; add the bus route name.   3. If the bus stop is not present then first create the bus stop and then follow step 2.  I am una...'''
date = "2020-04-17T11:34:00Z"
lastmod = "2020-04-22T08:52:00Z"
weight = 74238
keywords = [ "bus", "busstops", "busroute" ]
aliases = [ "/questions/74238" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to view the bus routes that I created](/questions/74238/unable-to-view-the-bus-routes-that-i-created)

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
<span id="post-74238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have created a bus route using the following steps 1. Check if the bus stop is present 2. At the end in the relation field, add a new relation as bus route and under "ref" add the bus route name. 3. If the bus stop is not present then first create the bus stop and then follow step 2.</p>
<p>I am unable to view the corresponding bus route from <a href="https://www.xn--pnvkarte-m4a.de/#80.2839;13.0797;15">OPNVKarte</a>. I am able to see the some of the stops being updated. Also when I go to <a href="http://overpass-turbo.eu/">Overpass turbo</a> to extract the bus stops, I can see the bus stops there but not the bus route. Can some one tell me what is it that am doing wrong in the route relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '20, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7206022e636d63ac32e8c02d27bf6a1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ganesh0709&#39;s gravatar image" />
<p><span>ganesh0709</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ganesh0709 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74238" class="comments-container">
&#10;</div>
<div id="comment-tools-74238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74238-form-container" class="comment-form-container">
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

<span id="74250"></span>

<div id="answer-container-74250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74250-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, You've actually made lots of route relations with a single feature (bus Stop) in them. A bus route relation needs all the route objects, bus stops, sections of highway of the route. With single objects in a route relation you'll never see a linear route.</p>
<p>This is a link to a bus route :-<a href="https://www.openstreetmap.org/relation/5356214">https://www.openstreetmap.org/relation/5356214</a> You will see in it all parts that make up the relation.</p>
<p>Route relations are rather difficult for a beginner to start on even experienced mappers can run into problems making them. Also, the iD editor is not the best tool for route relations, many folk have difficulties with it. JOSM editor is much better.</p>
<p>I respectfully think it would be best to revert the changes you've made and start again on relations after gaining a bit more experience.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '20, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-74250" class="comments-container">
<span id="74255"></span>
<div id="comment-74255" class="comment">
<div id="post-74255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thank you for the response. I have reverted my route relations but kept the bus stops since they do not need to be deleted.</p>
<p>The main problem that I faced is when I created the route relation for the first stop, I am unable to see the same relation for the second stop when I search for it and that is why I have created multiple relations but ensured all the relations had the same tags.</p>
<p>Is there any reason why I am unable to see the bus route relation when I search for it in the second stop relations ?</p>
<p>Also, as suggested I will try JOSM editor too.</p>
</div>
<div id="comment-74255-info" class="comment-info">
<span class="comment-age">(18 Apr '20, 03:13)</span> <span class="comment-user userinfo">ganesh0709</span>
</div>
</div>
<span id="74258"></span>
<div id="comment-74258" class="comment">
<div id="post-74258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you click the "+" to add the second stop to a relation, the relation for the first stop should be on the dropdown list.</p>
<p>Do you have the first stop visible in the editor when you are trying to add the second?</p>
<p>The list should have all relations that apply to the downloaded data, but if you are editing across two sessions, the first stop might not be loaded.</p>
</div>
<div id="comment-74258-info" class="comment-info">
<span class="comment-age">(18 Apr '20, 10:59)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="74261"></span>
<div id="comment-74261" class="comment">
<div id="post-74261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added a new relation for the first stop. Then, for the second stop, under relations when I add "+" the first relation that I created came up and I just added it.</p>
<p>Now, under relations I am able to see 2 members i.e both the bus stops. But when I am trying to add the same relation for the third stop, it is not showing up and hence am not able to add that relation.</p>
<p>All stops are visible in the editor and all are under the bus stop type.</p>
</div>
<div id="comment-74261-info" class="comment-info">
<span class="comment-age">(18 Apr '20, 16:33)</span> <span class="comment-user userinfo">ganesh0709</span>
</div>
</div>
<span id="74321"></span>
<div id="comment-74321" class="comment">
<div id="post-74321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sound like a bug in iD, they have an issue tracker <a href="https://github.com/openstreetmap/iD/issues">here</a> where you can report the problem.</p>
</div>
<div id="comment-74321-info" class="comment-info">
<span class="comment-age">(21 Apr '20, 20:50)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-74250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74250-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74253"></span>

<div id="answer-container-74253" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74253-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Routes are created as a single relation with all the relevant items added to it. In this case you would need to create a new relation for the first stop, and then add subsequent stops to the <em>same</em> relation you created for the first stop.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Relation">Relations</a> can be particularly difficult to edit in iD because you usually have to edit them "backwards" in that you have to select the element first and then "add" the relation (even though you are really adding the element to the relation).</p>
<p>The individual road segments are normally added as well if the bus has a fixed route between stops. The roads should be split at the point the bus route joins or leaves them. Normally all stops are listed in order first, then all ways that make up the route (also in order). You can change the order of members by dragging them up and down in the list so it isn't critical that you start at one end and work your way to the other. The roles for each member should normally be set according to the table on <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dbus">this wiki page</a>.</p>
<p>There are currently two tagging standards for these routes, the older method uses a single relation for both directions and the later method has a different relation for each direction (and for any variations) and then groups all of these into an overarching "route master" relation (PTv2). Both of these have vehement supporters within the community. A tutorial for creating the later type in JOSM can be found <a href="https://osmand.net/blog/guideline-pt">here</a>. Note that it is not strictly necessary to list both a stop ("<code>platform</code>") and stop position ("<code>stop</code>") if either of them are not visible '<a href="https://wiki.openstreetmap.org/wiki/Verifiability">on the ground</a>'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '20, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-74253" class="comments-container">
&#10;</div>
<div id="comment-tools-74253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74253-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74324"></span>

<div id="answer-container-74324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi ganesh0709,</p>
<p>That's a great effort and full marks for persevering. There's a heck of a lot to learn in OSM and I hope you can bear hearing of further problems.</p>
<p>Please have a look at this Route Manager page for your new route :-<a href="https://osmrm.openstreetmap.de/relation.jsp?id=11012554">https://osmrm.openstreetmap.de/relation.jsp?id=11012554</a> I'll try to point out the problems I can see and then you can fix them (with your new skills).</p>
<p>In the right panel zoom to the first segment. Inspect the map at left, there is a gap between segments 1 and 2. There is no connecting highway between these segments. Further the highways in each segment are opposing oneway highways.</p>
<p>Almost the same situation between segment 2 and 3. Except here there the two highways are on different layers as well.</p>
<p>Between segments 3 and 4, the last highway of segment 3 extends past the first highway of segment 4. A short section that highway should be sectioned off and removed from the relation.</p>
<p>Segment 6 shouldn't be in this linear route.</p>
<p>The first highway of segment 7 has a short section of highway that should be sectioned off and removed from the relation.</p>
<p>You can also see the problems if you zoom right into the route on this page <a href="https://www.openstreetmap.org/relation/11012554#map=13/13.0274/80.2836">https://www.openstreetmap.org/relation/11012554#map=13/13.0274/80.2836</a></p>
<p>Regards Bernard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '20, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-74324" class="comments-container">
&#10;</div>
<div id="comment-tools-74324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74324-form-container" class="comment-form-container">
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

