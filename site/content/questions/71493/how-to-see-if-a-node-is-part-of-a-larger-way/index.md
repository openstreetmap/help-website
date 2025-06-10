+++
type = "question"
title = "How to see if a node is &quot;part of&quot; a larger way"
description = '''If you use overpass turbo, you can click on a node that is a part of your query and it will take you to a new window for that node. There, you can see if the node is &quot;part of&quot; a way. Is there any way to get this information from a standard overpass api query?'''
date = "2019-11-06T19:45:00Z"
lastmod = "2019-11-14T03:53:00Z"
weight = 71493
keywords = [ "node", "overpass", "overpass-turbo", "way", "query" ]
aliases = [ "/questions/71493" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to see if a node is "part of" a larger way](/questions/71493/how-to-see-if-a-node-is-part-of-a-larger-way)

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
<span id="post-71493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71493-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If you use overpass turbo, you can click on a node that is a part of your query and it will take you to a new window for that node. There, you can see if the node is "part of" a way. Is there any way to get this information from a standard overpass api query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '19, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e9fd142658c2fabbd37ecaebb19c48d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Anthony%20Anthony&#39;s gravatar image" />
<p><span>John Anthony...</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Anthony Anthony has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71493" class="comments-container">
&#10;</div>
<div id="comment-tools-71493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71493-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="71517"></span>

<div id="answer-container-71517" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71517-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-71517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, please use <code>way(bn)</code>.</p>
<p>A simple example. We have queried for all the barriers in Watford near London:</p>
<pre><code>area[name=&quot;Watford&quot;];
node[barrier](area)(51.5,-1,52,0);
out;</code></pre>
<p>The query finds 84 or so.</p>
<p>Now we replace the output in line 3 by a couple of extra lines:</p>
<pre><code>area[name=&quot;Watford&quot;];
node[barrier](area)(51.5,-1,52,0);
way(bn)-&gt;.wy;
node._(w.wy);
out;</code></pre>
<p>In detail: <em><code>way(bn)-&gt;.wy</code> queries for all the ways that have the just found nodes as members</em> <code>node._(w.wy)</code> is composed of the two conditions that the node must be from the previous result (in this case line 2, since line 3 writes to elsewhere) and that it must be a node referenced by a just found way (from set <code>wy</code>, filled in line 3)</p>
<p>Thus we see only those nodes that are member of a way.</p>
<p>Further conditions on the interesting way can be injected in line 3:</p>
<pre><code>area[name=&quot;Watford&quot;];
node[barrier](area)(51.5,-1,52,0);
way(bn)[highway=cycleway]-&gt;.wy;
node._(w.wy);
out;</code></pre>
<p>Now the ways that our nodes of interest must be members of are restricted to those with the tag <code>highway=cycleway</code>.</p>
<p>It gets more tricky for the related question: What are the nodes of a way that are also connected to other ways? As an example, the query for the street named <code>Hyde Vale</code> ...</p>
<pre><code>( way[name=&quot;Hyde Vale&quot;];
  node(w); );
out;</code></pre>
<p>... becomes:</p>
<pre><code>( way[name=&quot;Hyde Vale&quot;]-&gt;.ways_to_exclude;
  node(w.ways_to_exclude)-&gt;.nodes_of_interest; );
( way(bn.nodes_of_interest)-&gt;.all_wy; - .ways_to_exclude; );
node.nodes_of_interest(w);
out geom;</code></pre>
<p>We divert this time already the ways of initial interest through a named set <code>ways_to_exclude</code> because we need them again to remove them from the list of eligible ways. Other than that, lines 3 and 4 do the exercse to walk from the nodes to the ways and back to their nodes; and line 4 ensures that we only consider nodes that we had found already. But to avoid that all nodes qualify by being part of the street <code>Hyde Vale</code> (and potentially no other way) we explicitly remove these ways with the difference statement in line 3.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-71517" class="comments-container">
<span id="71621"></span>
<div id="comment-71621" class="comment">
<div id="post-71621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So lets say this is my query:</p>
<p>[out:json]; node({}); way(bn)-&gt;.wy; node._(w.wy); out;</p>
<p>** {} is where a bounding box would go</p>
<p>Say one of the nodes that is returned is the node with id=4271787600. I can see from overpass turbo that that node is part of the way the Metropolitan Apartments. However, this query does not return me a way with name "The Metropolitan Apartments". How can I adjust the query so that I can get that information.</p>
<p>For context, I am looking to be able to query a bounding box and get names of all the buildings and streets that are found in that bounding box (all names that openstreetmap has at least).</p>
</div>
<div id="comment-71621-info" class="comment-info">
<span class="comment-age">(13 Nov '19, 22:28)</span> <span class="comment-user userinfo">John Anthony...</span>
</div>
</div>
<span id="71625"></span>
<div id="comment-71625" class="comment">
<div id="post-71625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>way({{bbox}})</code> gives you <a href="https://overpass-turbo.eu/s/O4W">all ways in the bounding box</a>. The query</p>
<pre><code>[out:json];
way({{bbox}})[building][name];
for (t[&quot;name&quot;])
{
  make building name=_.val,ids=set(id());
  out;
}
way({{bbox}})[highway][name];
for (t[&quot;name&quot;])
{
  make highway name=_.val,ids=set(id());
  out;
}</code></pre>
<p>returns <a href="https://overpass-turbo.eu/s/O4X">all names of buildings and highways</a> in the bounding box.</p>
</div>
<div id="comment-71625-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 03:53)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-71517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71512"></span>

<div id="answer-container-71512" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71512-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">recurse filters</a>. There's also an operator, <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_up_.28.3C.29"><code>&lt;</code></a>, that will find all parents of the input set.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '19, 11:37</strong> </span></p>
</div>
</div>
<div id="comments-container-71512" class="comments-container">
&#10;</div>
<div id="comment-tools-71512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71513"></span>

<div id="answer-container-71513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The recurse filter:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29</a></p>
<p>Simple example: <a href="https://overpass-turbo.eu/s/NRJ">https://overpass-turbo.eu/s/NRJ</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-71513" class="comments-container">
&#10;</div>
<div id="comment-tools-71513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71513-form-container" class="comment-form-container">
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

