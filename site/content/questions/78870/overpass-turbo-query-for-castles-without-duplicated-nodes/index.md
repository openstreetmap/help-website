+++
type = "question"
title = "Overpass turbo query for castles without duplicated nodes"
description = '''Hi, I want to build a query that returns for a given bbox:  List of POIs (one single node with coordinates) for all castles (historic=castle) Some castles are mapped multiple times, for example: castle Trifels (Germany), so these rules should be applied: If a single waypoint for historic=castle exis...'''
date = "2021-02-16T08:04:00Z"
lastmod = "2021-02-16T08:04:00Z"
weight = 78870
keywords = [ "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/78870" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo query for castles without duplicated nodes](/questions/78870/overpass-turbo-query-for-castles-without-duplicated-nodes)

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
<span id="post-78870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78870-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to build a query that returns for a given bbox:</p>
<ul>
<li>List of POIs (one single node with coordinates) for all castles (historic=castle)</li>
<li>Some castles are mapped multiple times, for example: castle Trifels (Germany), so these rules should be applied:</li>
<li>If a single waypoint for historic=castle exists, this should be choosen</li>
<li>If not waypoint exists, the center of a way or relation should be used</li>
<li>Multiple mappings should be detected by a radius, as sometimes names are mapped different and thus a name can not be used as unique identifier.</li>
</ul>
<p>In case of Trifels, there exists a way and a relation, both named different. But there is no single waypoint (node) for the castle.</p>
<p>Here is my code so far: <a href="https://overpass-turbo.eu/s/13Hp">https://overpass-turbo.eu/s/13Hp</a></p>
<pre><code>[out:json];
// Find all castles, for testing 
nwr
  [historic=castle][name~&quot;.*Trifels&quot;]
  ({{bbox}});
map_to_area -&gt; .a;
&#10;foreach.a-&gt;.elem(
  // find areas already in .final near the curreent element
  area.final(around.elem:200) -&gt; .deb;
  // get the nodes in this area, if any
  node(area.deb) -&gt; .deb2;
&#10;  // if no nodes are in deb2, this is not a duplicate, so we can add it to .final
  if(.deb2.count(nodes) == 0) {
    (.elem; .final;) -&gt; .final;
  }
);
&#10;.final out center; // .final contains areas, so we need center to get a single waypoint</code></pre>
<p>But this returns both areas. It seems that someting is going wrong with the count. And this code is not complete, as it as no weighting for nodes vs. ways vs. realations. It's just first come, first serve.</p>
<p>Can someone help me to understand how to build such a query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '21, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/97b633ea0f4a48b031df980a6eba8050?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cytrinox&#39;s gravatar image" />
<p><span>cytrinox</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cytrinox has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78870" class="comments-container">
&#10;</div>
<div id="comment-tools-78870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78870-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

