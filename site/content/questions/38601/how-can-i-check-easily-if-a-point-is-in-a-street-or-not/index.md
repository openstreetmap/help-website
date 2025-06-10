+++
type = "question"
title = "How can I check easily if a point is in a street or not."
description = '''I wish to create some statistic about a distance from different places in a city to the nearest bus station. For this, naturally, I need to check if a certain point is related to a street or not. I intend to do this via a python script, but I don&#x27;t really know how to approach this. I know python fai...'''
date = "2014-11-16T16:06:00Z"
lastmod = "2014-11-17T09:13:00Z"
weight = 38601
keywords = [ "python", "streets", "longitude", "coordinates", "api" ]
aliases = [ "/questions/38601" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I check easily if a point is in a street or not.](/questions/38601/how-can-i-check-easily-if-a-point-is-in-a-street-or-not)

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
<span id="post-38601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wish to create some statistic about a distance from different places in a city to the nearest bus station. For this, naturally, I need to check if a certain point is related to a street or not. I intend to do this via a python script, but I don't really know how to approach this. I know python fairly way, and I was hoping to use a python API rather than learning an entire API from scratch for a hobby project.</p>
<p>Any pointers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '14, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b5503df110a2855854e5656e4340abb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yotam&#39;s gravatar image" />
<p><span>Yotam</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yotam has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '14, 17:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38601" class="comments-container">
&#10;</div>
<div id="comment-tools-38601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38601-form-container" class="comment-form-container">
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

<span id="38613"></span>

<div id="answer-container-38613" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38613-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will likely not get around understanding the OSM data model regardless of which API you use. Given that the model is actually very simple that should not be a problem. The</p>
<p>See</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/API_v0.6">http://wiki.openstreetmap.org/wiki/API_v0.6</a></p>
<p>specifically for your problem see the "Ways for node" call.</p>
<p>A possible python API is <a href="http://wiki.openstreetmap.org/wiki/Osmapi">http://wiki.openstreetmap.org/wiki/Osmapi</a></p>
<p>That was the good news.</p>
<p>The bad news is that you are problably setting about this completely wrong.</p>
<p>If this is any more than a very very low volume cursory check you want to do, you should not try to do this via the editing API in the first place. Particularly if this is something you want to do on a regular base you will want to import osm data in to a suitable database schema and perform queries on that database.</p>
<p>Potentially (your question is not quite clear about what kind of distance you are trying to determine, straight line or an actual route on the road/way network) you should be doing this with a routing service/api see for example the accessibility analysis on <a href="http://openrouteservice.org/">http://openrouteservice.org/</a> .</p>
<p>If you give some more information on what you are actually trying to acheive, we can probably give some more pointers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '14, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '14, 22:05</strong> </span></p>
</div>
</div>
<div id="comments-container-38613" class="comments-container">
<span id="38619"></span>
<div id="comment-38619" class="comment">
<div id="post-38619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. Thanks for the replay. My initial though was to create a heat map of my city that show how far is a certain address from the nearest bus stop. I now think that maybe graph that shows the number of houses as a function of distance from the nearest bus stop would be good too. If I could harvest data about bus frequency at each stop, I would factor that in too. But that is not a priority for me.</p>
<p>Note that I have a (hebrew) list of streets in my city, but not house numbers.</p>
</div>
<div id="comment-38619-info" class="comment-info">
<span class="comment-age">(17 Nov '14, 09:13)</span> <span class="comment-user userinfo">Yotam</span>
</div>
</div>
</div>
<div id="comment-tools-38613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38613-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38615"></span>

<div id="answer-container-38615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38615-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass_API</a> there is a python wrapper for queries:</p>
<p>This leads you to <a href="https://github.com/mvexel/overpass-api-python-wrapper">https://github.com/mvexel/overpass-api-python-wrapper</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '14, 05:48</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-38615" class="comments-container">
&#10;</div>
<div id="comment-tools-38615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38615-form-container" class="comment-form-container">
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

