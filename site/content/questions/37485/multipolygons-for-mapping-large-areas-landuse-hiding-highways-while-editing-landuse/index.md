+++
type = "question"
title = "Multipolygons for mapping large areas landuse /  hiding highways while editing landuse"
description = '''Hello, I&#x27;m new to openstreetmap. I&#x27;m starting to map in my town which is in a rural area with lots of unmapped area. Its comprised of forest broken up with scattered houses and farmland. I have a few questions:   Are multipolygons easy to edit? I was thinking about drawing out large tracts of forest...'''
date = "2014-10-10T11:47:00Z"
lastmod = "2014-10-11T00:51:00Z"
weight = 37485
keywords = [ "nature_reserve", "multipolygon" ]
aliases = [ "/questions/37485" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multipolygons for mapping large areas landuse / hiding highways while editing landuse](/questions/37485/multipolygons-for-mapping-large-areas-landuse-hiding-highways-while-editing-landuse)

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
<span id="post-37485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37485-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm new to openstreetmap. I'm starting to map in my town which is in a rural area with lots of unmapped area. Its comprised of forest broken up with scattered houses and farmland. I have a few questions:</p>
<ul>
<li><p>Are multipolygons easy to edit? I was thinking about drawing out large tracts of forests and then subdividing the smaller polygons of residential and farmland within using multipolygons. Or is it better to break up the forest into smaller polygons the share borders with farmland and residential areas? I think I tried to edit a multipolygon and got some relation errors, but maybe that once get a hang of them they are ok to work with?</p></li>
<li><p>I use JOSM for editing. Is there a plugin or setting to hide highways? I was hoping to be able to hide highways while drawing landuse polygons.</p></li>
<li><p>Is there a good way to make the boundaries of forested nature reserves easily visible? I have been trying to look around at other countries to see how its done. The leisure=nature reserve border is a light dashed green line (which is used in Sweden, I believe). If the area within and around the nature reserve is tagged as landuse=forest, then the nature reserve border is not easily visible. It seems like the nature reserve border should be something that stands out at all zoom levels.</p></li>
</ul>
<p>I will likely ask around in sweden forum as well to see how others are doing things. It seems like there is a few different places to ask questions: IRC, help, forum, mailing list.</p>
<p>Thanks for help</p>
<p>seahik</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nature_reserve" rel="tag" title="see questions tagged &#39;nature_reserve&#39;">nature_reserve</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '14, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fdf9c1412cde7c351e48ea138c737351?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sea%20hik&#39;s gravatar image" />
<p><span>sea hik</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sea hik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '14, 12:04</strong> </span></p>
</div>
</div>
<div id="comments-container-37485" class="comments-container">
<span id="37487"></span>
<div id="comment-37487" class="comment">
<div id="post-37487-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As for your second point, JOSM has <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/Filter">filters</a> Create one with just highway=* (or even just highway, can't test it right now)</p>
</div>
<div id="comment-37487-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 12:55)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="37488"></span>
<div id="comment-37488" class="comment not_top_scorer">
<div id="post-37488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>as for your third point, where do you want to make it visible ? In JOSM ? Then you can use <a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSTutorial">MapCSS</a></p>
</div>
<div id="comment-37488-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 12:58)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="37489"></span>
<div id="comment-37489" class="comment">
<div id="post-37489-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Escada - Thank you for the filter. Seems to work great. Would you by chance know if the filter disables any underlying snapping behaviour to the hidden elements. I would like to hide the highways and avoid snapping to them when drawing landuse polygons.</p>
<p>For my third question, I was referring to how things appear on the Standard layer on OSM.</p>
</div>
<div id="comment-37489-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 13:37)</span> <span class="comment-user userinfo">sea hik</span>
</div>
</div>
<span id="37490"></span>
<div id="comment-37490" class="comment">
<div id="post-37490-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think it avoids snapping, to avoid snapping you can also use CTRL-click.</p>
<p>You cannot change the appearance of the standard layer, without modifying the underlying style file. You can always ask the maintainers whether they want to do this. The place to do that is <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">github</a></p>
</div>
<div id="comment-37490-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 14:05)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="37491"></span>
<div id="comment-37491" class="comment">
<div id="post-37491-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For your 1st point, I suggest that you don't make them too big, cumbersome and complex otherwise a new mapper will not be able to confidently edit anything in the area lest he breaks something. KISS is in general a good principle to apply.</p>
</div>
<div id="comment-37491-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 14:16)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="37492"></span>
<div id="comment-37492" class="comment">
<div id="post-37492-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nevw - that makes sense, thanks. By the way, would you happen to know if mapping landuse is in general a lower priority in osm?</p>
</div>
<div id="comment-37492-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 14:23)</span> <span class="comment-user userinfo">sea hik</span>
</div>
</div>
<span id="37494"></span>
<div id="comment-37494" class="comment not_top_scorer">
<div id="post-37494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On the "where to contact" question - different country and language communities tend to use different mechanisms (mailing lists, the forum, IRC, Facebook Groups and more). With IRC though, you may need to hang around for a 10 minutes or so to get an answer.</p>
</div>
<div id="comment-37494-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 14:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37495"></span>
<div id="comment-37495" class="comment not_top_scorer">
<div id="post-37495-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Individual mappers decide their own priorities and preferences. I find land use is often difficult to ascertain - managed forest or wood or wildlife reserve? Boundaries are also difficult to define, even with satellite imagery or looking over an area from the boundary. Whereas other elements like roads and buildings are more easily checked during a gps survey in person.</p>
</div>
<div id="comment-37495-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 15:14)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="37497"></span>
<div id="comment-37497" class="comment not_top_scorer">
<div id="post-37497-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>re OSM's priorities: There is no one priority for OSM--some people map everything in an area, while others focus on one specific kind of feature. I have definitely seen people focus on landuse--I think it esp appeals to people who loved SimCity :) Personally, after the transportation network, I think POIs and addresses are the info we could add which would create more value for people than landuse. But I add plenty of obscure things, too! Scratch your itch.</p>
</div>
<div id="comment-37497-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 15:22)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-37485" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-37485-form-container" class="comment-form-container">
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

<span id="37493"></span>

<div id="answer-container-37493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37493-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi sea hik, avoid large areas or multipolygons, there have been some questions about them read these lines. Besides there’s a limit of 2000 on the amount of nodes used in a way (string or multipolygon). <a href="https://help.openstreetmap.org/search/?csrfmiddlewaretoken=jVfxwqdgjonh8Cj1qHBy7W8vdAXDXUXw&amp;q=multipolygon&amp;t=question">https://help.openstreetmap.org/search/?csrfmiddlewaretoken=jVfxwqdgjonh8Cj1qHBy7W8vdAXDXUXw&amp;q=multipolygon&amp;t=question</a> I would not make the make a forest multi larger than necessary and use every path or track to make another parcel just as nevw stated. Avoid connecting forest borders to the way next to it, leave some space in between. It ain't forest but the border lines are separated just to let the water in. The first imports shared the connecting borders you will have to split them manually. <a href="http://www.openstreetmap.org/#map=17/52.48683/4.82834">http://www.openstreetmap.org/#map=17/52.48683/4.82834</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '14, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-37493" class="comments-container">
<span id="37500"></span>
<div id="comment-37500" class="comment">
<div id="post-37500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is incredible detail on your linked map. When I started mapping near me, I was re-using highway nodes for landuse. But I've since gone in a manually changed them all to be separate. It almost seems like landuse should be a separate layer in osm from highways.</p>
<p>I still struggle with decision on whether to make all my landuse polygons share borders with each other. It seems strange to leave small gaps of undesignated landuse, like for example when landuse crosses a road.</p>
</div>
<div id="comment-37500-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 15:47)</span> <span class="comment-user userinfo">sea hik</span>
</div>
</div>
<span id="37507"></span>
<div id="comment-37507" class="comment">
<div id="post-37507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not leave gaps. What is the reality ? E.g. Does the forest ends where the farmland begins ? If so, why would you leave a gap ? It's different when they are separated by a road</p>
</div>
<div id="comment-37507-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 20:31)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="37509"></span>
<div id="comment-37509" class="comment">
<div id="post-37509-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi remember how roads were created, in between 2 parcels. Farmers / owners did not want to lose fertile soil to a way. Neither is a road ploughed, except a right of way. Remember OSM is schematic. The roadside or shoulder could be used for harvesting grass by another farmer. Landuse borders join the ditch all together, sometimes even with a fence in the middle. Forest parcels could join borders, separate them if necessary ! Make up your mind, look in the neighborhood / forum, have fun and keep mapping.</p>
</div>
<div id="comment-37509-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 21:00)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="37510"></span>
<div id="comment-37510" class="comment">
<div id="post-37510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>escada - its landuse around roads that I meant. I've seen people leave a gap near the road. But I've decided to attach the landuse edge to the landuse edge that starts on otherside of road. In otherwords not leaving a gap. Not sure if thats best way or not. I'll keep checking in to see how others are doing it near me.</p>
</div>
<div id="comment-37510-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 21:42)</span> <span class="comment-user userinfo">sea hik</span>
</div>
</div>
<span id="37511"></span>
<div id="comment-37511" class="comment">
<div id="post-37511-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Along with Hendrick I also want to encourage you to keep those multipolygons small as they will be much easier to manage later. There are a number of wood multipolygons I work with here in northern Thailand, one of which is nearing 700 individual pieces. Every time I work on one of these monsters I must download the entire thing so as to be sure any changes I make are being done correctly. This is a good time to take a coffee break. Splitting a large multipolygon into smaller, more user-friendly pieces later is quite a chore.</p>
</div>
<div id="comment-37511-info" class="comment-info">
<span class="comment-age">(11 Oct '14, 00:51)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="37512"></span>
<div id="comment-37512" class="comment not_top_scorer">
<div id="post-37512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As for shared boundaries, it seems I am always looking for some sort of natural boundary where big multipolygons can be split so I recommend not sharing. Roads and rivers are places where landuse or forest multipolygons are naturally divided and the OSM should reflect that. Separating those boundaries later, should that become necessary, is another big chore that can be avoided by taking a little extra time initially.</p>
<p>By the way, the Make Parallel Copies of Ways add on in JOSM is an easy way to create those separate boundaries. I use it all the time for boundaries and riverbanks.</p>
<p>Cheers</p>
</div>
<div id="comment-37512-info" class="comment-info">
<span class="comment-age">(11 Oct '14, 00:51)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37493" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-37493-form-container" class="comment-form-container">
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

