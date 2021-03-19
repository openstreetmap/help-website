+++
type = "question"
title = "How to filter packets with BPF in a C program when they&#x27;re not read from a live capture or pcap/pcap-ng file?"
description = '''I am developing a component of a software on processing packets. The input comes as a pointer to an array of packets (each packet is a struct, with a field for pointer to packet data and a field for packet len). How would I use BPF rule to help me skip some packets, it will greatly reduce the proces...'''
date = "2015-07-31T07:27:00Z"
lastmod = "2015-07-31T15:23:00Z"
weight = 44689
keywords = [ "filter", "libpcap", "bpf" ]
aliases = [ "/questions/44689" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter packets with BPF in a C program when they're not read from a live capture or pcap/pcap-ng file?](/questions/44689/how-to-filter-packets-with-bpf-in-a-c-program-when-theyre-not-read-from-a-live-capture-or-pcappcap-ng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44689-score" class="post-score" title="current number of votes">0</div><span id="post-44689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a component of a software on processing packets. The input comes as a pointer to an array of packets (each packet is a struct, with a field for pointer to packet data and a field for packet len). How would I use BPF rule to help me skip some packets, it will greatly reduce the processing time since I don't need to waste time on packets that are not useful.</p><p>I know libpcap will allow this, but it assume the input is is a file in the form of pcap format.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-bpf" rel="tag" title="see questions tagged &#39;bpf&#39;">bpf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '15, 16:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44689" class="comments-container"></div><div id="comment-tools-44689" class="comment-tools"></div><div class="clear"></div><div id="comment-44689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44700"></span>

<div id="answer-container-44700" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44700-score" class="post-score" title="current number of votes">2</div><span id="post-44700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>pcap_open_dead()</code> to get a <code>pcap_t *</code> with whatever the appropriate DLT_ value is for the packet data.</p><p>Use <code>pcap_compile()</code> to compile your filter into BPF code, if you haven't hand-written a BPF program.</p><p>For each packet, construct a <code>struct pcap_pkthdr</code> (you don't need to give it a time stamp, as the filter doesn't look at that, and use the packet length for both the captured length and the on-the-network length), and use <code>pcap_offline_filter()</code> to run the filter against the packet (or, if you have an older version of libpcap that doesn't have <code>pcap_offline_filter()</code>, directly call <code>bpf_filter()</code>, which is in libpcap).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '15, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44700" class="comments-container"><span id="44711"></span><div id="comment-44711" class="comment"><div id="post-44711-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Guy! Really helpful. Wish I can vote you up multiple times.</p></div><div id="comment-44711-info" class="comment-info"><span class="comment-age">(31 Jul '15, 15:23)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-44700" class="comment-tools"></div><div class="clear"></div><div id="comment-44700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

