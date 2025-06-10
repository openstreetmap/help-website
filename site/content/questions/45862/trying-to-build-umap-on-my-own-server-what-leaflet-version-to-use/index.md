+++
type = "question"
title = "Trying to build uMap on my own server. What Leaflet versión to use?"
description = '''Hi everyone. I&#x27;m trying to build uMap on my own server and experiment with it for educational purposes. Really great software. I&#x27;m a bit confused about dependencies, and have spent some hours trying lots of things: What Leaflet and Leaflet.Editable versión should I use? Examining the compressed .js ...'''
date = "2015-10-13T11:20:00Z"
lastmod = "2015-10-13T11:55:00Z"
weight = 45862
keywords = [ "umap" ]
aliases = [ "/questions/45862" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to build uMap on my own server. What Leaflet versión to use?](/questions/45862/trying-to-build-umap-on-my-own-server-what-leaflet-version-to-use)

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
<span id="post-45862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45862-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>I'm trying to build uMap on my own server and experiment with it for educational purposes. Really great software. I'm a bit confused about dependencies, and have spent some hours trying lots of things: What Leaflet and Leaflet.Editable versión should I use?</p>
<p>Examining the compressed .js in online examples (i.e. <a href="http://umap.fluv.io/static/CACHE/js/28e5f8d7eaae.js),">http://umap.fluv.io/static/CACHE/js/28e5f8d7eaae.js),</a> all of them seem to use Leaflet 0.7.2. However, building the 'reqs' dir for Leaflet-Storage package I get 1.0 version for Leaflet by default and some js errors occur in leaflet.storage.controls.js and leaflet.storage.js.</p>
<p>In 'no-compressing' mode all static files are published and every resource is available (no 404 errors). In order to discard any other possible problem, just replacing my first Django compressed .js with the 28e5f8d7eaae.js file found on examples everything run OK.</p>
<p>Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '15, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/91f0be8518e3ae60fbb8753e5fae6c0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jesus_&#39;s gravatar image" />
<p><span>jesus_</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jesus_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45862" class="comments-container">
&#10;</div>
<div id="comment-tools-45862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45862-form-container" class="comment-form-container">
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

<span id="45863"></span>

<div id="answer-container-45863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45863-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>uMap is an unstable state at this moment, waiting for Leaflet 1.0 to be released.</p>
<p>Basically, you need to use master of uMap, django-leaflet-storage, Leaflet, Leaflet.Storage, Leaflet.Editable OR to use last stable tag from each of those.</p>
<p>Also, some Leaflet plugins (Leaflet.Toolbar, Leaflet.Label) have a dedicated branch to use with Leaflet master, and you whould use them if you go the unstable way.</p>
<p>Raise up on #umap on Freenode or <a href="https://gitter.im/umap-project/umap">https://gitter.im/umap-project/umap</a> to get help. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '15, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/2b1724b5d0f3b2d1473819e36212fd61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ybon&#39;s gravatar image" />
<p><span>ybon</span><br />
<span class="score" title="626 reputation points">626</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ybon has 6 accepted answers">42%</span></p>
</div>
</div>
<div id="comments-container-45863" class="comments-container">
<span id="45866"></span>
<div id="comment-45866" class="comment">
<div id="post-45866-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you ybon! Looking forward to Leaflet 1.0 and uMap stable.</p>
</div>
<div id="comment-45866-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 11:55)</span> <span class="comment-user userinfo">jesus_</span>
</div>
</div>
</div>
<div id="comment-tools-45863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45863-form-container" class="comment-form-container">
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

