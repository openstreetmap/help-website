+++
type = "question"
title = "Multiple errors with Nominatim 2.5.1 installation"
description = '''I just upgraded Nominatim to 2.5.1 from 2.4.0. Reverse geocoding works properly but I&#x27;m getting errors when I hit the details.php page PHP Parse error: syntax error, unexpected &#x27;[&#x27; in .../website/details.php on line 93 which keeps the page from rendering. Further, the map does not load on the search...'''
date = "2016-10-15T17:54:00Z"
lastmod = "2016-10-17T18:21:00Z"
weight = 52558
keywords = [ "nominatim" ]
aliases = [ "/questions/52558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple errors with Nominatim 2.5.1 installation](/questions/52558/multiple-errors-with-nominatim-251-installation)

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
<span id="post-52558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just upgraded Nominatim to 2.5.1 from 2.4.0. Reverse geocoding works properly but I'm getting errors when I hit the details.php page <code>PHP Parse error: syntax error, unexpected '[' in .../website/details.php on line 93</code> which keeps the page from rendering. Further, the map does not load on the search page and gives me <code>Uncaught ReferenceError: nominatim_map_init is not defined</code>. Both would seem like permissions errors but the permissions seem fine to access files. Further, as mentioned, reverse geocding works fine. Any help is appreciated, thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '16, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d2e7eae60626279a0687656a0d82a4c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cswrsinc&#39;s gravatar image" />
<p><span>cswrsinc</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cswrsinc has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-52558" class="comments-container">
&#10;</div>
<div id="comment-tools-52558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52558-form-container" class="comment-form-container">
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

<span id="52574"></span>

<div id="answer-container-52574" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This could be a mismatch of files in the <code>/website</code> and <code>build/website</code> directory. Try running the <code>create-website</code> setup step in <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '16, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52574" class="comments-container">
<span id="52575"></span>
<div id="comment-52575" class="comment">
<div id="post-52575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now tracked in <a href="https://github.com/twain47/Nominatim/issues/555">https://github.com/twain47/Nominatim/issues/555</a></p>
</div>
<div id="comment-52575-info" class="comment-info">
<span class="comment-age">(17 Oct '16, 17:54)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="52577"></span>
<div id="comment-52577" class="comment">
<div id="post-52577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using these directions, <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS">https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS</a> and don't see a <em>build</em> directory.</p>
</div>
<div id="comment-52577-info" class="comment-info">
<span class="comment-age">(17 Oct '16, 18:18)</span> <span class="comment-user userinfo">cswrsinc</span>
</div>
</div>
<span id="52578"></span>
<div id="comment-52578" class="comment">
<div id="post-52578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, don't see anything in <em>setup.php</em> related to a <em>build</em>s directory related to web site creation.</p>
</div>
<div id="comment-52578-info" class="comment-info">
<span class="comment-age">(17 Oct '16, 18:21)</span> <span class="comment-user userinfo">cswrsinc</span>
</div>
</div>
</div>
<div id="comment-tools-52574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52574-form-container" class="comment-form-container">
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

