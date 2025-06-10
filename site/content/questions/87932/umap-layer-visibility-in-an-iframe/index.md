+++
type = "question"
title = "uMap: Layer visibility in an iframe"
description = '''Is there a way of filtering which uMap layers are shown and which are hidden by default in an embedded iframe?  I have a map in uMap with 80 imported layers which I would like to display in different arrangements using iframes (with one iframe per arrangement). Making a new map for each of those arr...'''
date = "2023-10-24T10:16:00Z"
lastmod = "2023-10-25T16:48:00Z"
weight = 87932
keywords = [ "umap", "layer", "export", "visibility", "iframe" ]
aliases = [ "/questions/87932" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [uMap: Layer visibility in an iframe](/questions/87932/umap-layer-visibility-in-an-iframe)

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
<span id="post-87932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h2 id="is-there-a-way-of-filtering-which-umap-layers-are-shown-and-which-are-hidden-by-default-in-an-embedded-iframe">Is there a way of filtering which uMap layers are shown and which are hidden by default in an embedded iframe?</h2>
<hr />
<p>I have a map in uMap with 80 imported layers which I would like to display in different arrangements using iframes (with one iframe per arrangement).</p>
<p>Making a new map for each of those arrangements is certainly an option, but it will be nightmarishly labourious to maintain and update.</p>
<p>It would therefore be practical if there was a way of filtering which layers are to be shown using the parameters of the iframe, either based on the name of the layer or on one of the layer's other parameters.</p>
<p>There at least seem to have existed options for exporting iframes according to the wiki ( <a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Export_data_of_my_uMap">https://wiki.openstreetmap.org/wiki/UMap/Guide/Export_data_of_my_uMap</a> ), but I can't find any settings affecting the embedding code in the current version at <a href="https://umap.openstreetmap.fr/en/">https://umap.openstreetmap.fr/</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-visibility" rel="tag" title="see questions tagged &#39;visibility&#39;">visibility</span> <span class="post-tag tag-link-iframe" rel="tag" title="see questions tagged &#39;iframe&#39;">iframe</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '23, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/83eb92d6024050a3ebeea4a402f98db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BSKK&#39;s gravatar image" />
<p><span>BSKK</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BSKK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87932" class="comments-container">
&#10;</div>
<div id="comment-tools-87932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87932-form-container" class="comment-form-container">
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

<span id="87934"></span>

<div id="answer-container-87934" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87934-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BSKK has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you click <img src="https://wiki.openstreetmap.org/w/images/thumb/3/33/Icon-share.png/20px-Icon-share.png" alt="share" /> on the umap and then select "Export Options" in the new panel at the right, there is a switch that is labelled "Keep current visible layers". Does this do what you want?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '23, 02:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-87934" class="comments-container">
<span id="87945"></span>
<div id="comment-87945" class="comment">
<div id="post-87945-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You just saved me a lot of future headaches! I could have sworn I had tried that option to no avail, but the "Export Options" do indeed work also for iframe embedding. Thank you!</p>
</div>
<div id="comment-87945-info" class="comment-info">
<span class="comment-age">(25 Oct '23, 16:48)</span> <span class="comment-user userinfo">BSKK</span>
</div>
</div>
</div>
<div id="comment-tools-87934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87934-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

