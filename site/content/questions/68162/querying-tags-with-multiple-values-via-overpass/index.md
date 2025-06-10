+++
type = "question"
title = "Querying tags with multiple values via Overpass"
description = '''This example Overpass query for node[&quot;cuisine&quot;=&quot;coffee_shop&quot;] will not return nodes tagged &quot;cuisine&quot;=&quot;coffee_shop;sandwiches&quot;, i.e. with multiple values.  Shouldn&#x27;t it? Any workarounds? '''
date = "2019-02-26T17:18:00Z"
lastmod = "2019-02-26T19:32:00Z"
weight = 68162
keywords = [ "overpass" ]
aliases = [ "/questions/68162" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Querying tags with multiple values via Overpass](/questions/68162/querying-tags-with-multiple-values-via-overpass)

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
<span id="post-68162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68162-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This example <a href="https://overpass-turbo.eu/s/GtP">Overpass query</a> for <code>node["cuisine"="coffee_shop"]</code> will <strong>not</strong> return nodes tagged <code>"cuisine"="coffee_shop;sandwiches"</code>, i.e. with <a href="https://wiki.openstreetmap.org/wiki/Multiple_values">multiple values</a>.</p>
<ol>
<li>Shouldn't it?</li>
<li>Any workarounds?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '19, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f9fe45b76971785fd9287f048e9d3ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robinmetral&#39;s gravatar image" />
<p><span>robinmetral</span><br />
<span class="score" title="186 reputation points">186</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robinmetral has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68162" class="comments-container">
&#10;</div>
<div id="comment-tools-68162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68162-form-container" class="comment-form-container">
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

<span id="68163"></span>

<div id="answer-container-68163" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68163-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="robinmetral has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use a regular expression</p>
<pre><code>node[&quot;cuisine&quot;~&quot;coffee_shop&quot;]</code></pre>
<p>I would also suggest looking for ways (and relations)</p>
<pre><code>nwr[&quot;cuisine&quot;~&quot;coffee_shop&quot;]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '19, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
</div>
<div id="comments-container-68163" class="comments-container">
<span id="68164"></span>
<div id="comment-68164" class="comment">
<div id="post-68164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Amazing <a href="https://help.openstreetmap.org/users/9571/andrewblack">@andrewblack</a>, thanks! I didn't know of the <code>nwr</code> shortcut either, it's saving my query two lines 👍</p>
</div>
<div id="comment-68164-info" class="comment-info">
<span class="comment-age">(26 Feb '19, 19:16)</span> <span class="comment-user userinfo">robinmetral</span>
</div>
</div>
<span id="68166"></span>
<div id="comment-68166" class="comment">
<div id="post-68166-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>nwr is fairly new. It makes it easier/safer to edit. How many times have I edited node and not way.</p>
</div>
<div id="comment-68166-info" class="comment-info">
<span class="comment-age">(26 Feb '19, 19:20)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
<span id="68167"></span>
<div id="comment-68167" class="comment">
<div id="post-68167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FYI there are 41732 <code>coffee_shop</code>s in the world. Next step is dealing with this kind of data</p>
</div>
<div id="comment-68167-info" class="comment-info">
<span class="comment-age">(26 Feb '19, 19:32)</span> <span class="comment-user userinfo">robinmetral</span>
</div>
</div>
</div>
<div id="comment-tools-68163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68163-form-container" class="comment-form-container">
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

