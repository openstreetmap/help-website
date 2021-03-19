+++
type = "question"
title = "HTTP traffic sniffing"
description = '''I have question about using Wireshark filter. I want to sniff HTTP traffic on destination IP for this case: in our company we have many computers and of course communication server (Microsoft server). All of computers are in domain! So, my question: have computers in domain higher level of security?...'''
date = "2013-02-28T00:53:00Z"
lastmod = "2013-02-28T01:38:00Z"
weight = 18963
keywords = [ "sniffing" ]
aliases = [ "/questions/18963" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP traffic sniffing](/questions/18963/http-traffic-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18963-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have question about using Wireshark filter. I want to sniff HTTP traffic on destination IP for this case: in our company we have many computers and of course communication server (Microsoft server). All of computers are in domain! So, my question: have computers in domain higher level of security?</p><p>I have try to sniff dest. ip, and as result get back only ARP packages. Then I try with this filter: (ip.dst == (com.serv.IP) &amp;&amp; ip.src == (client.IP)) &amp;&amp; http</p><p>(com.serv.IP) and (client.IP) are IP addresses of course.<br />
</p><p>Can somebody please help me, how to use filter to sniff HTTP traffic?<br />
</p></div><div id="question-tags" class="tags-container tags">sniffing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/8b042d12bf6ca8c844f67ce57005706a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ninja4it&#39;s gravatar image" /><p>ninja4it<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ninja4it has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '13, 00:57</p></div></div><div id="comments-container-18963" class="comments-container"></div><div id="comment-tools-18963" class="comment-tools"></div><div class="clear"></div><div id="comment-18963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18965"></span>

<div id="answer-container-18965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18965-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is likely to be your network architecture. Most networks these days are switched which means the switch will only route packets out of the switch port that are directed to the host on that port, along with broadcast packets which go to all hosts.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18965" class="comments-container"><span id="20502"></span><div id="comment-20502" class="comment"><div id="post-20502-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply!<br />
</p><p>So, we must change switch settings .... and what is important for http traffic?</p><p>I have just one quick question: Is this may be possible, because we have Proxy server?<br />
</p></div><div id="comment-20502-info" class="comment-info"><span class="comment-age">(17 Apr '13, 01:19)</span> ninja4it</div></div><span id="20505"></span><div id="comment-20505" class="comment"><div id="post-20505-score" class="comment-score"></div><div class="comment-text"><p>Assuming you're using Ethernet, then there are some suggestions on the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Capturing on Ethernet</a> wiki page on how to make your capture in a switched environment. You'll have to choose one of the options that is most suitable for your particular environment. If you tell us some more about your environment we may be able to offer appropriate suggestions.</p></div><div id="comment-20505-info" class="comment-info"><span class="comment-age">(17 Apr '13, 01:32)</span> grahamb ♦</div></div><span id="20534"></span><div id="comment-20534" class="comment"><div id="post-20534-score" class="comment-score"></div><div class="comment-text"><blockquote><p>because we have Proxy server?</p></blockquote><p>well, if you have a proxy server, why not capture on the proxy server itself?</p></div><div id="comment-20534-info" class="comment-info"><span class="comment-age">(17 Apr '13, 12:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18965" class="comment-tools"></div><div class="clear"></div><div id="comment-18965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

