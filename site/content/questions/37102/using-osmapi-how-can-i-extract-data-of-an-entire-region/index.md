+++
type = "question"
title = "Using OsmApi, how can I extract data of an entire region?"
description = '''Hi! I&#x27;m using python with OsmApi - a beautiful python api that let&#x27;s me directly connect and download data as lists of dictionary objects based on things like nodes, ways, and relations. I&#x27;m trying to extract all the data in a region using its relation id, but since the way it works is to retrieve t...'''
date = "2014-09-29T01:51:00Z"
lastmod = "2014-10-07T17:05:00Z"
weight = 37102
keywords = [ "python", "newbie", "boundaries", "osm" ]
aliases = [ "/questions/37102" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Using OsmApi, how can I extract data of an entire region?](/questions/37102/using-osmapi-how-can-i-extract-data-of-an-entire-region)

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
<span id="post-37102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm using python with OsmApi - a beautiful python api that let's me directly connect and download data as lists of dictionary objects based on things like nodes, ways, and relations.</p>
<p>I'm trying to extract all the data in a region using its relation id, but since the way it works is to retrieve the boundary way objects of the region, I'm not too sure on how to get all the ways/nodes inside it efficiently.</p>
<p>Any help would be greatly appreciated :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '14, 01:51</strong></p>
<img src="https://secure.gravatar.com/avatar/393bd6eb6cac32c2655befe374e3135d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmoak3&#39;s gravatar image" />
<p><span>jmoak3</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmoak3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37102" class="comments-container">
&#10;</div>
<div id="comment-tools-37102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37102-form-container" class="comment-form-container">
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

<span id="37105"></span>

<div id="answer-container-37105" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37105-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jmoak3 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If that just front-ends the main OSM API (as the <a href="https://wiki.openstreetmap.org/wiki/Osmapi">wiki page</a> suggests) I wouldn't use it AT ALL for large downloads. What you need is something that front-ends something like <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a>. Perhaps ask the authors of your Python framework how they suggest that you do that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '14, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37105" class="comments-container">
<span id="37117"></span>
<div id="comment-37117" class="comment">
<div id="post-37117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was afraid of that, all roads always point to Overpass haha</p>
<p>Thanks, I'll send them some emails and look into how to integrate Overpass with my current python project :)</p>
</div>
<div id="comment-37117-info" class="comment-info">
<span class="comment-age">(29 Sep '14, 18:37)</span> <span class="comment-user userinfo">jmoak3</span>
</div>
</div>
</div>
<div id="comment-tools-37105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37105-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37391"></span>

<div id="answer-container-37391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to download all nodes, ways etc. inside the area using osmapi, all you can do at the moment is using a so called "bounding box", this means you simply specify a rectangle, and you get everything that's inside that rectangle. To do this, use the <code>Map</code> function.</p>
<p>But finally if you have a very specific area and you only want ways inside it, then you're better of to import the OpenStreetMap data in a database (e.g. PostgreSQL with PostGIS), and then you can use the full query power to achieve exactly what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '14, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/28183e09aff101bc1f80c7e7a1917d83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Odi&#39;s gravatar image" />
<p><span>Odi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Odi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37391" class="comments-container">
&#10;</div>
<div id="comment-tools-37391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37391-form-container" class="comment-form-container">
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

