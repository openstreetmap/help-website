+++
type = "question"
title = "Overpass query OR"
description = '''How can i express an logical OR in a query? For example if i would like to search node[&quot;amenity&quot;~&quot;courthouse|prison&quot; OR &quot;office&quot;=&quot;layer&quot;]'''
date = "2015-06-01T09:07:00Z"
lastmod = "2015-06-01T15:08:00Z"
weight = 43345
keywords = [ "overpass" ]
aliases = [ "/questions/43345" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query OR](/questions/43345/overpass-query-or)

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
<span id="post-43345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43345-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can i express an logical OR in a query? For example if i would like to search <code>node["amenity"~"courthouse|prison" OR "office"="layer"]</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '15, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/93f2ad2ef27d526cc19669a230bffc54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hwoehrle&#39;s gravatar image" />
<p><span>hwoehrle</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hwoehrle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43345" class="comments-container">
&#10;</div>
<div id="comment-tools-43345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43345-form-container" class="comment-form-container">
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

<span id="43352"></span>

<div id="answer-container-43352" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43352-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hwoehrle has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API#Union">Union query</a>:</p>
<pre><code>(node[&quot;amenity&quot;~&quot;courthouse|prison&quot;];
node[&quot;office&quot;=&quot;layer&quot;];);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '15, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '15, 19:56</strong> </span></p>
</div>
</div>
<div id="comments-container-43352" class="comments-container">
&#10;</div>
<div id="comment-tools-43352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43352-form-container" class="comment-form-container">
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

