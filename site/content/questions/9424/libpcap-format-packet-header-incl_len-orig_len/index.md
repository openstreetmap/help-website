+++
type = "question"
title = "libpcap format - packet header - incl_len / orig_len"
description = '''The libpcap packet header structure has 2 length fields: typedef struct pcaprec_hdr_s {  guint32 ts_sec; /* timestamp seconds */  guint32 ts_usec; /* timestamp microseconds */  guint32 incl_len; /* number of octets of packet saved in file */  guint32 orig_len; /* actual length of packet */ } pcaprec...'''
date = "2012-03-07T21:17:00Z"
lastmod = "2012-03-07T22:21:00Z"
weight = 9424
keywords = [ "header", "libpcap" ]
aliases = [ "/questions/9424" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [libpcap format - packet header - incl\_len / orig\_len](/questions/9424/libpcap-format-packet-header-incl_len-orig_len)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9424-score" class="post-score" title="current number of votes">0</div><span id="post-9424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The libpcap packet header structure has 2 length fields:</p><pre><code>typedef struct pcaprec_hdr_s {
        guint32 ts_sec;         /* timestamp seconds */
        guint32 ts_usec;        /* timestamp microseconds */
        guint32 incl_len;       /* number of octets of packet saved in file */
        guint32 orig_len;       /* actual length of packet */
} pcaprec_hdr_t;</code></pre><p><strong>incl_len</strong>: the number of bytes of packet data actually captured and saved in the file. This value should never become larger than orig_len or the snaplen value of the global header.</p><p><strong>orig_len</strong>: the length of the packet as it appeared on the network when it was captured. If incl_len and orig_len differ, the actually saved packet size was limited by snaplen.</p><p>Can any one tell me what is the difference between the 2 length fields? We are saving the packet in entirely then how can the 2 differ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '12, 21:17</strong></p><img src="https://secure.gravatar.com/avatar/83e04f89cabcf71f8efd2238a88905ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v%20j&#39;s gravatar image" /><p><span>v j</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v j has no accepted answers">0%</span></p></div></div><div id="comments-container-9424" class="comments-container"></div><div id="comment-tools-9424" class="comment-tools"></div><div class="clear"></div><div id="comment-9424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9425"></span>

<div id="answer-container-9425" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9425-score" class="post-score" title="current number of votes">1</div><span id="post-9425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="v j has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are capturing the entire packet they do not differ, but if yo have specified that only 96 bytes of each packet should be saved(snap lenght) then incl_lenght will be 96 and orig_len the actual lenght of the packets which makes it possible for a program reading the file to "know" that bytes are "missing".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '12, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-9425" class="comments-container"><span id="9426"></span><div id="comment-9426" class="comment"><div id="post-9426-score" class="comment-score"></div><div class="comment-text"><p>I am trying to capture TinyOS (telosb mote) packets in wireshark. Wireshark doesnt support direct capture from telosb motes so i am writing a application that fetches the packets and writes to a capture file in pcap format. The problem is the received packets are in TINYOS format so I need to create a 802.15.4 packet from it. I have used the structure Ieee802154_packet (from wirshark) to create the packet and write to the file. Here incl/cap len should be the size of Ieee802154_packet struct? Please correct me if I am wrong.</p></div><div id="comment-9426-info" class="comment-info"><span class="comment-age">(07 Mar '12, 22:21)</span> <span class="comment-user userinfo">v j</span></div></div></div><div id="comment-tools-9425" class="comment-tools"></div><div class="clear"></div><div id="comment-9425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

