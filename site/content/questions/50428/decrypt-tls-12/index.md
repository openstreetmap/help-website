+++
type = "question"
title = "decrypt Tls 1.2"
description = '''Hello all, I&#x27;m not able to decrypt TLS 1.2, ciper suite is TLS_RSA_WITH_AES_128_GCM_SHA256. dissect_ssl enter frame #2 (first time) association_find: TCP port 18819 found 0000000000000000 packet_from_server: is from server - FALSE  conversation = 0000000008081160, ssl_session = 0000000008081670  rec...'''
date = "2016-02-23T03:37:00Z"
lastmod = "2016-03-31T09:26:00Z"
weight = 50428
keywords = [ "tls", "decrypt" ]
aliases = [ "/questions/50428" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [decrypt Tls 1.2](/questions/50428/decrypt-tls-12)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50428-score" class="post-score" title="current number of votes">0</div><span id="post-50428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I'm not able to decrypt TLS 1.2, ciper suite is <code>TLS_RSA_WITH_AES_128_GCM_SHA256</code>.</p><pre><code>dissect_ssl enter frame #2 (first time)
association_find: TCP port 18819 found 0000000000000000
packet_from_server: is from server - FALSE
  conversation = 0000000008081160, ssl_session = 0000000008081670
  record: offset = 0, reported_length_remaining = 419
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 414, ssl state 0x10
association_find: TCP port 18819 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 18819 found 0000000000000000
association_find: TCP port 443 found 00000000065E8230

dissect_ssl enter frame #4 (first time)
association_find: TCP port 443 found 00000000065E8230
packet_from_server: is from server - TRUE
  conversation = 0000000008081160, ssl_session = 0000000008081670
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 608, ssl state 0x10
association_find: TCP port 443 found 00000000065E8230
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre><p>Any idea what is the issue ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/42aa3df21b57a5414773b4d29aaa1ad6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeril&#39;s gravatar image" /><p><span>jeril</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeril has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '16, 05:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50428" class="comments-container"></div><div id="comment-tools-50428" class="comment-tools"></div><div class="clear"></div><div id="comment-50428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51314"></span>

<div id="answer-container-51314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51314-score" class="post-score" title="current number of votes">0</div><span id="post-51314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not an answer but I have the same problem with both WireShark 2.0.2 and 1.99.9</p><p>Bob Wilson</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/de4c367e6f65c0c2a4a5c8947aa3abff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwilson4web&#39;s gravatar image" /><p><span>bwilson4web</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwilson4web has no accepted answers">0%</span></p></div></div><div id="comments-container-51314" class="comments-container"></div><div id="comment-tools-51314" class="comment-tools"></div><div class="clear"></div><div id="comment-51314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

