+++
type = "question"
title = "decrypt ssl from remote interface"
description = '''1 How can I decrypt https from remote interface (rpcap)? I run rpcapd on my router. I use premaster keys but they work only if i run wireshark with local interface 2 It seems dumpcap with rpcap interface is working only in windows. Ubuntu says &quot;ioctl failed: No such device&quot; Thank you'''
date = "2016-10-08T13:51:00Z"
lastmod = "2016-10-08T14:18:00Z"
weight = 56239
keywords = [ "ssl", "rpcap" ]
aliases = [ "/questions/56239" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decrypt ssl from remote interface](/questions/56239/decrypt-ssl-from-remote-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56239-score" class="post-score" title="current number of votes">0</div><span id="post-56239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1 How can I decrypt https from remote interface (rpcap)? I run rpcapd on my router. I use premaster keys but they work only if i run wireshark with local interface</p><p>2 It seems dumpcap with rpcap interface is working only in windows. Ubuntu says "ioctl failed: No such device"</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '16, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/af2e0eb5ddc88d69a09b22cad46f2460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="l0pan&#39;s gravatar image" /><p><span>l0pan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="l0pan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Oct '16, 13:54</strong> </span></p></div></div><div id="comments-container-56239" class="comments-container"><span id="56240"></span><div id="comment-56240" class="comment"><div id="post-56240-score" class="comment-score"></div><div class="comment-text"><p>If the remote device can run tcpdump, then have a look at the extcap sshdump interface in the latest development versions.</p><p>This allows running tcpdump on a remote system via ssh.</p></div><div id="comment-56240-info" class="comment-info"><span class="comment-age">(08 Oct '16, 14:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56241"></span><div id="comment-56241" class="comment"><div id="post-56241-score" class="comment-score"></div><div class="comment-text"><p>i tried capturing with tcpdump on my router too, but i also get "decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available" Is it theoretical possible to decrypt HTTPS captured on router with premaster keys from local PC?</p></div><div id="comment-56241-info" class="comment-info"><span class="comment-age">(08 Oct '16, 14:18)</span> <span class="comment-user userinfo">l0pan</span></div></div></div><div id="comment-tools-56239" class="comment-tools"></div><div class="clear"></div><div id="comment-56239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

