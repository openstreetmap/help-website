+++
type = "question"
title = "How often does the main (mapnik) map get updated"
description = '''When looking at the main map on OpenStreetMap.org, some of the data that was added only minutes ago already shows up, whereas other data that was added weeks or months ago isn&#x27;t visible yet. How does the update process of the main mapnik map work?'''
date = "2010-07-14T14:00:00Z"
lastmod = "2023-11-30T22:33:00Z"
weight = 178
keywords = [ "map", "rendering", "update", "expiry" ]
aliases = [ "/questions/178" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How often does the main (mapnik) map get updated](/questions/178/how-often-does-the-main-mapnik-map-get-updated)

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
<span id="post-178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-178-score" class="post-score" title="current number of votes">
46
</div>
<span id="post-178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
21
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When looking at the main map on OpenStreetMap.org, some of the data that was added only minutes ago already shows up, whereas other data that was added weeks or months ago isn't visible yet. How does the update process of the main mapnik map work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '10, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Oct '13, 03:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-178" class="comments-container">
&#10;</div>
<div id="comment-tools-178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-178-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="183"></span>

<div id="answer-container-183" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-183-score" class="post-score" title="current number of votes">
94
</div>
<span id="post-183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer to this question is: The rendering of the main (mapnik) map should typically update within a few (tens of) minutes, however occasionally it can take longer.</p>
<p>The longer answer is a little more complicated, as there are many components that interact in subtle ways to produce the updated results. So I'll try and explain the process, which may be a little technical at points:</p>
<p>First of all, if you edit OpenStreetMap data, your changes get applied to the main database and are immediately visible from the API. The rendering of the map however uses a secondary database that needs to be kept updated from the main database. For this purpose, the main database publishes <a href="http://planet.openstreetmap.org/replication/minute/">minutely diffs</a> that are then applied to the rendering database on OpenStreetMap.org and other rendering servers. As the name suggests, these diffs typically are produced once a minute and so the rendering database is typically 1 - 2 minutes behind the main database. Occasionally (although this shouldn't happen) the diffs get stuck though, and this delay may increase a bit. You can see graphs the current delay of imports for the two rendering servers, <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/replication_delay.html">yevaud</a> and <a href="http://munin.openstreetmap.org/openstreetmap/orm.openstreetmap/replication_delay.html">orm</a>.</p>
<p>Once the new data is in the rendering database, it then needs to actually get rendered. However, the server does not have the capacity and resources to rerender all changed tiles immediately, so a clever algorithm tries to only render those tiles that are necessary in an order to try and ensure that the map appears to be as up to date as possible:</p>
<p>When your browser requests a tile from the server, the server checks if it has already rendered an up to date copy of this tile. If it has, then it simply sends back that copy to the client. If the copy the server has on the other hand is found to be out of date, it checks to see if it (the server) is not overloaded (e.g. in peak time) then tries to rerender the tile from the current rendering database and send this back to the client. If however it is overloaded, it returns the out of date copy back to the client. Similarly, if the rendering process takes more than 3 seconds, again the old tile gets returned to the client to not make the browser wait for ages to get the map. In both cases though, the tile gets added to the rendering queue and will typically get rendered in the background in the next hour or so. Therefore if you visit the same area e.g. an hour later, it should then have finished the rendering and you will see the up to date data.</p>
<p>In some cases when the server is severely overloaded, the rendering queue might fill up and then the rendering request may get dropped, which means the area won't get rerendered and updated until someone else goes and views the area when the queues are no longer full, in which case the procedure above applies again.</p>
<p>You can see if the rendering queue is full and thus it is likely that the map currently won't appear to update on these <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/#renderd">graphs</a>.</p>
<p>Now this leaves the question of how and when does the server decide if a tile is out of date or not: For this purpose, during the import of the diffs into the rendering db, an extra program calculates which tiles need rerendering based on those diffs. As deciding which tiles are effected, is a hard problem without actually rendering everything, this is only based on heuristics. I.e. it is based upon if there are nodes in the tile, or ways that are in the diff have nodes in those tiles. Relations currently get ignored completely in this process. Similarly, for areas, only the perimeter of the area gets expired.</p>
<p>If you suspect that the tile was not correctly expired, there is a way to manually overwrite this expiry mechanism by appending a /dirty to the url which will append the tile to the back of the rendering queue. However, in nearly all cases this should not be necessary.</p>
<p>As tiles only get rerendered once they are viewed, some of the higher zoom levels that are seldomly viewed might therefore appear out of date by quite a bit. It also means that neighbouring tiles that might have been viewed recently are more up to date, and thus show some strange artefacts of different rendering times.</p>
<p>In most cases hitting the refresh button a couple of times a few minutes apart will fix these issues.</p>
<p>On top of all this, is the additional issue of (proxy) caching, both in your browser and server side to reduce load. This may introduce an additional delay of a few hours and may cause the tile not to get rerenderd as the request might never reaches the server to trigger the rerender.</p>
<p>As you see, this whole things is complicated, but in most cases the short answer is sufficient. i.e. it normally updates within a few minutes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '13, 07:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p>
</div>
</div>
<div id="comments-container-183" class="comments-container">
<span id="682"></span>
<div id="comment-682" class="comment">
<div id="post-682-score" class="comment-score">
7
</div>
<div class="comment-text">
<p>apmon excellent explanation, but it would benefit from a small additional mention that coastlines are an exception. Coastlines being updated every so often. (typically twice a month.)</p>
</div>
<div id="comment-682-info" class="comment-info">
<span class="comment-age">(20 Aug '10, 12:30)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
<span id="7977"></span>
<div id="comment-7977" class="comment">
<div id="post-7977-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>more information about the coastline process in the wiki: <a href="http://wiki.openstreetmap.org/wiki/Coastline#Main_Mapnik_layer">http://wiki.openstreetmap.org/wiki/Coastline#Main_Mapnik_layer</a></p>
</div>
<div id="comment-7977-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 16:40)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="10798"></span>
<div id="comment-10798" class="comment">
<div id="post-10798-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Seems like there is heavy daytime load dependency to be seen in the graphs. What about not dropping any tiles from rendering but instead moving them to rendering during night off-peak hours? Finally, higher server load is not a big financial issues, right? I mean in terms of higher electricity comsumption for instance...</p>
</div>
<div id="comment-10798-info" class="comment-info">
<span class="comment-age">(26 Feb '12, 10:14)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="12500"></span>
<div id="comment-12500" class="comment not_top_scorer">
<div id="post-12500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can see my changes are being applied to the standard map, but the open cyclemap layer remains unchanged. How often does the open cyclemap get updated? I have been making corrections to some cycle paths that are not connected correctly thus causing routing errors.</p>
</div>
<div id="comment-12500-info" class="comment-info">
<span class="comment-age">(02 May '12, 11:24)</span> <span class="comment-user userinfo">paulcooke</span>
</div>
</div>
<span id="12503"></span>
<div id="comment-12503" class="comment not_top_scorer">
<div id="post-12503-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The cycle map layer uses Andy Allen's <a href="http://www.opencyclemap.org/">opencyclemap</a> tiles. <a href="http://www.gravitystorm.co.uk/shine/cycle-info/">He says</a> that "The map is updated every week (on a Thursday or Friday, normally)".</p>
</div>
<div id="comment-12503-info" class="comment-info">
<span class="comment-age">(02 May '12, 12:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30150"></span>
<div id="comment-30150" class="comment">
<div id="post-30150-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Does the above described algorithm only apply for zoomlevels &gt;=13 ? I usually always have to manually <em>/dirty</em> tiles with zoomlevel 12, 11 and 10 to have tertiary roads show up on those tiles...</p>
</div>
<div id="comment-30150-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 12:58)</span> <span class="comment-user userinfo">katpatuka</span>
</div>
</div>
<span id="53908"></span>
<div id="comment-53908" class="comment not_top_scorer">
<div id="post-53908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What I read above seems quite clear but, what happens to me is a little more strange: I deleted an old obsolete track segment and I drew a new track more actual replacing the old one lightly displaced with respect the old one. I did all the modifications about 24 hours ago. Now I can see the updated situation if I set the zoom to have the map scale on 300m or 100m. If the map scale is on 50m the modification is only partial If the map scale is 30m no modification is shown and I see the old situation If the map scale is 20m the modifications are completely shown All these things happen using the Standard Map; if I set the Cycling Map no modification appears on every zoom level.</p>
</div>
<div id="comment-53908-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 17:25)</span> <span class="comment-user userinfo">gbal45</span>
</div>
</div>
<span id="53910"></span>
<div id="comment-53910" class="comment not_top_scorer">
<div id="post-53910-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/13168/gbal45">@gbal45</a> pls do not add further questions to existing question and pls don't add them as answers. In any case you are simply seeing in browser caching effects. Refreshing and/or deleting the cache should help except if there is an overload situation on the tile servers.</p>
</div>
<div id="comment-53910-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 20:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="53972"></span>
<div id="comment-53972" class="comment not_top_scorer">
<div id="post-53972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the great answer!</p>
<p>Just a heads up, the <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/#renderd">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/#renderd</a> link is broken, and returns a 404 error.</p>
</div>
<div id="comment-53972-info" class="comment-info">
<span class="comment-age">(11 Jan '17, 02:21)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="55450"></span>
<div id="comment-55450" class="comment not_top_scorer">
<div id="post-55450-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Additional info: zoom levels 12 and below do not get marked dirty by map changes. Apparently they only re-render manually or when render styles change.</p>
</div>
<div id="comment-55450-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 15:20)</span> <span class="comment-user userinfo">MrPete</span>
</div>
</div>
<span id="61246"></span>
<div id="comment-61246" class="comment">
<div id="post-61246-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Some additional details:</p>
<ul>
<li><p>we have now 4 rendering servers instead of 2 (orm, yevaud, scorch, vial - see <a href="https://wiki.openstreetmap.org/wiki/Servers/tile">https://wiki.openstreetmap.org/wiki/Servers/tile</a> )</p></li>
<li><p>global rendering graphs are here: <a href="https://munin.openstreetmap.org/openstreetmap/render.openstreetmap/index.html#renderd">https://munin.openstreetmap.org/openstreetmap/render.openstreetmap/index.html#renderd</a></p></li>
<li><p>Low and medium zoom tiles (z0-z12) are usually re-rendered only when a new osm-carto version is being deployed and on the first Sunday of each month (see <a href="https://github.com/openstreetmap/chef/issues/138#issuecomment-346863212">https://github.com/openstreetmap/chef/issues/138#issuecomment-346863212</a> )</p></li>
</ul>
</div>
<div id="comment-61246-info" class="comment-info">
<span class="comment-age">(18 Dec '17, 03:59)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-183" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88034"></span>

<div id="answer-container-88034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88034-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-88034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tested a bit, and it seems I am more successful in trigering a re-render of tiles when i use "force-reload" in my browser. This is done by pressing [Ctrl]+[F5] in most browsers on Windows or Linux. On Mac, try [Shift]+[Command]+[R]. Clicking the reload-button while holding down the [Shift]-key shold also do the trick in most browsers and OS'es.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '23, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/86eba4947ddf5c683b09aa5e54cebbfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frodeseverin&#39;s gravatar image" />
<p><span>frodeseverin</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frodeseverin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '23, 20:14</strong> </span></p>
</div>
</div>
<div id="comments-container-88034" class="comments-container">
<span id="88036"></span>
<div id="comment-88036" class="comment">
<div id="post-88036-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good points frodeseverin on the rendering. NOTE Newer users may expect routing to be quick but in my experience even though the road or path shows on mapnik routers will need a three to five days to react to an edit.</p>
</div>
<div id="comment-88036-info" class="comment-info">
<span class="comment-age">(30 Nov '23, 22:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-88034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88034-form-container" class="comment-form-container">
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

