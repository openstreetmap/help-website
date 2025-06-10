+++
type = "question"
title = "Administrative vs. Street names (and refs)"
description = '''I have an interesting situation: I&#x27;m currently adding lots of tracks and roads (which are used to access forests, meadows etc). Some of these tracks are part of normal hiking routes, therefore have ref=1, 1a, 16 etc. Then there are still houses alongside these roads, so I assume the name of the road...'''
date = "2010-11-21T00:19:00Z"
lastmod = "2010-11-21T11:54:00Z"
weight = 1570
keywords = [ "ref", "name" ]
aliases = [ "/questions/1570" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Administrative vs. Street names (and refs)](/questions/1570/administrative-vs-street-names-and-refs)

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
<span id="post-1570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1570-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an interesting situation: I'm currently adding lots of tracks and roads (which are used to access forests, meadows etc).</p>
<p>Some of these tracks are part of normal hiking routes, therefore have ref=1, 1a, 16 etc. Then there are still houses alongside these roads, so I assume the name of the road should be what the address indicates. But, the single roads themselves have names on their own.</p>
<p>An example: Way 81546521 is known to the administration as "Schuster am Stein". So, if there's road repair to do, then they say: "do this and that on the "Schuster am Stein" road!". But, houses on the road have the address "Prieler Weg No. xyz", as an entire area (consisting of more roads) make up for the same address. Whether this is practical or not is not the issue here, but since only a few houses are found alongside this road, it's probably easier not having as many different road names in the town as there are buildings... And, lastly, the road is also part of the hiking trail Nr. 3. It's clear, I tag the road ref=3, name=Prieler Weg, but where do I put the "Schuster am Stein"? Ref is already used, and I'm also a bit hesitant using it where there would be no clash with an existing ref number, as perhaps it would be rendered (as with other refs) as text in a long rounded box, cluttering the entire map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '10, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/720ecc66aa0d49f61a12c4d9e526e66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Roalter&#39;s gravatar image" />
<p><span>Alexander Ro...</span><br />
<span class="score" title="276 reputation points">276</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Roalter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1570" class="comments-container">
&#10;</div>
<div id="comment-tools-1570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1570-form-container" class="comment-form-container">
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

<span id="1571"></span>

<div id="answer-container-1571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1571-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand you correctly, the "Prieler Weg" is just a <em>postal</em> naming - people living in that road would say "I live in Schuster am Stein", not "I live in Prieler Weg".</p>
<p>If that is indeed the case, then you should really tag the road</p>
<pre><code>name=Schuster am Stein</code></pre>
<p>and then tag the houses with</p>
<pre><code>addr:housenumber=xyz
addr:street=Prieler Weg</code></pre>
<p>to record the postal address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '10, 08:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-1571" class="comments-container">
<span id="1572"></span>
<div id="comment-1572" class="comment">
<div id="post-1572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it's the way you understand. There's only one drawback (which brings us back to the rendering): On the map, the street is named according to the name tag, not the addr:street (which is quite obvious). On the other hand, on a printed out map (as with most city maps), I would search for the address by looking up the street to get the approximate location. If now the street name is nowhere to be found (only in the addr:street tags), it might be difficult finding the address.</p>
</div>
<div id="comment-1572-info" class="comment-info">
<span class="comment-age">(21 Nov '10, 11:54)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
</div>
<div id="comment-tools-1571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1571-form-container" class="comment-form-container">
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

