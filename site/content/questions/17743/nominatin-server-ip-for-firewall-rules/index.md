+++
type = "question"
title = "Nominatin Server Ip for Firewall rules"
description = '''Hello, We currently would like to use this service but the server is behind a firewall. We can open a connection to a specific IP address and I&#x27;m wondering if the IP for the service is static or not? or if there is a range I can add to ensure it works properly. currently I am able to find: Nominatim...'''
date = "2012-11-16T09:55:00Z"
lastmod = "2012-12-05T10:39:00Z"
weight = 17743
keywords = [ "nominatim", "server" ]
aliases = [ "/questions/17743" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatin Server Ip for Firewall rules](/questions/17743/nominatin-server-ip-for-firewall-rules)

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
<span id="post-17743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We currently would like to use this service but the server is behind a firewall. We can open a connection to a specific IP address and I'm wondering if the IP for the service is static or not? or if there is a range I can add to ensure it works properly.</p>
<p>currently I am able to find:</p>
<p>Nominatim</p>
<pre><code>128.40.168.106</code></pre>
<p>openstreetmap.org</p>
<pre><code>Address: 193.63.75.99
Address: 193.63.75.100
Address: 193.63.75.103</code></pre>
<p>Cheers for any info</p>
<p>Mart</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '12, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/5783e50b5b746a9727dcb7d0ddc90253?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mart&#39;s gravatar image" />
<p><span>Mart</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mart has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17743" class="comments-container">
<span id="17744"></span>
<div id="comment-17744" class="comment">
<div id="post-17744-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain what you're trying to do that needs a fixed IP address?</p>
</div>
<div id="comment-17744-info" class="comment-info">
<span class="comment-age">(16 Nov '12, 10:05)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="17745"></span>
<div id="comment-17745" class="comment">
<div id="post-17745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, our web application will geocode an address and then return that to the user. but for the server to do this we need to open the firewall from our server to the nominatim.openstreetmap.org. The firewall is annoying can only handle IP addresses. so if the nominatim is fairly static then we can add it, or if theres a range we can add the whole range. hope that makes sense.</p>
<p>Cheers</p>
</div>
<div id="comment-17745-info" class="comment-info">
<span class="comment-age">(16 Nov '12, 10:12)</span> <span class="comment-user userinfo">Mart</span>
</div>
</div>
</div>
<div id="comment-tools-17743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17743-form-container" class="comment-form-container">
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

<span id="18203"></span>

<div id="answer-container-18203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap currently uses the following IP address ranges:</p>
<ul>
<li>128.40.168.64/26 (UCL)</li>
<li>193.63.75.96/27 (Imperial)</li>
<li>89.16.179.150 (Bytemark)</li>
</ul>
<p>We also have a few distributed "CDN" tile.openstreetmap.org servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '12, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-18203" class="comments-container">
&#10;</div>
<div id="comment-tools-18203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18203-form-container" class="comment-form-container">
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

