+++
type = "question"
title = "Can I download a subset of data into JOSM?"
description = '''I have read the question and answer for &quot;Can I download only a subset of data in JOSM?&quot; and have tried to do what is suggested. When I want to download a location by using a url as mentioned, JOSM gives me an error &quot;Failed to open a connection to the remote server &#x27;https://api.openstreetmap.org/api/...'''
date = "2015-07-01T17:00:00Z"
lastmod = "2015-07-02T12:25:00Z"
weight = 43887
keywords = [ "josm", "filtering" ]
aliases = [ "/questions/43887" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I download a subset of data into JOSM?](/questions/43887/can-i-download-a-subset-of-data-into-josm)

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
<span id="post-43887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have read the question and answer for "Can I download only a subset of data in JOSM?" and have tried to do what is suggested. When I want to download a location by using a url as mentioned, JOSM gives me an error "Failed to open a connection to the remote server 'https://api.openstreetmap.org/api/0.6/'. Host name 'api.openstreetmap.org' could not be resolved. Please check the API URL in your preferences and your internet connection.". This error message is the first mentioned when I refer to the help button, but to resolve it says I should check the url and make sure my preferences are set to the api.openstreetmap.org url which is what it was. Any help will be very much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '15, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/19fd6c1499513907697c5821829c5e83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BmanS&#39;s gravatar image" />
<p><span>BmanS</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BmanS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43887" class="comments-container">
<span id="43901"></span>
<div id="comment-43901" class="comment">
<div id="post-43901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please share some details what you did?</p>
</div>
<div id="comment-43901-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 06:29)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="43902"></span>
<div id="comment-43902" class="comment">
<div id="post-43902-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you try the URL <a href="https://api.openstreetmap.org/api/0.6/">https://api.openstreetmap.org/api/0.6/</a> in a browser ? Does that work ? Does your browser use a proxy to go through a firewall and access the internet ? If so, you should configure that same proxy in JOSM.</p>
</div>
<div id="comment-43902-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 07:31)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="43914"></span>
<div id="comment-43914" class="comment">
<div id="post-43914-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I try the URL it gives me this error, "Couldn't find a file/directory/API operation by that name on the OpenStreetMap server (HTTP 404)". which I believe is normal</p>
</div>
<div id="comment-43914-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 10:49)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="43917"></span>
<div id="comment-43917" class="comment">
<div id="post-43917-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>(just in case of confusion) <a href="https://api.openstreetmap.org/api/0.6/">https://api.openstreetmap.org/api/0.6/</a> is expected not to give anything other than "Couldn't find a file/directory/API operation by that name on the OpenStreetMap server (HTTP 404)".</p>
<p>However if you try a request that's supposed to work, such as <a href="http://api.openstreetmap.org/api/0.6/changeset/32344153">http://api.openstreetmap.org/api/0.6/changeset/32344153</a> , you should get some valid data.</p>
</div>
<div id="comment-43917-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 12:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43887-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

