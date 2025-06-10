+++
type = "question"
title = "local Nominatim and R"
description = '''Hello, I need a batch geocoding server so I set up one in docker. But I need to do geocoding in R and package hrbrmstr/nominatim is mostly recommended for that. But it only provides the function for query to public OSM server. &#x27;Enable switching Nominatim API server providers&#x27; is on its TODO list and...'''
date = "2017-10-02T13:04:00Z"
lastmod = "2017-10-03T08:45:00Z"
weight = 59916
keywords = [ "r", "nominatim" ]
aliases = [ "/questions/59916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [local Nominatim and R](/questions/59916/local-nominatim-and-r)

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
<span id="post-59916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59916-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I need a batch geocoding server so I set up one in docker. But I need to do geocoding in <strong>R</strong> and package hrbrmstr/nominatim is mostly recommended for that. But it only provides the function for query to public OSM server. 'Enable switching Nominatim API server providers' is on its TODO list and the repo was updated two years ago. Is there any other solution for that. Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '17, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/7b5b9afd501c8b84fe1086ea959b4676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jimmy_Jin&#39;s gravatar image" />
<p><span>Jimmy_Jin</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jimmy_Jin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '17, 19:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-59916" class="comments-container">
&#10;</div>
<div id="comment-tools-59916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59916-form-container" class="comment-form-container">
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

<span id="59917"></span>

<div id="answer-container-59917" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59917-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've never so much as looked at R but I suspect the answer is fork <a href="https://github.com/hrbrmstr/nominatim">https://github.com/hrbrmstr/nominatim</a> in github, search your copy for references to "openstreetmap.org" and change them to point at your nominatim server.</p>
<p>Or have you tried that and it is more complicated than that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '17, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-59917" class="comments-container">
<span id="59920"></span>
<div id="comment-59920" class="comment">
<div id="post-59920-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>looks like there's a file specifying the querying URL</p>
</div>
<div id="comment-59920-info" class="comment-info">
<span class="comment-age">(02 Oct '17, 14:07)</span> <span class="comment-user userinfo">Jimmy_Jin</span>
</div>
</div>
<span id="59931"></span>
<div id="comment-59931" class="comment">
<div id="post-59931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, I've tried that. It the package has a dependency of Mapquest API which only requires a hash instead of a public URL. So by code hacking, it's not doable.</p>
</div>
<div id="comment-59931-info" class="comment-info">
<span class="comment-age">(03 Oct '17, 08:22)</span> <span class="comment-user userinfo">Jimmy_Jin</span>
</div>
</div>
<span id="59933"></span>
<div id="comment-59933" class="comment">
<div id="post-59933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Out of interest, which Mapquest API? I'd have thought that pretty much everything that Mapquest provide is available somewhere else (including self-hosted, but there may be practical reasons why that's not an option).</p>
</div>
<div id="comment-59933-info" class="comment-info">
<span class="comment-age">(03 Oct '17, 08:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59917-form-container" class="comment-form-container">
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

