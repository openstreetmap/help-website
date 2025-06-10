+++
type = "question"
title = "IE11 no longer supported?"
description = '''Starting yesterday OSM no longer loads properly on IE11. The map as a whole does not load. I&#x27;m scouring the forums but can&#x27;t find anyone else posting this yet (I&#x27;m assuming IE11 isn&#x27;t used much anymore). Is it true that IE11 has been dropped from a list of supported browsers? The HTML console gives ...'''
date = "2021-12-01T08:45:00Z"
lastmod = "2021-12-01T10:13:00Z"
weight = 82720
keywords = [ "internet_explorer", "ie11" ]
aliases = [ "/questions/82720" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IE11 no longer supported?](/questions/82720/ie11-no-longer-supported)

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
<span id="post-82720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82720-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Starting yesterday OSM no longer loads properly on IE11. The map as a whole does not load. I'm scouring the forums but can't find anyone else posting this yet (I'm assuming IE11 isn't used much anymore).</p>
<p>Is it true that IE11 has been dropped from a list of supported browsers?</p>
<p>The HTML console gives the following error when opening the site in IE11:</p>
<p>SCRIPT1002: Syntaxiserror index-082bdf22ac1acb0b592af44c07db66f0510f4716d509dd00e3f126a4c4365396.js (8,249)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internet_explorer" rel="tag" title="see questions tagged &#39;internet_explorer&#39;">internet_explorer</span> <span class="post-tag tag-link-ie11" rel="tag" title="see questions tagged &#39;ie11&#39;">ie11</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '21, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/82e80b34ed01a65bd0b2ba8f5f603697?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RemyS&#39;s gravatar image" />
<p><span>RemyS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RemyS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82720" class="comments-container">
<span id="82722"></span>
<div id="comment-82722" class="comment">
<div id="post-82722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can confirm openstreetmap.org is not loading properly on IE11.</p>
<p>Just curious: Is there a particular reason why you want to use IE?</p>
</div>
<div id="comment-82722-info" class="comment-info">
<span class="comment-age">(01 Dec '21, 09:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="82723"></span>
<div id="comment-82723" class="comment">
<div id="post-82723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using IE11 out of necessity. It's running on shielded hardware that has no other browsers (yet). A request for Edge is pending but getting that on there will take a while, so I was wondering if there's perhaps a workaround to get OSM working on IE11 again</p>
</div>
<div id="comment-82723-info" class="comment-info">
<span class="comment-age">(01 Dec '21, 09:35)</span> <span class="comment-user userinfo">RemyS</span>
</div>
</div>
</div>
<div id="comment-tools-82720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82720-form-container" class="comment-form-container">
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

<span id="82724"></span>

<div id="answer-container-82724" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82724-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-82724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm one of the developers of the openstreetmap website. We haven't made any decisions to drop IE11 support (yet!), but at the same time, we don't have anyone testing it to ensure that it keeps working.</p>
<p>I would encourage you to file an issue at <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a> and we can deal with it from there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '21, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-82724" class="comments-container">
<span id="82725"></span>
<div id="comment-82725" class="comment">
<div id="post-82725-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for the swift response Andy, I've filed an issue: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/3387">https://github.com/openstreetmap/openstreetmap-website/issues/3387</a></p>
</div>
<div id="comment-82725-info" class="comment-info">
<span class="comment-age">(01 Dec '21, 10:13)</span> <span class="comment-user userinfo">RemyS</span>
</div>
</div>
</div>
<div id="comment-tools-82724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82724-form-container" class="comment-form-container">
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

