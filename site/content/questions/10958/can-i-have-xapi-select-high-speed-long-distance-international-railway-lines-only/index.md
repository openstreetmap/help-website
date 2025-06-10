+++
type = "question"
title = "Can I have XAPI select high-speed/ long-distance/ international railway lines only?"
description = '''I&#x27;m creating a high level static navigation map of the Netherlands from OSM data, extracted via Overpass&#x27;s Xapi-style interface. At this scale I want to show how people might travel between cities/ countries -- the top level of the transport infrastructure for long distance intercity travel. The mot...'''
date = "2012-03-03T18:18:00Z"
lastmod = "2012-03-04T11:12:00Z"
weight = 10958
keywords = [ "high-speed", "railway", "intercity" ]
aliases = [ "/questions/10958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I have XAPI select high-speed/ long-distance/ international railway lines only?](/questions/10958/can-i-have-xapi-select-high-speed-long-distance-international-railway-lines-only)

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
<span id="post-10958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm creating a high level static navigation map of the Netherlands from OSM data, extracted via Overpass's Xapi-style interface. At this scale I want to show how people might travel between cities/ countries -- the top level of the transport infrastructure for long distance intercity travel.</p>
<p>The motorway network was really easy to collect and display (from <em>way[highway=motorway]</em>), but I'm getting time-outs pulling the <em>[railway=rail]</em> data back. Rather than increase the time-out and have a huge mass of data, is there any way to restrict the lines to the fast mainline intercity routes?</p>
<p>This works:<br />
<a href="http://www.overpass-api.de/api/xapi?way%5Bhighway=motorway%5D%5Bbbox=3.3,50.6,7.3,53.6%5D">http://www.overpass-api.de/api/xapi?way[highway=motorway][bbox=3.3,50.6,7.3,53.6]</a></p>
<p>This times out:<br />
<a href="http://www.overpass-api.de/api/xapi?way%5Brailway=rail%5D%5Bbbox=3.3,50.6,7.3,53.6%5D">http://www.overpass-api.de/api/xapi?way[railway=rail][bbox=3.3,50.6,7.3,53.6]</a></p>
<p>(Apologies if this is trivial .. I've browsed to and fro in the documentation and I just can't see the answer!)</p>
<p>PS: I've now loaded a small area of <em>way[railway=rail]</em> data, and it is far too detailed -- every line on every wharf in every port for instance -- so useless for my needs in its present state. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-high-speed" rel="tag" title="see questions tagged &#39;high-speed&#39;">high-speed</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-intercity" rel="tag" title="see questions tagged &#39;intercity&#39;">intercity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '12, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/6f7f371cdb061bf0d289a885af8705cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ViewFromTheBoundary&#39;s gravatar image" />
<p><span>ViewFromTheB...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ViewFromTheBoundary has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '12, 21:46</strong> </span></p>
</div>
</div>
<div id="comments-container-10958" class="comments-container">
<span id="10961"></span>
<div id="comment-10961" class="comment">
<div id="post-10961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thinking laterally, I should be able to get a handle on the long (distance) passenger train routes by looking for long passenger trains. Platforms over 300m long are unlikely to be used for local traffic only. Now all that's needed is a way of querying an external train service info provider such as <a href="http://diebahn.de">diebahn.de</a> to get average speeds (minimum journey times) between them, ..</p>
<p>If I get anywhere useful with this, I'll come back to see how to store the results in OSM</p>
</div>
<div id="comment-10961-info" class="comment-info">
<span class="comment-age">(04 Mar '12, 08:58)</span> <span class="comment-user userinfo">ViewFromTheB...</span>
</div>
</div>
<span id="10962"></span>
<div id="comment-10962" class="comment">
<div id="post-10962-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Solved, I think.</p>
<p>Train routes are stored as relations on the ways, eg the relation with id=1323496 is "Route train 9300 Thalys Paris- Amsterdam". If there are enough of these correctly identified, I can pull out all of the relations which include the texts "Eurostar", "Thalys", "IC" etc, and (manually) add the modifying tag "usage=main" to their ways.</p>
<p>OSM will then have the main routes tagged up, and my XAPI call will be able to pull them out.</p>
</div>
<div id="comment-10962-info" class="comment-info">
<span class="comment-age">(04 Mar '12, 11:12)</span> <span class="comment-user userinfo">ViewFromTheB...</span>
</div>
</div>
</div>
<div id="comment-tools-10958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10958-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

