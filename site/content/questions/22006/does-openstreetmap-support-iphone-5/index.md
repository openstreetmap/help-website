+++
type = "question"
title = "Does OpenStreetMap support iPhone 5?"
description = '''I am building an iPhone application using Phonegap and OpenStreeMap. However, while I load OSM on my iPhone 5, it displays pixels. Would you have any fix for this? Or alternative that support high resolution devices?'''
date = "2013-05-01T05:30:00Z"
lastmod = "2013-05-01T08:23:00Z"
weight = 22006
keywords = [ "highres", "retina", "iphone5" ]
aliases = [ "/questions/22006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does OpenStreetMap support iPhone 5?](/questions/22006/does-openstreetmap-support-iphone-5)

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
<span id="post-22006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22006-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building an iPhone application using Phonegap and OpenStreeMap.</p>
<p>However, while I load OSM on my iPhone 5, it displays pixels.</p>
<p>Would you have any fix for this? Or alternative that support high resolution devices?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highres" rel="tag" title="see questions tagged &#39;highres&#39;">highres</span> <span class="post-tag tag-link-retina" rel="tag" title="see questions tagged &#39;retina&#39;">retina</span> <span class="post-tag tag-link-iphone5" rel="tag" title="see questions tagged &#39;iphone5&#39;">iphone5</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '13, 05:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c487cf4205f4201f9b9c56151d212cdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s8902&#39;s gravatar image" />
<p><span>s8902</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s8902 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '13, 10:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-22006" class="comments-container">
&#10;</div>
<div id="comment-tools-22006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22006-form-container" class="comment-form-container">
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

<span id="22008"></span>

<div id="answer-container-22008" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22008-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-22008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is about high-resolution displays in general and not specific to one phone type.</p>
<p>OpenStreetMap.org does not provide double-resolution tiles. But <a href="http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy">you probably shouldn't be using OpenStreetMap.org's tiles for your iPhone app anyway.</a></p>
<p>Consequently you will need to either render your own tiles on your own server, or find a third-party service who can do this for you (probably at a cost). You can read a discussion on the OSM development mailing list in <a href="http://lists.openstreetmap.org/pipermail/dev/2012-June/date.html">June</a> and <a href="http://lists.openstreetmap.org/pipermail/dev/2012-July/date.html">July</a> last year; this suggests, to me, that Frederik Ramm's company <a href="http://www.geofabrik.de/">Geofabrik</a> would be good people to contact.</p>
<p>If you wish to set up your own server, the basic instructions are at <a href="http://switch2osm.org/">switch2osm.org</a> but you'll need to adjust them along <a href="http://lists.openstreetmap.org/pipermail/dev/2012-July/025165.html">these lines</a>. This is unlikely to be suitable for someone without specialist OSM knowledge.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '13, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-22008" class="comments-container">
&#10;</div>
<div id="comment-tools-22008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22008-form-container" class="comment-form-container">
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

