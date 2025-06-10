+++
type = "question"
title = "Error: you need to download the country_osm_grid first while building nominatim image"
description = '''http://www.nominatim.org/ is not working. I am trying to build docker image for nominatim. The build does not proceed until it downloads country grid data from nominatim.org but the website has not been working all day.  Is this a known issue? I am building nominatim image for the first time so I do...'''
date = "2021-07-02T07:32:00Z"
lastmod = "2021-07-02T09:04:00Z"
weight = 80792
keywords = [ "nominatim" ]
aliases = [ "/questions/80792" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error: you need to download the country_osm_grid first while building nominatim image](/questions/80792/error-you-need-to-download-the-country_osm_grid-first-while-building-nominatim-image)

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
<span id="post-80792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://www.nominatim.org/">http://www.nominatim.org/</a> is not working. I am trying to build docker image for nominatim. The build does not proceed until it downloads country grid data from nominatim.org but the website has not been working all day.</p>
<p>Is this a known issue? I am building nominatim image for the first time so I don't know if the website has been down for months but do anyone know workaround?</p>
<p>I tried to skip the command which download this data from dockerfile, and by doing so I can successfully create nominatim image but when I try to run container, I get this error <code>Error: you need to download the country_osm_grid first</code></p>
<p>so it seems I can't proceed further until I downlaod this data. Where can I download this?</p>
<p>the command in dockerfile is, <code>RUN curl </code><a href="https://www.nominatim.org/data/country_grid.sql.gz"><code>https://www.nominatim.org/data/country_grid.sql.gz</code></a><code> &gt; /app/src/data/country_osm_grid.sql.gz</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '21, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/93940bb3ab3199864cf7a447c51a78ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parth003&#39;s gravatar image" />
<p><span>parth003</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parth003 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80792" class="comments-container">
&#10;</div>
<div id="comment-tools-80792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80792-form-container" class="comment-form-container">
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

<span id="80797"></span>

<div id="answer-container-80797" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is resolved now. <a href="http://www.nominatim.org/">http://www.nominatim.org/</a> is back online.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '21, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/93940bb3ab3199864cf7a447c51a78ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parth003&#39;s gravatar image" />
<p><span>parth003</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parth003 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '21, 09:04</strong> </span></p>
</div>
</div>
<div id="comments-container-80797" class="comments-container">
&#10;</div>
<div id="comment-tools-80797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80797-form-container" class="comment-form-container">
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

