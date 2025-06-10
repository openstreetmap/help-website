+++
type = "question"
title = "Finding Areas within Areas with Overpass QL"
description = '''Hi All, I&#x27;m having a bit of trouble running queries for areas that are within other areas. For example: area  [name=&quot;United States of America&quot;]  [border_type=national] -&amp;gt; .usa; (  area  (area.usa)  [admin_level=4] ); out 100;  I would expect this to return a list of states in the US. However, wha...'''
date = "2014-03-07T04:15:00Z"
lastmod = "2014-03-07T10:03:00Z"
weight = 31376
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/31376" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Finding Areas within Areas with Overpass QL](/questions/31376/finding-areas-within-areas-with-overpass-ql)

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
<span id="post-31376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31376-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I'm having a bit of trouble running queries for areas that are within other areas. For example:</p>
<pre><code>area
  [name=&quot;United States of America&quot;]
  [border_type=national] -&gt; .usa;
(
  area
    (area.usa)
    [admin_level=4]
);
out 100;</code></pre>
<p>I would expect this to return a list of states in the US. However, what I actually get is a random hodgepodge of areas with admin_level=4, not just those in the US. Am I misunderstanding the area syntax?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '14, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/15b0a2369fa306e457e13ebb40f81f97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sib&#39;s gravatar image" />
<p><span>sib</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sib has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31376" class="comments-container">
&#10;</div>
<div id="comment-tools-31376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31376-form-container" class="comment-form-container">
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

<span id="31380"></span>

<div id="answer-container-31380" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31380-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sib has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two different problems entangled:</p>
<p>Overpass API doesn't support to query for areas in areas. It is just not implemented, but you could get a similar result with the query</p>
<pre><code>[timeout:3600];
area
  [name=&quot;United States of America&quot;]
  [border_type=national] -&gt; .usa;
(
  rel
    (area.usa)
    [admin_level=4];
);
out 100;</code></pre>
<p>It is unfortunately really slow.</p>
<p>Second, there are a lot of relations (and thus areas) tagged with "admin_level=4" although they are not states. One example is relation 80297 which is a park somewhere in Ohio.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '14, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-31380" class="comments-container">
&#10;</div>
<div id="comment-tools-31380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31380-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31379"></span>

<div id="answer-container-31379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31379-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, it is not yet possible to search for areas inside other areas. See <a href="https://github.com/drolbr/Overpass-API/issues/45">this ticket</a> on github. :/</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '14, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-31379" class="comments-container">
&#10;</div>
<div id="comment-tools-31379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31379-form-container" class="comment-form-container">
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

