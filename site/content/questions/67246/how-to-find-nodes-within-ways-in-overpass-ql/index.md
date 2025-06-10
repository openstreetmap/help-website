+++
type = "question"
title = "How to find nodes within ways in Overpass QL?"
description = '''I have a query which returns a number of ways. I want to find nodes matching certain criteria which appear within those ways. Note that the nodes I&#x27;m interested in do not form part of the way itself, but do appear within the bounds of the way. Also, the ways do not all have corresponding areas, so u...'''
date = "2018-12-17T12:27:00Z"
lastmod = "2018-12-17T12:27:00Z"
weight = 67246
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/67246" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find nodes within ways in Overpass QL?](/questions/67246/how-to-find-nodes-within-ways-in-overpass-ql)

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
<span id="post-67246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67246-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a query which returns a number of <code>way</code>s. I want to find <code>node</code>s matching certain criteria which appear within those ways. Note that the nodes I'm interested in <em>do not</em> form part of the way itself, but do appear within the bounds of the way. Also, the ways do not all have corresponding areas, so using the area search doesn't work in all cases.</p>
<p>I've got a minimal example which finds way 95677318, and I want to be able to find node 1552949334:</p>
<pre><code>(
  way({{bbox}})[&quot;man_made&quot;=&quot;lighthouse&quot;];
)-&gt;.searchArea;
&#10;/*doesn&#39;t work:*/
/*node(area.searchArea)[&quot;seamark:name&quot;];*/
&#10;/*recur down and find node directly, just for the purpose of this question*/
(
  .searchArea;&gt;;
  node({{bbox}})[&quot;seamark:name&quot;];
);
out;</code></pre>
<p>(Try it on <a href="https://overpass-turbo.eu/s/EpV">https://overpass-turbo.eu/s/EpV</a>)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '18, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/be32719574763adc22bb5049970498d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tstibbs&#39;s gravatar image" />
<p><span>tstibbs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tstibbs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67246" class="comments-container">
&#10;</div>
<div id="comment-tools-67246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67246-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

