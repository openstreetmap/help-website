+++
type = "question"
title = "How to get id of all cities (provinces) in a country ?"
description = '''Well normally, I need to search on the internet for all cities, provinces within a country. Then I search for that name on our site (openstreetmap), after that I click for suggestion to find the ID. My far purpose is to get Polygon of that region, from the ID by using this link: http://polygons.open...'''
date = "2021-05-10T04:32:00Z"
lastmod = "2021-05-10T09:53:00Z"
weight = 80093
keywords = [ "map", "id" ]
aliases = [ "/questions/80093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get id of all cities (provinces) in a country ?](/questions/80093/how-to-get-id-of-all-cities-provinces-in-a-country)

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
<span id="post-80093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80093-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Well normally, I need to search on the internet for all cities, provinces within a country.</p>
<p>Then I search for that name on our site (openstreetmap), after that I click for suggestion to find the ID.</p>
<p>My far purpose is to get Polygon of that region, from the ID by using this link: <a href="http://polygons.openstreetmap.fr/get_geojson.py?id=1903516">http://polygons.openstreetmap.fr/get_geojson.py?id=1903516</a></p>
<p>But I have a difficult time finding all ID.</p>
<p>Is there any api to get ID of all cities (provinces) within a country, or districts within a city ? or a site that can do so ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '21, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e224421abf98ea33d2baa8d59fff69ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LoiChau&#39;s gravatar image" />
<p><span>LoiChau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LoiChau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80093" class="comments-container">
<span id="80098"></span>
<div id="comment-80098" class="comment">
<div id="post-80098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like this ID is just the relation ID of the administrative boundary: <a href="https://www.openstreetmap.org/relation/1903516">https://www.openstreetmap.org/relation/1903516</a></p>
</div>
<div id="comment-80098-info" class="comment-info">
<span class="comment-age">(10 May '21, 08:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80093-form-container" class="comment-form-container">
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

<span id="80104"></span>

<div id="answer-container-80104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">Overpass QL</a>, some examples might even fit your bill.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '21, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80104" class="comments-container">
&#10;</div>
<div id="comment-tools-80104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80104-form-container" class="comment-form-container">
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

