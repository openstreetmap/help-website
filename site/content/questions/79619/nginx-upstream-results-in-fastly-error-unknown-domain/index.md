+++
type = "question"
title = "Nginx upstream results in :Fastly error: unknown domain"
description = '''I have a local server. I tried to cache/balance Openstreetmap very simple as you see in bellow: upstream osm {  server a.tile.openstreetmap.org; server b.tile.openstreetmap.org; server c.tile.openstreetmap.org; }  server { listen 80; server_name *.192.168.29.132 192.168.29.132;   location /myosm/ { ...'''
date = "2021-04-12T10:26:00Z"
lastmod = "2021-04-12T12:34:00Z"
weight = 79619
keywords = [ "openstreetmap", "upstream" ]
aliases = [ "/questions/79619" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nginx upstream results in :Fastly error: unknown domain](/questions/79619/nginx-upstream-results-in-fastly-error-unknown-domain)

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
<span id="post-79619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79619-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a local server. I tried to cache/balance Openstreetmap very simple as you see in bellow:</p>
<pre><code>upstream osm {                           
server  a.tile.openstreetmap.org;
server  b.tile.openstreetmap.org;
server  c.tile.openstreetmap.org;
}
&#10;server {
listen        80;
server_name     *.192.168.29.132  192.168.29.132;
&#10;   location /myosm/ {
     proxy_pass http://osm;
   }
}</code></pre>
<p>Good to say that I can use upstream for any internal servers correctly like this :</p>
<pre><code>upstream my_servers {                           
 server  192.168.29.100;
 server  192.168.29.101;
}</code></pre>
<p>But I have problem with openstreetmap servers. Any hint is appreciable.</p>
<p>Error is :</p>
<blockquote>
<p>Fastly error: unknown domain: osm. Please check that this domain has been added to a service.</p>
</blockquote>
<p>Details: cache-fra19124-FRA</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-upstream" rel="tag" title="see questions tagged &#39;upstream&#39;">upstream</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '21, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/3b7a89ef361fa79a5bdaa01c87dc23d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ehsan_1362&#39;s gravatar image" />
<p><span>Ehsan_1362</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ehsan_1362 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79619" class="comments-container">
&#10;</div>
<div id="comment-tools-79619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79619-form-container" class="comment-form-container">
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

<span id="79622"></span>

<div id="answer-container-79622" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79622-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ehsan_1362 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are sending a host header value of "osm" upstream. That won't work with fastly.</p>
<p>So try adding a</p>
<blockquote>
<pre><code>proxy_set_header Host tile.openstreetmap.org;</code></pre>
</blockquote>
<p>to the proxy location directive.</p>
<p>Please also note the tile usage policy that you'll have to follow: <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '21, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '21, 11:20</strong> </span></p>
</div>
</div>
<div id="comments-container-79622" class="comments-container">
<span id="79624"></span>
<div id="comment-79624" class="comment">
<div id="post-79624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for replying. Installing a fresh Nginx, adding</p>
<pre><code>proxy_set_header Host tile.openstreetmap.org;</code></pre>
<p>and finally changing this :</p>
<pre><code>proxy_pass http://osm;</code></pre>
<p>to this:</p>
<pre><code>proxy_pass http://osm/;</code></pre>
<p>saved me.</p>
</div>
<div id="comment-79624-info" class="comment-info">
<span class="comment-age">(12 Apr '21, 12:34)</span> <span class="comment-user userinfo">Ehsan_1362</span>
</div>
</div>
</div>
<div id="comment-tools-79622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79622-form-container" class="comment-form-container">
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

