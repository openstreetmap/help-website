+++
type = "question"
title = "Is there a way to align offset of satellite images while editing?"
description = '''Hello everyone, I was editing a very outdated map in OSM, and noticed how different satellite views aren&#x27;t properly aligned with the entire map. The map aligns fine with Bing, but those images are severely outdated (around a decade old). I had to use a recent (or as recent as I could) satellite view...'''
date = "2019-11-22T22:27:00Z"
lastmod = "2019-11-22T23:19:00Z"
weight = 71775
keywords = [ "satellite-images", "imagery_offset", "alignment" ]
aliases = [ "/questions/71775" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to align offset of satellite images while editing?](/questions/71775/is-there-a-way-to-align-offset-of-satellite-images-while-editing)

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
<span id="post-71775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71775-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, I was editing a very outdated map in OSM, and noticed how different satellite views aren't properly aligned with the entire map. The map aligns fine with Bing, but those images are severely outdated (around a decade old).</p>
<p>I had to use a recent (or as recent as I could) satellite view provider, but everything has a small, but significant offset (maybe of 10-15 meters). Istead of realigning the entire city with the more recent satellite views, is there a way to set an XY offset to the satellite images so that they would align better with the existing data? or maybe a tool to realign every road in a city with the more up to date views?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-satellite-images" rel="tag" title="see questions tagged &#39;satellite-images&#39;">satellite-images</span> <span class="post-tag tag-link-imagery_offset" rel="tag" title="see questions tagged &#39;imagery_offset&#39;">imagery_offset</span> <span class="post-tag tag-link-alignment" rel="tag" title="see questions tagged &#39;alignment&#39;">alignment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '19, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/8171348e26549c118dfc12bf9bb214a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheXDS&#39;s gravatar image" />
<p><span>TheXDS</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheXDS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71775" class="comments-container">
&#10;</div>
<div id="comment-tools-71775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71775-form-container" class="comment-form-container">
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

<span id="71776"></span>

<div id="answer-container-71776" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71776-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TheXDS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes.</p>
<p>If you are using iD (the editor built into the website), open the background panel by pressing <code>b</code> or clicking the layer stack icon on the right side of the screen. Scroll to the bottom of that panel and expand the 'Adjust imagery offset' section. You can use the arrows, click and drag, or enter an offset directly.</p>
<p>If you are using JOSM, there is an 'Imagery Offset' submenu under the 'Imagery' menu. Select the layer you want to adjust and the click and drag the in the main window to adjust the layer.</p>
<p>Other editors that support lots of layers should have some similar mechanism.</p>
<p>Take your time deciding whether to adjust the existing data or not. It usually isn't that big an improvement and it is a lot of work. It can also be a bit of a chore to figure out which layer is really more accurate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '19, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '19, 23:25</strong> </span></p>
</div>
</div>
<div id="comments-container-71776" class="comments-container">
&#10;</div>
<div id="comment-tools-71776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71776-form-container" class="comment-form-container">
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

