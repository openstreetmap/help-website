+++
type = "question"
title = "How to draw an OSM Entity on external map from Overpass API"
description = '''Hi there!  Say I have an arbitrary OSM entity which I want to display on a third party map (Google maps for arguments sake).. Say I want to display London Heathrow airport on my map. This is how I would like it highlighted here:  London Heathrow Airport Now, my server uses the awesome Overpass API, ...'''
date = "2015-06-15T21:47:00Z"
lastmod = "2015-06-17T21:16:00Z"
weight = 43581
keywords = [ "openstreetmap", "overpass", "draw", "osm", "map" ]
aliases = [ "/questions/43581" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to draw an OSM Entity on external map from Overpass API](/questions/43581/how-to-draw-an-osm-entity-on-external-map-from-overpass-api)

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
<span id="post-43581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there! Say I have an arbitrary OSM entity which I want to display on a third party map (Google maps for arguments sake)..</p>
<p>Say I want to display London Heathrow airport on my map. This is how I would like it highlighted here: <a href="http://www.openstreetmap.org/way/185882029#map=13/51.4698/-0.4531">London Heathrow Airport</a></p>
<p>Now, my server uses the awesome Overpass API, so if I want the bounds of the airport, I can get them like so: <a href="http://overpass-api.de/api/interpreter?data=%2F%2F%5Bout%3Acsv%28%3Bfalse%29%5D%3B%0A%5Bout%3Ajson%5D%3B%0Away%28185882029%29%3B%2F*added%20by%20auto%20repair*%2F%28._%3B%3E%3B%29%3B%2F*end%20of%20auto%20repair*%2Fout%3B">Raw Data from Overpass API for Heathrow Airport</a></p>
<p>Now this is the problem, I now have the ways and nodes that consist of the airport BUT the ways/ nodes are NOT in the correct order to outline. So how can I outline the data from the second link, like it is in the first one??</p>
<p>Or if this isnt easy/ trivial, is there any way to embed just the map section from the first link on a webpage?!</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-draw" rel="tag" title="see questions tagged &#39;draw&#39;">draw</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '15, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1382f87fca144452793d096a71d332da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister41&#39;s gravatar image" />
<p><span>gmeister41</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister41 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43581" class="comments-container">
&#10;</div>
<div id="comment-tools-43581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43581-form-container" class="comment-form-container">
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

<span id="43583"></span>

<div id="answer-container-43583" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43583-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gmeister41 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a misconception here: the nodes are in fact not in the wrong order, as the sequence information is stored in another location. You'd need to look at the node ids as they're listed in the way section of the Overpass API response. This will tell you in which sequence all nodes appear:</p>
<p>Here's the relevant part:</p>
<pre><code>  &quot;type&quot;: &quot;way&quot;,
  &quot;id&quot;: 185882029,
  &quot;nodes&quot;: [
    1216282838,
    2899060375,
    26352035,
    1215188013,
    1215188011,
    1215188014,
    1215188019,
    1215188093,
   [...]</code></pre>
<p>I'd suggest to try following alternative, which might be easier for you to parse: all nodes belonging to a way are put in place in the right order.</p>
<pre><code>[out:json];
way(185882029);
out tags geom;</code></pre>
<p>Overpass Turbo Link: <a href="http://overpass-turbo.eu/s/9WS">http://overpass-turbo.eu/s/9WS</a></p>
<p><strong>Please don't forget about correct OSM attribution, when embedding OSM data in other maps!</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '15, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-43583" class="comments-container">
<span id="43605"></span>
<div id="comment-43605" class="comment">
<div id="post-43605-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The geom command was exactly what I was after, thanks mmd. I have of course made appropriate references to the OSM data. You're the best!</p>
</div>
<div id="comment-43605-info" class="comment-info">
<span class="comment-age">(17 Jun '15, 21:16)</span> <span class="comment-user userinfo">gmeister41</span>
</div>
</div>
</div>
<div id="comment-tools-43583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43583-form-container" class="comment-form-container">
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

