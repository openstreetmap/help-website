+++
type = "question"
title = "Dutch Bicycle node network data missing?"
description = '''I am currently trying to get the full bicycle node network for the netherlands using the overpass API and I noticed something very odd. At least one (and probably loads more) node has no relations for connections to other nodes. By using the overpass query: &amp;lt;id-query ref=&quot;15080799&quot; type=&quot;node&quot;/&amp;g...'''
date = "2013-01-21T14:00:00Z"
lastmod = "2013-01-22T20:25:00Z"
weight = 19234
keywords = [ "data", "nodes", "bicycle", "incomplete" ]
aliases = [ "/questions/19234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dutch Bicycle node network data missing?](/questions/19234/dutch-bicycle-node-network-data-missing)

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
<span id="post-19234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to get the full bicycle node network for the netherlands using the overpass API and I noticed something very odd. At least one (and probably loads more) node has no relations for connections to other nodes.</p>
<p>By using the overpass query:</p>
<p>&lt;id-query ref="15080799" type="node"/&gt; &lt;recurse type="node-relation"/&gt; &lt;print/&gt;</p>
<p>I found that the only relation it is in is the bicycle node network for the province Utrecht. Which contains a number of relations that are connections between nodes, but none including this specific node.</p>
<p>If you look at the map at coordinates: 52.0917849 5.1047520 and set view to cycling, you see that this node 26 is connected by light blue lines to node 20 and it seems it's also connected to nodes 31, 38 and 23, but I can't find the data for that connection, I know it must exist because the line is there, but it doesn't seem to be a relation or a way...</p>
<p>can anyone tell me where to find it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-incomplete" rel="tag" title="see questions tagged &#39;incomplete&#39;">incomplete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '13, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/eae8ee6cf28243e8986e0175081a1c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoefschildpad&#39;s gravatar image" />
<p><span>Zoefschildpad</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoefschildpad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19234" class="comments-container">
&#10;</div>
<div id="comment-tools-19234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19234-form-container" class="comment-form-container">
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

<span id="19240"></span>

<div id="answer-container-19240" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19240-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://mijndev.openstreetmap.nl/~ligfietser/fiets/?map=route&amp;zoom=17&amp;lat=52.09139&amp;lon=5.10469&amp;layers=000B00FFTFFFFFFFFF">This map</a> uses the following query to get the bicycle node data in an area: <code>?data=relation(bbox)[network=rcn];(way(r)(bbox);node(w););out+skel;node(bbox)[rcn_ref];out;</code></p>
<p>I can also see all the bicycle route relations around node 26 in Utrecht in JOSM, so they definitely exist as relations.</p>
<p>What query are you using to get the cycle node data from the Overpass API?</p>
<p>Edit:</p>
<p>I have not tested the query below, but I think it is the one you need to get the complete Dutch cycle node network. That is a lot of data, so you might need to fiddle with timeouts.</p>
<pre><code>&lt;union&gt;
    &lt;query type=&quot;relation&quot;&gt;
        &lt;has-kv k=&quot;type&quot; v=&quot;network&quot;/&gt;
        &lt;has-kv k=&quot;network&quot; v=&quot;rcn&quot;/&gt;
        &lt;has-kv k=&quot;addr:country&quot; v=&quot;NL&quot;/&gt;
    &lt;/query&gt;
    &lt;recurse type=&quot;relation-node&quot; into=&quot;nodes&quot;/&gt;
    &lt;recurse type=&quot;relation-relation&quot;/&gt;
    &lt;recurse type=&quot;relation-way&quot;/&gt;
    &lt;recurse type=&quot;way-node&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '13, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '13, 23:52</strong> </span></p>
</div>
</div>
<div id="comments-container-19240" class="comments-container">
<span id="19242"></span>
<div id="comment-19242" class="comment">
<div id="post-19242-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This gets me the RCN by region (one big relation per region of nodes and relations):</p>
<p>&lt;query type="relation"&gt;<br />
&lt;has-kv k="network" v="rcn"/&gt;<br />
&lt;has-kv k="addr:country" v="NL"/&gt;<br />
&lt;/query&gt;<br />
&lt;print/&gt;</p>
<p>This should get me the nodes:</p>
<p>&lt;query type="relation"&gt;<br />
&lt;has-kv k="network" v="rcn"/&gt;<br />
&lt;has-kv k="addr:country" v="NL"/&gt;<br />
&lt;/query&gt;<br />
&lt;recurse type="relation-node"/&gt;<br />
&lt;print/&gt;</p>
<p>but neither:</p>
<p>&lt;query type="relation"&gt;<br />
&lt;has-kv k="network" v="rcn"/&gt;<br />
&lt;has-kv k="addr:country" v="NL"/&gt;<br />
&lt;/query&gt;<br />
&lt;recurse type="relation-relation"/&gt;<br />
&lt;print/&gt;</p>
<p>nor:</p>
<p>&lt;query type="relation"&gt;<br />
&lt;has-kv k="network" v="rcn"/&gt;<br />
&lt;has-kv k="addr:country" v="NL"/&gt;<br />
&lt;/query&gt;<br />
&lt;recurse type="relation-node"/&gt;<br />
&lt;recurse type="node-relation"/&gt;<br />
&lt;print/&gt;</p>
<p>nor:</p>
<p>&lt;id-query ref="15080799" type="node"/&gt;<br />
&lt;recurse type="node-relation" /&gt;<br />
&lt;print/&gt;</p>
<p>gets me any relation containing node id 15080799 other than the one for all of Utrecht I got with the very first query</p>
</div>
<div id="comment-19242-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 19:55)</span> <span class="comment-user userinfo">Zoefschildpad</span>
</div>
</div>
<span id="19244"></span>
<div id="comment-19244" class="comment">
<div id="post-19244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sometime last year some people have decided that the nodes no longer have to be part of the relations connecting the nodes. The whole of Flanders and large parts of the Netherlands are updated to this "improved" tagging scheme. See the changes to <a href="https://wiki.openstreetmap.org/wiki/Cycle_Node_Network_Tagging">Cycle Node Network Tagging</a> in October last year.</p>
<blockquote>
<p>There is no need to add the junction nodes to this relation. They are part of the ways, so inherently already part of it. This allows for a more controlled way of downloading the hierarchy (collection/network/route).</p>
</blockquote>
</div>
<div id="comment-19244-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 20:12)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="19248"></span>
<div id="comment-19248" class="comment">
<div id="post-19248-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm confused, I'm not really getting the information I need from that page. Your quote hints at a good way to download the network but I haven't been able to find what that is... In fact, I fail to see what part of that page is different from what I'm attempting to do...</p>
</div>
<div id="comment-19248-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 20:52)</span> <span class="comment-user userinfo">Zoefschildpad</span>
</div>
</div>
<span id="19271"></span>
<div id="comment-19271" class="comment">
<div id="post-19271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The node as a relation member is only present in the network relation. The only other place where you will see the node is as a way node of one of the member ways of the three route relations ending at the node. See the query in my updated answer.</p>
</div>
<div id="comment-19271-info" class="comment-info">
<span class="comment-age">(22 Jan '13, 20:25)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-19240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19240-form-container" class="comment-form-container">
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

