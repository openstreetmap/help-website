+++
type = "question"
title = "OsmAnd doesnt find places when online"
description = '''Hello,  I wanted to switch from google maps to OsmAnd. The problem is when I type anything in the search bar or when I try to use the navigation feature the app isn&#x27;t finding any address so I decided to download my region for offline use. After that I was able to find streets and places. But my ques...'''
date = "2021-02-18T08:37:00Z"
lastmod = "2021-02-19T23:13:00Z"
weight = 78923
keywords = [ "navigation", "search", "nominatim", "osmand", "online" ]
aliases = [ "/questions/78923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OsmAnd doesnt find places when online](/questions/78923/osmand-doesnt-find-places-when-online)

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
<span id="post-78923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I wanted to switch from google maps to OsmAnd. The problem is when I type anything in the search bar or when I try to use the navigation feature the app isn't finding any address so I decided to download my region for offline use. After that I was able to find streets and places. But my question is now if I can use OsmAnd in online mode like Google maps? Let's say I don't have a specific region downloaded. Does it mean I won't be able to start navigating or find that address even tho I am online? Is there a possibility to be able to search with the app like on the OpenStreetMaps website where its powered by nominatim? Is there a plug in for the app?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-online" rel="tag" title="see questions tagged &#39;online&#39;">online</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '21, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3bd23df202a6ee5000a09d2f5af48a45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="retset123&#39;s gravatar image" />
<p><span>retset123</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="retset123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78923" class="comments-container">
&#10;</div>
<div id="comment-tools-78923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78923-form-container" class="comment-form-container">
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

<span id="78924"></span>

<div id="answer-container-78924" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78924-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-78924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OsmAnd has a strong focus on offline usage, meaning that all basic functionality works without any Internet connection. Nevertheless, various online services are supported.</p>
<p>OsmAnd supports online routing. This feature has existed before, was then removed but came back in the recent 3.9 Android release. Online routing needs to be enabled in the profile settings: Settings -&gt; &lt;profile&gt; -&gt; Navigation settings -&gt; Navigation type -&gt; Add online routing engine. Here you can choose between GraphHopper, OSRM and OpenRouteService.</p>
<p>OsmAnd supports online searching. Go to search, choose categories, then online search. Unfortunately this won't find results that are too far away from your map position (<a href="https://github.com/osmandapp/Osmand/issues/7123).">https://github.com/osmandapp/Osmand/issues/7123).</a> Meaning you have to pan the map roughly to the feature you are searching for (I think the search radius is 200 km).</p>
<p>OsmAnd supports online tiles. There is a plugin called Online maps. After enabling it, you can choose online tile servers via Configure map -&gt; Map source. Note that these are really just images, they can't be used for routing and they can't be used for searching.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '21, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78924" class="comments-container">
<span id="78954"></span>
<div id="comment-78954" class="comment">
<div id="post-78954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your fast answer and support! Now I understand the concept better. Greetings</p>
</div>
<div id="comment-78954-info" class="comment-info">
<span class="comment-age">(19 Feb '21, 23:13)</span> <span class="comment-user userinfo">retset123</span>
</div>
</div>
</div>
<div id="comment-tools-78924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78924-form-container" class="comment-form-container">
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

