+++
type = "question"
title = "Get a list of nodes traversed by a list of coordinates"
description = '''Hi, I am looking for a way to get a list of nodes that essentially captures a list of gps coordinates. I would assume this to be in the &#x27;match&#x27; service where when you pass a list of gps points, it will match them to a route and then also return a list of nodes that belongs to that route. You current...'''
date = "2021-11-13T09:41:00Z"
lastmod = "2021-11-18T07:58:00Z"
weight = 82551
keywords = [ "osrm", "nodes", "matching" ]
aliases = [ "/questions/82551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get a list of nodes traversed by a list of coordinates](/questions/82551/get-a-list-of-nodes-traversed-by-a-list-of-coordinates)

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
<span id="post-82551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am looking for a way to get a list of nodes that essentially captures a list of gps coordinates. I would assume this to be in the 'match' service where when you pass a list of gps points, it will match them to a route and then also return a list of nodes that belongs to that route. You currently can pass annotations=true and 'legs' in the annotation object can be used for this by basically combining all the nodes for each tracepoint and removing the duplicates but it sounds like a hack and not a proper method. Also, not sure if that is going to be accurate. Any help will be greatly appreciated. :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '21, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/dc43ae77e987854246ab4f6c496da9a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ayuz&#39;s gravatar image" />
<p><span>ayuz</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ayuz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '21, 09:43</strong> </span></p>
</div>
</div>
<div id="comments-container-82551" class="comments-container">
&#10;</div>
<div id="comment-tools-82551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82551-form-container" class="comment-form-container">
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

<span id="82596"></span>

<div id="answer-container-82596" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82596-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are number of services that provide map matching, for example <a href="https://www.graphhopper.com/blog/2016/08/08/releasing-the-map-matching-api/">https://www.graphhopper.com/blog/2016/08/08/releasing-the-map-matching-api/</a> or <a href="http://project-osrm.org/docs/v5.5.1/api/#match-service">http://project-osrm.org/docs/v5.5.1/api/#match-service</a></p>
<p>You don't indicate what kind of volume of tracks you intend to process, so it isn't possible to determine if a public instance of such server will work for you, or if you need to use a paid service or run your own instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '21, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-82596" class="comments-container">
<span id="82611"></span>
<div id="comment-82611" class="comment">
<div id="post-82611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. I am aware of the map matching service provided by the osrm server. My exact question is if it is possible to get the OSM nodes along the path of the points that I pass. So, I need a service where I pass a list of gps coordinates and what I get back is a list of coordinates snapped to a route and also nodes that make up this route. Map match service from osrm server does return me the list of snapped coordinates but not the list of OSM nodes. Not sure if I am clear yet. :)</p>
</div>
<div id="comment-82611-info" class="comment-info">
<span class="comment-age">(17 Nov '21, 18:48)</span> <span class="comment-user userinfo">ayuz</span>
</div>
</div>
<span id="82613"></span>
<div id="comment-82613" class="comment">
<div id="post-82613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wouldn't expect this to be available out of the box as it would require the OSM ids for all the ways along the route to be retained.</p>
</div>
<div id="comment-82613-info" class="comment-info">
<span class="comment-age">(18 Nov '21, 07:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82596" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82596-form-container" class="comment-form-container">
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

