+++
type = "question"
title = "Coastal town / village centres located outside the county"
description = '''I have some code that works out which UK county a place node falls in. This is failing for some coastal towns / villages, because the latitude and longitude defined for the place node is actually in the sea or on the beach, and therefore falls outside of the county boundary. An example is Hugh Town ...'''
date = "2012-08-06T09:26:00Z"
lastmod = "2012-08-09T17:02:00Z"
weight = 14858
keywords = [ "nodes", "place", "coastal" ]
aliases = [ "/questions/14858" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Coastal town / village centres located outside the county](/questions/14858/coastal-town-village-centres-located-outside-the-county)

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
<span id="post-14858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some code that works out which UK county a place node falls in. This is failing for some coastal towns / villages, because the latitude and longitude defined for the place node is actually in the sea or on the beach, and therefore falls outside of the county boundary.</p>
<p>An example is <a href="https://www.openstreetmap.org/browse/node/380755986">Hugh Town</a> in the Scilly Isles. <a href="http://maps.google.co.uk/maps?q=49.9155917,+-6.3142438&amp;hl=en&amp;ll=49.915585,-6.314242&amp;spn=0.012242,0.033023&amp;sll=49.914592,-6.314244&amp;sspn=0.012242,0.033023&amp;t=m&amp;z=16">Here</a>'s how it looks on Google Maps, which doesn't show the beach.</p>
<p>Is this intentional, or could the node positions for such places be adjusted so that they were on land? I could easily come up with a list of them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-coastal" rel="tag" title="see questions tagged &#39;coastal&#39;">coastal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '12, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9b6b142985091a1566e3f91e1902284d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave&#39;s gravatar image" />
<p><span>Dave</span><br />
<span class="score" title="86 reputation points">86</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14858" class="comments-container">
&#10;</div>
<div id="comment-tools-14858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14858-form-container" class="comment-form-container">
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

<span id="14878"></span>

<div id="answer-container-14878" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14878-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my opinion, place nodes should be put at the position that is locally considered to be the "center" of the locality, not some mathematically determined point.</p>
<p>Judging by the Hugh Town map, I would have put the place node where Lower Strand, Church Street, Silver Street, Garrison Lane and Hugh Street meet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '12, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14878" class="comments-container">
<span id="14892"></span>
<div id="comment-14892" class="comment">
<div id="post-14892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks pbb. I've now made my first edit, and done precisely that ;-)</p>
</div>
<div id="comment-14892-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 15:59)</span> <span class="comment-user userinfo">Dave</span>
</div>
</div>
</div>
<div id="comment-tools-14878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14878-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14863"></span>

<div id="answer-container-14863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14863-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sure you can move the node towards the inner country. Actually the best way is, to put the node in the center of the area, where it belongs to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '12, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/97d8f28f404fa1c071546be595713c1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HostedDinner&#39;s gravatar image" />
<p><span>HostedDinner</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HostedDinner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14863" class="comments-container">
&#10;</div>
<div id="comment-tools-14863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14863-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14888"></span>

<div id="answer-container-14888" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14888-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is best to map town and village areas as polygons so that the nominatim works properly, addresses get linked to nearest node otherwise. This will put the name in the middle of the polygon on the map page. I do not know if your code also searches for village and town polygons as well as nodes. Some say after drawing the polygon the node is not needed any more so delete it, again to assit the nominatim. I hope this is not a problem for your purposes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '12, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '12, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-14888" class="comments-container">
<span id="14889"></span>
<div id="comment-14889" class="comment">
<div id="post-14889-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Andy, that's very useful information. At the moment my code doesn't look for village/town polygons. I will add that, and probably geometrically generate my own centre points for them (as my code needs to calculate proximity to points of reference, rather than positioning within polygons).</p>
</div>
<div id="comment-14889-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 14:39)</span> <span class="comment-user userinfo">Dave</span>
</div>
</div>
<span id="14902"></span>
<div id="comment-14902" class="comment">
<div id="post-14902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy. It is my understanding/interpretation that it is normally best to use nodes for places (<a href="https://wiki.openstreetmap.org/wiki/Key:place)">https://wiki.openstreetmap.org/wiki/Key:place)</a> (towns, villages, etc) and areas for administrative boundaries (<a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative).">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative).</a> See also this discussion: (<a href="/questions/4658/tagging-areas-as-place-vs-boundaryadministrative).">https://help.openstreetmap.org/questions/4658/tagging-areas-as-place-vs-boundaryadministrative).</a></p>
</div>
<div id="comment-14902-info" class="comment-info">
<span class="comment-age">(08 Aug '12, 00:04)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
<span id="14908"></span>
<div id="comment-14908" class="comment">
<div id="post-14908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Peter I looked at your links thanks,but one seemed to be empty. The decision to use nodes or polygons seems to be split. In my experience if I search for a street I have found that it will grab the nearest town or village which may not be the correct one. Nodes may work if all houses,and buildings have all the address tags filled in.Back to Dave's Question I wanted to add relevant info for him or others doing similar work. I'm no expert!</p>
</div>
<div id="comment-14908-info" class="comment-info">
<span class="comment-age">(08 Aug '12, 09:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="14910"></span>
<div id="comment-14910" class="comment">
<div id="post-14910-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your code should definitely prefer positioning withing polygon if it exists. The other calculation (distance on place node, real or virtual) will lead to many errors. Imagine two adjacent villages, one is 10x10 km square, one is 1x1 km square. If you use the geometrical polygon centre, a street within the big village but nearby the smaller village will be identified to the wrong village. If you use the real "place" node, you have to rely on its positioning by contributors (fluctuating).</p>
</div>
<div id="comment-14910-info" class="comment-info">
<span class="comment-age">(08 Aug '12, 12:23)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="14911"></span>
<div id="comment-14911" class="comment">
<div id="post-14911-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that it is possible to link the place node and the boundary with the relation role "admin_centre" (although we have cases where one boundary includes many places, usually only one of them is the administrative centre).</p>
</div>
<div id="comment-14911-info" class="comment-info">
<span class="comment-age">(08 Aug '12, 12:25)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="14927"></span>
<div id="comment-14927" class="comment not_top_scorer">
<div id="post-14927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy, I see I made a mistake with my links. Here are they as they should have been: <a href="https://wiki.openstreetmap.org/wiki/Key:place">https://wiki.openstreetmap.org/wiki/Key:place</a> - <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative</a> - <a href="/questions/4658/tagging-areas-as-place-vs-boundaryadministrative">https://help.openstreetmap.org/questions/4658/tagging-areas-as-place-vs-boundaryadministrative</a></p>
</div>
<div id="comment-14927-info" class="comment-info">
<span class="comment-age">(09 Aug '12, 17:02)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
</div>
<div id="comment-tools-14888" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14888-form-container" class="comment-form-container">
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

