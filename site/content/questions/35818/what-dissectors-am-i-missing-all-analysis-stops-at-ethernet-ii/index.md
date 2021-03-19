+++
type = "question"
title = "What dissectors am I missing? All analysis stops at Ethernet II"
description = '''Noob question here. I wanted to see the performance difference between having all the dissectors turned on vs. only those for the protocols that I was interested in. I ran: tshark -r dump.pcap -qz io,phs  I can see the following protocols used: eth, ip, tcp, udp, icmp, igmp, arp. After adding all of...'''
date = "2014-08-27T13:31:00Z"
lastmod = "2014-08-28T08:54:00Z"
weight = 35818
keywords = [ "dissector", "tshark", "wireshark" ]
aliases = [ "/questions/35818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What dissectors am I missing? All analysis stops at Ethernet II](/questions/35818/what-dissectors-am-i-missing-all-analysis-stops-at-ethernet-ii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35818-score" class="post-score" title="current number of votes">0</div><span id="post-35818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Noob question here. I wanted to see the performance difference between having all the dissectors turned on vs. only those for the protocols that I was interested in. I ran:</p><pre><code>tshark -r dump.pcap -qz io,phs</code></pre><p>I can see the following protocols used: eth, ip, tcp, udp, icmp, igmp, arp. After adding all of these from the dissectors list I only get dissection up the the ethernet layer, for every packet, everything else it just treats as 'data'. What am I missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/5032e6783aeacbd305a38c0bb622b329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blackdragon1400&#39;s gravatar image" /><p><span>Blackdragon1400</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blackdragon1400 has no accepted answers">0%</span></p></div></div><div id="comments-container-35818" class="comments-container"></div><div id="comment-tools-35818" class="comment-tools"></div><div class="clear"></div><div id="comment-35818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35825"></span>

<div id="answer-container-35825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35825-score" class="post-score" title="current number of votes">0</div><span id="post-35825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What am I missing?</p></blockquote><p>ethertype ?</p><p>Enable all the protocols and then, for a random sample of frames in your capture, look (with wireshark) in the details pane under 'frame' at the generated field 'protocols in frame' to see the list of protocols in the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '14, 18:05</strong> </span></p></div></div><div id="comments-container-35825" class="comments-container"><span id="35843"></span><div id="comment-35843" class="comment"><div id="post-35843-score" class="comment-score"></div><div class="comment-text"><p>Ethertype was it, thanks for the help. Is there a tshark command that won't miss that?</p><p>Obviously I could use tshark -Tfields -e frame.protocols, but I'm just curious why -qz doesn't include it.</p></div><div id="comment-35843-info" class="comment-info"><span class="comment-age">(28 Aug '14, 08:34)</span> <span class="comment-user userinfo">Blackdragon1400</span></div></div><span id="35844"></span><div id="comment-35844" class="comment"><div id="post-35844-score" class="comment-score"></div><div class="comment-text"><p>I don't know....</p></div><div id="comment-35844-info" class="comment-info"><span class="comment-age">(28 Aug '14, 08:54)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-35825" class="comment-tools"></div><div class="clear"></div><div id="comment-35825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

