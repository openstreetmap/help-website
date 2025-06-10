+++
type = "question"
title = "Download a list of my GPX traces using API"
description = '''Hi I&#x27;m attempting to download a list of my GPX traces using the API call:  https://wiki.openstreetmap.org/wiki/API_v0.6#List:_GET_.2Fapi.2F0.6.2Fuser.2Fgpx_files curl -o my_gpx.xml -u DaveF:&#x27;password&#x27; https://www.openstreetmap.org/api/0.6/DaveF/gpx_files  This call returns a 404 error: &quot;Couldn&#x27;t fin...'''
date = "2021-07-03T15:48:00Z"
lastmod = "2021-07-03T21:48:00Z"
weight = 80813
keywords = [ "download", "api", "gpx" ]
aliases = [ "/questions/80813" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download a list of my GPX traces using API](/questions/80813/download-a-list-of-my-gpx-traces-using-api)

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
<span id="post-80813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80813-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'm attempting to download a list of my GPX traces using the API call:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/API_v0.6#List:_GET_.2Fapi.2F0.6.2Fuser.2Fgpx_files">https://wiki.openstreetmap.org/wiki/API_v0.6#List:_GET_.2Fapi.2F0.6.2Fuser.2Fgpx_files</a></p>
<pre><code>curl -o my_gpx.xml -u DaveF:&#39;password&#39; https://www.openstreetmap.org/api/0.6/DaveF/gpx_files</code></pre>
<p>This call returns a 404 error: "Couldn't find a file/directory/API operation by that name on the OpenStreetMap server (HTTP 404)"</p>
<p>I've successfully use a similar call to download a singular gpx file by its #id, so I have established a connection with the server. What am I missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '21, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '21, 17:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span></p>
</div>
</div>
<div id="comments-container-80813" class="comments-container">
&#10;</div>
<div id="comment-tools-80813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80813-form-container" class="comment-form-container">
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

<span id="80814"></span>

<div id="answer-container-80814" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80814-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Dave, the string "user" in the API URL is a literal, not to be subbed with the user name. Try;</p>
<pre><code>curl -o my_gpx.xml -u DaveF:PASSWORD_HERE https://www.openstreetmap.org/api/0.6/user/gpx_files</code></pre>
<p>I've updated the API docs for clarification.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '21, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-80814" class="comments-container">
<span id="80816"></span>
<div id="comment-80816" class="comment">
<div id="post-80816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ta. Is there away to get it sorted by timestamp? The file I get returned starts with the latest upload &amp; lists back to mid 2019 then jumps back to my first upload &amp; continues to that mid 2019 pint.</p>
<p>A lot could do with amending on OSM wiki pages. They should be written with the newbie to each topic in mind. Lots of real world examples to show how it's done &amp; less xml output.</p>
</div>
<div id="comment-80816-info" class="comment-info">
<span class="comment-age">(03 Jul '21, 18:57)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="80817"></span>
<div id="comment-80817" class="comment">
<div id="post-80817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>A lot could do with amending on OSM wiki pages</p>
</blockquote>
<p>Agreed - but if you've just managed to do something (after figuring out how the wiki page was wrong) I'd say that you are supremely qualified to do that!</p>
</div>
<div id="comment-80817-info" class="comment-info">
<span class="comment-age">(03 Jul '21, 19:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80818"></span>
<div id="comment-80818" class="comment">
<div id="post-80818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know of any way to request a sorted version of the GPX traces from the API. And I wouldn't assume the current semi-order will remain constant in the future either -- best to just treat the list as unordered and sort it clientside if needed.</p>
</div>
<div id="comment-80818-info" class="comment-info">
<span class="comment-age">(03 Jul '21, 21:48)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-80814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80814-form-container" class="comment-form-container">
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

