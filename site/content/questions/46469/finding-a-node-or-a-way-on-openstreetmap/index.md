+++
type = "question"
title = "Finding a node or a way on openstreetmap"
description = '''I am happily compiling maps using MKGMAP and I am trying to make sure I don&#x27;t miss any stuff, so I have put &quot;highway=* &amp;amp; area=yes { echotags &quot; Found highway POLYGON&quot;}&quot; in the style file for Polygons. it happily throws out a messages for me. my question is how can I find and view them on openstre...'''
date = "2015-11-09T08:18:00Z"
lastmod = "2015-11-09T23:13:00Z"
weight = 46469
keywords = [ "ways", "map", "nodes", "find" ]
aliases = [ "/questions/46469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding a node or a way on openstreetmap](/questions/46469/finding-a-node-or-a-way-on-openstreetmap)

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
<span id="post-46469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46469-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am happily compiling maps using MKGMAP and I am trying to make sure I don't miss any stuff, so I have put "highway=* &amp; area=yes { echotags " Found highway POLYGON"}" in the style file for Polygons. it happily throws out a messages for me.</p>
<p>my question is how can I find and view them on openstreetmap ?</p>
<p>what I get is</p>
<p>305293190 - [area=yes,mkgmap:country=GBR,mkgmap:admin_level2=GBR,mkgmap:region=Greater Manchester,mkgmap:admin_level4=England,mkgmap:city=Bury,mkgmap:admin_level8=Bury,mkgmap:admin_level6=Greater Manchester,highway=residential,mkgmap:admin_level5=North West England] Found highway POLYGON</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '15, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-46469" class="comments-container">
&#10;</div>
<div id="comment-tools-46469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46469-form-container" class="comment-form-container">
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

<span id="46470"></span>

<div id="answer-container-46470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46470-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-46470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Rossendale,</p>
<p>If it's a polygon, then it's a closed way in the OSM database. You can find ways by id as simple as this: <a href="https://www.openstreetmap.org/way/305293190">https://www.openstreetmap.org/way/305293190</a></p>
<p>If a specific node (the building blocks of ways) is giving a problem, the link would be <a href="https://www.openstreetmap.org/node/305293190">https://www.openstreetmap.org/node/305293190</a> .</p>
<p>If it is a multipolygon (for example a building with a hole in it), the link would be <a href="https://www.openstreetmap.org/relation/305293190">https://www.openstreetmap.org/relation/305293190</a></p>
<p>I don't think your case is an error, but that would be the subject of a different question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '15, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-46470" class="comments-container">
<span id="46471"></span>
<div id="comment-46471" class="comment">
<div id="post-46471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick response, I had no idea, you could search that way.</p>
</div>
<div id="comment-46471-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 08:38)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="46472"></span>
<div id="comment-46472" class="comment">
<div id="post-46472-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It is practical that way. You can also get a link like that when browsing the map, activating "Map data" under Layers, or by querying the data using the question mark at the right hand side of the map. Just don't count on these links to work forever, because ID's change when someone decides to re-map from scratch.</p>
</div>
<div id="comment-46472-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 08:48)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="46473"></span>
<div id="comment-46473" class="comment">
<div id="post-46473-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can also use Overpass API. It uses a simpler syntax but unfortunately if your object isn't within your current bounding box it will report an empty dataset. Zooming out manually will reveal it but again, regrettably, using the Zoom to Data tool on the Overpass UI page does not.</p>
<p><a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
<p>Just click on Wizard, enter id:305293190 into the text box and your object will be found.</p>
</div>
<div id="comment-46473-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 09:39)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="46478"></span>
<div id="comment-46478" class="comment">
<div id="post-46478-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Adding 'global' to the wizard query, like "id:305293190 global", prevents the Wizard from inserting a bounding box.</p>
<p>It will probably time out for queries that return many objects. Not a problem when searching by id, just worth mentioning.</p>
</div>
<div id="comment-46478-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 14:02)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46482"></span>
<div id="comment-46482" class="comment">
<div id="post-46482-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Awesome, Max. I will add that information to my little bag of Wizard tricks and features.</p>
</div>
<div id="comment-46482-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 23:13)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-46470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46470-form-container" class="comment-form-container">
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

