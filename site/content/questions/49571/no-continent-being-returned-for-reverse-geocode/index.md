+++
type = "question"
title = "No Continent being returned for reverse geocode"
description = '''I am wanting to return the Continent for a reverse geocode, I have used the documentation links as an example but I seem to be getting everything but the continent returned. http://nominatim.openstreetmap.org/search/Unter%20den%20Linden%201%20Berlin?format=json&amp;amp;addressdetails=1&amp;amp;limit=1&amp;amp;p...'''
date = "2016-05-04T12:11:00Z"
lastmod = "2016-05-04T13:57:00Z"
weight = 49571
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/49571" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No Continent being returned for reverse geocode](/questions/49571/no-continent-being-returned-for-reverse-geocode)

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
<span id="post-49571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am wanting to return the Continent for a reverse geocode, I have used the documentation links as an example but I seem to be getting everything but the continent returned.</p>
<p><a href="http://nominatim.openstreetmap.org/search/Unter%20den%20Linden%201%20Berlin?format=json&amp;addressdetails=1&amp;limit=1&amp;polygon_svg=1">http://nominatim.openstreetmap.org/search/Unter%20den%20Linden%201%20Berlin?format=json&amp;addressdetails=1&amp;limit=1&amp;polygon_svg=1</a></p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1</a></p>
<p>Am I doing something wrong? missing parameter?</p>
<p>Any help greatly appreciated.</p>
<p>Regards,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '16, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/fa9b4d779fe00b5f5e55b879dd238d5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john5092563&#39;s gravatar image" />
<p><span>john5092563</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john5092563 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49571" class="comments-container">
&#10;</div>
<div id="comment-tools-49571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49571-form-container" class="comment-form-container">
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

<span id="49572"></span>

<div id="answer-container-49572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49572-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim imports the 7 continents, but only as center point. So you can search for "Europe" only and get a result back.</p>
<p>That means for example Europe <a href="http://www.openstreetmap.org/node/25871341">http://www.openstreetmap.org/node/25871341</a> is treated as a child of Germany, not its parent.</p>
<p>What is the usecase you need continents for? I wanted to add those to <a href="https://geocoder.opencagedata.com/">https://geocoder.opencagedata.com/</a> because we use multiple geocoders and some return a continent while others (like Nominatim) don't and that's inconsistent. I would probably use a fixed country=&gt;continent mapping though which might be incorrect for cities which are on two continents (Istanbul).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '16, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-49572" class="comments-container">
<span id="49573"></span>
<div id="comment-49573" class="comment">
<div id="post-49573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess the actual reason is that <a href="https://taginfo.openstreetmap.org/tags/?key=place&amp;value=continent#overview">OSM has all its continents just defined as nodes</a>, not as ways / boundary relations. I wonder what the reason for this is.</p>
</div>
<div id="comment-49573-info" class="comment-info">
<span class="comment-age">(04 May '16, 13:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49574"></span>
<div id="comment-49574" class="comment">
<div id="post-49574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the general avoidance of super-national borders, be it continents or trade areas (European Union, NAFTA). In Taginfo all admin_level 0 or 1 I see are errors. admin_level=2 are countries.</p>
</div>
<div id="comment-49574-info" class="comment-info">
<span class="comment-age">(04 May '16, 13:57)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-49572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49572-form-container" class="comment-form-container">
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

