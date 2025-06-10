+++
type = "question"
title = "How to query all junctions in a city"
description = '''I am trying to get the node (for the GPS) of all driveable junctions in a city.  Here is what I have tried out : import overpy  api = overpy.Overpass()  osmid_f = 62422 + 3600000000  result = api.query(  f&quot;&quot;&quot;  [timeout:1000][out:json];  area({osmid_f})-&amp;gt;.a; (  node(area.a)   [&#x27;junction&#x27; = &#x27;circul...'''
date = "2020-12-18T09:17:00Z"
lastmod = "2020-12-19T12:48:00Z"
weight = 77983
keywords = [ "overpass", "nodes", "query", "area" ]
aliases = [ "/questions/77983" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to query all junctions in a city](/questions/77983/how-to-query-all-junctions-in-a-city)

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
<span id="post-77983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77983-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get the node (for the GPS) of all driveable junctions in a city.<br />
Here is what I have tried out :</p>
<pre><code>import overpy
&#10;api = overpy.Overpass()
&#10;osmid_f = 62422 + 3600000000
&#10;result = api.query(
&#10;f&quot;&quot;&quot;
&#10;[timeout:1000][out:json];
&#10;area({osmid_f})-&gt;.a;
(
  node(area.a)
&#10;  [&#39;junction&#39; = &#39;circular&#39;]
&#10;  [&#39;junction&#39; = &#39;roundabout&#39;]
&#10;  [&#39;junction&#39; = &#39;jughandle&#39;]
&#10;  [&#39;junction&#39; = &#39;filter&#39;]
&#10;  [&#39;traffic_calming&#39; = &#39;island&#39;]
&#10;  [&#39;highway&#39; = &#39;mini_roundabout&#39;]
&#10;  [&#39;highway&#39; = &#39;turning_circle&#39;]
&#10;  [&#39;highway&#39; = &#39;turning_loop&#39;]
&#10;  [&#39;highway&#39; = &#39;motorway_junction&#39;]
&#10;  [&#39;highway&#39; = &#39;passing_place&#39;];
&#10;  node(w)(area.a);
&#10;);
&#10;out;
&#10;&quot;&quot;&quot;)</code></pre>
<p>But I get an empty result. Is there something I am missing ?<br />
I would appreciate any hints.<br />
Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '20, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/68b001d382235f9caa18384183210af0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dykay&#39;s gravatar image" />
<p><span>Dykay</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dykay has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '20, 10:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></br></p>
</div>
</div>
<div id="comments-container-77983" class="comments-container">
&#10;</div>
<div id="comment-tools-77983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77983-form-container" class="comment-form-container">
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

<span id="77991"></span>

<div id="answer-container-77991" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77991-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dykay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your query is searching for nodes with all of those tags together. Make a separate query for each tag:</p>
<pre><code>(
  node(area.a)[junction];
  node(area.a)[highway=mini_roundabout];
  ...
);</code></pre>
<p>and so on. Some junctions might be modeled as ways, tagged as roundabouts (rather than mini_roundabouts).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '20, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77991" class="comments-container">
<span id="78005"></span>
<div id="comment-78005" class="comment">
<div id="post-78005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a></p>
</div>
<div id="comment-78005-info" class="comment-info">
<span class="comment-age">(19 Dec '20, 12:48)</span> <span class="comment-user userinfo">Dykay</span>
</div>
</div>
</div>
<div id="comment-tools-77991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77991-form-container" class="comment-form-container">
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

