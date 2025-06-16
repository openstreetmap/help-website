+++
type = "question"
title = "Can I filter to view only street lights?"
description = '''When using https://www.openstreetmap.org/ when I zoom in on a city I can see street lights on a junction. However they are not clearly visible due to their small size and the numerous other small symbols. I would like to view every traffic light in a city to compare with this post which displays ever...'''
date = "2014-03-12T14:24:00Z"
lastmod = "2014-03-12T15:56:00Z"
weight = 31484
keywords = [ "filter", "traffic_lights", "zoom", "traffic_signals" ]
aliases = [ "/questions/31484" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I filter to view only street lights?](/questions/31484/can-i-filter-to-view-only-street-lights)

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
<span id="post-31484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31484-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> when I zoom in on a city I can see street lights on a junction. However they are not clearly visible due to their small size and the numerous other small symbols.</p>
<p>I would like to view every traffic light in a city to compare with <a href="http://www.aviewfromthecyclepath.com/2014/02/every-traffic-light-in-assen.html">this post</a> which displays every traffic light in a Dutch city.</p>
<p>Is there a way of filtering the key to only display traffic lights, and when zoomed out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-traffic_lights" rel="tag" title="see questions tagged &#39;traffic_lights&#39;">traffic_lights</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '14, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0b7a4520354e979ecad4ebf0e276039b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WheelsOnTheBike&#39;s gravatar image" />
<p><span>WheelsOnTheBike</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WheelsOnTheBike has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31484" class="comments-container">
<span id="31489"></span>
<div id="comment-31489" class="comment">
<div id="post-31489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you write "street lights" in the title. But you are not referring to lighting, right? Maybe change this to "traffic light / signals" then.</p>
</div>
<div id="comment-31489-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 15:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31484-form-container" class="comment-form-container">
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

<span id="31487"></span>

<div id="answer-container-31487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31487-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WheelsOnTheBike has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this is possible. For example by using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> or <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">overpass turbo</a>.</p>
<p>Here is an example using overpass turbo:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
  &lt;union&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;highway&quot; v=&quot;traffic_signals&quot;/&gt;
      &lt;bbox-query {{nominatimBbox:Dresden}}/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>It will <a href="http://overpass-turbo.eu/s/2KP">display</a> all traffic signal for the city <em>Dresden</em>. If you choose to use the Overpass API instead, you will have to replace the <code>{{nominatimBbox:Dresden}}</code> keyword with the <a href="https://wiki.openstreetmap.org/wiki/Bounding_Box">bounding box</a> of the corresponding city, because <code>nominatimBbox</code> is an extension specific for overpass turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '14, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31487" class="comments-container">
<span id="31490"></span>
<div id="comment-31490" class="comment">
<div id="post-31490-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Perfect, thank you.</p>
</div>
<div id="comment-31490-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 15:56)</span> <span class="comment-user userinfo">WheelsOnTheBike</span>
</div>
</div>
</div>
<div id="comment-tools-31487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31487-form-container" class="comment-form-container">
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

