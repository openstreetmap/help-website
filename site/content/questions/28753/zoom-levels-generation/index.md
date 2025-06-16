+++
type = "question"
title = "Zoom levels&#x27; generation"
description = '''Hi. I am confused with and I don&#x27;t understand the zoom levels&#x27; generation. More precisely - what are the criteria for objects (for example, area objects) to appear or disappear in the zoom levels. For illustration, access the link https://www.openstreetmap.org/#map=6/50.345/-99.55 and so zoom out one...'''
date = "2013-12-04T11:27:00Z"
lastmod = "2013-12-04T13:19:00Z"
weight = 28753
keywords = [ "zoomlevel", "objects", "criteria" ]
aliases = [ "/questions/28753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Zoom levels' generation](/questions/28753/zoom-levels-generation)

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
<span id="post-28753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28753-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I am confused with and I don't understand the zoom levels' generation. More precisely - what are the criteria for objects (for example, area objects) to appear or disappear in the zoom levels. For illustration, access the link <a href="https://www.openstreetmap.org/#map=6/50.345/-99.55">https://www.openstreetmap.org/#map=6/50.345/-99.55</a> and so zoom out one step. Many large lakes will disappear while much smaller islands don't. If I repeat the experiment with other apps in the Slippymap (like the Cycle map, Transport map ...) I am getting even more confused. Even just pointing to some related documentation would be much appreciated. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-criteria" rel="tag" title="see questions tagged &#39;criteria&#39;">criteria</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '13, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-28753" class="comments-container">
&#10;</div>
<div id="comment-tools-28753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28753-form-container" class="comment-form-container">
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

<span id="28773"></span>

<div id="answer-container-28773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28773-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The features that show on each zoom level are controlled by the stylesheets. For example, the stylesheets controlling the "Standard" layer are found here:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
<p>The strange behaviour that you are seeing here is because lakes are only shown from zoom 6. The lower zoom levels (0-5) only show water defined by coastlines. But here one lake has been mapped as a coastline, and the other as a lake (with natural=water tags), which is why one disappears and the other doesn't.</p>
<p>In future, I would expect the zoom 5 to take into account very large lakes, but that's not something that's likely to happen soon. As for the tagging, it's important that people stop tagging large lakes with natural=coastline since that's incorrect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '13, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-28773" class="comments-container">
&#10;</div>
<div id="comment-tools-28773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28773-form-container" class="comment-form-container">
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

