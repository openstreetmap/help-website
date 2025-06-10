+++
type = "question"
title = "which POST request headers to use for OSM Basic Authentication?"
description = '''Hi, I have a problem with basic authentication in OSM. To upload gps traces it is required. So it would be great if someone can paste the headers with message body of &#x27;upload traces&#x27; POST request. Thanks in advance !'''
date = "2012-12-14T16:08:00Z"
lastmod = "2013-07-23T19:31:00Z"
weight = 18460
keywords = [ "basic_authentication", "api", "traces", "upload" ]
aliases = [ "/questions/18460" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [which POST request headers to use for OSM Basic Authentication?](/questions/18460/which-post-request-headers-to-use-for-osm-basic-authentication)

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
<span id="post-18460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18460-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a problem with basic authentication in OSM. To upload gps traces it is required.</p>
<p>So it would be great if someone can paste the headers with message body of 'upload traces' POST request.</p>
<p>Thanks in advance !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-basic_authentication" rel="tag" title="see questions tagged &#39;basic_authentication&#39;">basic_authentication</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '12, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/658670034a8466e9db4fb65067d310f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhima&#39;s gravatar image" />
<p><span>buddhima</span><br />
<span class="score" title="116 reputation points">116</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhima has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '13, 01:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-18460" class="comments-container">
<span id="18462"></span>
<div id="comment-18462" class="comment">
<div id="post-18462-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's easy to gather those information for yourself. Just get <a href="http://www.wireshark.org/">wireshark</a> or <a href="http://www.tcpdump.org/">tcpdump</a> and keep it running when uploading a trace. Then just identify the corresponding packet(s) and read their content. Alternatively read the code of one open source tool that is capable of GPS trace uploading.</p>
</div>
<div id="comment-18462-info" class="comment-info">
<span class="comment-age">(15 Dec '12, 09:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="18464"></span>
<div id="comment-18464" class="comment">
<div id="post-18464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Scai,</p>
<p>It's k Scai. But it would be great if someone can give the set of headers, because it would be useful for developers who are using OSM API and track the concept Basic Authentication.</p>
<p>Thanks !!!</p>
</div>
<div id="comment-18464-info" class="comment-info">
<span class="comment-age">(15 Dec '12, 11:53)</span> <span class="comment-user userinfo">buddhima</span>
</div>
</div>
</div>
<div id="comment-tools-18460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18460-form-container" class="comment-form-container">
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

<span id="24500"></span>

<div id="answer-container-24500" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24500-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You just follow instructions for <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Uploading_traces">API uploading traces</a>. The <a href="http://en.wikipedia.org/wiki/Basic_access_authentication">basic auth</a> (which is deprecated and you should use <a href="http://wiki.openstreetmap.org/wiki/OAuth">OAuth</a> instead) is trivially encoded into URL, for example using POST to "http://username:password@api.openstreetmap.org/"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '13, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-24500" class="comments-container">
&#10;</div>
<div id="comment-tools-24500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24500-form-container" class="comment-form-container">
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

