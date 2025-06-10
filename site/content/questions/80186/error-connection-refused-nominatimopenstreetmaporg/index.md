+++
type = "question"
title = "Error connection refused nominatim.openstreetmap.org"
description = '''Hello! I recently started learning and using OSM. I used Java scrip with action &quot;oninput&quot; and I assume this caused the IP address to be blocked. I expect that it violated policy calls to the server. I used this query: var url = &quot;https://nominatim.openstreetmap.org/search?format=json&amp;amp;limit=3&amp;amp;...'''
date = "2021-05-14T18:23:00Z"
lastmod = "2021-05-14T18:54:00Z"
weight = 80186
keywords = [ "refused" ]
aliases = [ "/questions/80186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error connection refused nominatim.openstreetmap.org](/questions/80186/error-connection-refused-nominatimopenstreetmaporg)

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
<span id="post-80186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80186-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I recently started learning and using OSM. I used Java scrip with action "oninput" and I assume this caused the IP address to be blocked. I expect that it violated policy calls to the server. I used this query: var url = "https://nominatim.openstreetmap.org/search?format=json&amp;limit=3&amp;q=" + inp.value; xmlhttp.open ("GET", url, true); Could you please help how can I unblock my IP?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-refused" rel="tag" title="see questions tagged &#39;refused&#39;">refused</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '21, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a9e42aa8990df03a1ffc0f9dabce7f24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Enzo37&#39;s gravatar image" />
<p><span>Enzo37</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Enzo37 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80186" class="comments-container">
&#10;</div>
<div id="comment-tools-80186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80186-form-container" class="comment-form-container">
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

<span id="80187"></span>

<div id="answer-container-80187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80187-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the <a href="https://operations.osmfoundation.org/policies/nominatim/">Nominatim usage policy</a> clearly says that:</p>
<p>"The following uses are strictly forbidden and will get you banned: ... Auto-complete search This is not yet supported by Nominatim and you must not implement such a service on the client side using the API."</p>
<p>By sending a query every time a key was pressed, you have violated this rule. If you have not done this in an egregious fashion then your IP block will be lifted after a while automatically. You can use the time until then to read the policy ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '21, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80187" class="comments-container">
<span id="80188"></span>
<div id="comment-80188" class="comment">
<div id="post-80188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for explanation. I have already become acquainted with politics:) IP was blocked more than 2 hours ago, could you please tell how long the IP will be blocked? My IP 62.140.252.35</p>
<p>Thanks.</p>
</div>
<div id="comment-80188-info" class="comment-info">
<span class="comment-age">(14 May '21, 18:54)</span> <span class="comment-user userinfo">Enzo37</span>
</div>
</div>
</div>
<div id="comment-tools-80187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80187-form-container" class="comment-form-container">
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

