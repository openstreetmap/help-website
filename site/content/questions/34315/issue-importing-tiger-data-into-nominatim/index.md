+++
type = "question"
title = "Issue importing tiger data into nominatim"
description = '''Hi, I&#x27;ve imported openstreet data successfully, and now I&#x27;m importing the tiger2013 edges files into nominatim, all seems to go well when running the script but querying the local nominatim gives no results while the public server does. EDIT: tail of /var/log/prosgres im getting close - its looks li...'''
date = "2014-06-25T13:59:00Z"
lastmod = "2014-06-26T17:32:00Z"
weight = 34315
keywords = [ "tiger", "import", "nominatim", "edges" ]
aliases = [ "/questions/34315" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Issue importing tiger data into nominatim](/questions/34315/issue-importing-tiger-data-into-nominatim)

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
<span id="post-34315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34315-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've imported openstreet data successfully, and now I'm importing the tiger2013 edges files into nominatim, all seems to go well when running the script but querying the local nominatim gives no results while the public server does.</p>
<p>EDIT:</p>
<p>tail of /var/log/prosgres im getting close - its looks like an issue with function get_partition</p>
<hr />
<p>UTC ERROR: function get_partition(geometry, unknown) does not exist at character 8</p>
<p>UTC HINT: No function matches the given name and argument types. You might need to add explicit type casts</p>
<p>UTC QUERY: SELECT get_partition(place_centroid, 'us')</p>
<hr />
<p>how do i fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-edges" rel="tag" title="see questions tagged &#39;edges&#39;">edges</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '14, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/54c570b1b5dcb86c33708fccc198bdbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob&#39;s gravatar image" />
<p><span>Rob</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '14, 14:40</strong> </span></p>
</div>
</div>
<div id="comments-container-34315" class="comments-container">
&#10;</div>
<div id="comment-tools-34315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34315-form-container" class="comment-form-container">
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

<span id="34355"></span>

<div id="answer-container-34355" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34355-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like an incompatibility was introduced when some of the functions where updated. I've committed something that should fix the problem although I've not completely tested it yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '14, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-34355" class="comments-container">
<span id="34356"></span>
<div id="comment-34356" class="comment">
<div id="post-34356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response, I've pulled the latest version and now the error is slightly different:</p>
<hr />
<p>UTC ERROR: function tigger_create_interpolation(geometry, unknown, unknown, unknown, unknown, unknown, unknown) does not exist at character 8</p>
<p>UTC HINT: No function matches the given name and argument types. You might need to add explicit type casts.</p>
<hr />
<p>EDIT:</p>
<p>when i ran the tigger_create_interpolation function manually i got errors about postgis .so files</p>
<p>i found a fix &gt; <a href="http://gis.stackexchange.com/questions/97871/postgis-2-1-error-after-update">http://gis.stackexchange.com/questions/97871/postgis-2-1-error-after-update</a></p>
<p>its rolling along importing now! :)</p>
</div>
<div id="comment-34356-info" class="comment-info">
<span class="comment-age">(26 Jun '14, 17:32)</span> <span class="comment-user userinfo">Rob</span>
</div>
</div>
</div>
<div id="comment-tools-34355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34355-form-container" class="comment-form-container">
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

