+++
type = "question"
title = "Do any routing engines pay attention to the `sidewalk=separate` tag?"
description = '''I&#x27;ve noticed that the routing engines avalable on OSM.org often route pedestrians down the roadway when a sidewalk is mapped as a separate way. I added the sidewalk=separate tag to some roadways in my area, but it does not seem to make a difference. Do any routing engines give any weight to the side...'''
date = "2021-08-04T02:19:00Z"
lastmod = "2021-08-04T11:34:00Z"
weight = 81183
keywords = [ "osrm", "sidewalks", "routing", "footway", "graphhopper" ]
aliases = [ "/questions/81183" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do any routing engines pay attention to the \`sidewalk=separate\` tag?](/questions/81183/do-any-routing-engines-pay-attention-to-the-sidewalkseparate-tag)

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
<span id="post-81183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed that the routing engines avalable on OSM.org often route pedestrians down the roadway when a sidewalk is mapped as a separate way. I added the <code>sidewalk=separate</code> tag to some roadways in my area, but it does not seem to make a difference. Do any routing engines give any weight to the sidewalk=separate tag? Is there some other way I could help routing engines stick to footways when they are a better option?</p>
<p>It's not a big thing, but It'd be nice if they routed on the sidewalk when it's available.</p>
<p><strong>Edit</strong> <a href="https://graphhopper.com/maps/?point=49.2712%2C-123.10465&amp;point=49.271683%2C-123.109177&amp;locale=en-CA&amp;elevation=true&amp;profile=foot&amp;use_miles=false&amp;selected_detail=Elevation&amp;layer=OpenStreetMap">here's</a> an example.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-sidewalks" rel="tag" title="see questions tagged &#39;sidewalks&#39;">sidewalks</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '21, 02:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Aug '21, 15:53</strong> </span></p>
</div>
</div>
<div id="comments-container-81183" class="comments-container">
<span id="81192"></span>
<div id="comment-81192" class="comment">
<div id="post-81192-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It might be worth providing a link to a specific example, in case there is something about the mapping that could be improved.</p>
</div>
<div id="comment-81192-info" class="comment-info">
<span class="comment-age">(04 Aug '21, 10:50)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81193"></span>
<div id="comment-81193" class="comment">
<div id="post-81193-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As an aside, I wouldn't use the routing engines on osm.org for anything too serious - they're basically just there to say "you can do routing with this data". For example:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=53.99224%2C-0.91063%3B53.99115%2C-0.91367#map=13/53.9931/-0.9093&amp;layers=N">https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=53.99224%2C-0.91063%3B53.99115%2C-0.91367#map=13/53.9931/-0.9093&amp;layers=N</a></p>
<p>seems to think that "how trunk roads are mapped in Germany" applies to the rest of the world, and ignores the "sidewalk" tag on <a href="https://www.openstreetmap.org/way/132453634#map=18/53.99166/-0.91227&amp;layers=N">https://www.openstreetmap.org/way/132453634#map=18/53.99166/-0.91227&amp;layers=N</a> altogether. For completeness</p>
<p><a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=53.9922%2C-0.9106%3B53.9912%2C-0.9137#map=18/53.99169/-0.91216&amp;layers=N">https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=53.9922%2C-0.9106%3B53.9912%2C-0.9137#map=18/53.99169/-0.91216&amp;layers=N</a></p>
<p>doesn't make the same mistake.</p>
<p>Solving this globally is a hard problem to solve, and not really a fair thing to ask of a simple proof-of-concept.</p>
</div>
<div id="comment-81193-info" class="comment-info">
<span class="comment-age">(04 Aug '21, 11:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81183-form-container" class="comment-form-container">
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

<span id="81188"></span>

<div id="answer-container-81188" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81188-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know of this dedicated <a href="https://www.routago.de/pedestrian-routing/">Routago pedestrian routing engine</a>. It was specifically developed for blind people to receive safe walking routes. For that reason it might not always produce the shortest route but it uses sidewalks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '21, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81188" class="comments-container">
&#10;</div>
<div id="comment-tools-81188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81188-form-container" class="comment-form-container">
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

