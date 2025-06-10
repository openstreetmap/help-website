+++
type = "question"
title = "Overpass QL: Nodes and ways in area"
description = '''I want to get nodes and ways (amenity~fastfood|restaurant) for a specific area. I tried with a boundingbox, which works well, but when i change the query to use area, i only get the the first query results in the union (nodes). If i put the way-query first, i only get ways. The QL i have so far:  [o...'''
date = "2013-03-06T14:58:00Z"
lastmod = "2013-03-07T08:28:00Z"
weight = 20531
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/20531" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass QL: Nodes and ways in area](/questions/20531/overpass-ql-nodes-and-ways-in-area)

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
<span id="post-20531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20531-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get nodes and ways (amenity~fastfood|restaurant) for a specific area. I tried with a boundingbox, which works well, but when i change the query to use area, i only get the the first query results in the union (nodes). If i put the way-query first, i only get ways.</p>
<p>The QL i have so far:</p>
<pre><code>[out:json];
area
  [&quot;boundary&quot;=&quot;administrative&quot;]
  [&quot;name&quot;=&quot;Calw&quot;];
out body qt;
(
  node
    (area)
    [&quot;amenity&quot;~&quot;fast_food|restaurant&quot;];
  way
    (area)
    [&quot;amenity&quot;~&quot;fast_food|restaurant&quot;];
);
out body qt;
&gt;;
out skel qt;</code></pre>
link:<a href="http://goo.gl/ZcFj1">Link to overpass-turbo with query running</a>
<p>Any help to get the ways and nodes in one run?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '13, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9c75aa423b0ee7b79376646a662c0688?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dooley&#39;s gravatar image" />
<p><span>dooley</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dooley has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '16, 19:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-20531" class="comments-container">
&#10;</div>
<div id="comment-tools-20531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20531-form-container" class="comment-form-container">
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

<span id="20549"></span>

<div id="answer-container-20549" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20549-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dooley has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to store the query result in a dedicated variable and to use it from there:</p>
<pre><code>[out:json];
area
  [&quot;boundary&quot;=&quot;administrative&quot;]
  [&quot;name&quot;=&quot;Calw&quot;]-&gt;.a;          // Redirect result to &quot;.a&quot;
out body qt;
(
  node
    (area.a)                    // Use result from &quot;.a&quot;
    [&quot;amenity&quot;~&quot;fast_food|restaurant&quot;];
  way
    (area.a)                    // Use again result from &quot;.a&quot;
    [&quot;amenity&quot;~&quot;fast_food|restaurant&quot;];
);
out body qt;
&gt;;
out skel qt;</code></pre>
<p>Without the variable, the result of the area query is overwritten by the "node(area)..." statement. Thus the next statement doesn't find any area to recurse from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '13, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-20549" class="comments-container">
<span id="20551"></span>
<div id="comment-20551" class="comment">
<div id="post-20551-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, works fine :-)</p>
</div>
<div id="comment-20551-info" class="comment-info">
<span class="comment-age">(07 Mar '13, 08:28)</span> <span class="comment-user userinfo">dooley</span>
</div>
</div>
</div>
<div id="comment-tools-20549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20549-form-container" class="comment-form-container">
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

