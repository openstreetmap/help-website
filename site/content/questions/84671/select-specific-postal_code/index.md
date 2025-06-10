+++
type = "question"
title = "Select specific postal_code"
description = '''So the &quot;ask first, the sign up&quot; did not work for me. The wiki for boundary:postal_code links to overpass turbo with the following query: /* This query looks for nodes, ways and relations  with the given key/value combination. Choose your region and hit the Run button above! */ [out:json][timeout:25]...'''
date = "2022-06-02T09:36:00Z"
lastmod = "2022-06-02T13:53:00Z"
weight = 84671
keywords = [ "filter", "overpass", "postal_code", "syntax" ]
aliases = [ "/questions/84671" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Select specific postal_code](/questions/84671/select-specific-postal_code)

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
<span id="post-84671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So the "ask first, the sign up" did not work for me.</p>
<p>The wiki for boundary:postal_code links to overpass turbo with the following query:</p>
<pre><code>/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “boundary=postal_code”
  node[&quot;boundary&quot;=&quot;postal_code&quot;]({{bbox}});
  way[&quot;boundary&quot;=&quot;postal_code&quot;]({{bbox}});
  relation[&quot;boundary&quot;=&quot;postal_code&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>It shows all ZIP code boundaries visible on the map How can I filter for one specific code by adding postal_code=12345?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span> <span class="post-tag tag-link-syntax" rel="tag" title="see questions tagged &#39;syntax&#39;">syntax</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '22, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d6c69bd5322e65ac515b2f430c35f0f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ohcomeon&#39;s gravatar image" />
<p><span>ohcomeon</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ohcomeon has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-84671" class="comments-container">
&#10;</div>
<div id="comment-tools-84671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84671-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="84673"></span>

<div id="answer-container-84673" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84673-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never mind, I tried the Wizard with "postal_code"=12345 and that generated pretty much the above code except for "postal_code"="12345" instead of "boundary"="postal_code"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '22, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d6c69bd5322e65ac515b2f430c35f0f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ohcomeon&#39;s gravatar image" />
<p><span>ohcomeon</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ohcomeon has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-84673" class="comments-container">
&#10;</div>
<div id="comment-tools-84673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84673-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84678"></span>

<div id="answer-container-84678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://overpass-turbo.eu/s/1iXL">https://overpass-turbo.eu/s/1iXL</a></p>
<pre><code>rel[boundary=postal_code][postal_code=04030]({{bbox}});
out body;
&gt;;
out skel qt;</code></pre>
<p>Only relations need to be searched.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '22, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-84678" class="comments-container">
&#10;</div>
<div id="comment-tools-84678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84678-form-container" class="comment-form-container">
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

