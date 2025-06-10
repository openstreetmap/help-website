+++
type = "question"
title = "Overpass: polygon query"
description = '''I want to create a polygon-query with the points of the following query: &amp;lt;osm-script&amp;gt;  &amp;lt;union into=&quot;_&quot;&amp;gt;  &amp;lt;id-query into=&quot;_&quot; ref=&quot;134816256&quot; type=&quot;way&quot;/&amp;gt;  &amp;lt;id-query into=&quot;_&quot; ref=&quot;95661967&quot; type=&quot;way&quot;/&amp;gt;  &amp;lt;id-query into=&quot;_&quot; ref=&quot;201062997&quot; type=&quot;way&quot;/&amp;gt;  &amp;lt;id-query into=&quot;...'''
date = "2013-02-13T14:39:00Z"
lastmod = "2013-02-14T12:51:00Z"
weight = 19914
keywords = [ "overpass", "polygon", "query" ]
aliases = [ "/questions/19914" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: polygon query](/questions/19914/overpass-polygon-query)

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
<span id="post-19914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19914-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a polygon-query with the points of the following query:</p>
<pre><code>&lt;osm-script&gt;
  &lt;union into=&quot;_&quot;&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;134816256&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;95661967&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;201062997&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;95675717&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;96007270&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;96007267&quot; type=&quot;way&quot;/&gt;
    &lt;id-query into=&quot;_&quot; ref=&quot;95663153&quot; type=&quot;way&quot;/&gt;
  &lt;/union&gt;
  &lt;recurse from=&quot;_&quot; into=&quot;_&quot; type=&quot;down&quot;/&gt;
  &lt;print from=&quot;_&quot; limit=&quot;&quot; mode=&quot;body&quot; order=&quot;id&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>Can I directly insert the output-nodes of the first query into a polygon query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '13, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/2c52393df51ceb5327c1e19e3b0efbfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mattes_tili&#39;s gravatar image" />
<p><span>Mattes_tili</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mattes_tili has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '13, 15:36</strong> </span></p>
</div>
</div>
<div id="comments-container-19914" class="comments-container">
&#10;</div>
<div id="comment-tools-19914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19914-form-container" class="comment-form-container">
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

<span id="19927"></span>

<div id="answer-container-19927" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19927-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mattes_tili has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>EDIT: This is possible since a couple of years, see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_polygon_.28poly.29">here</a>.</p>
<hr />
<p>No, I'm sorry this isn' possible so far. You would have to receive the coordinates and then form a polygon query out of them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '13, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '19, 12:45</strong> </span></p>
</div>
</div>
<div id="comments-container-19927" class="comments-container">
&#10;</div>
<div id="comment-tools-19927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19927-form-container" class="comment-form-container">
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

