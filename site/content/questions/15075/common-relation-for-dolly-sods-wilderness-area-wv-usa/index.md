+++
type = "question"
title = "Common Relation for Dolly Sods Wilderness Area, WV, USA"
description = '''I have entered most of the hiking trail in the Dolly Sods Wilderness Area, URL=http://osm.org/go/ZT~CCig and I would like to group the trails and the wilderness area boundary with a common relation, similar to the way segments of the Appalachian Trail are grouped under state wide routes. I am not su...'''
date = "2012-08-14T15:19:00Z"
lastmod = "2012-08-14T16:06:00Z"
weight = 15075
keywords = [ "nature-preserve", "relation", "hiking" ]
aliases = [ "/questions/15075" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Common Relation for Dolly Sods Wilderness Area, WV, USA](/questions/15075/common-relation-for-dolly-sods-wilderness-area-wv-usa)

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
<span id="post-15075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15075-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have entered most of the hiking trail in the Dolly Sods Wilderness Area, URL=<a href="http://osm.org/go/ZT~CCig">http://osm.org/go/ZT~CCig</a> and I would like to group the trails and the wilderness area boundary with a common relation, similar to the way segments of the Appalachian Trail are grouped under state wide routes. I am not sure that the regional route designation is appropriate because the trail form a network and not a long route.</p>
<p>Before I create a new relation is there a means to search for existing relations in an area?</p>
<p>Are there standards for relations that group elements of a nature preserve?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nature-preserve" rel="tag" title="see questions tagged &#39;nature-preserve&#39;">nature-preserve</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '12, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/31393c8dfc76d3e3c585227cfef175c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johntrudy&#39;s gravatar image" />
<p><span>johntrudy</span><br />
<span class="score" title="110 reputation points">110</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johntrudy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15075" class="comments-container">
&#10;</div>
<div id="comment-tools-15075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15075-form-container" class="comment-form-container">
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

<span id="15077"></span>

<div id="answer-container-15077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15077-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First,</p>
<pre><code>http://overpass-api.de/api/interpreter?data=(rel(38.95,-79.4,39.1,-79.3);&lt;&lt;;);out;</code></pre>
<p>gives you all relations in this area. These are only county boundaries, so you need to make your own relation.</p>
<p>The next thing is think whether it is a geographical unit or not. If it is, it can be named. As it is a network, the relation should get [type=network] and [network="some name"]. But in general I think, it is just fine to leave it as ways - because they are grouped by the mere fact that they are in this area and don't need a relation for that purpose.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-15077" class="comments-container">
<span id="15078"></span>
<div id="comment-15078" class="comment">
<div id="post-15078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the link to overpass-api.de. That answers the question of searches.</p>
</div>
<div id="comment-15078-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 16:06)</span> <span class="comment-user userinfo">johntrudy</span>
</div>
</div>
</div>
<div id="comment-tools-15077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15077-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15076"></span>

<div id="answer-container-15076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15076-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Like you stated use the Apalachian trail tags methode. The regional trails can be joined by using multipolygones. By selecting the right numbers thy become connected. Search for similar situations in other national parks with hiking facilyties, like Yellowstone Keep mapping, Hendrik</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-15076" class="comments-container">
&#10;</div>
<div id="comment-tools-15076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15076-form-container" class="comment-form-container">
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

