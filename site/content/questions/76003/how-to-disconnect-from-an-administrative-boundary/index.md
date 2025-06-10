+++
type = "question"
title = "How to disconnect from an administrative boundary?"
description = '''I&#x27;m trying to edit the area here https://www.openstreetmap.org/edit?editor=id#map=17/42.86431/22.57677 because the border between the heath and forest areas north of the boundary stone named Руй on the Bulgarian side of the border is wrong. The forest area appears to be connected to the Administrati...'''
date = "2020-08-04T17:41:00Z"
lastmod = "2020-08-06T18:46:00Z"
weight = 76003
keywords = [ "disconnecting" ]
aliases = [ "/questions/76003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to disconnect from an administrative boundary?](/questions/76003/how-to-disconnect-from-an-administrative-boundary)

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
<span id="post-76003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76003-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to edit the area here <a href="https://www.openstreetmap.org/edit?editor=id#map=17/42.86431/22.57677">https://www.openstreetmap.org/edit?editor=id#map=17/42.86431/22.57677</a> because the border between the heath and forest areas north of the boundary stone named Руй on the Bulgarian side of the border is wrong. The forest area appears to be connected to the Administrative Boundary, so I would like to disconnect it so I can expand the heath area. However, at the boundary stone, I can't disconnect because the point is part of a relation, while the other points on the administrative boundary can't be disconnected because "there aren't enough lines/areas to disconnect here" (i.e. the look connected but they aren't?). How to make this edit?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disconnecting" rel="tag" title="see questions tagged &#39;disconnecting&#39;">disconnecting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '20, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/8485f01f7d674ebb41d4af742bee2b30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rhhsmits&#39;s gravatar image" />
<p><span>rhhsmits</span><br />
<span class="score" title="3 reputation points">3</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rhhsmits has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76003" class="comments-container">
&#10;</div>
<div id="comment-tools-76003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76003-form-container" class="comment-form-container">
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

<span id="76011"></span>

<div id="answer-container-76011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>A quick warning first:</strong> This forest area is tagged as <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest"><code>landuse=forest</code></a>, this can include forests managed for things like paper production where areas may be clear-cut and re-seeded. Recently cut or seeded areas are generally considered to still be part of this kind of landuse.</p>
<p><strong>Assuming that's not the case here:</strong></p>
<p><a href="https://www.openstreetmap.org/relation/2410903">This forest</a> and <a href="https://www.openstreetmap.org/relation/2409040">heath</a> are mapped as part of multipolygons. These are relations used to describe more complex areas made up of several different ways. In this case <a href="https://www.openstreetmap.org/way/397592575">the border line</a> was used as one of the outer ways of the forest multipolygon so the forest doesn't have dedicated geometry here.</p>
<p>A good description of how multipolygons work is <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">here on the wiki</a>.</p>
<p>This is quite a large edit for one session in iD. You are probably better off using something like <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a>. JOSM can view a way this long without dropping out of edit mode and has a relation window that displays relations in a better format (closer to the way they are described and stored).</p>
<p>If you use iD:</p>
<p>The easiest way to correct the forest geometry is probably to:</p>
<ul>
<li>Add a node to the <a href="https://www.openstreetmap.org/way/653106665">way shared by the heath and forest</a> at the point where the forest breaks away from the existing line.</li>
<li>Split the way at this point.</li>
<li>If you now select the way to the left of the new split and scroll down on the left panel you will be able to delete the way from the forest relation (iD describes it a little backwards).</li>
<li>You can also now delete the border way from the forest relation.</li>
<li>Now draw a new way from the split you created to the other end of the border way following the edge of the forest</li>
<li>Add the new way to the (correct) forest relation using the + symbol under the relations heading in the left panel.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '20, 00:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '20, 00:17</strong> </span></p>
</div>
</div>
<div id="comments-container-76011" class="comments-container">
<span id="76012"></span>
<div id="comment-76012" class="comment">
<div id="post-76012-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Editing relations like this is a good reason to avoid using iD. It's tricky enough doing it in JOSM, especially if you are new to relations. Using the Relation Toolbox inside JOSM makes these sorts of operations much easier but it still takes some practice.</p>
<p>My 2 cents</p>
</div>
<div id="comment-76012-info" class="comment-info">
<span class="comment-age">(05 Aug '20, 00:38)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="76014"></span>
<div id="comment-76014" class="comment">
<div id="post-76014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your replies! I think I'll read a bit more about relations and JOSM, because I might mess up if I don't :) Here's a picture of the actual area that I took yesterday morning. <a href="https://commons.wikimedia.org/wiki/File:View_from_Ruj_summit.jpg">https://commons.wikimedia.org/wiki/File:View_from_Ruj_summit.jpg</a></p>
</div>
<div id="comment-76014-info" class="comment-info">
<span class="comment-age">(05 Aug '20, 08:09)</span> <span class="comment-user userinfo">rhhsmits</span>
</div>
</div>
<span id="76015"></span>
<div id="comment-76015" class="comment">
<div id="post-76015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The mapping in that area is a mess. Landuse=forest is not what I would choose for any of those wooded areas, rather use natural=wood. Then there are long ways of landuse=forest polygons that are adjacent but do not touch for some reason even though the "forest" is contiguous. When rendered by any software, this leaves a gap in the forest where none exists.</p>
</div>
<div id="comment-76015-info" class="comment-info">
<span class="comment-age">(05 Aug '20, 08:54)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="76016"></span>
<div id="comment-76016" class="comment">
<div id="post-76016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a> for some reason the heath multipolygon has a disconnected sections elsewhere and the holes in the forest are grouped together as a separate scrub relation. Unless they are closely associated or managed as a group most should probably be broken up into simple polygons. Some of the tags look a little odd too.</p>
</div>
<div id="comment-76016-info" class="comment-info">
<span class="comment-age">(05 Aug '20, 09:36)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76039"></span>
<div id="comment-76039" class="comment">
<div id="post-76039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed it looks like someone in the local municipality uploaded their own landuse data to OSM. They might be out of date: the area is getting depopulated and land that used to be grazed is getting overgrown and becomes scrub and then unmanaged forest.</p>
</div>
<div id="comment-76039-info" class="comment-info">
<span class="comment-age">(06 Aug '20, 18:46)</span> <span class="comment-user userinfo">rhhsmits</span>
</div>
</div>
</div>
<div id="comment-tools-76011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76011-form-container" class="comment-form-container">
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

