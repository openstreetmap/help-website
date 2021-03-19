+++
type = "question"
title = "Question about opening netmon capture file with libpcap"
description = '''When open a netmon pcap file (file magic GMBU) with the following code snippet, got error message failed in function pcap_open_offline(): unknown file format  My code snippet:  libpcapHandler = pcap_open_offline(pcapFile, errbuf);  if(libpcapHandler == NULL) {  printf(&quot;failed in function pcap_open_o...'''
date = "2017-01-04T21:06:00Z"
lastmod = "2017-01-05T18:22:00Z"
weight = 58524
keywords = [ "libpcap" ]
aliases = [ "/questions/58524" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Question about opening netmon capture file with libpcap](/questions/58524/question-about-opening-netmon-capture-file-with-libpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58524-score" class="post-score" title="current number of votes">0</div><span id="post-58524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When open a netmon pcap file (file magic GMBU) with the following code snippet, got error message</p><pre><code>failed in function pcap_open_offline(): unknown file format</code></pre><p>My code snippet:</p><pre><code>    libpcapHandler = pcap_open_offline(pcapFile, errbuf);
    if(libpcapHandler == NULL) {
        printf(&quot;failed in function pcap_open_offline(): %s\n&quot;, errbuf);
        exit(1);
    }</code></pre><p>the libpcap library I used is libpcap.so.0.8. It's strange because wireshark 1.10.6 can open this pcap file even though it uses the libpcap too (according to "ldd" command). The OS here is ubuntu 14.04.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '17, 21:06</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '17, 11:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58524" class="comments-container"></div><div id="comment-tools-58524" class="comment-tools"></div><div class="clear"></div><div id="comment-58524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58529"></span>

<div id="answer-container-58529" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58529-score" class="post-score" title="current number of votes">3</div><span id="post-58529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You assume that libpcap is linked to Wireshark to open these capture files, but it's not. Wireshark uses another library, part of the Wireshark distribution, called wiretap to read all capture file formats. Originally the intend was to make it a super-libpcap, but only it's capture file reading capabilities were developed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '17, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58529" class="comments-container"><span id="58550"></span><div id="comment-58550" class="comment"><div id="post-58550-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap!</p></div><div id="comment-58550-info" class="comment-info"><span class="comment-age">(05 Jan '17, 18:22)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-58529" class="comment-tools"></div><div class="clear"></div><div id="comment-58529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

