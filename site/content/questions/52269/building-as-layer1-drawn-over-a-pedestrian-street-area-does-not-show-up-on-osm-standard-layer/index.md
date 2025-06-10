+++
type = "question"
title = "Building as layer=1 drawn over a pedestrian street area does not show up on OSM-Standard layer"
description = '''Hi, I have a building, an historic monument (old tower), standing in the middle of a public square. Here it is : https://www.openstreetmap.org/way/83785370  The square is mapped with highway=pedestrian and area=yes.  The building is mapped with building=yes and layer=1.  But the renderer does not sh...'''
date = "2016-09-28T10:16:00Z"
lastmod = "2022-03-05T16:56:00Z"
weight = 52269
keywords = [ "building", "pedestrian", "layer", "mapnik", "area" ]
aliases = [ "/questions/52269" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Building as layer=1 drawn over a pedestrian street area does not show up on OSM-Standard layer](/questions/52269/building-as-layer1-drawn-over-a-pedestrian-street-area-does-not-show-up-on-osm-standard-layer)

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
<span id="post-52269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52269-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
I have a building, an historic monument (old tower), standing in the middle of a public square.<br />
Here it is : <a href="https://www.openstreetmap.org/way/83785370">https://www.openstreetmap.org/way/83785370</a></p>
<p>The square is mapped with highway=pedestrian and area=yes.<br />
The building is mapped with building=yes and layer=1.</p>
<p>But the renderer does not show the building, and it keeps being drawn UNDER the highway.<br />
Is ther a bug, or am I missing something else ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '16, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/86072009837505c7d34dbc551ac5b31e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Romainbou&#39;s gravatar image" />
<p><span>Romainbou</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Romainbou has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52269" class="comments-container">
&#10;</div>
<div id="comment-tools-52269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52269-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="52372"></span>

<div id="answer-container-52372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52372-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In a related question somewhere around here (?) it was explained that the crucial thing is the "highway" tag here. ALL highways get forced priority over everything else, no matter any layers, no matter if it's just a pedestrian square. Even tunnels are painted ABOVE everything else, just in another style (dashed).<br />
Buildings usually have an automatic higher priority too, just not over highways. Highways always win, no matter what. Because streets would vanish if in far zooms buildings would be painted over them with a higher priority.</p>
<p>Things get especially tricky if not even a multipolygon helps anymore, if buildings still do not show up! For example a church in a pedestrian area, cut out correctly by an MP. Have seen such a case, and the reason was: The pedestrian tag was not only in the relation, but ALSO still on the outer square way! Removing it from there finally unearthed the building.</p>
<p>This is funny, because this prob with tagged outer ways is usually auto-corrected by Mapnik. Usually only less powerful apps, like Mapsforge (offline vector maps), start showing nonsense if outers are tagged, causing crazy forest floods etc. People just don't notice this dangerous prob because Mapnik does so much self-repairing and guessing and nearly always successful. Obviously highways areas are the only exception where even Mapnik still trips over that mix of old-style-new-style MP mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '16, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1d0a9b10a28fd4ae36b38b5fbcc534d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wycbtma&#39;s gravatar image" />
<p><span>wycbtma</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wycbtma has one accepted answer">33%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52372" class="comments-container">
&#10;</div>
<div id="comment-tools-52372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52277"></span>

<div id="answer-container-52277" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52277-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The area where the tower is located is NOT part of the pedestrian area. You need to make the pedestrian area a relation with the building=tower as an inner. This models the actual situation more accurately than at present.</p>
<p>In the past the way in which buildings and pedestrian areas were rendered did show buildings mapped in the way described. I dont think the layer tag is necessarily that significant; CartoCSS uses area size as well when determining whether to render which areas on top of others. Changes were made to the layering some time ago (at least as far back as 2014 because I remember being puzzled about the same thing at the time of Wikimania in London). See the relevant issue on <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/688">github</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '16, 09:08</strong> </span></p>
</div>
</div>
<div id="comments-container-52277" class="comments-container">
&#10;</div>
<div id="comment-tools-52277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52277-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52271"></span>

