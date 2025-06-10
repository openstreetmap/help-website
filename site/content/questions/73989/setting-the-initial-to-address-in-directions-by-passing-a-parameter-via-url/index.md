+++
type = "question"
title = "Setting the initial To-address in .../directions/ by passing a parameter via URL"
description = '''I would like to know how I can call https://www.openstreetmap.org/directions/ with a parameter so that the field To: is filled with a value. Is this possible?'''
date = "2020-04-03T12:55:00Z"
lastmod = "2020-04-06T08:03:00Z"
weight = 73989
keywords = [ "url", "parameter" ]
aliases = [ "/questions/73989" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Setting the initial To-address in .../directions/ by passing a parameter via URL](/questions/73989/setting-the-initial-to-address-in-directions-by-passing-a-parameter-via-url)

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
<span id="post-73989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to know how I can call <a href="https://www.openstreetmap.org/directions/">https://www.openstreetmap.org/directions/</a> with a parameter so that the field To: is filled with a value. Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-parameter" rel="tag" title="see questions tagged &#39;parameter&#39;">parameter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '20, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f51de73dca59b277693da03ad9b45c66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="normannescio&#39;s gravatar image" />
<p><span>normannescio</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="normannescio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73989" class="comments-container">
&#10;</div>
<div id="comment-tools-73989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73989-form-container" class="comment-form-container">
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

<span id="74005"></span>

<div id="answer-container-74005" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74005-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-74005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sure, it's easy, just add <strong><code>?to=[your destination]</code></strong> to the end of the URL.</p>
<p>Example: <a href="https://www.openstreetmap.org/directions?to=London">https://www.openstreetmap.org/directions?to=London</a></p>
<p>Note:</p>
<ul>
<li>The destination string is interpreted (by Nominatum I think) so what appears in the "To" box might not be an exact match. In this case "London" becomes "London, Greater London, England, SW1A 2DX, United Kingdom"</li>
<li>You can add more detail to the destination but you may have to URL-encode some characters, eg <a href="https://www.openstreetmap.org/directions?to=London%2C%20Ontario">https://www.openstreetmap.org/directions?to=London%2C%20Ontario</a> becomes "London, Ontario" which is interpreted as "London, Southwestern Ontario, Ontario, N6A 1G4, Canada."</li>
<li>You can also use coordinates as the destination -- but OSM will still attempt to guess an address, which sometimes succeeds and sometimes doesn't, eg <a href="https://www.openstreetmap.org/directions?to=51.4918%2C-0.1588">https://www.openstreetmap.org/directions?to=51.4918%2C-0.1588</a></li>
<li>If the user has visited openstreetmap.org before, the map will <em>not</em> automatically center on the destination. It will show wherever the user last was looking at OSM. If you want to control the map center and zoom, you can do so with additional URL parameters like this: <a href="https://www.openstreetmap.org/directions?to=London#map=10/51.4818/-0.1414">https://www.openstreetmap.org/directions?to=London#map=10/51.4818/-0.1414</a> (here, 10 is the zoom level, 51.4818 is the latitude, and -0.1414 is the longitude.)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '20, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '20, 04:04</strong> </span></p>
</div>
</div>
<div id="comments-container-74005" class="comments-container">
<span id="74020"></span>
<div id="comment-74020" class="comment">
<div id="post-74020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, works like a charm.</p>
</div>
<div id="comment-74020-info" class="comment-info">
<span class="comment-age">(06 Apr '20, 08:03)</span> <span class="comment-user userinfo">normannescio</span>
</div>
</div>
</div>
<div id="comment-tools-74005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74005-form-container" class="comment-form-container">
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

