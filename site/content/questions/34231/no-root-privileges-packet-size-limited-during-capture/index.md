+++
type = "question"
title = "No root privileges: Packet size limited during capture"
description = '''Hi all, I&#x27;m using Wireshark 1.0.15 to capture and dissect a custom protocol. I tried to capture these packets with both tcpdump ... -s 0 and through the GUI (unchecking the limit packet size box). When I run: sudo wireshark -r ~/Desktop/capture.pcap  I dissect the packet to great success. The packet...'''
date = "2014-06-26T10:31:00Z"
lastmod = "2014-08-25T13:38:00Z"
weight = 34231
keywords = [ "capture", "dissector", "tcpdump", "tcp", "packet" ]
aliases = [ "/questions/34231" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [No root privileges: Packet size limited during capture](/questions/34231/no-root-privileges-packet-size-limited-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34231-score" class="post-score" title="current number of votes">0</div><span id="post-34231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm using Wireshark 1.0.15 to capture and dissect a custom protocol. I tried to capture these packets with both tcpdump ... -s 0 and through the GUI (unchecking the limit packet size box). When I run:</p><pre><code>sudo wireshark -r ~/Desktop/capture.pcap</code></pre><p>I dissect the packet to great success. The packet is approximately 50K bytes when reassembled using tcp_dissect_pdus. However, when I run it without root privileges, I get:</p><pre><code>[Packet size limited during capture: XXX truncated]</code></pre><p>I can see the header has been successfully dissected, since it gives me the same info as when I run it as root. However, the rest of the packets show the error mentioned above.</p><p>What am I doing wrong? Am I capturing it wrong or is there a bug in my code? Or is it because of how Wireshark is set up on my system?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '14, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/7781069f122c3b3eef20438565e7e36f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barney&#39;s gravatar image" /><p><span>barney</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barney has one accepted answer">100%</span></p></div></div><div id="comments-container-34231" class="comments-container"><span id="34262"></span><div id="comment-34262" class="comment"><div id="post-34262-score" class="comment-score"></div><div class="comment-text"><p>What is your</p><ul><li>OS and OS version</li></ul><p>Can you post a sample capture file at googgle drive, dropbox or cloudshark.org?</p></div><div id="comment-34262-info" class="comment-info"><span class="comment-age">(28 Jun '14, 15:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34298"></span><div id="comment-34298" class="comment"><div id="post-34298-score" class="comment-score"></div><div class="comment-text"><p>Here's a sample capture that exhibits this problem:</p><p><a href="https://www.dropbox.com/s/r9ehpjs5d8lwpgr/askwireshark">https://www.dropbox.com/s/r9ehpjs5d8lwpgr/askwireshark</a></p><p>I'm running Red Hat Enterprise Linux 5.</p></div><div id="comment-34298-info" class="comment-info"><span class="comment-age">(30 Jun '14, 13:05)</span> <span class="comment-user userinfo">barney</span></div></div><span id="34325"></span><div id="comment-34325" class="comment"><div id="post-34325-score" class="comment-score"></div><div class="comment-text"><p>I don't seem to have the same problem in Wireshark 1.6.7/Ubuntu. I'm having trouble building the same version (1.0.15) on 12.04 though so it's hard to say if it's the OS or the Wireshark version.</p></div><div id="comment-34325-info" class="comment-info"><span class="comment-age">(01 Jul '14, 11:22)</span> <span class="comment-user userinfo">barney</span></div></div><span id="35716"></span><div id="comment-35716" class="comment"><div id="post-35716-score" class="comment-score"></div><div class="comment-text"><p>What's printed if you type</p><pre><code>which wireshark</code></pre><p>and if you type</p><pre><code>sudo which wireshark</code></pre></div><div id="comment-35716-info" class="comment-info"><span class="comment-age">(25 Aug '14, 11:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35725"></span><div id="comment-35725" class="comment"><div id="post-35725-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I can't answer that since I don't have access to the machine anymore. If it helps, I installed it on RHEL 5.4 with the wireshark-gnome package.</p><p>I forgot to follow up here, but the problem went away I disabled TCP Checksum Validation. After some really basic research, it seemed that the TCP offloading was a plausible cause.</p></div><div id="comment-35725-info" class="comment-info"><span class="comment-age">(25 Aug '14, 13:38)</span> <span class="comment-user userinfo">barney</span></div></div></div><div id="comment-tools-34231" class="comment-tools"></div><div class="clear"></div><div id="comment-34231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34328"></span>

<div id="answer-container-34328" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34328-score" class="post-score" title="current number of votes">1</div><span id="post-34328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="barney has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Or is it because of how Wireshark is set up on my system?</p></blockquote><p>It might be. If, when running Wireshark as root, it uses root's preferences, which have TCP checksum validation turned off, but, when running it as yourself, it uses your preferences, which have TCP checksum validation turned on, then some packets will get errors because they have invalid checksums (which, as the message Wireshark displays in that case says, may be due to TCP checksum offloading - that will cause packets sent by the machine running a packet sniffer to, when captured by that sniffer, have an invalid TCP checksum, because the checksum is set on the NIC, and the packets seen by a sniffer are the packets as handed to the NIC), and that may disable TCP reassembly.</p><p>"Packet size limited during capture: XXX truncated" <em>should</em> only be reported if a snapshot length was specified, but there might be a Wireshark bug causing it to be reported for non-reassembled packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '14, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34328" class="comments-container"></div><div id="comment-tools-34328" class="comment-tools"></div><div class="clear"></div><div id="comment-34328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

