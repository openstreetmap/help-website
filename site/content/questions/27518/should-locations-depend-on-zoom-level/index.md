+++
type = "question"
title = "Should locations depend on zoom level?"
description = '''I saw that the Lodner, a mountain in the Texel group in northern Italy, was located too far to the north. I joined the OSM community to improve it. I needed two attempts, but then it looked better, on the OSM site that is. A few hours later, I looked at the OSM map using a different site (the one wh...'''
date = "2013-10-27T04:22:00Z"
lastmod = "2013-10-30T16:51:00Z"
weight = 27518
keywords = [ "node", "mountains", "rendering", "location", "label" ]
aliases = [ "/questions/27518" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Should locations depend on zoom level?](/questions/27518/should-locations-depend-on-zoom-level)

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
<span id="post-27518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I saw that the Lodner, a mountain in the Texel group in northern Italy, was located too far to the north. I joined the OSM community to improve it. I needed two attempts, but then it looked better, on the OSM site that is.</p>
<p>A few hours later, I looked at the OSM map using a different site (the one where I had seen the error in the first place). Alas, the location was not changed. I was disappointed. I forgot why, but for some reason I zoomed out, and got a surprise: on zooming out two levels (the highest was 16, I zoomed out to 14), suddenly the label moved to the new location, the one that I had specified! Being curious, I zoomed out one level more, and the label jumped back to the old, incorrect location! So, it looks as if the label only shows up at the correct location when viewing the map at level 14.</p>
<p>Here is the link to the map, at level 14, showing the correct location: <a href="http://www.mappingsupport.com/p/gmap4.php?ll=46.7337,11.0402&amp;z=14&amp;t=osm">http://www.mappingsupport.com/p/gmap4.php?ll=46.7337,11.0402&amp;z=14&amp;t=osm</a> Zoom in and out, and you'll see what I mean.</p>
<p>Perhaps it was a gmap4 problem, not an OSM one? To find out, I dug deeper, and searched for another site that uses OSM data. I found this one: <a href="http://blog.openstreetmap.it/la-mappa/">http://blog.openstreetmap.it/la-mappa/</a></p>
<p>I zoomed in on the Lodner, expecting either to see the correct position at every level (which would imply that it was either a gmap4 problem or my computer was caching data for gmap4), or to see the same strange effect as with gmap4 (which would point to a problem at OSM). But no, I got something else again: At the highest zoom level, the position was correct, but on zooming out two levels, it moved to the old, incorrect place. Just the opposite of gmap4. I zoomed out one more level, and it didn't move. I zoomed out another one, and this time it did move! For the record, I had never used this Italian site before, so this strange behaviour can't be a caching issue. Apparently, the location of label apparently depends both on the site that I use to look at the OSM map and the zoom level. Gmap4 has it right on one of the levels and wrong on others, whereas the Italian site has it wrong on two levels, and right on the others.</p>
<p>Am I missing something, or is there a problem here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-mountains" rel="tag" title="see questions tagged &#39;mountains&#39;">mountains</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-label" rel="tag" title="see questions tagged &#39;label&#39;">label</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '13, 04:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d0fee6ea6a3327151906722775e32a8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20Holland&#39;s gravatar image" />
<p><span>Rob Holland</span><br />
<span class="score" title="72 reputation points">72</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob Holland has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '13, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-27518" class="comments-container">
&#10;</div>
<div id="comment-tools-27518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27518-form-container" class="comment-form-container">
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

<span id="27610"></span>

<div id="answer-container-27610" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27610-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob Holland has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a caching/rendering issue. The tiles could be cached both on your computer and on the server (which renders tiles on demand).</p>
<p>You can try to force the involved systems to re-render and re-load the tiles. Choose the desired zoom level, get a permalink of the current view, enter it in your browser's address bar and press ctrl+f5 a few times (should work for Chrome/Firefox on Win/Linux). Keep in mind that tiles for different zoom levels are rendered separately, so if it looks correct in one zoom level, it does not imply that the other zoom levels are up to date too.</p>
<p>On OSM.org you can also right-click on a tile, copy the URL (Chrome: "Open image in new tab") and then append "/dirty" to the URL to force re-rendering the tile. To check the status of the tile, you can append "/status" to the tile URL.</p>
<p>I'm not sure about gmap4, but on the OSM main website this works fine (although it usually needs a few minutes until it really re-renders the tiles).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '13, 01:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1e0588e345236881aff23040eb1d5dc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbrgn&#39;s gravatar image" />
<p><span>dbrgn</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbrgn has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '13, 01:36</strong> </span></p>
</div>
</div>
<div id="comments-container-27610" class="comments-container">
<span id="27664"></span>
<div id="comment-27664" class="comment">
<div id="post-27664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I first read this reply, I didn't fully understood, but thanks to the other answers and comments below I finally did. Over time, more and more levels came to show the new location, but until a few minutes ago, still two lower zoom levels were not. So I used the "/dirty" trick to force a new rendering of the tiles involved, and, sure enough, in a matter of seconds it was fine!</p>
</div>
<div id="comment-27664-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 16:51)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
</div>
<div id="comment-tools-27610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27610-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27519"></span>

