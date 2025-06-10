+++
type = "question"
title = "how to get the position of polygon label in OSM"
description = '''Dear all, There is a question on my side about the polygon label on Map.  As Australia, the admin_centre node is located at Canberra (21674637) but the label for Australia is located in the middle of Australia. I have checked the attributes of Australia in planet OSM pbf and there is nothing found. ...'''
date = "2017-11-06T11:02:00Z"
lastmod = "2021-01-30T10:25:00Z"
weight = 60473
keywords = [ "osm", "polygon", "label" ]
aliases = [ "/questions/60473" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get the position of polygon label in OSM](/questions/60473/how-to-get-the-position-of-polygon-label-in-osm)

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
<span id="post-60473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60473-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>There is a question on my side about the polygon label on Map.</p>
<p>As Australia, the admin_centre node is located at Canberra (21674637) but the label for Australia is located in the middle of Australia.</p>
<p>I have checked the attributes of Australia in planet OSM pbf and there is nothing found.</p>
<p>Could you please provide any clue how to get the NODE info or position about the polygon label?</p>
<p>Great thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-label" rel="tag" title="see questions tagged &#39;label&#39;">label</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '17, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/95d580c60b9b016849766d2781c46af9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xiaoweishen&#39;s gravatar image" />
<p><span>xiaoweishen</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xiaoweishen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60473" class="comments-container">
&#10;</div>
<div id="comment-tools-60473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60473-form-container" class="comment-form-container">
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

<span id="60476"></span>

<div id="answer-container-60476" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60476-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The node for a polygon label is placed by whichever software is rendering the data. It's not something that's controlled by the OSM data itself. In the case of OSM's "standard" map, the map design is "OpenStreetMap Carto", and the software doing the rendering is called "Mapnik". Mapnik's rules for adding labels can be influenced by the map design, but even then it can be difficult to determine why it has put a label in a particular place (and it can vary with Mapnik software versions, too).</p>
<p>However, "determining where some rendering software might have placed a label" seems like an odd request - perhaps if you explain a bit more about why you're asking the question we'll be able to help more?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '17, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Nov '17, 13:00</strong> </span></p>
</div>
</div>
<div id="comments-container-60476" class="comments-container">
&#10;</div>
<div id="comment-tools-60476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60476-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78594"></span>

<div id="answer-container-78594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78594-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm a bit late here, but just now stumbled upon what I was looking for here:</p>
<p><a href="https://github.com/mapbox/polylabel">https://github.com/mapbox/polylabel</a> is the JS library/algorithm used by <a href="https://github.com/mapnik/mapnik/blob/master/src/geometry/polylabel.cpp">Mapnik</a> to place the labels, which is <a href="https://wiki.openstreetmap.org/wiki/Mapnik">the rendering engine behind openstreetmap.org</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '21, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/09f491ff872d3ed578d7e246d1bf30cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerusf&#39;s gravatar image" />
<p><span>xerusf</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerusf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78594" class="comments-container">
<span id="78601"></span>
<div id="comment-78601" class="comment">
<div id="post-78601-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also IIRC patented <a href="https://patents.justia.com/patent/10380454">https://patents.justia.com/patent/10380454</a></p>
</div>
<div id="comment-78601-info" class="comment-info">
<span class="comment-age">(30 Jan '21, 10:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78594-form-container" class="comment-form-container">
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

