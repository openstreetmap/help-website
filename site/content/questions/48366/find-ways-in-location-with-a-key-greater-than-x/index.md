+++
type = "question"
title = "Find ways in location with a key greater than X"
description = '''In a city-sized area, I&#x27;m looking for buildings that have more levels than 12. I know that those are tagged with building:levels (untagged buildings are not interesting in this case). I have been trying to get them from Overpass Turbo, but AFAIK there&#x27;s no way to say &quot;find value &amp;gt; 12&quot;, and matchi...'''
date = "2016-02-26T10:18:00Z"
lastmod = "2022-01-14T08:37:00Z"
weight = 48366
keywords = [ "filter", "overpass-turbo" ]
aliases = [ "/questions/48366" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find ways in location with a key greater than X](/questions/48366/find-ways-in-location-with-a-key-greater-than-x)

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
<span id="post-48366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48366-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a city-sized area, I'm looking for buildings that have more levels than 12. I know that those are tagged with <code>building:levels</code> (untagged buildings are not interesting in this case). I have been trying to get them from Overpass Turbo, but AFAIK there's no way to say "find value &gt; 12", and matching way["building:levels"~"^[234][0-9]$"]; times out (and only matches 20-49 anyway).</p>
<p>Is this the right tool? If so, how should I do this? If not - should I perhaps get an OSM extract and process it as XML with some other tool?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '16, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-48366" class="comments-container">
<span id="48369"></span>
<div id="comment-48369" class="comment">
<div id="post-48369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a>: While fiddling with the OpT query, I have found a working solution - I had a typo in there :(</p>
</div>
<div id="comment-48369-info" class="comment-info">
<span class="comment-age">(26 Feb '16, 11:29)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="48371"></span>
<div id="comment-48371" class="comment">
<div id="post-48371-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>BTW: Here's a link to the respective feature request: <a href="https://github.com/drolbr/Overpass-API/issues/78">https://github.com/drolbr/Overpass-API/issues/78</a></p>
</div>
<div id="comment-48371-info" class="comment-info">
<span class="comment-age">(26 Feb '16, 11:36)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48366-form-container" class="comment-form-container">
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

<span id="48370"></span>

<div id="answer-container-48370" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48370-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have found a way to hack around this in Overpass Turbo. Apparently, it's not possible to directly compare numbers, but it's possible to use regex - match "100-499" or match "20-99" or match "13-19". It's still not foolproof (fortunately, this key is unitless), but works with buildings up to 499 floors:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // 100-499
  way[&quot;building:levels&quot;~&quot;^[1234][0-9]{2}$&quot;]({{bbox}});
  // 20-99
  way[&quot;building:levels&quot;~&quot;^[23456789][0-9]$&quot;]({{bbox}});
  // 13-19
  way[&quot;building:levels&quot;~&quot;^1[3-9]$&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>(Yes, I'm aware that with regex, I now have two problems ;))</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '16, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '16, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-48370" class="comments-container">
&#10;</div>
<div id="comment-tools-48370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48370-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83076"></span>

<div id="answer-container-83076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83076-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try</p>
<pre><code>way (if:number(t[&quot;building:levels&quot;])&gt;10)  ({{bbox}}); (._;&gt;;); out;</code></pre>
<p>Based on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Buildings_that_are_taller_than_they_are_wide">Overpass API/Overpass API by Example: Buildings that are taller than they are wide</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '22, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c7494ba96cbace6144068d12db80ebbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" />
<p><span>Marc</span><br />
<span class="score" title="11 reputation points">11</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83076" class="comments-container">
&#10;</div>
<div id="comment-tools-83076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83076-form-container" class="comment-form-container">
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

