+++
type = "question"
title = "Non-HTTP requests inside own OSM server"
description = '''Is it possible? Are there tools like Overpass API that work without using HTTP?'''
date = "2015-01-06T14:54:00Z"
lastmod = "2015-01-06T18:12:00Z"
weight = 40064
keywords = [ "tools", "request" ]
aliases = [ "/questions/40064" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Non-HTTP requests inside own OSM server](/questions/40064/non-http-requests-inside-own-osm-server)

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
<span id="post-40064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40064-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible? Are there tools like Overpass API that work without using HTTP?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '15, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/aeafd4156483ce12e60c02d426635abe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yaahor&#39;s gravatar image" />
<p><span>yaahor</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yaahor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40064" class="comments-container">
<span id="40065"></span>
<div id="comment-40065" class="comment">
<div id="post-40065-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain in a few more words what it is that you are actually trying to do?</p>
</div>
<div id="comment-40065-info" class="comment-info">
<span class="comment-age">(06 Jan '15, 15:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40064-form-container" class="comment-form-container">
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

<span id="40074"></span>

<div id="answer-container-40074" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40074-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yaahor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't have to use HTTP for overpass api on your own server. There's a binary called <code>osm3s_query</code> which will happily accept your Overpass XML or QL queries on <code>stdin</code> and return some OSM xml result on stdout. That's actually quite handy once in a while for some local tests. Even overpass-api.de leverages <code>osm3s_query</code> for the purpose of creating/updating areas (see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/install#Area_creation">Wiki</a> for details).</p>
<p>However, HTTP is clearly more convenient for overpass turbo and other web based apps, even if you're only pointing your browser to <code>localhost</code>.</p>
<p>This brings up the question why you want to avoid HTTP in the first place??</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '15, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '15, 19:16</strong> </span></p>
</div>
</div>
<div id="comments-container-40074" class="comments-container">
&#10;</div>
<div id="comment-tools-40074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40074-form-container" class="comment-form-container">
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

