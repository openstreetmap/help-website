+++
type = "question"
title = "Openlayers - how do a create a moveable marker?"
description = '''How do i make my marker moveable or draggable? var markers = new OpenLayers.Layer.Markers(&quot;Markers&quot;);  map.addLayer(markers);  markers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(data[0][&#x27;lon&#x27;], data[0][&#x27;lat&#x27;]).transform( fromProjection, toProjection),icon)); '''
date = "2012-08-23T13:34:00Z"
lastmod = "2012-08-23T21:46:00Z"
weight = 15441
keywords = [ "marker", "dragging", "openlayers", "move" ]
aliases = [ "/questions/15441" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Openlayers - how do a create a moveable marker?](/questions/15441/openlayers-how-do-a-create-a-moveable-marker)

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
<span id="post-15441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15441-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do i make my marker moveable or draggable?</p>
<pre><code>var markers = new OpenLayers.Layer.Markers(&quot;Markers&quot;);
            map.addLayer(markers);
            markers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(data[0][&#39;lon&#39;], data[0][&#39;lat&#39;]).transform( fromProjection, toProjection),icon));</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-dragging" rel="tag" title="see questions tagged &#39;dragging&#39;">dragging</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-move" rel="tag" title="see questions tagged &#39;move&#39;">move</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '12, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/160ac3b841317c725f34a8bc22a40e2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kristiann&#39;s gravatar image" />
<p><span>kristiann</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kristiann has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '12, 15:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-15441" class="comments-container">
&#10;</div>
<div id="comment-tools-15441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15441-form-container" class="comment-form-container">
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

<span id="15457"></span>

<div id="answer-container-15457" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15457-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi; this isn't an OpenLayers support channel. You might have better luck with one of their <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">mailing lists</a> or #openlayers on IRC.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5eea0a101ed06779f56546479dcc80b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcw&#39;s gravatar image" />
<p><span>mcw</span><br />
<span class="score" title="416 reputation points">416</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcw has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-15457" class="comments-container">
&#10;</div>
<div id="comment-tools-15457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15457-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15462"></span>

<div id="answer-container-15462" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15462-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For completing <span>@mcw</span> answer, your question isn't trivial. Take look at the OpenLayers documentation, and at <a href="http://openlayers.org/dev/examples/modify-feature.html">this example</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15462" class="comments-container">
&#10;</div>
<div id="comment-tools-15462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15462-form-container" class="comment-form-container">
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

