+++
type = "question"
title = "Overpass : id-query with  has-kv ?"
description = '''Is it possible to combine an id-querywith some sort of has-kv ?  &amp;lt; osm-script&amp;gt;  &amp;lt; id-query ref=&quot;3300434&quot; type=&quot;relation&quot; /&amp;gt;  &amp;lt; recurse type=&quot;relation-relation&quot; /&amp;gt;   &amp;lt; recurse type=&quot;relation-relation&quot; /&amp;gt;   &amp;lt; recurse type=&quot;relation-node&quot; /&amp;gt;  &amp;lt; print/&amp;gt; &amp;lt; /osm-scri...'''
date = "2014-02-12T11:49:00Z"
lastmod = "2014-02-12T12:07:00Z"
weight = 30678
keywords = [ "overpass" ]
aliases = [ "/questions/30678" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass : id-query with has-kv ?](/questions/30678/overpass-id-query-with-has-kv)

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
<span id="post-30678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to combine an <code>id-query</code>with some sort of <code>has-kv</code> ?</p>
<pre><code>&lt; osm-script&gt;
   &lt; id-query ref=&quot;3300434&quot; type=&quot;relation&quot; /&gt;
   &lt; recurse type=&quot;relation-relation&quot; /&gt;  
   &lt; recurse type=&quot;relation-relation&quot; /&gt;  
   &lt; recurse type=&quot;relation-node&quot; /&gt;  
&lt; print/&gt;
&lt; /osm-script&gt;</code></pre>
<p>I have this code which list each nodes of a transport network. I'd like to get only the ones with <code>&lt; tag k="public_transport" v="stop_position"/&gt;</code> and not the ones with <code>&lt; tag k="public_transport" v="platform"/&gt;</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '14, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30678" class="comments-container">
&#10;</div>
<div id="comment-tools-30678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30678-form-container" class="comment-form-container">
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

<span id="30679"></span>

<div id="answer-container-30679" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30679-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kyro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can wrap a <em>clause</em> with a <code>&lt;query&gt;</code>-tag to do further filtering:</p>
<pre><code>…
&lt;query type=&quot;node&quot;&gt;
  &lt;recurse type=&quot;relation-node&quot; /&gt;
  &lt;has-kv k=&quot;public_transport&quot; v=&quot;platform&quot; /&gt;
&lt;/query&gt;
…</code></pre>
<p><a href="http://overpass-turbo.eu/s/2uI">http://overpass-turbo.eu/s/2uI</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 12:05</strong> </span></p>
</div>
</div>
<div id="comments-container-30679" class="comments-container">
<span id="30680"></span>
<div id="comment-30680" class="comment">
<div id="post-30680-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's it, thanks !</p>
</div>
<div id="comment-30680-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 12:07)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
</div>
<div id="comment-tools-30679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30679-form-container" class="comment-form-container">
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

