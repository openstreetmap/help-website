+++
type = "question"
title = "How to calculate street length from osm data?"
description = '''Hello people! I am new to OSM so I am sorry if my question seems stupid to someone. Currently I am doing a Java project using real world map data, so naturally OSM was my choice to obtain the data. The idea of the project is simple - osm data (in my case in json format) is parsed and loaded into the...'''
date = "2015-10-04T18:03:00Z"
lastmod = "2015-10-04T22:58:00Z"
weight = 45705
keywords = [ "calculation", "graph", "length", "java", "development" ]
aliases = [ "/questions/45705" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate street length from osm data?](/questions/45705/how-to-calculate-street-length-from-osm-data)

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
<span id="post-45705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45705-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello people!</p>
<p>I am new to OSM so I am sorry if my question seems stupid to someone. Currently I am doing a Java project using real world map data, so naturally OSM was my choice to obtain the data.</p>
<p>The idea of the project is simple - osm data (in my case in json format) is parsed and loaded into the java and from there I build a weighted directed graph to represent the whole map. All calculations that I need to do are done on the graph. So far i've made a simple module to parse the nodes and ways from the OSM json file thus I have the nodes and the edges of my graph. The problem is that OSM data did not have any info on the length of the ways/streets. I need that information because this is going to be the weights on my graph.</p>
<p>I tried using JOSM, it had a measurement tool which gave me the lengths of the road segments but I have absolutely no idea how it works.</p>
<p>Is there a way to obtain this kind of data? Are there any other services on the internet that provide real world map data but with lengths of street segments included?</p>
<p>Thanks for you help! If you have any clarifying questions I will gladly answer!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-calculation" rel="tag" title="see questions tagged &#39;calculation&#39;">calculation</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '15, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/420c661426ff2fcb9a0176a68d73bb69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PepeTheFrog&#39;s gravatar image" />
<p><span>PepeTheFrog</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PepeTheFrog has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '15, 21:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45705" class="comments-container">
&#10;</div>
<div id="comment-tools-45705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45705-form-container" class="comment-form-container">
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

<span id="45706"></span>

<div id="answer-container-45706" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45706-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Each <a href="https://wiki.openstreetmap.org/wiki/Elements">node</a> has a real-world coordinate. To get the length of a way, calculate the distance based on the coordinates of its nodes (WGS84 projection). A popular formula for these calculations is the Haversine formula, and you'll find example implementations for many programming languages on the web. Way lengths are not explicitly saved in the OSM data.</p>
<p>If you are doing a routing software, have a look at the many open source <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> software which uses OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '15, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '15, 22:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-45706" class="comments-container">
<span id="45707"></span>
<div id="comment-45707" class="comment">
<div id="post-45707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Esp. the <a href="http://code.google.com/p/trafficmining/">trafficmining</a> framework might be interesting to you to play around with routing, without struggling to much with our raw data ;-)</p>
</div>
<div id="comment-45707-info" class="comment-info">
<span class="comment-age">(04 Oct '15, 21:26)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="45709"></span>
<div id="comment-45709" class="comment">
<div id="post-45709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not only related to routing, i have other stuff to do as well, but thanks anyway! I have also found this, for anyone who is trying to tackle the same problem, it might be useful: <a href="https://skorasaurus.wordpress.com/2014/05/07/how-i-measured-clevelands-length-of-roads-with-postgis-and-osm/">https://skorasaurus.wordpress.com/2014/05/07/how-i-measured-clevelands-length-of-roads-with-postgis-and-osm/</a></p>
</div>
<div id="comment-45709-info" class="comment-info">
<span class="comment-age">(04 Oct '15, 22:58)</span> <span class="comment-user userinfo">PepeTheFrog</span>
</div>
</div>
</div>
<div id="comment-tools-45706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45706-form-container" class="comment-form-container">
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

