+++
type = "question"
title = "API to find the nearest major highway to a smaller road?"
description = '''I&#x27;m currently using the Overpass API to do some queries that give me a particular Way of interest with highway=residential|unclassified|tertiary|secondary. Now I would like to find the nearest Way with highway=motorway|trunk|primary. I know I could do something like this: way(123456789)-&amp;gt;.myroad;...'''
date = "2017-02-03T00:37:00Z"
lastmod = "2017-02-04T03:31:00Z"
weight = 54434
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/54434" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [API to find the nearest major highway to a smaller road?](/questions/54434/api-to-find-the-nearest-major-highway-to-a-smaller-road)

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
<span id="post-54434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently using the Overpass API to do some queries that give me a particular Way of interest with highway=residential|unclassified|tertiary|secondary. Now I would like to find the nearest Way with highway=motorway|trunk|primary. I know I could do something like this:</p>
<pre><code>way(123456789)-&gt;.myroad;
way(around.myroad:5000)[highway~&quot;^(motorway|trunk|primary)$&quot;];
out qt;</code></pre>
<p>and then process through the results, calculating the distance between each of the returned ways and my original road way and take the shortest one. If none are found I could requery for 10000 meters, etc. But that is not precise enough for my needs. The closest Way in straight overland distance is not necessarily the closest by roads. It may not even connect for dozens of miles due to terrain.</p>
<p>Is there maybe a routing API that could handle this type of need? I'd prefer something that uses OSM data so I could feed it in the way ID for my starting road, but I could just as easily specify a coordinate. I wouldnt be able to specify a definite destination.</p>
<p>As a bonus, I'd also like to be able to do the same thing for other types of map features as well, like nearest (by road distance, not as the crow flies) city/town, bus stop, gas station, etc to the smaller road.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '17, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c49788c38bdb7c114ccf27d800a3bd73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joshcoady&#39;s gravatar image" />
<p><span>joshcoady</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joshcoady has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '17, 00:44</strong> </span></p>
</div>
</div>
<div id="comments-container-54434" class="comments-container">
&#10;</div>
<div id="comment-tools-54434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54434-form-container" class="comment-form-container">
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

<span id="54438"></span>

<div id="answer-container-54438" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I doubt that there is a off the shelf solution but it wouldn't be particularly difficult to do with any of the available routing engines (for example OSRM or graphhopper), you should however probably run your own instance if you are planing to do such queries in a larger way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '17, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54438" class="comments-container">
<span id="54443"></span>
<div id="comment-54443" class="comment">
<div id="post-54443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you give me a push in the right direction? I looked (briefly) at OSRM, but it seemed like I needed to know the destination in order for it to route. Did I miss another way to query for a route? Yes, I'll be doing this on private instances.</p>
</div>
<div id="comment-54443-info" class="comment-info">
<span class="comment-age">(03 Feb '17, 17:34)</span> <span class="comment-user userinfo">joshcoady</span>
</div>
</div>
<span id="54444"></span>
<div id="comment-54444" class="comment">
<div id="post-54444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you need to know two points. One point is the road you are currently on and the other point the road you found via Overpass API. With OSRM you can check if the road is connected to your road and how long the distance/drive time will be. Needs still a lot of queries in the worst case, though.</p>
</div>
<div id="comment-54444-info" class="comment-info">
<span class="comment-age">(03 Feb '17, 19:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54448"></span>
<div id="comment-54448" class="comment">
<div id="post-54448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right. I think that should mostly be doable. I think I could do it with a max of 1-2 overpass queries to see if there are a couple highways in the immediate vicinity of the road (maybe 3km then 10km radius). If that results in 1-4 highways, route to each and find the nearest one. If results in zero or 5+ then I'm thinking I could just route to 4 points 200km N, S, E, and W of the road and one of those should eventually use a highway. So a max of 4 routing queries.</p>
</div>
<div id="comment-54448-info" class="comment-info">
<span class="comment-age">(04 Feb '17, 03:31)</span> <span class="comment-user userinfo">joshcoady</span>
</div>
</div>
</div>
<div id="comment-tools-54438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54438-form-container" class="comment-form-container">
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

