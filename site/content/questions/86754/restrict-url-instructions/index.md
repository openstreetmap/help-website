+++
type = "question"
title = "Restrict URL instructions"
description = '''Hi to all, I want to setup an own OSM Tile server for integration into my application. But I&#x27;m a little concerned that it&#x27;s very easy to cause the OSM tile server to fail with a denial of service attack on the URL-instructions ...123.png/dirty or /statusinfo. Now, of course, I could put an NGNX in f...'''
date = "2023-02-20T22:24:00Z"
lastmod = "2023-02-20T23:29:00Z"
weight = 86754
keywords = [ "osm", "tileserver" ]
aliases = [ "/questions/86754" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Restrict URL instructions](/questions/86754/restrict-url-instructions)

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
<span id="post-86754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I want to setup an own OSM Tile server for integration into my application. But I'm a little concerned that it's very easy to cause the OSM tile server to fail with a denial of service attack on the URL-instructions ...123.png/dirty or /statusinfo.</p>
<p>Now, of course, I could put an NGNX in front and filter out the URL-instructions via regex. Nevertheless I would like to ask here in the round whether the server has perhaps a simple option to disable these URL instructions?</p>
<p>I thank you in advance...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '23, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/d72a4bc707e757ac3575540813ba62f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ulrich%20Cech&#39;s gravatar image" />
<p><span>Ulrich Cech</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ulrich Cech has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86754" class="comments-container">
&#10;</div>
<div id="comment-tools-86754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86754-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="86756"></span>

<div id="answer-container-86756" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86756-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A typical tile server configuration would include something like</p>
<pre><code>RedirectMatch 404 /tiles/.*/dirty
RedirectMatch 404 /tiles/.*/status</code></pre>
<p>to disallow the "dirty" and "status" requests. (Replace "tiles" with whatever your tile URL is.) You could do the same with mod_tile's status request (/mod_tile) although this is not expensive to serve, it is just information that you might not want to publish. If you're using something that monitors your tile server, e.g. munin, you would not outright disallow /mod_tile but do something like</p>
<pre><code>&lt;Location &quot;/mod_tile&quot;&gt;
   Require local  
&lt;/Location&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '23, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86756" class="comments-container">
&#10;</div>
<div id="comment-tools-86756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86756-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86755"></span>

<div id="answer-container-86755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86755-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, it's just Apache. Any filtering, throttling or other restrictions that work with Apache elsewhere will also work here.</p>
<p>Secondly, mod_tile supports throttling - see <a href="https://github.com/openstreetmap/mod_tile/search?q=throttling">https://github.com/openstreetmap/mod_tile/search?q=throttling</a> . If you change anything from the defaults you'll want to make sure that "normal" actions like just browsing around the map aren't throttled too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '23, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86755" class="comments-container">
&#10;</div>
<div id="comment-tools-86755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86755-form-container" class="comment-form-container">
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

