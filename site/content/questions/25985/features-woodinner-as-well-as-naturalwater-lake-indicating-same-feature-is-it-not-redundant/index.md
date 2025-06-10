+++
type = "question"
title = "features:  Wood=inner as well as natural=water (Lake) indicating same feature, is it not redundant?"
description = '''Many lakes in my current mapping area are in thick forest. A Dataset uploaded recently (last year or so: NRCan-CanVec-10.0)has added the missing forest to the dataset/area among other features.  The lakes in question show both a body of water as a single feature tagged as natural=water, water=lake e...'''
date = "2013-08-31T02:11:00Z"
lastmod = "2013-09-23T15:19:00Z"
weight = 25985
keywords = [ "lake", "wood", "inner", "forest" ]
aliases = [ "/questions/25985" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [features: Wood=inner as well as natural=water (Lake) indicating same feature, is it not redundant?](/questions/25985/features-woodinner-as-well-as-naturalwater-lake-indicating-same-feature-is-it-not-redundant)

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
<span id="post-25985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Many lakes in my current mapping area are in thick forest. A Dataset uploaded recently (last year or so: NRCan-CanVec-10.0)has added the missing forest to the dataset/area among other features.</p>
<p>The lakes in question show both a body of water as a single feature tagged as natural=water, water=lake etc... but also have a separate feature associated with it that is usually offset a little from the body of water showing the end of the forest as white areas, and the only data referring to it is a tag saying wood=inner. Heres an example of what Im talking about: <a href="http://www.openstreetmap.org/#map=17/45.70116/-74.93533">http://www.openstreetmap.org/#map=17/45.70116/-74.93533</a></p>
<p>Perhaps this is a necessary mapping protocol as it indicates the end of a forested area, and the beginning of the lake? But to me it seems redundant as the lake already indicates that theres a lake and its in the forest no?</p>
<p>What I have done once already but it is very time consuming is trace the line/area tagged as wood=inner and connected it to every node of the lake so that they are in essence one and the same,</p>
<p>Is this a waste of time? cant i just delete the feature indicating wood=inner and simply have the lake?</p>
<p>Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-wood" rel="tag" title="see questions tagged &#39;wood&#39;">wood</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '13, 02:11</strong></p>
<img src="https://secure.gravatar.com/avatar/66001846f0632f073fa821d84341d7cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Azzitizz&#39;s gravatar image" />
<p><span>Azzitizz</span><br />
<span class="score" title="445 reputation points">445</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Azzitizz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25985" class="comments-container">
&#10;</div>
<div id="comment-tools-25985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25985-form-container" class="comment-form-container">
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

<span id="25989"></span>

<div id="answer-container-25989" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25989-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you have here is a work of two different mappers.</p>
<p>The first mapper mapped the forest and left holes in the forest (in this case the outline of the lake) but he neglected to tag it as a lake so if the lake from the dataset (in blue) was not uploaded, it would only show as a white hole.</p>
<p>Then, as you indicated the dataset was uploaded which has the outlines of the lake, but slightly different in shape, so it covers a part of the white hole but not entirely, so this narrow white area is the result of mapping the same lake twice, each of a different shape.</p>
<p>First you need to decide, which lake is correct, I guess the one from the dataset (in blue). Then you need to delete the other outline that created the white hole. Then the white narrow strip will disappear. To make everything correctly, you should then create a multipolygon relationship between the new lake and the forest.</p>
<p>Also, when you have a lake within the forest, you don't trace and connect every node around the lake to create a lake, as you suggested. Here are some examples how you do it. <a href="http://wiki.openstreetmap.org/wiki/Multipolygon_Examples">http://wiki.openstreetmap.org/wiki/Multipolygon_Examples</a></p>
<p>If you need help with this particular lake, I can show it to you step by step.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '13, 03:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06b9779157ed5d9958611cdc3b6aa4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slover98&#39;s gravatar image" />
<p><span>slover98</span><br />
<span class="score" title="567 reputation points">567</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slover98 has one accepted answer">5%</span></p>
</div>
</div>
<div id="comments-container-25989" class="comments-container">
<span id="25991"></span>
<div id="comment-25991" class="comment">
<div id="post-25991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>PS. I forgot, that you cannot do these multipolygon relationships with iD editor, I use Potlatch which is accessible from iD editor.</p>
</div>
<div id="comment-25991-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 04:22)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="25992"></span>
<div id="comment-25992" class="comment not_top_scorer">
<div id="post-25992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that explains alot. Are you sure you cant do the multipolygon relationships in iD? There seems to be an option to add tags and relations and polygons in the menu to add or change a feature, near the bottom...</p>
</div>
<div id="comment-25992-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 05:28)</span> <span class="comment-user userinfo">Azzitizz</span>
</div>
</div>
<span id="25995"></span>
<div id="comment-25995" class="comment not_top_scorer">
<div id="post-25995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure you need a multipolygon relation for small area within a large area when the large area is something else (rather than just a hole), or you'd then do things like an inner member for every building within a residential area.</p>
</div>
<div id="comment-25995-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 07:39)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="25996"></span>
<div id="comment-25996" class="comment not_top_scorer">
<div id="post-25996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>iD info <a href="https://help.openstreetmap.org/questions/22542/how-do-i-map-an-island-in-a-lake-using-id-editor-and-the-multipolygon-tag">https://help.openstreetmap.org/questions/22542/how-do-i-map-an-island-in-a-lake-using-id-editor-and-the-multipolygon-tag</a></p>
</div>
<div id="comment-25996-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 07:45)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="25998"></span>
<div id="comment-25998" class="comment">
<div id="post-25998-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>using relations <a href="https://help.openstreetmap.org/questions/14732/using-inner-and-outer-relations">https://help.openstreetmap.org/questions/14732/using-inner-and-outer-relations</a></p>
</div>
<div id="comment-25998-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 07:47)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="26004"></span>
<div id="comment-26004" class="comment not_top_scorer">
<div id="post-26004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>I prefer iD myself and I see the tags at the bottom but I don't see how you add relationships.</li>
<li>EdLoach...re...inner member for each building. Whenever I have an area within area I always do it via polygons. In terms of having many buildings, it is not that time consuming. Here is one of the areas I did recently: <a href="http://www.openstreetmap.org/#map=18/38.79449/-77.52220">http://www.openstreetmap.org/#map=18/38.79449/-77.52220</a></li>
</ol>
<p>When you tag each building parking etc when you create them then tags are are automatically added once you create relationships via Potlatch (the double square icon in the tool box), no need to do each building separately.</p>
</div>
<div id="comment-26004-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 10:34)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="26607"></span>
<div id="comment-26607" class="comment">
<div id="post-26607-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So it looks to me that iD has a way to add multipolygon tags, but I havent seen anyone spell it out yet. I think I got it for the quoted lake above, would someone be able to let me know if I got it right or not, and if not how it should be tagged properly?</p>
<p>I did notice now, I uploaded the map onto my garmin etrex 30 and the lake doesn't show up. it shows the forest at it tells me the lake is there when the cursor is in the area, it give s the name of the lake but its showing only forest. I think I changed it now.</p>
<p>Thanks for any help</p>
</div>
<div id="comment-26607-info" class="comment-info">
<span class="comment-age">(22 Sep '13, 03:43)</span> <span class="comment-user userinfo">Azzitizz</span>
</div>
</div>
<span id="26618"></span>
<div id="comment-26618" class="comment not_top_scorer">
<div id="post-26618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you can't do it in iD. iD just shows that there is a multipolygon. In order for this to work you need to create relationships between the outer ways and then inner ways, like lakes. The lake that you show is not part of any relationship perhaps that's the reason it does not render on some maps. Potlatch editor can be used to do this.</p>
</div>
<div id="comment-26618-info" class="comment-info">
<span class="comment-age">(22 Sep '13, 13:12)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="26627"></span>
<div id="comment-26627" class="comment">
<div id="post-26627-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, It looks like you can do it. Im just not sure if Im doing it right.</p>
<p>If I trace/create and area within a wooded area, using iD, in the menu on the left, theres an option to add relations. When you click on it a new menu comes up and adding a multipolygon is one of the options you can select.</p>
<p>Now where im a little lost is how to enter the data properly.</p>
<p>Can anyone confirm or clarify this?</p>
</div>
<div id="comment-26627-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 02:23)</span> <span class="comment-user userinfo">Azzitizz</span>
</div>
</div>
<span id="26648"></span>
<div id="comment-26648" class="comment">
<div id="post-26648-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What you need to do is make the lake's way part of the "wood" multipolygon relation (2581595), and give it the role "inner". You can remove the "lake" multipolygon relation (3166167), as it is unnecessary (since the lake doesn't have an island, etc inside it). Although you <em>can</em> edit relations in iD, I would recommend you do so in Potlatch 2, as I find it much easier to understand what's going on (you just need to switch to the Advanced view at the bottom left).</p>
</div>
<div id="comment-26648-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 15:19)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-25989" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25989-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26634"></span>

<div id="answer-container-26634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From my point of view (or, from a vector-mapping point of view) the source data presentation is absolutely correct as described. The forest's multi-polygon border area presentation tells us that in the hole there is no forest (simply, we don't know what is there). The lake area data layer tells us that there is a lake in that particular hole. Whether the lake's border is exactly the same (just a reference to) or slightly inside the hole's border (quite natural) is right now irrelevant. There are several arguments supporting this view:</p>
<ul>
<li>The suggested overlap of the lake-area over the forest area (with no hole) assumes a particular rendering order (first forests so lakes) typical for raster mapping systems. This is in conflict with the basic motto of OSM "we don't tag for renderers". Besides, this would be just an inverse of the frequent forest-over-water (lakes, rivers, sea) cases.</li>
<li>In vector mapping systems we do much more than just viewing map images. Switching on and off, moving up and down data layers, estimating area sizes... all would be wrong with the suggested overlaps. And so on.</li>
</ul>
<p>So, my general suggestion could be: insert/upload an area with a multi-polygon borders definition (in this case, the forest). If needed, insert/upload a new area (in this case, the lake) into the hole independently from the former area class (but of cause, you may just refer to the holes border polygon).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-26634" class="comments-container">
<span id="26639"></span>
<div id="comment-26639" class="comment">
<div id="post-26639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>" Whether the lake's border is exactly the same (just a reference to) or slightly inside the hole's border (quite natural) is right now irrelevant."</p>
<p>I think it is relevant as this was the essence of the question.</p>
</div>
<div id="comment-26639-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 10:38)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="26641"></span>
<div id="comment-26641" class="comment">
<div id="post-26641-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, no. The question was "cant i just delete the feature indicating wood=inner and simply have the lake?". In other words, just have a lake overlapping the forest (with no hole under it). My answer was critical to this solution compared to that having a hole and a new area object (lake) in that hole (as it was in the source data). By the way, if you study the corresponding aerial photo and other images of that lake you will see that the forest does not go down to the water edge on many places (a natural event). Probably, to show these stripes was the motivation to the local editor.</p>
</div>
<div id="comment-26641-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 13:25)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-26634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26634-form-container" class="comment-form-container">
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

