+++
type = "question"
title = "How to mark a Dutch &quot;Fietsstraat&quot;"
description = '''Relevant: https://help.openstreetmap.org/questions/39500/dutch-cycle-paths-with-cars-as-guests The traffic sign: https://www.informatiebord.nl/oefenen/verkeersborden-overzicht/2335/l51-fietsstraat/ Example: https://www.openstreetmap.org/way/251672751#map=15/51.4572/5.4427 The example, and more towar...'''
date = "2018-09-20T17:41:00Z"
lastmod = "2018-09-26T07:39:00Z"
weight = 65994
keywords = [ "cycling", "highway", "tagging", "fietsstraat" ]
aliases = [ "/questions/65994" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to mark a Dutch "Fietsstraat"](/questions/65994/how-to-mark-a-dutch-fietsstraat)

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
<span id="post-65994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65994-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Relevant: <a href="https://help.openstreetmap.org/questions/39500/dutch-cycle-paths-with-cars-as-guests">https://help.openstreetmap.org/questions/39500/dutch-cycle-paths-with-cars-as-guests</a></p>
<p>The traffic sign: <a href="https://www.informatiebord.nl/oefenen/verkeersborden-overzicht/2335/l51-fietsstraat/">https://www.informatiebord.nl/oefenen/verkeersborden-overzicht/2335/l51-fietsstraat/</a></p>
<p>Example: <a href="https://www.openstreetmap.org/way/251672751#map=15/51.4572/5.4427">https://www.openstreetmap.org/way/251672751#map=15/51.4572/5.4427</a></p>
<p>The example, and more toward the north west, is a Fietsstraat. Both bicycles and cars are allowed, but it's mostly a cycling path, not a car street. Visually it's exactly like other (real) car streets, not like a cycling path. In this case that's confusing. Is that how OSM works? If cars are allowed, it looks like a car street? Or does it look like that because <code>highway=residential</code>? Maybe removing <code>highway</code> is better?, since there's also a <code>motor_vehicle=destination</code>? Or is <code>motor_vehicle</code> only a subspecification of <code>highway</code>?</p>
<p>Technically the example is correct, because both cars and cyclists are allowed, but the visuals are confusing. Almost all streets are both cars and cyclists, but Fietsstraat are really different.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cycling" rel="tag" title="see questions tagged &#39;cycling&#39;">cycling</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-fietsstraat" rel="tag" title="see questions tagged &#39;fietsstraat&#39;">fietsstraat</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '18, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f620e1b87dcc174d33bba9c919f2ed77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="De%20Rudie2&#39;s gravatar image" />
<p><span>De Rudie2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="De Rudie2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '18, 10:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-65994" class="comments-container">
<span id="66000"></span>
<div id="comment-66000" class="comment">
<div id="post-66000-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Don't remove the <code>highway</code> tag. This tag is necessary for all routable ways, regardless of whether they are for cars, bicycles or pedestrians.</p>
</div>
<div id="comment-66000-info" class="comment-info">
<span class="comment-age">(21 Sep '18, 08:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65994-form-container" class="comment-form-container">
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

<span id="65995"></span>

<div id="answer-container-65995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65995-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bicycle roads are, surprise, tagged as bicycle roads see <a href="https://wiki.openstreetmap.org/wiki/Key:bicycle_road">https://wiki.openstreetmap.org/wiki/Key:bicycle_road</a></p>
<p>If this really fits from a legal pov you would need to discuss with the NL-community (the wiki seems to indicate that actually using bicycle_road is not common in NL, but rules of the road change and it may simply be that the wiki is out of date).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '18, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '18, 18:52</strong> </span></p>
</div>
</div>
<div id="comments-container-65995" class="comments-container">
<span id="65996"></span>
<div id="comment-65996" class="comment">
<div id="post-65996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, but I'm mostly curious about the style/rendering. When is a road rendered like a bicycle path and when like a car street etc? The example URL makes no distinction in this case. Maptiler does, somehow: <a href="https://www.maptiler.com/maps/#bright//raster/14.84/5.44754/51.45376">https://www.maptiler.com/maps/#bright//raster/14.84/5.44754/51.45376</a> and even more differences around there. That's OSM data too, isn't it?</p>
</div>
<div id="comment-65996-info" class="comment-info">
<span class="comment-age">(20 Sep '18, 19:44)</span> <span class="comment-user userinfo">De Rudie2</span>
</div>
</div>
<span id="65997"></span>
<div id="comment-65997" class="comment">
<div id="post-65997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And when I edit tags, how do I see the result?, to be sure OSM understands what I'm trying to convey. So many tags. So many many ways to render.</p>
</div>
<div id="comment-65997-info" class="comment-info">
<span class="comment-age">(20 Sep '18, 19:47)</span> <span class="comment-user userinfo">De Rudie2</span>
</div>
</div>
<span id="65998"></span>
<div id="comment-65998" class="comment">
<div id="post-65998-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>You are adding to the OpenStreetMap -database-, rendering is completely independent and up to the creators of the individual map styles.</p>
<p>I would assume that for non-specialist maps you will simply get the rendering of the highway type, specialist maps may so it differently.</p>
</div>
<div id="comment-65998-info" class="comment-info">
<span class="comment-age">(20 Sep '18, 20:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66001"></span>
<div id="comment-66001" class="comment">
<div id="post-66001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The standard map style on OSM has no strong preference for bicycle tags. It tries to show a map that is useful for all users (pedestrians, cyclists and motorists). An OSM-based map specialized for (NL) cyclists will choose a different rendering style with a stronger preference for showing bicycle tags. Either way, make sure to apply the correct <em>tags</em> as described in the OSM wiki, <em>independent of the rendering</em>.</p>
</div>
<div id="comment-66001-info" class="comment-info">
<span class="comment-age">(21 Sep '18, 08:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66003"></span>
<div id="comment-66003" class="comment not_top_scorer">
<div id="post-66003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM has their own map tiles, so there's probably some kind of standard. It's not JUST a db. I can add 30 tags that aren't recognized anywhere, or 2 that all map tile makers use. There must be some convention.</p>
</div>
<div id="comment-66003-info" class="comment-info">
<span class="comment-age">(21 Sep '18, 15:36)</span> <span class="comment-user userinfo">De Rudie2</span>
</div>
</div>
<span id="66018"></span>
<div id="comment-66018" class="comment not_top_scorer">
<div id="post-66018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are certain tagging guidelines in the OSM wiki and there is common practice. These "standards" mainly apply to <em>tags</em>. For <em>rendering</em> (of which we are really talking here, aren't we?) there can't be a strict standard. A bicycle map will look completely different than a hiking map, both will omit certain features. And OSM's standard map style is more like a general purpose style, also omitting certain features. If you add bicycle tags that aren't rendered on the standard style then take a look at specific bicycle maps (see <a href="https://wiki.openstreetmap.org/wiki/Bicycle#See_also">Bicycle -&gt; See also</a> and <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services#Biking.2C_geocaching.2C_hiking.2C_sport">List of OSM-based services -&gt; Biking, geocaching, hiking, sport</a>). Always remember, <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">don't tag for the renderer</a>.</p>
</div>
<div id="comment-66018-info" class="comment-info">
<span class="comment-age">(22 Sep '18, 08:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66025"></span>
<div id="comment-66025" class="comment">
<div id="post-66025-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's worth noting that cycle.travel prioritises fietsstraats tagged with one of the above when planning routes (it wouldn't surprise me if CycleStreets does, too). So the common tags <em>are</em> used and it's definitely worth adding them, even if the default openstreetmap-carto style doesn't show anything.</p>
</div>
<div id="comment-66025-info" class="comment-info">
<span class="comment-age">(23 Sep '18, 19:49)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="66049"></span>
<div id="comment-66049" class="comment not_top_scorer">
<div id="post-66049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>according to one of the <a href="https://forum.openstreetmap.org/viewtopic.php?pid=712830#p712830">comments</a> in the topic in the Dutch forum, there is an essential difference between bicycle road and cyclestreet. The former (German bicycle road) does not allow other traffic unless indicated. This is not the case for the Dutch and Belgian Fietsstraten (cyclestreets).</p>
</div>
<div id="comment-66049-info" class="comment-info">
<span class="comment-age">(26 Sep '18, 06:24)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-65995" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65995-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65999"></span>

<div id="answer-container-65999" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65999-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Dutch and Belgian communities use either cyclestreet=yes or cycleway=cyclestreet in addition to (typically) highway=residential.</p>
<p>This is explained on <a href="https://wiki.openstreetmap.org/wiki/Bicycle_tags_map,">https://wiki.openstreetmap.org/wiki/Bicycle_tags_map,</a> which is the legend for a Dutch map on cycling tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '18, 05:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-65999" class="comments-container">
<span id="66002"></span>
<div id="comment-66002" class="comment">
<div id="post-66002-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Wow, even more wikis... There are so many wiki pages about almost the same thing, with different info =(</p>
</div>
<div id="comment-66002-info" class="comment-info">
<span class="comment-age">(21 Sep '18, 15:35)</span> <span class="comment-user userinfo">De Rudie2</span>
</div>
</div>
<span id="66017"></span>
<div id="comment-66017" class="comment">
<div id="post-66017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that <a href="https://wiki.openstreetmap.org/wiki/Bicycle_tags_map">bicycle tags map</a> is not a tagging guideline! This page only explains which tags this specific map recognizes. These tags <em>should</em> but <em>don't have to</em> match OSM tagging guidelines.</p>
</div>
<div id="comment-66017-info" class="comment-info">
<span class="comment-age">(22 Sep '18, 08:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66048"></span>
<div id="comment-66048" class="comment">
<div id="post-66048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are 2 topics on the Dutch forum about "Fietsstraten"</p>
<ul>
<li><a href="https://forum.openstreetmap.org/viewtopic.php?id=63473">https://forum.openstreetmap.org/viewtopic.php?id=63473</a></li>
<li><a href="https://forum.openstreetmap.org/viewtopic.php?pid=709379#p709379">https://forum.openstreetmap.org/viewtopic.php?pid=709379#p709379</a></li>
</ul>
<p>a.o. they refer to <a href="https://wiki.openstreetmap.org/wiki/Key:cyclestreet">https://wiki.openstreetmap.org/wiki/Key:cyclestreet</a></p>
</div>
<div id="comment-66048-info" class="comment-info">
<span class="comment-age">(26 Sep '18, 06:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="66050"></span>
<div id="comment-66050" class="comment">
<div id="post-66050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>, I should have mentioned the cyclestreet page in my answer instead.</p>
</div>
<div id="comment-66050-info" class="comment-info">
<span class="comment-age">(26 Sep '18, 06:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="66051"></span>
<div id="comment-66051" class="comment">
<div id="post-66051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> Maybe, or both should have been mentioned. However this was just a hint at De Rudie2 and a response to "even more wikis" :)</p>
</div>
<div id="comment-66051-info" class="comment-info">
<span class="comment-age">(26 Sep '18, 07:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65999-form-container" class="comment-form-container">
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

