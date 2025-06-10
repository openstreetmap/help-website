+++
type = "question"
title = "Highlighting a route (to create routing instructions)"
description = '''Hi, I want to pass some instructions on how to reach a certain place to friends. Several routes are available with advantages and disadvantages (like shortest route, fastest route, prettiest route, most fun route,...). A simple solution would be to download the map tiles and then use a graphic edito...'''
date = "2011-09-14T19:52:00Z"
lastmod = "2014-08-10T17:13:00Z"
weight = 7876
keywords = [ "highlight", "route", "export", "openlayer" ]
aliases = [ "/questions/7876" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Highlighting a route (to create routing instructions)](/questions/7876/highlighting-a-route-to-create-routing-instructions)

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
<span id="post-7876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7876-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to pass some instructions on how to reach a certain place to friends. Several routes are available with advantages and disadvantages (like shortest route, fastest route, prettiest route, most fun route,...).</p>
<p>A simple solution would be to download the map tiles and then use a graphic editor such as gimp and add a transparent colored line covering the routes I recommend. Then I can share the resulting image file and I have the desired effect. The problem is, that I need to repeat this task over and over if the map updates (at least if I want my map to be up to date as well) and people can't scroll or zoom.</p>
<p>Next solution would be to create a little html/javascript page that uses OpenLayers. But then I need a gpx-trace for all the routes. Where get those from short of driving the entire routes again? After all OSM has all the traces. I played with JOSM a little to figure out whether I can export some roads as GPX, but I could only figure out how to export entire layers which is clearly to much. Does anyone know a tool for extracting GPX files for a certain route from OSM?</p>
<p>I am open for other ideas as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highlight" rel="tag" title="see questions tagged &#39;highlight&#39;">highlight</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-openlayer" rel="tag" title="see questions tagged &#39;openlayer&#39;">openlayer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '11, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/722c01d97af67e0fa77a7015a90ebe62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yankee&#39;s gravatar image" />
<p><span>yankee</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yankee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '14, 15:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-7876" class="comments-container">
<span id="7896"></span>
<div id="comment-7896" class="comment">
<div id="post-7896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know the present OSM html renderer is tile-based, but from potlach for instance, could we print the webpage to a <em>vectorial</em> pdf? If yes then one then can reedit this with any serious vector drawing application (ie, capable to "eat" vector pdf), just highlighting the ways of interest and changing their draw attributes...</p>
<p>Another point: did you check all the open OSM-based routers around, which may offer you up-to-date pages with the right routing preset?</p>
</div>
<div id="comment-7896-info" class="comment-info">
<span class="comment-age">(15 Sep '11, 13:31)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
<span id="7902"></span>
<div id="comment-7902" class="comment">
<div id="post-7902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Herve5</span>: <a href="http://yournavigation.org">yournavigation.org</a> partially does not place the overlay over the road for some reason, on <a href="http://maps.cloudmade.com">maps.cloudmade.com</a> the target road is not in so far (it's obviously not through the tile cache since parts a visible on some zoom levels, even though I added the road in April), I could not get <a href="http://roadee.net">roadee.net</a> to calculate any route at all, MapQuest is ok, except for one road which involves a track (MapQuest refuses to use that track). Any more proposals?</p>
</div>
<div id="comment-7902-info" class="comment-info">
<span class="comment-age">(15 Sep '11, 18:23)</span> <span class="comment-user userinfo">yankee</span>
</div>
</div>
<span id="7961"></span>
<div id="comment-7961" class="comment">
<div id="post-7961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried <a href="http://openrouteservice.org">openrouteservice.org</a>? To route over tracks, you would need to choose the Pedestrian or Bicycle Profile. Besides GPX download you could also simply send a "Route link".</p>
</div>
<div id="comment-7961-info" class="comment-info">
<span class="comment-age">(17 Sep '11, 14:49)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
<span id="7983"></span>
<div id="comment-7983" class="comment">
<div id="post-7983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yankee, sorry for being away... Besides the ones already mentioned for routing you have <a href="http://www.gpsdrive.de/download.shtml">http://www.gpsdrive.de/download.shtml</a> (linux), <a href="http://navigatorfree.mapfactor.com/en/download/">http://navigatorfree.mapfactor.com/en/download/</a> nav gps turn-by-turn (windows) <a href="http://sourceforge.net/projects/travelingsales/">http://sourceforge.net/projects/travelingsales/</a> (java) <a href="http://wiki.openstreetmap.org/wiki/Navit">http://wiki.openstreetmap.org/wiki/Navit</a> (java?) <a href="http://we-travel.biz/wetravel/">http://we-travel.biz/wetravel/</a> <a href="http://wiki.openstreetmap.org/wiki/KDE_Marble">http://wiki.openstreetmap.org/wiki/KDE_Marble</a></p>
</div>
<div id="comment-7983-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 19:45)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
</div>
<div id="comment-tools-7876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7876-form-container" class="comment-form-container">
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

<span id="7909"></span>

<div id="answer-container-7909" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could get the whole layer into JOSM, select your route, then make an inverse selection so everything else is selected. Now go to EDIT-&gt;PURGE (do NOT DELETE instead) and export the result as GPX.</p>
<p>Btw.: I doubt you would have to change your GIMP-overlay very often. Mostly the route overlay would not change when the map slightly changes (simply keep the layers separate and exchange the map underneath), but I agree that an openlayers overlay is nicer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '11, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-7909" class="comments-container">
<span id="7934"></span>
<div id="comment-7934" class="comment">
<div id="post-7934-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>OK, well... That IS a lot of work! But it works! So here's the stuff in more detail:</p>
<ol>
<li>Select all ways to be included (possibly have to split ways)</li>
<li>Edit → Search → "child selected" to select the nodes for the ways as well. Check "add to selection".</li>
<li>Edit → Search → "-selected" to inverse selection. Check "replace selection".</li>
<li>Edit → Purge</li>
<li>Right click the data layer → export to GPX</li>
<li>Follow these instructions to display the track: <span>Openlayers_Track_example</span></li>
</ol>
</div>
<div id="comment-7934-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 12:25)</span> <span class="comment-user userinfo">yankee</span>
</div>
</div>
<span id="35686"></span>
<div id="comment-35686" class="comment">
<div id="post-35686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The old reply to a query may help in some way ... or not? Using josm right-click over the Downloaded GPX Data in the layers pane, then select Info - you'll see a table of tracks with some of them showing links in the URL column which you then can select and copy into your browser.</p>
</div>
<div id="comment-35686-info" class="comment-info">
<span class="comment-age">(10 Aug '14, 17:13)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-7909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7909-form-container" class="comment-form-container">
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

