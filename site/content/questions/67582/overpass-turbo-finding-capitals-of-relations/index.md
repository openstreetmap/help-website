+++
type = "question"
title = "Overpass turbo: Finding capitals of relations"
description = '''I&#x27;m looking for a way to grab the capital of a relation, for which I have the OSM ID. I can print out the relation like this: [out:json]; relation(8654); out body;  and I have the data (node with &quot;role&quot;: &quot;admin_centre&quot;), however I would then need to parse the JSON myself which is:  a waste of bandwi...'''
date = "2019-01-14T19:55:00Z"
lastmod = "2019-01-15T09:44:00Z"
weight = 67582
keywords = [ "admin_centre", "relations" ]
aliases = [ "/questions/67582" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass turbo: Finding capitals of relations](/questions/67582/overpass-turbo-finding-capitals-of-relations)

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
<span id="post-67582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67582-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a way to grab the capital of a relation, for which I have the OSM ID.</p>
<p>I can print out the relation like this:</p>
<pre><code>[out:json];
relation(8654);
out body;</code></pre>
<p>and I have the data (node with "role": "admin_centre"), however I would then need to parse the JSON myself which is:</p>
<ul>
<li>a waste of bandwidth for everyone involved.</li>
<li>needless processing on my side</li>
<li>I would then need to make another query to OSM to get data for the node</li>
</ul>
<p>What I need is the data found here <a href="https://www.openstreetmap.org/node/26761400">https://www.openstreetmap.org/node/26761400</a> , but in JSON format and through the API. I don't have the OSM ID of the node, only the relation.</p>
<p>So I would like to know if there is a way to get just the node data.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_centre" rel="tag" title="see questions tagged &#39;admin_centre&#39;">admin_centre</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '19, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fa48a42d552e7171c4ad4f5b8342a11c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ianare&#39;s gravatar image" />
<p><span>ianare</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ianare has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '19, 19:56</strong> </span></p>
</div>
</div>
<div id="comments-container-67582" class="comments-container">
&#10;</div>
<div id="comment-tools-67582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67582-form-container" class="comment-form-container">
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

<span id="67586"></span>

<div id="answer-container-67586" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67586-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ianare has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">recurse filter</a>:</p>
<pre><code>[out:json];
relation(8654);
node(r:&quot;admin_centre&quot;);
out body;</code></pre>
<p><a href="http://overpass-turbo.eu/s/FdV">Here's a demo.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '19, 01:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-67586" class="comments-container">
<span id="67590"></span>
<div id="comment-67590" class="comment">
<div id="post-67590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect, thank you! I had seen the recurse filter in the docs but did not understand it.</p>
</div>
<div id="comment-67590-info" class="comment-info">
<span class="comment-age">(15 Jan '19, 09:44)</span> <span class="comment-user userinfo">ianare</span>
</div>
</div>
</div>
<div id="comment-tools-67586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67586-form-container" class="comment-form-container">
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