<div id="answer-container-52271" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52271-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Romainbou, there is no mistake the pedestrian tag covers everything else at the same spot. The tower has a tag layer=1 why ? Because it is a tower and you could walk through ? If so, tag the short stretch of the way beneath or inside the tower with tunnel=building_passage and make a connection to some of the roads around the pedestrian area. And delete the layer=1 tag. The method thats used to draw the highway=pedestrian is confusing, it covers the living streets, it should not be drawn over ways besides it, but next to the excisting infrastructure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-52271" class="comments-container">
<span id="52273"></span>
<div id="comment-52273" class="comment">
<div id="post-52273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your answer Hendrik,<br />
No, you can not walk under the tower: it's a closed buiding that you can't enter in.<br />
The issue is that the building is not displayed by mapnik/OSM-Standard map. So I tried to add the tag layer=1, to see if it will be displayed above the pedestrian area.<br />
Actually I was searching for other examples of buildings built in the middle of pedestrian places, and I figured out that they are usually mapped using multipolygons. It seems that you have to make a "hole" inside your highway=pedestrian, and fill it with the building.<br />
See for example : <a href="http://www.openstreetmap.org/relation/556816#map=19/48.86143/2.35226">http://www.openstreetmap.org/relation/556816#map=19/48.86143/2.35226</a><br />
I have been told to try replacing area=yes by place=square. But it does not seems to work either.<br />
And using OverpassTurbo, I saw that very very few place=square are used in France. weird.<br />
With this work, the building does not overlap with any other area and is thus rendered correctly.<br />
I think it should be simpler to allow it to render it using layer=1, but maybe there are good reasons.</p>
</div>
<div id="comment-52273-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 11:16)</span> <span class="comment-user userinfo">Romainbou</span>
</div>
</div>
<span id="52274"></span>
<div id="comment-52274" class="comment">
<div id="post-52274-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Go for the multipolygone, you should not tag +1 to get the building visible, it looks like tagging for the renderer :-( By using the multi polygone method, the tower is getting a special treatment, since there only a few buildings mapped by that method inside a area.</p>
</div>
<div id="comment-52274-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 12:38)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="52275"></span>
<div id="comment-52275" class="comment">
<div id="post-52275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. It's weird because in my opinion, I think this way of making the multipolygon IS the "tagging for the renderer" way! :) I am currently reading the main topic about the issue discussed on github : <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/688">https://github.com/gravitystorm/openstreetmap-carto/issues/688</a> and it looks like it's not solved and they don't find a way to treat it.</p>
</div>
<div id="comment-52275-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 13:02)</span> <span class="comment-user userinfo">Romainbou</span>
</div>
</div>
<span id="52376"></span>
<div id="comment-52376" class="comment">
<div id="post-52376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Couldn't resist... after studying again through that bugdiscussion 688 on github, and fighting with myself some hours, finally tested a tiny tag change on the square under Eiffel Tower. Wouldn't argue if one of the experts prefers to change it back again, but what makes me really wonder is that strange pedestrian relation: one big rectangle and then the whole middle part cut out as "inner", thus faking 2 outers?? Shouldn't that rather be just 3 independant parts, no relation necessary at all?</p>
<p>And found two other interesting pedestrian areas:<br />
<a href="http://tools.geofabrik.de/mc/#18/46.9485/7.4368&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap">http://tools.geofabrik.de/mc/#18/46.9485/7.4368&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap</a> <a href="http://tools.geofabrik.de/mc/#18/47.3584/8.5235&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap">http://tools.geofabrik.de/mc/#18/47.3584/8.5235&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap</a></p>
</div>
<div id="comment-52376-info" class="comment-info">
<span class="comment-age">(06 Oct '16, 02:37)</span> <span class="comment-user userinfo">wycbtma</span>
</div>
</div>
</div>
<div id="comment-tools-52271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52271-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83646"></span>

<div id="answer-container-83646" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83646-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am also confused by this fact that pedestrian area always drawn over everything else. I created a building that is over a pedestrian area. It is called "Piloti". The building over the pedestrian area doesn't show on OSM-standard-layer. The building shows on OSM-cyclemap-layer.</p>
<p><a href="http://tools.geofabrik.de/mc/#18/36.5636/139.8827&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap">http://tools.geofabrik.de/mc/#18/36.5636/139.8827&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '22, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08f7ac2db31d66e3efdd3a33fe0e7e22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yasobara&#39;s gravatar image" />
<p><span>yasobara</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yasobara has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-83646" class="comments-container">
<span id="83650"></span>
<div id="comment-83650" class="comment">
<div id="post-83650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think your example is only showing on the Cyclemap layer as it isn't rendering the invalid multipolygon relation <a href="https://www.openstreetmap.org/relation/13039524">https://www.openstreetmap.org/relation/13039524</a> with inner <a href="https://www.openstreetmap.org/way/691943195">https://www.openstreetmap.org/way/691943195</a> touching outer <a href="https://www.openstreetmap.org/way/969085164">https://www.openstreetmap.org/way/969085164</a> as one possible issue.</p>
</div>
<div id="comment-83650-info" class="comment-info">
<span class="comment-age">(04 Mar '22, 19:33)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83646-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83672"></span>

<div id="answer-container-83672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fixed the invalid multipolygon relation you pointed out, but the renderings are still the same. <a href="http://tools.geofabrik.de/mc/#18/36.5636/139.8827&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap">http://tools.geofabrik.de/mc/#18/36.5636/139.8827&amp;num=2&amp;mt0=mapnik&amp;mt1=cyclemap</a></p>
<p>I think the issue is a pedestrian area being a highway and a priority over a building. I looked at the issue discussed on github : <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/688">https://github.com/gravitystorm/openstreetmap-carto/issues/688</a> and it looks like it's not solved since it's been first reported in 2014. I think it could be resolved if pedestrian area is defined as landuse rather than highway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '22, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/08f7ac2db31d66e3efdd3a33fe0e7e22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yasobara&#39;s gravatar image" />
<p><span>yasobara</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yasobara has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-83672" class="comments-container">
&#10;</div>
<div id="comment-tools-83672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83672-form-container" class="comment-form-container">
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

