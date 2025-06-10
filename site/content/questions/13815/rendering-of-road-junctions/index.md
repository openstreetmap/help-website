+++
type = "question"
title = "Rendering of road junctions"
description = '''Normally, where a minor road meets a main road, the Mapnik rendering draws the main road over the minor road. However, in the map at http://www.openstreetmap.org/?lat=50.85242&amp;amp;lon=-1.169066&amp;amp;zoom=18&amp;amp;layers=M, both Deane&#x27;s Park Road, and the short loop of minor road opposite it, are render...'''
date = "2012-06-26T21:29:00Z"
lastmod = "2012-06-26T23:10:00Z"
weight = 13815
keywords = [ "rendering", "junction" ]
aliases = [ "/questions/13815" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering of road junctions](/questions/13815/rendering-of-road-junctions)

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
<span id="post-13815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13815-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Normally, where a minor road meets a main road, the Mapnik rendering draws the main road over the minor road. However, in the map at <a href="http://www.openstreetmap.org/?lat=50.85242&amp;lon=-1.169066&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=50.85242&amp;lon=-1.169066&amp;zoom=18&amp;layers=M</a>, both Deane's Park Road, and the short loop of minor road opposite it, are rendered over the main road. Is that because of something in the map data that could be improved, or is it purely an artefact of the rendering engine?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '12, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '12, 21:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-13815" class="comments-container">
&#10;</div>
<div id="comment-tools-13815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13815-form-container" class="comment-form-container">
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

<span id="13820"></span>

<div id="answer-container-13820" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13820-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's because Mapnik draws '_link' roads below all other roads. The major road is tagged as 'primary_link' and the minor one as 'residential'. There's nothing wrong with the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '12, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-13820" class="comments-container">
<span id="13824"></span>
<div id="comment-13824" class="comment">
<div id="post-13824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-13824-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 23:10)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-13820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13820-form-container" class="comment-form-container">
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

