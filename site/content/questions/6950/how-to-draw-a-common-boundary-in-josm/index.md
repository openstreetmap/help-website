+++
type = "question"
title = "How to draw a common boundary in JOSM?"
description = '''I want to draw two adjacent areas that share a common boundary using JOSM, or more generally, an area that is divided into two or more sub-areas. How do I do this?'''
date = "2011-08-07T22:25:00Z"
lastmod = "2011-08-12T22:53:00Z"
weight = 6950
keywords = [ "josm", "boundary", "common", "shared" ]
aliases = [ "/questions/6950" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to draw a common boundary in JOSM?](/questions/6950/how-to-draw-a-common-boundary-in-josm)

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
<span id="post-6950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to draw two adjacent areas that share a common boundary using JOSM, or more generally, an area that is divided into two or more sub-areas. How do I do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-common" rel="tag" title="see questions tagged &#39;common&#39;">common</span> <span class="post-tag tag-link-shared" rel="tag" title="see questions tagged &#39;shared&#39;">shared</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '11, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/660363689cead9b16bfce059d49fe7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceperman&#39;s gravatar image" />
<p><span>ceperman</span><br />
<span class="score" title="291 reputation points">291</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceperman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6950" class="comments-container">
&#10;</div>
<div id="comment-tools-6950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6950-form-container" class="comment-form-container">
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

<span id="6951"></span>

<div id="answer-container-6951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6951-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Let's say you have two adjacent areas a bit like the geometry formed by the letters "CD".</p>
<p>You would create three ways; one for the "C", one for the "D"'s belly, and one for the line that separates them (let's call it "I" because it looks like one). These ways would go untagged, or maybe tagged <code>boundary=administrative</code> so that people know what they are. Then you would create two relations, one containing the "C" way and the "I" way, and one containing the "I" and the "D" way. The relations should be tagged <code>type=multipolygon</code>, <code>boundary=administrative</code>, <code>admin_level=x</code> (whatever level it is), and <code>name=y</code> (each with its own name).</p>
<p>Some people also use <code>type=boundary</code> but multipolygon is more commonly understood.</p>
<p>The above is the "proper" method that can be used for any number of adjacent areas - if you have a mesh of areas then your relations will often have more than two members. In its relation editor, JOSM provides a visual clue as to whether all the ways you have assembled in that relation really form a closed ring or not.</p>
<p>There is also a simpler method that you can use if the "I" way is rather short and has few nodes only. In that case, you can simply draw both areas as a closed way - two ways only, no relations - and have them share the nodes of the "I" way. This is perfectly ok for small stretches of coincidence. It avoids the relations which are difficult for many newcomers, but at the same time modifications to the shared "I" border will often be more difficult.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '11, 23:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6951" class="comments-container">
<span id="7010"></span>
<div id="comment-7010" class="comment">
<div id="post-7010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that. In my typical cases the areas are small and simple, so the second method would be OK. But how do I share the nodes - that's the bit I'm missing. Once the common nodes belong to one closed way, say D in your example, they aren't available to close the C way.</p>
</div>
<div id="comment-7010-info" class="comment-info">
<span class="comment-age">(10 Aug '11, 16:23)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
<span id="7013"></span>
<div id="comment-7013" class="comment">
<div id="post-7013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The two nodes of the I part are available to close the C way: simply use them to close the C way. Avoid pressing any of the modifiers key (CTRL, SHIFT, ALT) while clicking on these nodes (see JOSM Help, <a href="http://josm.openstreetmap.de/wiki/Help/Action/Draw).">http://josm.openstreetmap.de/wiki/Help/Action/Draw).</a></p>
<p>The simple method works very well to draw a pair of semi-detached houses: first draw the first house, then draw the second house using the two common nodes from the first.</p>
</div>
<div id="comment-7013-info" class="comment-info">
<span class="comment-age">(10 Aug '11, 21:08)</span> <span class="comment-user userinfo">mmehl</span>
</div>
</div>
<span id="7016"></span>
<div id="comment-7016" class="comment">
<div id="post-7016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In my case the I part is not a simple straight line, but a squiggly way with multiple nodes. When I try this, a segment is drawn between the two common end nodes, ignoring the way between them. It seems that what you're suggesting only works for common nodes that are adjacent. Or am I just being a newbie?</p>
</div>
<div id="comment-7016-info" class="comment-info">
<span class="comment-age">(11 Aug '11, 08:45)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
<span id="7057"></span>
<div id="comment-7057" class="comment">
<div id="post-7057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the "I" has more then two nodes, then you have to add every node to share these in the second way.</p>
<p>If the "I" has too many nodes, you may consider the approach with relations.</p>
</div>
<div id="comment-7057-info" class="comment-info">
<span class="comment-age">(12 Aug '11, 22:17)</span> <span class="comment-user userinfo">mmehl</span>
</div>
</div>
<span id="7058"></span>
<div id="comment-7058" class="comment">
<div id="post-7058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use the "Follow" feature in JOSM. ie draw the way, connecting to the first two shared nodes. Then press F for as many times as is needed. The way will continue along the way, sharing nodes. See <a href="http://josm.openstreetmap.de/wiki/Help/Action/FollowLine">http://josm.openstreetmap.de/wiki/Help/Action/FollowLine</a></p>
</div>
<div id="comment-7058-info" class="comment-info">
<span class="comment-age">(12 Aug '11, 22:53)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-6951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6951-form-container" class="comment-form-container">
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

