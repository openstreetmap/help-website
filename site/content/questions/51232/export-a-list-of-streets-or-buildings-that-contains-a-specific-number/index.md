+++
type = "question"
title = "export a list of streets or buildings that contains a specific number"
description = '''Hi, I am totally new to OSM and would like to know if OSM will be able do to the following: Export a list of all streets (or building/house)in a certain town that contains a specific number/housenumber. For example no 88.  If it is possible, how do I do that? I am searching for a specific building i...'''
date = "2016-08-03T14:06:00Z"
lastmod = "2016-08-05T12:34:00Z"
weight = 51232
keywords = [ "export", "housenumbers", "list" ]
aliases = [ "/questions/51232" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [export a list of streets or buildings that contains a specific number](/questions/51232/export-a-list-of-streets-or-buildings-that-contains-a-specific-number)

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
<span id="post-51232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51232-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am totally new to OSM and would like to know if OSM will be able do to the following:</p>
<p>Export a list of all streets (or building/house)in a certain town that contains a specific number/housenumber. For example no 88.</p>
<p>If it is possible, how do I do that?</p>
<p>I am searching for a specific building in a photograph. The building number is visible so that's all I got.</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '16, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/596310d5c7176c31e84c39c9da6b9980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fivefootnine&#39;s gravatar image" />
<p><span>fivefootnine</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fivefootnine has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51232" class="comments-container">
&#10;</div>
<div id="comment-tools-51232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51232-form-container" class="comment-form-container">
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

<span id="51235"></span>

<div id="answer-container-51235" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51235-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://overpass-turbo.eu/">Overpass Turbo</a> would work well for doing what you want. You can move the map pane to the relevant area, use the wizard and simply enter...</p>
<p><code>addr:housenumber=88</code></p>
<p>...and run the query to search for objects in the current view with that house number. If you want it limited to a specific area rather than just the visible area, you could do something like</p>
<p><code>addr:housenumber=88 in "Paris, France"</code></p>
<p>Keep in mind that not all town boundaries are mapped, so the search using the visible area might be the most reliable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '16, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-51235" class="comments-container">
<span id="51236"></span>
<div id="comment-51236" class="comment">
<div id="post-51236-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Another thing to watch out for is that the housenumbers may not be present in OpenStreetMap. Some areas do have good address coverage, but there are many areas with few or no addresses at all.</p>
</div>
<div id="comment-51236-info" class="comment-info">
<span class="comment-age">(03 Aug '16, 17:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="51264"></span>
<div id="comment-51264" class="comment">
<div id="post-51264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This approach also has some shortcomings with <a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">interpolated address schemas</a>. A nominatim based query would probably be more to the point. Anyone volunteering to provide one?</p>
</div>
<div id="comment-51264-info" class="comment-info">
<span class="comment-age">(05 Aug '16, 12:34)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51234"></span>

<div id="answer-container-51234" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51234-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-51234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, theres a litlle trick, read these pages and use Overpass turbo to handle the OSM database. And make your selektion</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '16, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-51234" class="comments-container">
&#10;</div>
<div id="comment-tools-51234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51234-form-container" class="comment-form-container">
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

