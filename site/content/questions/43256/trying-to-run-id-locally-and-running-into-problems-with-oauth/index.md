+++
type = "question"
title = "Trying to run iD locally and running into problems with OAUTH"
description = '''I&#x27;m trying to run a local version of iD and am having problems. I&#x27;m on windows. Here&#x27;s what I&#x27;ve done so far: git clone git@github.com:openstreetmap/iD cd iD python -m SimpleHTTPServer  I can then visit 127.0.0.1:8000 in browser &amp;amp; the map loads, everything seems to work. The browser is logged in...'''
date = "2015-05-27T13:42:00Z"
lastmod = "2015-05-27T14:33:00Z"
weight = 43256
keywords = [ "ideditor" ]
aliases = [ "/questions/43256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to run iD locally and running into problems with OAUTH](/questions/43256/trying-to-run-id-locally-and-running-into-problems-with-oauth)

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
<span id="post-43256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43256-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to run a local version of iD and am having problems. I'm on windows.</p>
<p>Here's what I've done so far:</p>
<pre><code>git clone git@github.com:openstreetmap/iD
cd iD
python -m SimpleHTTPServer</code></pre>
<p>I can then visit 127.0.0.1:8000 in browser &amp; the map loads, everything seems to work.</p>
<p>The browser is logged in to openstreetmap.org, so I think that it picks up that I'm logged into osm automatically. But when I try to save changes, an OAUTH permission window pops up. I accept everything there, and it redirects me to <a href="http://127.0.0.1:8000/land.html?oauth_token=%5Bremoved%5D">http://127.0.0.1:8000/land.html?oauth_token=[removed]</a> which is a page whose content is just:</p>
<pre><code>!ÿþdist/land.html</code></pre>
<p>Here's what view source on it looks like - maybe a broken unicode page which mentions symlink?:</p>
<pre><code>!&lt;symlink&gt;ÿþd</code></pre>
<p>It looks like iD may need more config to run locally? Is it just missing the hostname of the page OAUTH wants to redirect me to?</p>
<p>Also, "ÿþ" is the UTF-16 BOM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '15, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f6f5ee4b3a9eed93b932d670d186f811?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RationalTangle&#39;s gravatar image" />
<p><span>RationalTangle</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RationalTangle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '15, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-43256" class="comments-container">
&#10;</div>
<div id="comment-tools-43256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43256-form-container" class="comment-form-container">
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

<span id="43257"></span>

<div id="answer-container-43257" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43257-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It was a symlink problem due to windows. I just had to move <code>&lt;root&gt;dist/land.html</code> to &lt;root&gt;/land.html (replacing the symlink originally at land.html)</p>
<p>There is symlink for css/img - you have to copy dist/img to replace css/img also.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '15, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f6f5ee4b3a9eed93b932d670d186f811?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RationalTangle&#39;s gravatar image" />
<p><span>RationalTangle</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RationalTangle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43257" class="comments-container">
&#10;</div>
<div id="comment-tools-43257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43257-form-container" class="comment-form-container">
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

