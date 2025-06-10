+++
type = "question"
title = "Large islands - more than 2000 nodes of coastline - how to tag/render?"
description = '''Hi, I&#x27;m mapping Kerrera in Scotland: http://www.openstreetmap.org/#map=14/56.3962/-5.5459 The coastline is made up of two parts because it is more than 2000 nodes and can&#x27;t be joined into a single outline for the whole island.  I want to add the place=island and name=Kerrera to the coastline so it c...'''
date = "2014-10-06T20:59:00Z"
lastmod = "2014-10-09T20:42:00Z"
weight = 37353
keywords = [ "island", "kerrera", "multipolygon", "coastline", "2000_points" ]
aliases = [ "/questions/37353" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Large islands - more than 2000 nodes of coastline - how to tag/render?](/questions/37353/large-islands-more-than-2000-nodes-of-coastline-how-to-tagrender)

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
<span id="post-37353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37353-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm mapping Kerrera in Scotland: <a href="http://www.openstreetmap.org/#map=14/56.3962/-5.5459">http://www.openstreetmap.org/#map=14/56.3962/-5.5459</a></p>
<p>The coastline is made up of two parts because it is more than 2000 nodes and can't be joined into a single outline for the whole island.</p>
<p>I want to add the place=island and name=Kerrera to the coastline so it can renders. I've added this to the two separate parts of the coastline but this does not render also when searching for Kerrera on nominatim it returns only one section of the outline highlighted. Do I need to put these two parts into a relation? The place=island wikipage doesn't mention using relations. I've add relation now but still doesn't seem to quite work as expected.</p>
<p>Anyway, looking for anyway help with tagging large islands so the name is rendered and nominatim search returns full outline and more importantly the 'place=' is regarding as an area within the OSM data model.</p>
<p>Thanks</p>
<p>Hawkeye</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-kerrera" rel="tag" title="see questions tagged &#39;kerrera&#39;">kerrera</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-2000_points" rel="tag" title="see questions tagged &#39;2000_points&#39;">2000_points</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '14, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/aefd12236ce046b3929cb63fca818119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hawkeye&#39;s gravatar image" />
<p><span>Hawkeye</span><br />
<span class="score" title="241 reputation points">241</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hawkeye has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37353" class="comments-container">
&#10;</div>
<div id="comment-tools-37353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37353-form-container" class="comment-form-container">
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

<span id="37354"></span>

<div id="answer-container-37354" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37354-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oh well, now I see, after messing around. Adding as Mutli-polygon works. So large islands (greater than 2000 points/nodes) need to be added at a series of coastline segments draw in counter-clockwise directions then a multi-polygon relation added to each segment. The relation should then include the tags for place=island, name=??? and then that works/renders...</p>
<p>:)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '14, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/aefd12236ce046b3929cb63fca818119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hawkeye&#39;s gravatar image" />
<p><span>Hawkeye</span><br />
<span class="score" title="241 reputation points">241</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hawkeye has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37354" class="comments-container">
<span id="37356"></span>
<div id="comment-37356" class="comment">
<div id="post-37356-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've added a note to the place=island wikipage:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Disland">http://wiki.openstreetmap.org/wiki/Tag:place%3Disland</a></p>
</div>
<div id="comment-37356-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 21:18)</span> <span class="comment-user userinfo">Hawkeye</span>
</div>
</div>
<span id="37377"></span>
<div id="comment-37377" class="comment">
<div id="post-37377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All tag wiki pages have a "used on these elements" section in the green box on the side, which tells you wether the tag is typically used on nodes, ways, areas (either a closed way or a multipolygon relation), and relations.</p>
<p>The place=island was already documented as being usable on areas, so most contributors did not feel the need to add a paragraph to that effect.</p>
</div>
<div id="comment-37377-info" class="comment-info">
<span class="comment-age">(07 Oct '14, 09:45)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37354-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37437"></span>

<div id="answer-container-37437" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I understand now. It's because there is no strict definition of an area in the osm model. Area is defined by a closed line, area=yes or mutlipolygon relation. So mutlipolygon is a 'relation' but when used to describe an area then it is not a 'relation' element but an area element...</p>
<p>There is a video about area data types here: <a href="http://lanyrd.com/2013/sotm/scpkrr/">http://lanyrd.com/2013/sotm/scpkrr/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '14, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/aefd12236ce046b3929cb63fca818119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hawkeye&#39;s gravatar image" />
<p><span>Hawkeye</span><br />
<span class="score" title="241 reputation points">241</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hawkeye has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37437" class="comments-container">
<span id="37441"></span>
<div id="comment-37441" class="comment">
<div id="post-37441-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not clear what you mean by "area element" – however, to make it clear there is no "area" data element in OSM. There are <span>only</span> nodes, ways and relations.</p>
</div>
<div id="comment-37441-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 22:57)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="37447"></span>
<div id="comment-37447" class="comment">
<div id="post-37447-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"area=yes" is a bit misleading - the iD editor adds this to things that it processes internally as areas, but this does cause a certain amount of confusion. Nothing processes areas in exactly the same way. Where "area=yes" is more generally used it's where something that would usually be a closed way is actually an area. Things that are very obviously already areas (e.g. landuse) don't generally have "area=yes" tags.</p>
</div>
<div id="comment-37447-info" class="comment-info">
<span class="comment-age">(09 Oct '14, 00:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37472"></span>
<div id="comment-37472" class="comment">
<div id="post-37472-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, yes. No such thing as an 'area element'. That should read 'way element' as defined here <a href="https://wiki.openstreetmap.org/wiki/Elements#Way">https://wiki.openstreetmap.org/wiki/Elements#Way</a></p>
</div>
<div id="comment-37472-info" class="comment-info">
<span class="comment-age">(09 Oct '14, 20:42)</span> <span class="comment-user userinfo">Hawkeye</span>
</div>
</div>
</div>
<div id="comment-tools-37437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37437-form-container" class="comment-form-container">
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

