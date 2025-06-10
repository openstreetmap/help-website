+++
type = "question"
title = "fixing overlapping roads/ways where there&#x27;s several relations involved"
description = '''I think I may have inadvertently inherited two streets that were overlapped but I fixed a broken turn restriction on...so I got left with the last edit. Unfortunately I have absolutely no idea how to fix this or where even to begin, so here&#x27;s a request for help. The problem is here: https://www.open...'''
date = "2019-07-07T22:39:00Z"
lastmod = "2019-07-10T07:32:00Z"
weight = 69920
keywords = [ "ways", "landuse", "relation", "overlap", "fixup" ]
aliases = [ "/questions/69920" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [fixing overlapping roads/ways where there's several relations involved](/questions/69920/fixing-overlapping-roadsways-where-theres-several-relations-involved)

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
<span id="post-69920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69920-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think I may have inadvertently inherited two streets that were overlapped but I fixed a broken turn restriction on...so I got left with the last edit. Unfortunately I have absolutely no idea how to fix this or where even to begin, so here's a request for help.</p>
<p>The problem is here:</p>
<p><a href="https://www.openstreetmap.org/note/1834724#map=19/34.07372/-118.44531">https://www.openstreetmap.org/note/1834724#map=19/34.07372/-118.44531</a></p>
<p>Unfortunately this is so bungled up with relations (turn restrictions and landuse) as well as shared nodes that I don't know where to start how to fix this. I believe I may have had to split a way in order to properly add the turn restriction which may have worsened the situation, but don't believe I put two ways on top of each other as it's pretty tough to do so in iD. Where can I start if I finally get enough tools and ideas to fix this without damaging the layout?</p>
<p>From a really generalized point of view I wish I could just cut and paste the landuse and then fix the roads. Then paste back the landuse. But I have no idea how or if this methodology is possible...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-fixup" rel="tag" title="see questions tagged &#39;fixup&#39;">fixup</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '19, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c86f4c99960b2c3ffdeb1698ba833b52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpserror&#39;s gravatar image" />
<p><span>gpserror</span><br />
<span class="score" title="171 reputation points">171</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpserror has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69920" class="comments-container">
&#10;</div>
<div id="comment-tools-69920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69920-form-container" class="comment-form-container">
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

<span id="69923"></span>

<div id="answer-container-69923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69923-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Yes areas of landuse extended over and joined to highway centerlines makes future editing more difficult. I think it's done for easiness, quickness and to make areas look prettier. But it's not correct!</p>
<p>Anyway I've unjoined the landuse from the center line of the highway and relocated the nodes to the highway sides. The highway section you are concerned about is now clear of landuse. I've added an extra node to the duplicated section that it looks like you added as a duplication. If you delete this, (your new section,) the highway will be back as it was. I'm pretty sure you didn't make any amendment to the original highway. I hope this helps.</p>
<p>If it is wished my changes can be reversed by reverting Changeset: 71999372</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '19, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-69923" class="comments-container">
<span id="69933"></span>
<div id="comment-69933" class="comment">
<div id="post-69933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that helps. If nobody complains that the map is no longer correct I think it should stand, though for consistency the rest of the highway needs to be separated from landuse, which would be the main reason for not separating the two -- if it were correct to do so.</p>
<p>So how did you do that? Which editor did you use? I hope the solution wasn't to remove and redraw, there must be a better way of fixing something like this for future reference.</p>
<p>Thanks again, now I need to figure out how to solve the next problem of two highways on top of each other and each having relations, hopefully not with each other...</p>
</div>
<div id="comment-69933-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 16:16)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69938"></span>
<div id="comment-69938" class="comment">
<div id="post-69938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I unpicked each node with the JOSM editor and moved the node to the side. You can move several nodes at a time but if to many are moved it can get confusing, patience is helpful. I'll stress again in allmost all cases landuse does not extend to the highway center line, it is therefore wrong to map in this way. Even if someone complains it is still incorrect.</p>
<p>You copied and added Way: West Sunset Boulevard (701258669) in duplication of the original/existing Way: West Sunset Boulevard (381210291). Just delete your Way: West Sunset Boulevard (701258669) and amend the way that is left. (I'm pretty sure before your amendment there was only one highway, no duplication.) Then make any amendment to the single original highway.</p>
<p>You duplicated the route relation onto the duplicate highway. Removing Way: West Sunset Boulevard (701258669) will make no difference to the relations.</p>
<p>I can remove the duplicate if you wish. Any further questions please just ask.</p>
</div>
<div id="comment-69938-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 18:07)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="69940"></span>
<div id="comment-69940" class="comment">
<div id="post-69940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You have now removed/deleted one node from the center of that highway, you have not removed the duplicated section of highway.</p>
<p>You can see below the changeset comment box, the node that's been deleted from West Sunset Boulevard (701258669, v3). The duplicate highway in now again exactly on top of the original way.</p>
<p>Do you want me to remove the duplicate way?</p>
</div>
<div id="comment-69940-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 07:09)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="69941"></span>
<div id="comment-69941" class="comment">
<div id="post-69941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm...still need to figure out how to do this. If you view this as an emergency to fix, go ahead, else I'm trying to figure this thing out... Thanks.</p>
</div>
<div id="comment-69941-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 08:15)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69942"></span>
<div id="comment-69942" class="comment">
<div id="post-69942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW, I downloaded JOSM ... and nice, able to easily select the overlapping way, unlike iD or Potlatch2 (or at least I couldn't the other two out yet). Unfortunately I need to get to bed now so I can't work on this tonight. The status still stands, if you feel it's an emergency to fix this bug, go ahead and fix it, though it'd be nice to figure this out for the next time I see something like this! (And any hints on how to use the tools are welcome!)</p>
</div>
<div id="comment-69942-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 08:38)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69943"></span>
<div id="comment-69943" class="comment not_top_scorer">
<div id="post-69943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I can't see a way to separate duplicate ways in the iD editor. The iD editor will not allow you to delete a way which has routes or relations until you remove the way from the routes/relations. It gets complicated!</p>
<p>It's an easy task with JOSM, (which IMHO is far superior to any other OSM editor). I think the duplication should be removed so I have removed the section you added. I hope that's OK, Changeset: 72042219 if you need to reverse my removal.</p>
<p>Edit comment Sorry I posted before seeing your last comment.</p>
</div>
<div id="comment-69943-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 08:55)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="69949"></span>
<div id="comment-69949" class="comment not_top_scorer">
<div id="post-69949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh well, that's fine, no sense in reverting something that made the map better. I wish I could have used this as a learning experience for fixing something I had never fixed before (just like fixing those turn relations that causes issues with routing software.) Thanks though.</p>
</div>
<div id="comment-69949-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 18:34)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69954"></span>
<div id="comment-69954" class="comment not_top_scorer">
<div id="post-69954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can have a go at fixing some of the landuse overlaps at <a href="https://www.openstreetmap.org/way/305906891">https://www.openstreetmap.org/way/305906891</a> if you want - there a drain has been drawn in mostly the right place (see the OS OpenDataStreetView background) and farmland has been drawn along the screen but (see the Bing imagery) actually the farmland stops north of the drain and there's a hedge.</p>
</div>
<div id="comment-69954-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 19:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69956"></span>
<div id="comment-69956" class="comment not_top_scorer">
<div id="post-69956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, yeah I poked at it a bit with iD and this one seems fixable with iD, though I'm not 100% sure what the best representation of this anyway. I also went ahead and separated a bit of the road and the landuse that was further west on the initial question point, but that too was done with iD.</p>
<p>Just was trying to find something that I needed to use JOSM to fix as iD is much more convenient as HTML5 is readily available. Again trying to avoid Potlatch due to Adobe-Flash.</p>
</div>
<div id="comment-69956-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 20:04)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
</div>
<div id="comment-tools-69923" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69935"></span>

<div id="answer-container-69935" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69935-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's roughly what I'd do if I was editing the area in the editor I normally use (Potlatch 2):</p>
<p>I'd notice that there were overlaid ways because each node is displayed differently to make that clear.</p>
<p>Click on a node, click "/" to cycle around the joining ways there until you get to the offending landuse.</p>
<p>"x" to split, and move both ends away from the middle of the road, and then rejoin both ends.</p>
<p>Used "delete" to undo one side of the way from the middle of the road, then draw in where the edge actually is. Repeat for the other side, and join the two ends.</p>
<p>Repeat ^^ for the landuse polygon at the other side of the road.</p>
<p>If there are still overlapping nodes, use "/" to see what they are. These might be legitimate (e.g. townland boundaries in Ireland) or might not be - split, move or delete as required.</p>
<p>Other OSM editors are available - perhaps someone can add an answer explaining the buttons to press in (e.g.) JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '19, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69935" class="comments-container">
<span id="69937"></span>
<div id="comment-69937" class="comment">
<div id="post-69937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Aha. Thanks for the Potlatch idea, yeah I think this may be a limitation of iD or at least I don't know how to deal with it in iD. There were some other issues that I could solve by the "disconnect" feature in iD. However, if I click on a node there and "disconnect" it would disconnect everything under that node -- which it would refuse to do because of the relations attached to that node -- even though I just wanted to disconnect the landuse from highway.</p>
<p>I may have to look more into Potlatch, after getting used to iD the selection features seem really awkward. I've been sort of apprehensive about Flash, which was my main holdback.</p>
</div>
<div id="comment-69937-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 17:52)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
<span id="69957"></span>
<div id="comment-69957" class="comment">
<div id="post-69957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM: Depending on the number of nodes that overlap between the way and the area, you might either ungroup node by node or the complete area. - node by node -&gt; select node, press "G" - the whole area, select area, press "G", make sure you validate at the end and fix overlapping nodes. This is a 1-click operation and might therefore be faster that ungrouping many individual nodes. The area will have overlapping nodes with areas on the other side than the highway - select the area and use the <a href="https://josm.openstreetmap.de/wiki/Help/Action/ImproveWayAccuracy">improve way accuracy (W)</a> to reposition the nodes that overlapped with the highway, in the process you can add or delete nodes With this approach you will not have to fix the relations, and you preserve as much history as possible.</p>
</div>
<div id="comment-69957-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 04:19)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69958"></span>
<div id="comment-69958" class="comment">
<div id="post-69958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure if already mentioned here but there is a handy shortcut using JOSM to select individual overlapping ways.<br />
See 'Cycle in dense or overlapping objects with pop-up' on the following page...<br />
<a href="https://josm.openstreetmap.de/wiki/Help/Action/Select">https://josm.openstreetmap.de/wiki/Help/Action/Select</a></p>
</div>
<div id="comment-69958-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 05:46)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="69960"></span>
<div id="comment-69960" class="comment">
<div id="post-69960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks nevw, Wow there's always something new to learn. I had been using Alt+left click to cycle through multiple ways (two fingers). Never even thought to click the middle mouse wheel. For me it's now going to be click middle mouse wheel every time (single finger), should save hours.</p>
</div>
<div id="comment-69960-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 07:32)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-69935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69935-form-container" class="comment-form-container">
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

