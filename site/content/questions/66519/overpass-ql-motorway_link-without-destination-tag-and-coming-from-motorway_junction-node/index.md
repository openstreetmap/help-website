+++
type = "question"
title = "Overpass QL: motorway_link without destination tag and coming from motorway_junction node"
description = '''Hi, I&#x27;m trying to find the motorway_link ways coming from a motorway_junction node (and so exiting a motorway) and which don&#x27;t have a destination=* set. Here&#x27;s an example of the current query where it shouldn&#x27;t return anything: http://overpass-turbo.eu/s/Dar And here it should return only two motorw...'''
date = "2018-10-28T11:00:00Z"
lastmod = "2018-10-28T11:30:00Z"
weight = 66519
keywords = [ "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/66519" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass QL: motorway_link without destination tag and coming from motorway_junction node](/questions/66519/overpass-ql-motorway_link-without-destination-tag-and-coming-from-motorway_junction-node)

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
<span id="post-66519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to find the <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link"><code>motorway_link</code></a> ways coming from a <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_junction"><code>motorway_junction</code></a> node (and so exiting a motorway) and which don't have a <a href="https://wiki.openstreetmap.org/wiki/Key:destination">destination=*</a> set.</p>
<p>Here's an example of the current query where it shouldn't return anything:</p>
<p><a href="http://overpass-turbo.eu/s/Dar">http://overpass-turbo.eu/s/Dar</a></p>
<p>And here it should return only two <code>motorway_junction</code> ways:</p>
<p><a href="http://overpass-turbo.eu/s/Dat">http://overpass-turbo.eu/s/Dat</a></p>
<p>Thanks in advance for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '18, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e2b1857c1d017a9936d5e48d3621884e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20RedBurn&#39;s gravatar image" />
<p><span>The RedBurn</span><br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The RedBurn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '18, 11:04</strong> </span></p>
</div>
</div>
<div id="comments-container-66519" class="comments-container">
&#10;</div>
<div id="comment-tools-66519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66519-form-container" class="comment-form-container">
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

<span id="66520"></span>

<div id="answer-container-66520" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66520-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="The RedBurn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">node-&gt;way recurse filter</a> does exactly what you want:</p>
<pre><code>node[highway=motorway_junction]({{bbox}});
way(bn)[&quot;highway&quot;=&quot;motorway_link&quot;][!&quot;destination&quot;];
out body;
&gt;;
out skel qt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/DaA">http://overpass-turbo.eu/s/DaA</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '18, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-66520" class="comments-container">
<span id="66521"></span>
<div id="comment-66521" class="comment">
<div id="post-66521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow, thanks that's great (and that was fast)! And thanks for the link!</p>
</div>
<div id="comment-66521-info" class="comment-info">
<span class="comment-age">(28 Oct '18, 11:30)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
</div>
<div id="comment-tools-66520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66520-form-container" class="comment-form-container">
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

