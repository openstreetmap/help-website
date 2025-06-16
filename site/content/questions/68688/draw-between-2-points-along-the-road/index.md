+++
type = "question"
title = "Draw between 2 points along the road"
description = '''Hi there! I have collected bus GPS data and I want to draw a route of that bus according to that GPS data on a map. I tried to use available services that provide Directions API. But there I can either choose car, bicycle or pedestrian as a travel mode, and those services try to avoid some places, w...'''
date = "2019-04-07T17:16:00Z"
lastmod = "2019-05-01T21:17:00Z"
weight = 68688
keywords = [ "directions", "route", "road" ]
aliases = [ "/questions/68688" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Draw between 2 points along the road](/questions/68688/draw-between-2-points-along-the-road)

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
<span id="post-68688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>I have collected bus GPS data and I want to draw a route of that bus according to that GPS data on a map. I tried to use available services that provide Directions API. But there I can either choose car, bicycle or pedestrian as a travel mode, and those services try to avoid some places, where the bus definitely goes, but it is either not allowed to driver there by car or the route under construction. Pedestrian type doesn't work for me because the services draw a route next to the road, but not over it. What I basically want is to draw a line on the road between multiple GPS points, but I don't want any "smart" functions that such services provide.</p>
<p>Don't you have any suggestions how it can be done? E.g. get a pice of road where GPS coordinate point to.</p>
<p>UPD:</p>
<p>Here is the example how direction services draw a route and how it should be. Blue line is how the mapbox draws the route. Red line is where the actual route is located.</p>
<p><img src="/upfiles/screenshot_XxVHH0q.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '19, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/77c6e568f61b2067b0fe11ab760cac9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RokrVPV&#39;s gravatar image" />
<p><span>RokrVPV</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RokrVPV has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '19, 19:53</strong> </span></p>
</div>
</div>
<div id="comments-container-68688" class="comments-container">
<span id="68689"></span>
<div id="comment-68689" class="comment">
<div id="post-68689-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, it's not immediately clear what your end goal is here and how it involves OpenStreetMap.</p>
<p>Are you trying to add a bus route to OSM and then create a map from that data that shows the route?</p>
<p>Are you trying to find a router that will get you from A to B using public transport data? That's unlikely to be OSM-based as although bus routes may be in OSM actual timetables won't be.</p>
</div>
<div id="comment-68689-info" class="comment-info">
<span class="comment-age">(07 Apr '19, 17:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68692"></span>
<div id="comment-68692" class="comment">
<div id="post-68692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Are you trying to add a bus route to OSM and then create a map from that data that shows the route?" - yes.</p>
<p>What I have is GPS coordinates of a bus that traveled along its route. Now I want to use these coordinates to draw a bus route. Finally, I would like to have an encoded polyline of the route so that later I could use this polyline to show the route on a map.</p>
<p>To achieve this, I tried several Directions API services like mapbox or graphhopper, but they don't always draw a route correctly, because some roads are not accessible by car. Instead, they try to navigate around such roads. I will upload picture to the post to show what I want.</p>
<p>I believe that OSM has stored roads as a data. So what I am thinking about now is e.g. try to get a polyline of a part of the road by GPS coordinate and then glue these polylines together to get the whole route. Or maybe there is a way to force such Directions services to draw what I want. I also know that OSM has bus routes, but they contain partially old or wrong data so I can't use it.</p>
</div>
<div id="comment-68692-info" class="comment-info">
<span class="comment-age">(07 Apr '19, 19:47)</span> <span class="comment-user userinfo">RokrVPV</span>
</div>
</div>
</div>
<div id="comment-tools-68688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68688-form-container" class="comment-form-container">
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

<span id="68696"></span>

<div id="answer-container-68696" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68696-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RokrVPV has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have two options:</p>
<ol>
<li>Simply draw your GPX track onto a map. This can be done with standalone programs like those mentioned by Gys de Jongh or with QGIS, and alternatively with online services like UMap. The advantage is that this shows exactly the path you have recorded. The disadvantage is that it does not take the road network into account at all, so if you have some recording errors or missing points, your track will not follow the road nicely.</li>
<li>Use a "track matching" software that finds the most likely route travelled by a vehicle when you have a GPS track as input. Popular routing engines like GraphHopper an OSRM offer this feature, but as you have already seen, when you use the standard routing profiles they will refuse to route over roads that are not allowed for cars. But if you install the software yourself then you have full control over the routing profile, and you could for example take the car profile and remove all the rules about "do not use a road that is only for buses" and so on. For example, in OSRM the code in <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua#L82">https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua#L82</a> means that everything with access=psv will not be considered; if you drop that line, the router will consider such roads as well. (You might need to make a few more changes than this to achive the desired result but it's a start).</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '19, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68696" class="comments-container">
<span id="68736"></span>
<div id="comment-68736" class="comment">
<div id="post-68736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is an option, thanks! I'll need to dig into it.</p>
</div>
<div id="comment-68736-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 20:02)</span> <span class="comment-user userinfo">RokrVPV</span>
</div>
</div>
<span id="69036"></span>
<div id="comment-69036" class="comment">
<div id="post-69036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Marking the answer as a correct. I was able to do that was suggested by <a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a> in the 2nd point. The only problem I see now is that when I set overview=full for route service, the points are a bit shifted from their correct location and don't point to roads, but next to it. But I am able to construct a route if use geometry from each step by setting steps=true in the request.</p>
</div>
<div id="comment-69036-info" class="comment-info">
<span class="comment-age">(01 May '19, 21:17)</span> <span class="comment-user userinfo">RokrVPV</span>
</div>
</div>
</div>
<div id="comment-tools-68696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68696-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68694"></span>

<div id="answer-container-68694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68694-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(answering the points in the comment "What I have is GPS coordinates...")</p>
<p>Once you've added a bus route to OSM you'll be able to create a map that shows that bus route on it. The route will get added to OSM as a relation, and whatever you use to create a map will need to display that. See for example <a href="https://www.openstreetmap.org/relation/332069">this example</a> on the OSM website.</p>
<p>It doesn't make sense to expect a router (foot, car, or bicycle) to follow a bus route.</p>
<p>Depending on what sort of "map" you're creating you'll need to do something different to display relation data. I wrote <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/38988">this diary entry</a> ages ago about doing it in a style similar to OSM's OSM Carto style.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '19, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68694" class="comments-container">
&#10;</div>
<div id="comment-tools-68694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68694-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68691"></span>

<div id="answer-container-68691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi RokrVPV, you can do that in BaseCamp <a href="https://www8.garmin.com/support/download_details.jsp?id=4435">https://www8.garmin.com/support/download_details.jsp?id=4435</a> or in QMapShack <a href="https://bitbucket.org/maproom/qmapshack/wiki/Home">https://bitbucket.org/maproom/qmapshack/wiki/Home</a> There you can draw whatever you want, or even just import your Gpx trace, and print your map. What you want is not possible in Openstreet map. Here buroutes must follow established roads and not Gpx traces. You can use your Gpx trace only as a guide to edit the bus route. If the roads are not present yet, you have to draw those first from an opensource. Bus routes are not for the faint of heart though : <a href="https://wiki.openstreetmap.org/wiki/Buses">https://wiki.openstreetmap.org/wiki/Buses</a></p>
<p>Gys</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '19, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5c3b258ebdc5943f1ab6008f146e7f7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gys%20de%20Jongh&#39;s gravatar image" />
<p><span>Gys de Jongh</span><br />
<span class="score" title="713 reputation points">713</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gys de Jongh has 5 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68691" class="comments-container">
<span id="68735"></span>
<div id="comment-68735" class="comment">
<div id="post-68735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I'll have a look at these tools.</p>
</div>
<div id="comment-68735-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 19:59)</span> <span class="comment-user userinfo">RokrVPV</span>
</div>
</div>
</div>
<div id="comment-tools-68691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68691-form-container" class="comment-form-container">
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

