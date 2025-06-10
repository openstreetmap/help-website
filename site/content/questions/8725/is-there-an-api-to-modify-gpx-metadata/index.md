+++
type = "question"
title = "Is there an API to modify GPX metadata?"
description = '''Hello I uploaded bunch of GPX traces using batch upload but I accidentally left visibility to PUBLIC instead of IDENTIFIABLE. I would like to use API to fix it, but I found nothing there about updating the metadata. I can do it on the webpage, but the list is too long. Is there some API-like way to ...'''
date = "2011-10-31T19:54:00Z"
lastmod = "2011-11-01T08:28:00Z"
weight = 8725
keywords = [ "modify", "api", "gpx" ]
aliases = [ "/questions/8725" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an API to modify GPX metadata?](/questions/8725/is-there-an-api-to-modify-gpx-metadata)

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
<span id="post-8725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8725-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I uploaded bunch of GPX traces using batch upload but I accidentally left visibility to PUBLIC instead of IDENTIFIABLE. I would like to use API to fix it, but I found nothing there about updating the metadata. I can do it on the webpage, but the list is too long. Is there some API-like way to do it?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-modify" rel="tag" title="see questions tagged &#39;modify&#39;">modify</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '11, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/45b708b160b691d79e08415f24642ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin&#39;s gravatar image" />
<p><span>Martin</span><br />
<span class="score" title="75 reputation points">75</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8725" class="comments-container">
&#10;</div>
<div id="comment-tools-8725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8725-form-container" class="comment-form-container">
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

<span id="8731"></span>

<div id="answer-container-8731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8731-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can update the metadata of the GPX trace via the API. Simply PUT the new details to <code>api/0.6/gpx/[id of trace]</code>. If you need to see the format of the XML required to do this, GET the same URL first.</p>
<p>To get a list of all the traces that you have uploaded already, then <code>GET /api/0.6/user/gpx_files</code></p>
<p>Some additional resources to help you are</p>
<ul>
<li><a href="http://git.openstreetmap.org/rails.git/blob/HEAD:/config/routes.rb#l62">The api routes available</a>, which I often use to find out this kind of thing</li>
<li><a href="http://wiki.openstreetmap.org/wiki/OAuth_ruby_examples">Examples of ruby scripts using OAuth</a>, which may be useful when you try writing to the API</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '11, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-8731" class="comments-container">
&#10;</div>
<div id="comment-tools-8731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8731-form-container" class="comment-form-container">
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

