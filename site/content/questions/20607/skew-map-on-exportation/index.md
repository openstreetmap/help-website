+++
type = "question"
title = "skew map on exportation"
description = '''Hi!! I have GostTown a 3ds Max plugin that can use OSM to build towns. But the problem is that the maps looks skew or compressed more you get away the 0:0 coordinate. Can you explain why?'''
date = "2013-03-10T10:23:00Z"
lastmod = "2013-03-10T17:01:00Z"
weight = 20607
keywords = [ "ghosttown", "skew", "gt", "compensation" ]
aliases = [ "/questions/20607" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [skew map on exportation](/questions/20607/skew-map-on-exportation)

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
<span id="post-20607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20607-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!! I have GostTown a 3ds Max plugin that can use OSM to build towns.</p>
<p>But the problem is that the maps looks skew or compressed more you get away the 0:0 coordinate.</p>
<p>Can you explain why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ghosttown" rel="tag" title="see questions tagged &#39;ghosttown&#39;">ghosttown</span> <span class="post-tag tag-link-skew" rel="tag" title="see questions tagged &#39;skew&#39;">skew</span> <span class="post-tag tag-link-gt" rel="tag" title="see questions tagged &#39;gt&#39;">gt</span> <span class="post-tag tag-link-compensation" rel="tag" title="see questions tagged &#39;compensation&#39;">compensation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '13, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/4c474b11f057f4ad9064aa42ac464c11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ornix24&#39;s gravatar image" />
<p><span>Ornix24</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ornix24 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20607" class="comments-container">
&#10;</div>
<div id="comment-tools-20607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20607-form-container" class="comment-form-container">
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

<span id="20612"></span>

<div id="answer-container-20612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20612-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds like it's a <a href="http://en.wikipedia.org/wiki/Map_projection">projection</a> issue.</p>
<p>Map co-ordinates are usually measured in 'degrees' of latitude (y / vertical) and longitude (x / horizontal). All of OpenStreetMap's data is stored in co-ordinates like this. Have a look at a spherical globe to see how big a degree is.</p>
<p>If you simply draw your map such that each degree is represented by a constant distance - say, 1cm on the map for 1 degree of the world - then the map will end up squished in exactly the way you describe.</p>
<p>A 'projection' determines how much space on your screen/print-out each degree takes up. To avoid this squishing effect, a simple projection - such as the one used on most mapping sites, technically known as 'Spherical Mercator' (or 'Web Mercator') - gives more space for each degree of latitude (y) as you get further away from the equator. (In this projection, each degree of longitude takes up the same space.)</p>
<p>You therefore need to tell Ghost Town to use a different projection. You'll need to ask on the forums for that product how to do that.</p>
<p>(For a more light-hearted look at projections, see this <a href="http://xkcd.com/977/">xkcd cartoon</a>.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '13, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Mar '13, 15:58</strong> </span></p>
</div>
</div>
<div id="comments-container-20612" class="comments-container">
<span id="20614"></span>
<div id="comment-20614" class="comment">
<div id="post-20614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great !</p>
<p>Thank you For your quick answer (and the terribly funny cartoon) !</p>
<p>I will give it to KilaD, the amazing guy who created this very useful plugin. I hope it can help...</p>
</div>
<div id="comment-20614-info" class="comment-info">
<span class="comment-age">(10 Mar '13, 17:01)</span> <span class="comment-user userinfo">Ornix24</span>
</div>
</div>
</div>
<div id="comment-tools-20612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20612-form-container" class="comment-form-container">
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

