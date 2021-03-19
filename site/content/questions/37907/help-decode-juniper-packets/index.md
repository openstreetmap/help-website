+++
type = "question"
title = "Help decode Juniper packets"
description = '''Hello, I am trying to decode below type of packets. They&#x27;re captured on multicast service interface (mt-*), and after a proprietary header, it&#x27;s simple L3 data.  &amp;lt;-- Juniper header 0000 4d 47 43 83 00 16 03 01 0c 06 01 16 01 02 b4 00 MGC............. 0010 04 04 70 00 00 00 05 04 00 80 10 00 02 00...'''
date = "2014-11-17T10:59:00Z"
lastmod = "2014-11-17T11:16:00Z"
weight = 37907
keywords = [ "juniper", "wireshark" ]
aliases = [ "/questions/37907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help decode Juniper packets](/questions/37907/help-decode-juniper-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37907-score" class="post-score" title="current number of votes">0</div><span id="post-37907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to decode below type of packets. They're captured on multicast service interface (mt-*), and after a proprietary header, it's simple L3 data.</p><p><code> &lt;-- Juniper header 0000   4d 47 43 83 00 16 03 01 0c 06 01 16 01 02 b4 00  MGC............. 0010   04 04 70 00 00 00 05 04 00 80 10 00 02 00 00 00  ..p............. &lt;-- followed by L3 data (IP PIM Assert in this case) 0020   45 c0 00 2e 28 37 00 00 01 67 1d f2 a6 69 ec 09  E...(7...g...i.. 0030   e0 00 00 0d 25 00 f5 0b 01 00 00 20 e0 00 01 27  ....%...... ...' 0040   01 00 01 01 01 01 00 00 00 aa 00 00 00 00        ..............</code></p><p>There seem to be some work already done in this regards, as the first 4 bytes are defined in there: <code> #define JUNIPER_PCAP_MAGIC 0x4d4743</code></p><code></code><blockquote><p><code></code></p><p><code>http://anonsvn.wireshark.org/viewvc/trunk-1.8/epan/dissectors/packet-juniper.c?revision=43119&amp;view=markup</code></p></blockquote><p>Alternatively, I can convert the pcap to text, add a L2 header, and convert it back to pcap, but that is a cumbersome process.</p><p>Any other ideas how to decode those packets?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-juniper" rel="tag" title="see questions tagged &#39;juniper&#39;">juniper</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/487db3c76036a1afb3fa7a71f37211ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YLT&#39;s gravatar image" /><p><span>YLT</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YLT has no accepted answers">0%</span></p></div></div><div id="comments-container-37907" class="comments-container"></div><div id="comment-tools-37907" class="comment-tools"></div><div class="clear"></div><div id="comment-37907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37908"></span>

<div id="answer-container-37908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37908-score" class="post-score" title="current number of votes">0</div><span id="post-37908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try stripping the Juniper header using an "Edit" task in <a href="http://www.tracewrangler.com">TraceWrangler</a>, but so far I have only coded it to support doing that for packets with Ethernet headers following the Juniper header. I'll have to add code to be able to add a pseudo Ethernet header, but if this isn't urgent I could do it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37908" class="comments-container"></div><div id="comment-tools-37908" class="comment-tools"></div><div class="clear"></div><div id="comment-37908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

