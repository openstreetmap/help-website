+++
type = "question"
title = "Isolating buildings (and all member ways) using the Filter objects tool"
description = '''Hello, I&#x27;m rather new to JOSM, so please bear with me, and thanks in advance for any advice. I&#x27;m working on a quite dense and complicated area, and would like to isolate &quot;building&quot; ways and their dependencies using the &quot;filter object&quot; tool - but I see no straightforward way to do this. I can isolate...'''
date = "2011-04-08T15:52:00Z"
lastmod = "2011-04-09T09:39:00Z"
weight = 4340
keywords = [ "filter", "buildings", "filtering", "tool", "multipolygon" ]
aliases = [ "/questions/4340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Isolating buildings (and all member ways) using the Filter objects tool](/questions/4340/isolating-buildings-and-all-member-ways-using-the-filter-objects-tool)

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
<span id="post-4340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4340-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm rather new to JOSM, so please bear with me, and thanks in advance for any advice.</p>
<p>I'm working on a quite dense and complicated area, and would like to isolate "building" ways and their dependencies using the "filter object" tool - but I see no straightforward way to do this. I can isolate the ways containing the "building" tag, but I am not sure how to "chase" the member ways if they are part of a multipolygon.</p>
<p>Can anyone please show me how to do this?</p>
<p>Best,</p>
<p>ThePromenader.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-tool" rel="tag" title="see questions tagged &#39;tool&#39;">tool</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '11, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/52a6a6b11937c74b955186933f651b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThePromenader&#39;s gravatar image" />
<p><span>ThePromenader</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThePromenader has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4340" class="comments-container">
&#10;</div>
<div id="comment-tools-4340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4340-form-container" class="comment-form-container">
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

<span id="4341"></span>

<div id="answer-container-4341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to select all objects in the relation #1.374.453 you make a filter like:</p>
<pre><code>child id:1374453</code></pre>
<p>You can find the relation id in the title bar of the relation editor (and probably somewhere else). Then tick the <em>Inverse Filter</em> box and everything else will be unselected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '11, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-4341" class="comments-container">
<span id="4342"></span>
<div id="comment-4342" class="comment">
<div id="post-4342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply - but egads, my goal is to isolate buildings in a dataset containing over 1m objects.</p>
<p>I seem to be in a catch-22 situation here: if I do a '-building' (or inverted 'building') filter, I will show all the "role:outer" polygons (as these are the only ones with the "building" tag), but what I need to do is a) find what relation (#?) that 'outer' polygon belongs to, then b) find all of that relation's children. As far as I know, it is not possible to 're-select' any object already de-selected by the filter.</p>
</div>
<div id="comment-4342-info" class="comment-info">
<span class="comment-age">(08 Apr '11, 17:41)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
<span id="4344"></span>
<div id="comment-4344" class="comment">
<div id="post-4344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You cannot trust that the building tag is placed on the outer polygons. In fact the recommended way is to put the tags on the relation itself: <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Tagging">https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Tagging</a></p>
<p>The building in my answer is done like that: <a href="https://www.openstreetmap.org/browse/relation/1374453">https://www.openstreetmap.org/browse/relation/1374453</a></p>
</div>
<div id="comment-4344-info" class="comment-info">
<span class="comment-age">(08 Apr '11, 17:50)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="4345"></span>
<div id="comment-4345" class="comment">
<div id="post-4345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...exactly! Yet as far as my target is concerned (Paris, France), this is not the case. I've managed a workaround through extraction through Osmosis (to a mysql database), then reiteration through php - but I think this sort of 'data isolation' should be possible directly through JOSM. In spite of all its positive aspects, I see a lot of inconsistancies in OSM's treatment of data... every point and polygon, if it is a member of something, should be indicated as such. If every way of every building (multipolygon or no) had a building tag, my problem would be easily resolved.</p>
</div>
<div id="comment-4345-info" class="comment-info">
<span class="comment-age">(08 Apr '11, 18:28)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
<span id="4349"></span>
<div id="comment-4349" class="comment">
<div id="post-4349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question has given me unexpected understanding why one should put the tags on the relation and not on the members.</p>
<p>It may be easy for your specific task if there were building tags on every way, but what if two multipolygon buildings share the same wall and have different building=&lt;building typology=""&gt;?</p>
<p>Outer-tagging gives you surprises in JOSM even with simple filters. Apply "-(parent building)" to Musée du Petit Palais <a href="https://www.openstreetmap.org/?lat=48.866102&amp;lon=2.315534&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=48.866102&amp;lon=2.315534&amp;zoom=18&amp;layers=M</a> and watch which areas get selected.</p>
<p>It took me hours to realize that it's not a bug in JOSM.</p>
</div>
<div id="comment-4349-info" class="comment-info">
<span class="comment-age">(08 Apr '11, 21:24)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="4350"></span>
<div id="comment-4350" class="comment">
<div id="post-4350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, it's not a bug, it's just the way the data was uploaded. I do understand the concept of an "role:outer" polygon assuming the "master" role (thus getting all the tags), but from a data point of view, and especially in regards to how (J)OSM works, this is not the best approach, as it makes selecting/editing certain elements in groups well-neigh impossible.</p>
</div>
<div id="comment-4350-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 05:46)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
<span id="4351"></span>
<div id="comment-4351" class="comment not_top_scorer">
<div id="post-4351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>P.S.: I managed to isolate all multipolygon buildings by using an inverted "child parent building" filter. To display both non-multipolygon buildings and multipolygon buildings, though...</p>
<p>I see where this has caused problems - the shapefile output from <a href="http://cloudmade.com">cloudmade.com</a> for the Paris area does not include building 'child' polygons - only the "master" polygon is shown (meaning some buildings have no 'holes').</p>
</div>
<div id="comment-4351-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 06:15)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
<span id="4352"></span>
<div id="comment-4352" class="comment not_top_scorer">
<div id="post-4352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But an inverted "child parent building" will not give you just the buildings. It must have been more complicated. Probably the filter should look something like this:</p>
<p>-(-((parent((role:outer) -building))|-parent building) | child(-((parent((role:outer) -building))|-parent building))|building|child building)</p>
<p>That filter selects ways, relations and some nodes of outer-tagged buildings, relation-tagged buildings and non-relation buildings. But it doesn't select <em>all</em> nodes, so it probably needs to be even more complicated.</p>
</div>
<div id="comment-4352-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 06:35)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="4353"></span>
<div id="comment-4353" class="comment not_top_scorer">
<div id="post-4353-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that. I think 'child parent building' worked because it selects "all the children of elements that are the parent of a building) - but as I said, I could only get multipolygon buildings (both inner and outer) with that command.</p>
<p>Your filter example is quite logical - I'll play around with it today. Thanks!</p>
</div>
<div id="comment-4353-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 09:00)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
<span id="4354"></span>
<div id="comment-4354" class="comment not_top_scorer">
<div id="post-4354-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But does your simple filter handle the case when the outer wall of a building also has the inner role of a surrounding area in another relation, like Musée du Petit Palais <a href="https://www.openstreetmap.org/?lat=48.866102&amp;lon=2.315534&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=48.866102&amp;lon=2.315534&amp;zoom=18&amp;layers=M</a> ?</p>
<p>'parent building' will select the relations for both the surrounding gravel area and the building, and then 'child parent building' selects both the house and the surroundings.</p>
<p>It is complicated to cover all cases when multiple objects share the same way, and there may be houses inside houses and so on.</p>
</div>
<div id="comment-4354-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 09:12)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="4355"></span>
<div id="comment-4355" class="comment not_top_scorer">
<div id="post-4355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, but I consider that to be a mistake - the same is repeated to the nearby eastern end of the Champs-Elysées (the buildings there are "inner" polygons of its surrounding garden multipolygon). By what logic would a building be a member of the outline of the land it is upon (no matter what use the land has)? Is every city building a member of the city block it is upon? In fact, if you look above and to the left of the Grand Palais, you'll see that the round building within isn't rendered correctly at all (in Potlatch or JOSM).</p>
</div>
<div id="comment-4355-info" class="comment-info">
<span class="comment-age">(09 Apr '11, 09:39)</span> <span class="comment-user userinfo">ThePromenader</span>
</div>
</div>
</div>
<div id="comment-tools-4341" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-4341-form-container" class="comment-form-container">
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

