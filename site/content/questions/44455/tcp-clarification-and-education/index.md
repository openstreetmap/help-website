+++
type = "question"
title = "[closed] TCP Clarification and Education"
description = '''All, I was analyzing a packet capture that a co-worker performed while he was troubleshooting a problem between a load balancer and a certificate server. For some reason the load balancer was having problems with the certificate revocation list. He fixed the problem by deleting and recreating the co...'''
date = "2015-07-24T15:09:00Z"
lastmod = "2015-07-24T15:09:00Z"
weight = 44455
keywords = [ "tcp" ]
aliases = [ "/questions/44455" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] TCP Clarification and Education](/questions/44455/tcp-clarification-and-education)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44455-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>I was analyzing a packet capture that a co-worker performed while he was troubleshooting a problem between a load balancer and a certificate server. For some reason the load balancer was having problems with the certificate revocation list. He fixed the problem by deleting and recreating the configuration in the load balancer.</p><p>Analyzing this capture is no longer needed to troubleshoot the original problem but the capture itself did raise some questions for me and I was hoping I could use this forum to teach me a few things and answer some specific questions I have about this capture.</p><p>The file can be viewed here. All my questions/observations are either in the file comments section or the packet comments section. <a href="https://www.dropbox.com/s/na2fytt0ez44nid/crl_anon.pcap?dl=0">https://www.dropbox.com/s/na2fytt0ez44nid/crl_anon.pcap?dl=0</a></p><p>Thank you in advance for any insight you can provide,</p><p>Bruno</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/03769b6187cefe87be2b755ce4b27e8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruno%20Wollmann&#39;s gravatar image" /><p>Bruno Wollmann<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruno Wollmann has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 25 Jul '15, 04:23</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-44455" class="comments-container"><span id="44466"></span><div id="comment-44466" class="comment"><div id="post-44466-score" class="comment-score"></div><div class="comment-text"><p>Answers can be found here, a forum it is not. Please refer to <a href="https://www.wireshark.org/mailman/listinfo/wireshark-users"><span class="__cf_email__" data-cfemail="ccbba5bea9bfa4adbea7e1b9bfa9bebf8cbba5bea9bfa4adbea7e2a3beab">[email protected]</span></a></p></div><div id="comment-44466-info" class="comment-info"><span class="comment-age">(25 Jul '15, 04:22)</span> Jaap ♦</div></div><span id="44472"></span><div id="comment-44472" class="comment"><div id="post-44472-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>Why did you close this question? I'm asking for help on a trace file which is the purpose of this website. Am I wrong?</p><p>Bruno</p></div><div id="comment-44472-info" class="comment-info"><span class="comment-age">(25 Jul '15, 08:18)</span> Bruno Wollmann</div></div><span id="44475"></span><div id="comment-44475" class="comment"><div id="post-44475-score" class="comment-score"></div><div class="comment-text"><p>You have to ask a question, not request general observations.</p></div><div id="comment-44475-info" class="comment-info"><span class="comment-age">(25 Jul '15, 08:59)</span> grahamb ♦</div></div><span id="44478"></span><div id="comment-44478" class="comment"><div id="post-44478-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the clarification. I do have specific questions about the trace and they are listed in the comments of the trace file but I realize that it is inconvenient to download a file to get at the questions.</p><p>I'll start another conversation with my specific questions.</p><p>Thanks</p></div><div id="comment-44478-info" class="comment-info"><span class="comment-age">(25 Jul '15, 10:22)</span> Bruno Wollmann</div></div><span id="44481"></span><div id="comment-44481" class="comment"><div id="post-44481-score" class="comment-score"></div><div class="comment-text"><p>Ideally one question per post, unless they really are related, otherwise all the partial answers become confusing.</p></div><div id="comment-44481-info" class="comment-info"><span class="comment-age">(25 Jul '15, 11:48)</span> grahamb ♦</div></div></div><div id="comment-tools-44455" class="comment-tools"></div><div class="clear"></div><div id="comment-44455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by Jaap 25 Jul '15, 04:23

</div>

</div>

</div>

