+++
type = "question"
title = "Maperitive Rules not loading"
description = '''When I open rules in Maperitive. I keep getting an Error. Here&#x27;s the link to my Maperitive rules: Maperitive Rules This is the output I get  &amp;gt; use-ruleset location=&quot;C:&#92;Program Files&#92;Maperitive&#92;Rules&#92;Better mapnik.mrules&quot;  Rendering rules could not be parsed:  ERROR: Unexpected character &#x27;;&#x27; (0x3b...'''
date = "2014-02-21T11:49:00Z"
lastmod = "2014-02-24T14:26:00Z"
weight = 30871
keywords = [ "rules", "maperitive", "osm" ]
aliases = [ "/questions/30871" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive Rules not loading](/questions/30871/maperitive-rules-not-loading)

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
<span id="post-30871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I open rules in Maperitive. I keep getting an Error. Here's the link to my Maperitive rules: <a href="https://drive.google.com/file/d/0B3WmHpDwomtNc3l5WGdZc2hNcDg/edit?usp=sharing">Maperitive Rules</a></p>
<p>This is the output I get</p>
<pre><code>   &gt; use-ruleset location=&quot;C:\Program Files\Maperitive\Rules\Better mapnik.mrules&quot;
      Rendering rules could not be parsed:
      ERROR: Unexpected character &#39;;&#39; (0x3b) (line=904, col=7)
      ERROR: Unknown command &#39;10,-10&#39; (line=904, col=1)
   SCRIPT FAILED
   Script execution error (line 1): Rendering rules could not be parsed</code></pre>
<p>How do I fix this? I want to use this because the default rule set is missing objects.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '14, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/cd6f9338a5588f839cbaa01a3e21aad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deco2208&#39;s gravatar image" />
<p><span>deco2208</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deco2208 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30871" class="comments-container">
<span id="30876"></span>
<div id="comment-30876" class="comment">
<div id="post-30876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please show us your rules file at the corresponding lines (around 904).</p>
</div>
<div id="comment-30876-info" class="comment-info">
<span class="comment-age">(21 Feb '14, 13:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30871-form-container" class="comment-form-container">
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

<span id="30975"></span>

<div id="answer-container-30975" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30975-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an error on line 904 (exactly what the output says): you have some numbers wrapped to a line, which Maperitive cannot parse, obviously.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '14, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-30975" class="comments-container">
&#10;</div>
<div id="comment-tools-30975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30975-form-container" class="comment-form-container">
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

