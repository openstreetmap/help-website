+++
type = "question"
title = "How to geocode using nominatim with no webserver integration ?"
description = '''Is there help available in internet on how to geocode using nominatim php scripts ? I don&#x27;t wanna install webserver and query(geocode) using http protocol.'''
date = "2017-02-09T16:33:00Z"
lastmod = "2017-02-09T22:48:00Z"
weight = 54572
keywords = [ "openstreetmap", "nominatim" ]
aliases = [ "/questions/54572" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to geocode using nominatim with no webserver integration ?](/questions/54572/how-to-geocode-using-nominatim-with-no-webserver-integration)

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
<span id="post-54572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there help available in internet on how to geocode using nominatim php scripts ? I don't wanna install webserver and query(geocode) using http protocol.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '17, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/2a95229b87eba17c63a633a8fe609aa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3yK&#39;s gravatar image" />
<p><span>3yK</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3yK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '17, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-54572" class="comments-container">
<span id="54577"></span>
<div id="comment-54577" class="comment">
<div id="post-54577-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't cross-post on several forums. (<a href="https://github.com/twain47/Nominatim/issues/627">https://github.com/twain47/Nominatim/issues/627</a> )</p>
</div>
<div id="comment-54577-info" class="comment-info">
<span class="comment-age">(09 Feb '17, 22:48)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-54572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54572-form-container" class="comment-form-container">
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

<span id="54573"></span>

<div id="answer-container-54573" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54573-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="3yK has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not really a Nominatim specific question; if you have a little experience with PHP you can come up with generic answers to your question. For example, if you have a working Nominatim installation with the database loaded and all, you could run this from Nominatim's <code>website</code> directory:</p>
<pre><code>php -r &#39;$_GET[&quot;q&quot;]=&quot;karlsruhe&quot;; $_GET[&quot;format&quot;]=&quot;jsonv2&quot;; include(&quot;search.php&quot;);&#39;</code></pre>
<p>to call the standard search script and feed it with the search term "karlsruhe" and request a JSON response. Of course that's just a quick hack, and you would probably take search.php and modify it slightly so that it takes its search string from a file or directly from stdin.</p>
<p>From your other questions it appears that you might hope for a nicely documented, no-programming-required solution that will give you instant satisfaction. I am afraid such a solution does not exist; you will have to at least spend a little time reading up on PHP basics if you want to succeed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '17, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54573" class="comments-container">
&#10;</div>
<div id="comment-tools-54573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54573-form-container" class="comment-form-container">
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

