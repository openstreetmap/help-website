+++
type = "question"
title = "route and distance cache"
description = '''I want to calculate all the possible distances between all the large towns and cities in the UK (about 2,500 places - my matrix will be about 6.3 million items) How should I go about this? I am on a windows machine. All distances can be approximated to the nearest mile. Why: My hosting site has gigs...'''
date = "2011-02-24T13:56:00Z"
lastmod = "2011-02-28T12:59:00Z"
weight = 3347
keywords = [ "route" ]
aliases = [ "/questions/3347" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [route and distance cache](/questions/3347/route-and-distance-cache)

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
<span id="post-3347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to calculate all the possible distances between all the large towns and cities in the UK (about 2,500 places - my matrix will be about 6.3 million items)</p>
<p>How should I go about this? I am on a windows machine. All distances can be approximated to the nearest mile.</p>
<p>Why: My hosting site has gigs of disc space but won't let me run a route finder.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '11, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/5dd08c07bd022f04e331f5dbfea5b159?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monkeboy&#39;s gravatar image" />
<p><span>monkeboy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monkeboy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3347" class="comments-container">
<span id="3373"></span>
<div id="comment-3373" class="comment">
<div id="post-3373-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>could you be a little more specific about "My hosting site [...] won't let me run a route finder"? what exactly don't they allow, and what do they? do they let you run a postgis database? sqlite/spatialite? especially the latter could be an alternative to having to precompute all 6.3 million combinations.</p>
</div>
<div id="comment-3373-info" class="comment-info">
<span class="comment-age">(25 Feb '11, 12:27)</span> <span class="comment-user userinfo">axk</span>
</div>
</div>
</div>
<div id="comment-tools-3347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3347-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="3433"></span>

<div id="answer-container-3433" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3433-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please email me at <a href="http://mailto:nroets@gmail.com"></a><a href="mailto:nroets@gmail.com"></a><a href="mailto:nroets@gmail.com">nroets@gmail.com</a>. The <a href="https://wiki.openstreetmap.org/wiki/Osm.org_Routing_Demo"></a><a href="http://Osm.org"></a><a href="http://Osm.org">Osm.org</a> Routing Demo has lots of spare computing power and I think it will have the answer in a few weeks.</p>
<p>Also note that the plain Dijkstra routing algorithm can find the shortest route from one point to many other points at the same cost of finding the route between that point and the farthest point. Running Dijkstra 2500 times on the UK network should not take more than 1 hour on a mere netbook.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '11, 21:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '11, 21:54</strong> </span></p>
</div>
</div>
<div id="comments-container-3433" class="comments-container">
<span id="3436"></span>
<div id="comment-3436" class="comment">
<div id="post-3436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which software would you use for that? I tested gosmore on a pak file covering Germany on an Atom D510 @ 1.66 Ghz with 2 GB of Ram available.</p>
</div>
<div id="comment-3436-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 08:43)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="3437"></span>
<div id="comment-3437" class="comment">
<div id="post-3437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The routing server takes 2.24 CPU seconds and uses 1.8GB RAM to calculate the 1400km route route across the UK. <a href="http://goo.gl/Shc8f">http://goo.gl/Shc8f</a> It will certainly run a little bit faster and use less memory using a UK extract. So perhaps 2 or 3 hours on a netbook is more accurate, but certainly not years.</p>
<p>Gosmore does not support point to multipoint. Perhaps other routers do.</p>
</div>
<div id="comment-3437-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 09:13)</span> <span class="comment-user userinfo">Nic Roets</span>
</div>
</div>
<span id="3439"></span>
<div id="comment-3439" class="comment">
<div id="post-3439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's why I asked which software you'd use for point to multipoint.</p>
</div>
<div id="comment-3439-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 11:06)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-3433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3433-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3363"></span>

<div id="answer-container-3363" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3363-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is a cross country route might very well take a minute or more to generate. So for 6.3 million entries your are looking at several CPU <strong>years</strong> to generate all routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '11, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-3363" class="comments-container">
<span id="3364"></span>
<div id="comment-3364" class="comment">
<div id="post-3364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So how do other sites do this? They must cache the results to some degree... do they just cache the M and A roads? Or if they are doing it in real time, how?</p>
</div>
<div id="comment-3364-info" class="comment-info">
<span class="comment-age">(24 Feb '11, 23:33)</span> <span class="comment-user userinfo">monkeboy</span>
</div>
</div>
<span id="3368"></span>
<div id="comment-3368" class="comment">
<div id="post-3368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically they just generate the route on the fly. Main routes will generate in a few seconds and users wont mind to wait for that. Long routes across the whole country take a but longer but users will in general understand if they feel that it is a long trip. But even at a second each 6.3 million routes take 10 weeks to generate.</p>
<p>Of course the site will cache the generated routes for some time, but cache hit rate will be rather low as most routing services offer more then 2500 places to choose from and the number of potential routes simply explodes.</p>
</div>
<div id="comment-3368-info" class="comment-info">
<span class="comment-age">(25 Feb '11, 06:16)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-3363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3363-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3443"></span>

<div id="answer-container-3443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Look at the <a href="https://secure.wikimedia.org/wikipedia/en/wiki/Floyd-Warshall_algorithm">Floyd-Warshall algorithm</a> for finding the shortest path betwean all nodes in a graph in O(n^3) time. I am not sure what performence you might get out of the implementation and how well it will work on the OSM data but it is worth a shot. You might want to filter all non-routable elements and simplefy the ways (keeping the distance) to minimize the cost.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '11, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-3443" class="comments-container">
&#10;</div>
<div id="comment-tools-3443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3443-form-container" class="comment-form-container">
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

