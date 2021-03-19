+++
type = "question"
title = "Fuzzing - Wireshark Continuation or non-HTTP traffic (Regarding Buffer overflow)"
description = '''Hi, I am currently doing a test out of some security vulnerabilities, which the call fuzzing. As I am trying to figure out how to know where a web server is crashed from buffer overflow and its minimum bytes to crash it. So I used a Wireshark to view the traffic packet coming in and out.  After doin...'''
date = "2013-01-20T23:01:00Z"
lastmod = "2013-01-20T23:01:00Z"
weight = 17802
keywords = [ "buffer", "continuation", "wireshark" ]
aliases = [ "/questions/17802" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fuzzing - Wireshark Continuation or non-HTTP traffic (Regarding Buffer overflow)](/questions/17802/fuzzing-wireshark-continuation-or-non-http-traffic-regarding-buffer-overflow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17802-score" class="post-score" title="current number of votes">0</div><span id="post-17802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am currently doing a test out of some security vulnerabilities, which the call fuzzing. As I am trying to figure out how to know where a web server is crashed from buffer overflow and its minimum bytes to crash it. So I used a Wireshark to view the traffic packet coming in and out.</p><p>After doing the fuzzing technique, I obtain a result of this and I am not sure of which is the part that crash the server. And I do not know what does the 'Continuation or non-HTTP traffic' means, is it means that my server start crashes at that point? This is the result that shown in Wireshark:</p><pre><code>HTTP        | HEAD / AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
HTTP        | Continuation or non-HTTP traffic
HTTP        | HEAD /     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
HTTP        | Continuation or non-HTTP traffic
HTTP        | HEAD / AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
HTTP         | HEAD / AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</code></pre><p>So I would like to seek help/ assistance in this issue. Hope anyone could please help me up. Thanks x10. And sorry about the result above, as I do not know why I can't attach a image.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span> <span class="post-tag tag-link-continuation" rel="tag" title="see questions tagged &#39;continuation&#39;">continuation</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '13, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/1309e4e2ed0abf6edc49d4d6d066f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ebiz&#39;s gravatar image" /><p><span>ebiz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ebiz has no accepted answers">0%</span></p></div></div><div id="comments-container-17802" class="comments-container"></div><div id="comment-tools-17802" class="comment-tools"></div><div class="clear"></div><div id="comment-17802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