<div id="answer-container-27519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27519-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is probably a rendering issue with each site. Tiles on each zoom level are normally rendered on demand or based on an algorithm of some sort. Others should be able to provide more insight into this.</p>
<p>The key thing is to check if the data is correct on the OSM site by using one of the editors. The rendering on the various sites will catch up over time.</p>
<p>Alternatively, contact the respective site admin to check on how often their tiles are rerendered or how a rerendering can be forced to be done.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '13, 05:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e466cf295ae880686a4b809362f931b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rovingmedic&#39;s gravatar image" />
<p><span>rovingmedic</span><br />
<span class="score" title="1060 reputation points"><span>1.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rovingmedic has one accepted answer">5%</span></p>
</div>
</div>
<div id="comments-container-27519" class="comments-container">
<span id="27520"></span>
<div id="comment-27520" class="comment">
<div id="post-27520-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good to hear that it's probably not an OSM site problem, as it does indeed look fine there. I'll keep an eye on what gmap4 shows in the near future, and if the problem persists I'll contact the person behind it.</p>
</div>
<div id="comment-27520-info" class="comment-info">
<span class="comment-age">(27 Oct '13, 07:13)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
</div>
<div id="comment-tools-27519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27519-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27526"></span>

<div id="answer-container-27526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27526-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Gmap4 renders tiles on demand and does not cache them.</p>
<p>Joseph, the Gmap4 guy</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '13, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/61999ddbd5eb58ef824cdfa6722b1e97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jelf&#39;s gravatar image" />
<p><span>Jelf</span><br />
<span class="score" title="17 reputation points">17</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jelf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27526" class="comments-container">
<span id="27597"></span>
<div id="comment-27597" class="comment">
<div id="post-27597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting. That suggests that there is nothing wrong with the Gmap4 site, so the problem lies elsewhere.</p>
<p>I just had another look at what it looks like on Gmap4. There is a minor improvement: now the new position is displayed at zoom level 15 as well as at 14. But it's still wrong at level 16 and 13 or lower.</p>
<p>I also checked the Italian site again. There is a change there too, but it's become plain weird now! As before, it's correct at the two highest levels, then it's wrong on one, then two more levels are right again ... but all lower levels are now also wrong!</p>
</div>
<div id="comment-27597-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 20:27)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
<span id="27598"></span>
<div id="comment-27598" class="comment not_top_scorer">
<div id="post-27598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess that it's possible that there's a browser (and possibly also an ISP?) cache in the way somewhere too?</p>
</div>
<div id="comment-27598-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 20:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="27608"></span>
<div id="comment-27608" class="comment not_top_scorer">
<div id="post-27608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You never know where things get cached I suppose, but I don't think so. Since my original question, I cleared my own browser's cache (I'm using Chrome). But your comment made me try something else, and so I opened the same map in both IE and Firefox. It looks exactly the same.</p>
<p>No, I presume it's not a caching problem, but something on the OSM side. The change that I made was my very first contribution. I think that either I've missed something, meaning that my location change is restricted to certain zoom levels somehow, or, more seriously, that there is some kind of bug on the OSM side.</p>
</div>
<div id="comment-27608-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 23:05)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
<span id="27627"></span>
<div id="comment-27627" class="comment">
<div id="post-27627-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Gmap4 doesn't "render" anything... it just shows tiles from tile.openstreetmap.org (or whichever tile provider you choose).</p>
</div>
<div id="comment-27627-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 12:11)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="27629"></span>
<div id="comment-27629" class="comment">
<div id="post-27629-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the correction Richard. Of course you are right. Gmap4 just displays tiles. My bad.</p>
</div>
<div id="comment-27629-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 14:12)</span> <span class="comment-user userinfo">Jelf</span>
</div>
</div>
<span id="27653"></span>
<div id="comment-27653" class="comment not_top_scorer">
<div id="post-27653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I'm starting to understand. While I made the change, I was looking at the Bing aerial imagery. The new location showed on all the zoom levels that I checked, but if I zoom out to level 15 or lower, only the aerial map is displayed, and to the left a message says that I should zoom in to edit.</p>
<p>So, now I viewed only the OSM map itself, and, sure enough, the problem shows up there too: Levels 19, 18 and 17 are correct, but at 16 it's wrong. Then 15 and 14 are correct again, but 13 and lower are wrong.</p>
<p>Is this a time lag thing? I mean, are different levels updated slowly and randomly?</p>
</div>
<div id="comment-27653-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 07:42)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
<span id="27654"></span>
<div id="comment-27654" class="comment">
<div id="post-27654-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There's a long detailed answer about why edits show up when they do <a href="https://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated">here</a>.</p>
</div>
<div id="comment-27654-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 09:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="27663"></span>
<div id="comment-27663" class="comment">
<div id="post-27663-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, that was really helpful! And when I checked again just now, the tiles on levels 16 and 13 have joined the ranks of the correct ones. Just levels 12 and 11 left now, for on 10 and lower the node for the mountain isn't displayed anyway. And, frankly, on zoom levels 12 and 11 the difference is small, most people proably won't even notice it.</p>
</div>
<div id="comment-27663-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 16:35)</span> <span class="comment-user userinfo">Rob Holland</span>
</div>
</div>
</div>
<div id="comment-tools-27526" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-27526-form-container" class="comment-form-container">
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

