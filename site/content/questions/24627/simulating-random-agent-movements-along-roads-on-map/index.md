+++
type = "question"
title = "Simulating Random Agent Movements along Roads on Map"
description = '''I need to simulate agent movements on map as follows: Agent starts a known location and moves along a road. At each road intersection, the agent uniformly chooses one possible road and moves along that. The path chosen is to be traced with a poly-line. I know how to choose a path uniformly and mark ...'''
date = "2013-07-27T17:50:00Z"
lastmod = "2013-07-27T21:00:00Z"
weight = 24627
keywords = [ "intersection", "routing", "road" ]
aliases = [ "/questions/24627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Simulating Random Agent Movements along Roads on Map](/questions/24627/simulating-random-agent-movements-along-roads-on-map)

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
<span id="post-24627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24627-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to simulate agent movements on map as follows:</p>
<p>Agent starts a known location and moves along a road. At each road intersection, the agent uniformly chooses one possible road and moves along that. The path chosen is to be traced with a poly-line.</p>
<p>I know how to choose a path uniformly and mark it with poly-lines once I have the data. But I am looking for how I can retrieve data like road intersection points and the roads leading from there on.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '13, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/16b0145fe34736a4c2c882ea6e5204dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nadeem&#39;s gravatar image" />
<p><span>Nadeem</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nadeem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>27 Jul '13, 19:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-24627" class="comments-container">
<span id="24629"></span>
<div id="comment-24629" class="comment">
<div id="post-24629-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This question belongs on gis.stackexchange.com or similar SE sites, because it has no specific connection to OSM (you are just using OSM data).</p>
</div>
<div id="comment-24629-info" class="comment-info">
<span class="comment-age">(27 Jul '13, 19:15)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="24632"></span>
<div id="comment-24632" class="comment">
<div id="post-24632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The question belongs to this forum, as I want to find road intersection along a given road form osm data</p>
</div>
<div id="comment-24632-info" class="comment-info">
<span class="comment-age">(27 Jul '13, 19:22)</span> <span class="comment-user userinfo">Nadeem</span>
</div>
</div>
<span id="24634"></span>
<div id="comment-24634" class="comment">
<div id="post-24634-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Gormo is right, this has very little to do with OSM, the issue is a generic data issue and would be the same if your underlying geodata came from any other source. (Not that I am not interested in how useful OSM data might be for such an application.</p>
</div>
<div id="comment-24634-info" class="comment-info">
<span class="comment-age">(27 Jul '13, 19:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="24636"></span>
<div id="comment-24636" class="comment">
<div id="post-24636-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Besides, <a href="/questions/15442/detection-of-intersections-in-the-maps">how to detect intersections</a> has already been answered in a different question.</p>
</div>
<div id="comment-24636-info" class="comment-info">
<span class="comment-age">(27 Jul '13, 21:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

