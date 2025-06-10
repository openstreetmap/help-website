+++
type = "question"
title = "Overpass: check double node elements nearby"
description = '''For example trees on nodes natural=tree. Most trees have a distance to the other tree. They a planted line or random but mostly with a space between them. If I want to see only the trees that are close by, say less then 5 meter. [out:json];  (  node[&quot;natural&quot;=&quot;tree&quot;]({{bbox}}); )-&amp;gt;.a;  (  node(ar...'''
date = "2018-09-05T00:53:00Z"
lastmod = "2018-09-05T15:18:00Z"
weight = 65745
keywords = [ "overpass", "check", "distance" ]
aliases = [ "/questions/65745" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: check double node elements nearby](/questions/65745/overpass-check-double-node-elements-nearby)

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
<span id="post-65745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65745-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example trees on nodes natural=tree. Most trees have a distance to the other tree. They a planted line or random but mostly with a space between them. If I want to see only the trees that are close by, say less then 5 meter.</p>
<pre><code>[out:json];
&#10;(
  node[&quot;natural&quot;=&quot;tree&quot;]({{bbox}});
)-&gt;.a;
&#10;(
  node(around.a:5)[&quot;natural&quot;=&quot;tree&quot;];
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>This give all trees even with around.a:0</p>
<p>Of course the node natural=tree is the base, the base is always a distance of 0m. Only to a other node should be calculated.</p>
<p>How to fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '18, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '18, 15:16</strong> </span></p>
</div>
</div>
<div id="comments-container-65745" class="comments-container">
&#10;</div>
<div id="comment-tools-65745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65745-form-container" class="comment-form-container">
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

<span id="65759"></span>

<div id="answer-container-65759" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65759-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to <a href="http://overpass-turbo.eu/s/BEK">evaluate the trees one at a time</a> and subtract the base tree from the <code>around</code> result:</p>
<pre><code>[out:json];
(
  node[&quot;natural&quot;=&quot;tree&quot;]({{bbox}});
)-&gt;.a;
foreach.a-&gt;.tree(
  node(around.tree:10)[&quot;natural&quot;=&quot;tree&quot;];
  (._; - .tree;) -&gt; .others;
  (.collect; .others;) -&gt;.collect;
);
.collect out;</code></pre>
<p>(setting <code>around.tree</code> to 5 returns 0 results at the location there)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '18, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65759" class="comments-container">
<span id="65760"></span>
<div id="comment-65760" class="comment">
<div id="post-65760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it works. A little slow, when I take a bigger area or a adm_level.</p>
</div>
<div id="comment-65760-info" class="comment-info">
<span class="comment-age">(05 Sep '18, 15:18)</span> <span class="comment-user userinfo">Allroads</span>
</div>
</div>
</div>
<div id="comment-tools-65759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65759-form-container" class="comment-form-container">
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

