+++
type = "question"
title = "Unknown error when trying to filter nodes in Overpass Turbo using regular expression"
description = '''Using in Overpass Turbo, I am trying to filter nodes tagged with key place:PH and with values which are not any of the following: barangay, municipality, sitio, purok, or province. I tried this code below : [out:xml]/*fixed by auto repair*/[timeout:50]; // gather results (  node[&quot;place:PH&quot;!~&quot;(barang...'''
date = "2020-12-28T09:28:00Z"
lastmod = "2020-12-28T11:22:00Z"
weight = 78083
keywords = [ "regex", "filtering", "overpass-turbo", "tags", "error" ]
aliases = [ "/questions/78083" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown error when trying to filter nodes in Overpass Turbo using regular expression](/questions/78083/unknown-error-when-trying-to-filter-nodes-in-overpass-turbo-using-regular-expression)

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
<span id="post-78083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using in Overpass Turbo, I am trying to filter nodes tagged with key <code>place:PH</code> and with values which are <strong>not</strong> any of the following: <code>barangay</code>, <code>municipality</code>, <code>sitio</code>, <code>purok</code>, or <code>province</code>.</p>
<p>I tried this code below :</p>
<pre><code>[out:xml]/*fixed by auto repair*/[timeout:50];
// gather results
(
  node[&quot;place:PH&quot;!~&quot;(barangay|municipality|sitio|purok|province)&quot;]{{bbox}};
);
// print results
out meta;/*fixed by auto repair*/
&gt;;
out meta qt;/*fixed by auto repair*/</code></pre>
<p>but it gives the following unknown error:</p>
<pre><code>An error occured during the execution of the overpass query! This is what overpass API returned:
&#10;Error: line 4: parse error: &#39;;&#39; expected - &#39;17.731682803940448&#39; found.</code></pre>
<p>Can anybody please help on how to fix the query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '20, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78083" class="comments-container">
&#10;</div>
<div id="comment-tools-78083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78083-form-container" class="comment-form-container">
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

<span id="78085"></span>

<div id="answer-container-78085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your query is missing round brackets before and after {{bbox}}. The correct query is</p>
<pre><code>[out:xml]/*fixed by auto repair*/[timeout:50];
// gather results
(
  node[&quot;place:PH&quot;!~&quot;(barangay|municipality|sitio|purok|province)&quot;]({{bbox}});
);
// print results
out meta;/*fixed by auto repair*/
&gt;;
out meta qt;/*fixed by auto repair*/</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '20, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-78085" class="comments-container">
&#10;</div>
<div id="comment-tools-78085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78085-form-container" class="comment-form-container">
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

