+++
type = "question"
title = "How to find node which belongs to multiple ways"
description = '''Hello, I want to find all crossroads with their associated street names, but there are nodes without any attributes I can search for (like highway=crossing). For example: http://overpass-turbo.eu/s/KAg So I guess I have to search in an area for nodes which belong to two or more ways. Unfortunately I...'''
date = "2019-07-09T11:07:00Z"
lastmod = "2019-07-12T05:13:00Z"
weight = 69944
keywords = [ "node", "ways", "nominatim", "multiple", "overpass" ]
aliases = [ "/questions/69944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find node which belongs to multiple ways](/questions/69944/how-to-find-node-which-belongs-to-multiple-ways)

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
<span id="post-69944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69944-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to find all crossroads with their associated street names, but there are nodes without any attributes I can search for (like highway=crossing).</p>
<p>For example: <a href="http://overpass-turbo.eu/s/KAg">http://overpass-turbo.eu/s/KAg</a></p>
<p>So I guess I have to search in an area for nodes which belong to two or more ways. Unfortunately I don't know how to achieve such a query.</p>
<p>Any help would be appreciated, thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '19, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/89ce921afb9a7548b4ca023fd24eb564?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chrno&#39;s gravatar image" />
<p><span>Chrno</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chrno has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69944" class="comments-container">
&#10;</div>
<div id="comment-tools-69944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69944-form-container" class="comment-form-container">
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

<span id="69946"></span>

<div id="answer-container-69946" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69946-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at the examples in the wiki: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Search_for_nodes_which_belong_to_two_different_ways">Search for nodes which belong to two different ways</a> and the following one, as well as <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Search_for_street_intersections">Search for street intersections</a>. Can you take it from there to adapt these queries to your specific needs?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '19, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '19, 12:15</strong> </span></p>
</div>
</div>
<div id="comments-container-69946" class="comments-container">
<span id="69947"></span>
<div id="comment-69947" class="comment">
<div id="post-69947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just tried pasting a variation on the first of those into an overpass turbo window and got "Error: runtime error: […] The server is probably too busy to handle your request. ". Only if I zoom in to around 100m2 does it work - <a href="https://overpass-turbo.eu/s/KAD">https://overpass-turbo.eu/s/KAD</a> .</p>
</div>
<div id="comment-69947-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 12:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69959"></span>
<div id="comment-69959" class="comment">
<div id="post-69959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The example in the wiki helped, thank you!</p>
<p>Got this for now and it's showing the node I need:</p>
<p>[bbox:{{bbox}}];</p>
<p>way[highway][name="Haimhauserstraße"]-&gt;.w1;</p>
<p>way [highway] (around:1, 48.1624106, 11.5884358)-&gt;.w2;</p>
<p>node(w.w1)(w.w2);</p>
<p>out;</p>
<p><a href="http://overpass-turbo.eu/s/KCf">http://overpass-turbo.eu/s/KCf</a></p>
<p>At "48.1624106,11.5884358" I'm on/around the street of w2. Given this point, how is it possible to get the crossing street of w1 for the query without a constant value ("Haimhauserstraße")?</p>
</div>
<div id="comment-69959-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 06:19)</span> <span class="comment-user userinfo">Chrno</span>
</div>
</div>
<span id="69962"></span>
<div id="comment-69962" class="comment">
<div id="post-69962-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That works with the code given under the heading "If ways cannot be split into two distinct groups..." (although two ";" were missing):</p>
<pre><code>way[highway]({{bbox}})-&gt;.allways;  
foreach .allways -&gt; .currentway(  
  (.allways; - .currentway;)-&gt;.allotherways;  
  node(w.currentway)-&gt;.e;  
  node(w.allotherways)-&gt;.f;  
  node.e.f;  
  (._ ; .result;) -&gt; .result;  
);  
.result out meta;</code></pre>
<p><a href="http://overpass-turbo.eu/s/KCR">http://overpass-turbo.eu/s/KCR</a></p>
<p>This finds also the connection point of two road segments, though, not only strict intersections.</p>
</div>
<div id="comment-69962-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 09:50)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70001"></span>
<div id="comment-70001" class="comment">
<div id="post-70001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that works for me!</p>
</div>
<div id="comment-70001-info" class="comment-info">
<span class="comment-age">(12 Jul '19, 05:13)</span> <span class="comment-user userinfo">Chrno</span>
</div>
</div>
</div>
<div id="comment-tools-69946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69946-form-container" class="comment-form-container">
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

