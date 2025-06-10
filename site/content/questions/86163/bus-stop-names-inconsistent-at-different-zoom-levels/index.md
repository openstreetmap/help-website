+++
type = "question"
title = "Bus stop names inconsistent at different zoom levels"
description = '''Hi. I have been updating some bus stops with confusing results. When rendered on the official OSM site, the names display inconsistently. According to my limited understanding of the rendering rules here, I should see an icon at zoom levels 16 and above. This part is working OK. I should also see th...'''
date = "2022-11-16T12:52:00Z"
lastmod = "2022-11-16T16:42:00Z"
weight = 86163
keywords = [ "zoomlevel", "rendering", "bus_stop" ]
aliases = [ "/questions/86163" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Bus stop names inconsistent at different zoom levels](/questions/86163/bus-stop-names-inconsistent-at-different-zoom-levels)

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
<span id="post-86163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I have been updating some bus stops with confusing results. When rendered on the official OSM site, the names display inconsistently. According to my limited understanding of the rendering rules <a href="https://github.com/gravitystorm/openstreetmap-carto/tree/master/style">here</a>, I should see an icon at zoom levels 16 and above. This part is working OK. I should also see the name at zoom levels 17 and above. This is inconsistent. At certain zoom levels, some names are displayed and some are not.</p>
<p>For example, what is the difference between these two? At some zoom levels, one shows a name and the other doesn't.</p>
<p><a href="https://www.openstreetmap.org/node/502548863">opp Barnfield Road</a></p>
<p><a href="https://www.openstreetmap.org/node/502545637">nr Barnfield Road</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-bus_stop" rel="tag" title="see questions tagged &#39;bus_stop&#39;">bus_stop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '22, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/3f8ba5952c1b172566d49666c9c38f8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tenbob0&#39;s gravatar image" />
<p><span>Tenbob0</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tenbob0 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '22, 12:54</strong> </span></p>
</div>
</div>
<div id="comments-container-86163" class="comments-container">
&#10;</div>
<div id="comment-tools-86163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86163-form-container" class="comment-form-container">
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

<span id="86164"></span>

<div id="answer-container-86164" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86164-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tenbob0 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The label for "opp Barnfield Road" would conflict with the street name "The Ridgeway" and is therefore omitted. The rendering engine is not clever enough to displace the street name in this situation (as it has already been rendered by the time the engine looks as bus stops).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '22, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86164" class="comments-container">
<span id="86168"></span>
<div id="comment-86168" class="comment">
<div id="post-86168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Frederik. This explains what is going on. It seems quite odd, as certain names come and go as you zoom in with the scroll wheel.</p>
</div>
<div id="comment-86168-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 16:42)</span> <span class="comment-user userinfo">Tenbob0</span>
</div>
</div>
</div>
<div id="comment-tools-86164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86164-form-container" class="comment-form-container">
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

