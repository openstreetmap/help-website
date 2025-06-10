+++
type = "question"
title = "Where can I find the source code of the main osm page"
description = '''Hi: I found that the osm main page use the openlayers with custom some features. I am interested in this, but I only find the compressed codes. Is it possible to get the uncompressed codes(openlayers related)?'''
date = "2013-05-30T01:15:00Z"
lastmod = "2013-05-30T08:36:00Z"
weight = 22884
keywords = [ "website", "osm.org", "openlayers", "slippymap", "server" ]
aliases = [ "/questions/22884" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where can I find the source code of the main osm page](/questions/22884/where-can-i-find-the-source-code-of-the-main-osm-page)

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
<span id="post-22884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22884-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi:</p>
<p>I found that the <a href="http://www.openstreetmap.org/">osm main page</a> use the openlayers with custom some features.</p>
<p>I am interested in this, but I only find the compressed codes.</p>
<p>Is it possible to get the uncompressed codes(openlayers related)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '13, 01:15</strong></p>
<img src="https://secure.gravatar.com/avatar/8b5f2224482b0bc3648353d36a0c8814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hguser&#39;s gravatar image" />
<p><span>hguser</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hguser has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '13, 15:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22884" class="comments-container">
&#10;</div>
<div id="comment-tools-22884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22884-form-container" class="comment-form-container">
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

<span id="22885"></span>

<div id="answer-container-22885" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22885-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hguser has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have not looked at the code before / am not involved, but I think you are searching for this: <span>The Rails Port</span> and especially the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/app/views/site/index.html.erb">source code of the main osm page</a>. Well, the main JavaScript code is still loaded into some placeholders there - somewhere (<a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/app/assets/javascripts">/app/assets/javascripts</a>?) in the github repo, I guess. By the way: if I see correctly the main page uses <span>Leaflet</span>, not (anymore) <span>OpenLayers</span>.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '13, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '13, 02:08</strong> </span></p>
</div>
</div>
<div id="comments-container-22885" class="comments-container">
<span id="22886"></span>
<div id="comment-22886" class="comment">
<div id="post-22886-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>In case it helps I think <a href="https://github.com/openstreetmap/openstreetmap-website/tree/c0b47c0c2a3c31b42ef946aa6e07b85305091a0c">https://github.com/openstreetmap/openstreetmap-website/tree/c0b47c0c2a3c31b42ef946aa6e07b85305091a0c</a> allows you to browse the site code as it was as at the last commit before merging the Leaflet branch.</p>
</div>
<div id="comment-22886-info" class="comment-info">
<span class="comment-age">(30 May '13, 08:36)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22885-form-container" class="comment-form-container">
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

