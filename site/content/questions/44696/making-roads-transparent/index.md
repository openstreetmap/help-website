+++
type = "question"
title = "Making roads transparent"
description = '''I recently added that a new overpass has been built to by-pass a roundabout at this location (https://www.openstreetmap.org/#map=18/37.80087/27.28999) I have now added this to OSM and as I usually do I have gone back and checked how it looks outside of the editor - and it now looks very unclear. I h...'''
date = "2015-08-10T11:18:00Z"
lastmod = "2015-08-12T09:53:00Z"
weight = 44696
keywords = [ "overpass", "bridge" ]
aliases = [ "/questions/44696" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Making roads transparent](/questions/44696/making-roads-transparent)

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
<span id="post-44696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44696-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added that a new overpass has been built to by-pass a roundabout at this location (<a href="https://www.openstreetmap.org/#map=18/37.80087/27.28999">https://www.openstreetmap.org/#map=18/37.80087/27.28999</a>) I have now added this to OSM and as I usually do I have gone back and checked how it looks outside of the editor - and it now looks very unclear. I have tagged the overpass as a bridge but is there another tag I need to apply because it looks horrible and is hard to follow (thinking one which makes the road transparent?). Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '15, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/2c58b9207373c87e253d0b7433dca98a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skifans&#39;s gravatar image" />
<p><span>skifans</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skifans has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44696" class="comments-container">
<span id="44699"></span>
<div id="comment-44699" class="comment">
<div id="post-44699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems to be clear at one zoom level higher. And turn-by-turn directions should be correct in any case.</p>
</div>
<div id="comment-44699-info" class="comment-info">
<span class="comment-age">(10 Aug '15, 12:28)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-44696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44696-form-container" class="comment-form-container">
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

<span id="44701"></span>

<div id="answer-container-44701" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44701-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="skifans has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't really have to "make roads transparent" - usually you should tag to the best you can, and leave the displaying to the renderers. You might have heard "<a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">do not tag for the renderer</a>" suggestion :) The idea is that it's best to tag things as they are. There are various renderers and styles, and it is up to them to get things right/beautiful.</p>
<p>In this case, though, you could make the roundabout and connected trunk_link ways all trunk, or make those two secondary attachments secondary_link. With the default renderer, it would draw trunk segments on top of the secondary segments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '15, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '15, 14:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-44701" class="comments-container">
<span id="44726"></span>
<div id="comment-44726" class="comment">
<div id="post-44726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I'm quite new here so havnt heard the phrase before. Il change the roads as per you advice when I'm next on a PC, thanks again!</p>
</div>
<div id="comment-44726-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 09:53)</span> <span class="comment-user userinfo">skifans</span>
</div>
</div>
</div>
<div id="comment-tools-44701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44701-form-container" class="comment-form-container">
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

