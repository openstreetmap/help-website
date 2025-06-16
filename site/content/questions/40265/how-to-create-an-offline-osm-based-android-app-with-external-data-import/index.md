+++
type = "question"
title = "How to create an offline OSM based Android app with external data import ?"
description = '''I am new to OpenStreetMap and I would like to develop and android app that can work offline by using the tiles downloaded from any OSM data source like MapNik,MapQuest etc. In addition to offline functionality, the app should display new places as well as new routes from an external file/ data which...'''
date = "2015-01-12T19:49:00Z"
lastmod = "2015-01-12T21:11:00Z"
weight = 40265
keywords = [ "android", "gpx", "offlinemaps" ]
aliases = [ "/questions/40265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create an offline OSM based Android app with external data import ?](/questions/40265/how-to-create-an-offline-osm-based-android-app-with-external-data-import)

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
<span id="post-40265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to OpenStreetMap and I would like to develop and android app that can work offline by using the tiles downloaded from any OSM data source like MapNik,MapQuest etc. In addition to offline functionality, the app should display new places as well as new routes from an external file/ data which is placed on my own server.</p>
<p>I tried using GPX files to load the routes and it doesn't look interactive as it is always displaying as a single line for all zoom levels.</p>
<p>So anyone please let me know whether the above things are achievable or not ? If yes, kindly suggest a way to implement this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '15, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/8f48a6d85fe9cfcf171a5628264b7330?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuantony&#39;s gravatar image" />
<p><span>manuantony</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuantony has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '15, 23:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-40265" class="comments-container">
&#10;</div>
<div id="comment-tools-40265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40265-form-container" class="comment-form-container">
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

<span id="40267"></span>

<div id="answer-container-40267" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40267-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, of course that is possible, such <span>Android apps</span> (e.g. OsmAnd) and frameworks/libraries exist already. I would suggest you look at those (many are OpenSource). After reading more you could ask a more specific question.</p>
<p>Note, that downloading tiles (parts of a rendered map) from openstreetmap.org is subject to the <span>tile usage policy</span>. Downloading tiles for offline usage is usually also not a good idea for other reasons.</p>
<p>Also we have already many older questions (with answers) regarding android development; please just click the tag below your question (note that those lists can be sorted) and read those.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '15, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '15, 20:16</strong> </span></p>
</div>
</div>
<div id="comments-container-40267" class="comments-container">
<span id="40268"></span>
<div id="comment-40268" class="comment">
<div id="post-40268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. I have successfully loaded offline data with the map by using the data from atlas creator and OSMDroid android library. Also I checked the OSMAnd app and I haven't found any way to edit the map data(not sure if such features exists with it). I still confused about how we can edit the map offline ? will it possible by using GPX files ?</p>
</div>
<div id="comment-40268-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 20:45)</span> <span class="comment-user userinfo">manuantony</span>
</div>
</div>
<span id="40269"></span>
<div id="comment-40269" class="comment">
<div id="post-40269-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10312/manuantony"></a><a href="https://help.openstreetmap.org/users/10312/manuantony">@manuantony</a>: what do you mean by "edit the map data"? Do you want to use a mobile application (your newly developed one?) to edit the OSM data on the main server (the data for everyone)? And could you please clarify what you mean by "by using GPX files" in the context of "edit the map data"?</p>
</div>
<div id="comment-40269-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 21:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40267-form-container" class="comment-form-container">
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

