+++
type = "question"
title = "Best way to get the road name for a node"
description = '''I&#x27;m interested in displaying the name of road/street that certain features sit on. One feature I&#x27;m interested in is &#x27;crossing&#x27; another is traffic_signal. I&#x27;ve come up with some Overpass QL (below), but is this a sensible approach, or is there a more efficient method? The bbox I&#x27;m interested in is No...'''
date = "2019-07-19T12:22:00Z"
lastmod = "2019-07-19T12:22:00Z"
weight = 70133
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/70133" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to get the road name for a node](/questions/70133/best-way-to-get-the-road-name-for-a-node)

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
<span id="post-70133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70133-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interested in displaying the name of road/street that certain features sit on. One feature I'm interested in is 'crossing' another is traffic_signal. I've come up with some Overpass QL (below), but is this a sensible approach, or is there a more efficient method? The bbox I'm interested in is Norwich, UK [bbox:52.578228,1.171761,52.693864,1.525726].<br />
Thanks, Robin</p>
<pre><code>node[&quot;highway&quot;=&quot;crossing&quot;];
    foreach {
      way(bn)[&quot;name&quot;]-&gt; .ways;
      convert result
          ::id   = id(),
          ::geom = center(geom()),
          road_name    = ways.set(t[&quot;name&quot;] ),
          road_speed = ways.set(t[&quot;maxspeed&quot;]),
          :: = ::;
    out geom;
    }
&#10; (node[&quot;highway&quot;=&quot;traffic_signals&quot;];);
    foreach {
      way(bn)[&quot;name&quot;]-&gt; .ways;
      convert result
          ::id   = id(),
          ::geom = center(geom()),
          road_name    = ways.set(t[&quot;name&quot;] ),
          road_speed = ways.set(t[&quot;maxspeed&quot;]),
          ::     = ::;
    out geom;
    }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '19, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b9eab4ea8764b8d62641c748321bf65b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobinK&#39;s gravatar image" />
<p><span>RobinK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobinK has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '19, 23:46</strong> </span></p>
</div>
</div>
<div id="comments-container-70133" class="comments-container">
&#10;</div>
<div id="comment-tools-70133" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70133-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

