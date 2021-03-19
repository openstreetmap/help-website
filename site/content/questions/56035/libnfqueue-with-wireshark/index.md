+++
type = "question"
title = "Libnfqueue with wireshark"
description = '''Hi,  I recently made changes to a dissector file: packets-ssl-utils.c . I added code which uses API calls from libnetfilter_queue. Sample code and api calls are here When I try to compile wireshark I face the following errors  make[2]: Entering directory &#x27;/home/machine/wireshark-2.0.4&#x27;  CXXLD wiresh...'''
date = "2016-09-30T18:01:00Z"
lastmod = "2016-09-30T18:01:00Z"
weight = 56035
keywords = [ "libraries", "compile", "wireshark-undefined", "make", "nfqueue" ]
aliases = [ "/questions/56035" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Libnfqueue with wireshark](/questions/56035/libnfqueue-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56035-score" class="post-score" title="current number of votes">0</div><span id="post-56035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I recently made changes to a dissector file: packets-ssl-utils.c . I added code which uses API calls from libnetfilter_queue. Sample code and api calls are <a href="https://home.regit.org/netfilter-en/using-nfqueue-and-libnetfilter_queue/">here</a></p><p>When I try to compile wireshark I face the following errors</p><pre><code>    make[2]: Entering directory &#39;/home/machine/wireshark-2.0.4&#39;
  CXXLD    wireshark
epan/.libs/libwireshark.so: undefined reference to `nfq_get_indev&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_create_queue&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_nfnlh&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_close&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_set_verdict&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_get_payload&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_set_mode&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_get_outdev&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_get_msg_packet_hdr&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_bind_pf&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_destroy_queue&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_open&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_unbind_pf&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_get_nfmark&#39;
epan/.libs/libwireshark.so: undefined reference to `nfq_handle_packet&#39;
epan/.libs/libwireshark.so: undefined reference to `nfnl_fd&#39;
collect2: error: ld returned 1 exit status</code></pre><p>The typical way to compile a file using libnetfitler_queue is</p><p>gcc -Wall -o test nfqnl_test.c -lnfnetlink -lnetfilter_queue</p><p>So I added -lnfnetlink -lnetfilter_queue to the CFLAGS in the make file of the epan directory. However I still am not able to compile the source code.</p><p>Can someone please guide me how to compile the project properly.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libraries" rel="tag" title="see questions tagged &#39;libraries&#39;">libraries</span> <span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-wireshark-undefined" rel="tag" title="see questions tagged &#39;wireshark-undefined&#39;">wireshark-undefined</span> <span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-nfqueue" rel="tag" title="see questions tagged &#39;nfqueue&#39;">nfqueue</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '16, 18:01</strong></p><img src="https://secure.gravatar.com/avatar/4cbb3f28051c110806a5f1beb0d93788?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhi93&#39;s gravatar image" /><p><span>Abhi93</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhi93 has no accepted answers">0%</span></p></div></div><div id="comments-container-56035" class="comments-container"></div><div id="comment-tools-56035" class="comment-tools"></div><div class="clear"></div><div id="comment-56035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

