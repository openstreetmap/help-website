+++
type = "question"
title = "Best approach for rotated maps?"
description = '''I&#x27;m building a mobile app in which I&#x27;d like to show maps relative to a user&#x27;s direction of motion, so that up is always forward for the user. (Sort of like what navigation apps do.) When I try this with normal tiles, the text is awkward to read. What&#x27;s my best approach to fixing the text orientation...'''
date = "2019-09-13T17:42:00Z"
lastmod = "2019-09-15T23:31:00Z"
weight = 70767
keywords = [ "vector", "rendering", "rotate", "custom_tiles" ]
aliases = [ "/questions/70767" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best approach for rotated maps?](/questions/70767/best-approach-for-rotated-maps)

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
<span id="post-70767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm building a mobile app in which I'd like to show maps relative to a user's direction of motion, so that up is always forward for the user. (Sort of like what navigation apps do.) When I try this with normal tiles, the text is awkward to read. What's my best approach to fixing the text orientation?</p>
<p>The two obvious approaches I can find are rendering my own bitmap tiles and dynamically rendering from vector tiles. Are there other approaches I should be looking at? And what are the tradeoffs?</p>
<p>If it's helpful in answering the question, I'm a developer comfortable running my own servers, but the tile-server stuff looks complicated enough I'm happy to avoid that. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-rotate" rel="tag" title="see questions tagged &#39;rotate&#39;">rotate</span> <span class="post-tag tag-link-custom_tiles" rel="tag" title="see questions tagged &#39;custom_tiles&#39;">custom_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '19, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/19a866fd7c999be94578126c56f2b65a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WilliamPietri&#39;s gravatar image" />
<p><span>WilliamPietri</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WilliamPietri has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70767" class="comments-container">
<span id="70769"></span>
<div id="comment-70769" class="comment">
<div id="post-70769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Non-answer: In case you haven't seen it, there is a rather long list of <a href="https://wiki.openstreetmap.org/wiki/Frameworks#Displaying_interactive_maps">frameworks on the wiki</a>.</p>
</div>
<div id="comment-70769-info" class="comment-info">
<span class="comment-age">(13 Sep '19, 18:53)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="70770"></span>
<div id="comment-70770" class="comment">
<div id="post-70770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! In this case I'm writing in Dart and Flutter, so none of the existing tools will do. I could build something based on MapBox's vector tiles, but I thought I'd first look at what I could do with OSM, as I'd rather go an open-source route if it's not too much extra work.</p>
</div>
<div id="comment-70770-info" class="comment-info">
<span class="comment-age">(13 Sep '19, 22:18)</span> <span class="comment-user userinfo">WilliamPietri</span>
</div>
</div>
<span id="70796"></span>
<div id="comment-70796" class="comment">
<div id="post-70796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mapbox vector tiles are almost certainly the way to go, but there are lots of open-source options for generating them from OSM data.</p>
</div>
<div id="comment-70796-info" class="comment-info">
<span class="comment-age">(15 Sep '19, 23:31)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70767-form-container" class="comment-form-container">
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

<span id="70771"></span>

<div id="answer-container-70771" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70771-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's likely no such thing as the "best approach" InsertUser has already pointed to the wiki list of frameworks, so I'll leave that out.</p>
<p>Essentially it really depends on if you believe that asking your users to download an area in advance is a good idea or not. If the answer is yes you could use mapsforge, OsmAnd or mapsme format (you would likely need to produce the necessary glue/bindings for Dart). If no then you are stuck with vector tiles either with mapbox gl, or if you are in to zombies, mapzens tangram. You don't necessarily need to have a lot of infrastructure to do that, you just need something serving pre-generated tiles if you don't mind having stale data (see for example <a href="https://openmaptiles.org/">https://openmaptiles.org/</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '19, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '19, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-70771" class="comments-container">
&#10;</div>
<div id="comment-tools-70771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70771-form-container" class="comment-form-container">
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

