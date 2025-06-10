+++
type = "question"
title = "Fail getting static maps since March 1st 2012."
description = '''Hi I have been using the static map API (osm-tah-cache.firefishy.com) to render maps into the background of my Java desktop application. This method worked fast and satisfying for almost a year now. However, it seems like since Match 1st one of the OSM servers retired - and this URL is not available...'''
date = "2012-03-06T13:07:00Z"
lastmod = "2012-03-06T13:41:00Z"
weight = 11007
keywords = [ "static" ]
aliases = [ "/questions/11007" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fail getting static maps since March 1st 2012.](/questions/11007/fail-getting-static-maps-since-march-1st-2012)

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
<span id="post-11007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have been using the static map API (<a href="http://osm-tah-cache.firefishy.com">osm-tah-cache.firefishy.com</a>) to render maps into the background of my Java desktop application. This method worked fast and satisfying for almost a year now. However, it seems like since Match 1st one of the OSM servers retired - and this URL is not available anymore. I have tried to use alternatives I saw in <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">http://wiki.openstreetmap.org/wiki/Static_map_images</a> (like <a href="http://pafciu17.dev.openstreetmap.org">pafciu17.dev.openstreetmap.org</a> and <a href="http://staticmap.openstreetmap.de">staticmap.openstreetmap.de</a>) - but they are very not responsive and give a very bad performance (takes something like 30 seconds to download a single image from a fast internet connection).</p>
<p>Are you aware of this performance? Is it going to be improved? Is there anything I can do (use another server? I have searched the web and haven't found alternatives so far)?</p>
<p>Thanks a lot!</p>
<p>Doron.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '12, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e9e63666f555e34b9a36d73aa1778162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dorfri&#39;s gravatar image" />
<p><span>dorfri</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dorfri has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11007" class="comments-container">
&#10;</div>
<div id="comment-tools-11007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11007-form-container" class="comment-form-container">
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

<span id="11008"></span>

<div id="answer-container-11008" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11008-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Static maps are not good for use in applications. For that you might get better performence and responsiveness by using a tile server. The only slippymap implementation in java I know of is for JOSM and can be found at <a href="https://josm.openstreetmap.de/browser/josm/trunk/src/org/openstreetmap/josm/gui/layer/TMSLayer.java">the josm svn</a> under GPL.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '12, 13:25</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '12, 13:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-11008" class="comments-container">
<span id="11009"></span>
<div id="comment-11009" class="comment">
<div id="post-11009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>+1 for using tiles.</p>
<p>However, it'd be interesting to know why those other staticmap servers are so much slower than the tah one.</p>
</div>
<div id="comment-11009-info" class="comment-info">
<span class="comment-age">(06 Mar '12, 13:41)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-11008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11008-form-container" class="comment-form-container">
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

