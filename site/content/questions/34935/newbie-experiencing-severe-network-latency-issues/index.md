+++
type = "question"
title = "Newbie - experiencing severe network latency issues"
description = '''Hello, experiencing severe network latency issues. I&#x27;m not a network administrator but rather systems admin, and ERP admin.  Info:  - network is strictly IPv4, with one DHCP server running on W2K8 R2 server;  - 4 Netgear switches on the LAN (2 x GSM7248, 1 x GSM7248R, 1 x FS750T2);  - ran an 11 seco...'''
date = "2014-07-27T19:51:00Z"
lastmod = "2014-07-29T01:46:00Z"
weight = 34935
keywords = [ "latency", "network" ]
aliases = [ "/questions/34935" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie - experiencing severe network latency issues](/questions/34935/newbie-experiencing-severe-network-latency-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34935-score" class="post-score" title="current number of votes">0</div><span id="post-34935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, experiencing severe network latency issues. I'm not a network administrator but rather systems admin, and ERP admin.<br />
</p><p>Info: - network is strictly IPv4, with one DHCP server running on W2K8 R2 server; - 4 Netgear switches on the LAN (2 x GSM7248, 1 x GSM7248R, 1 x FS750T2); - ran an 11 second wireshark capture on the LAN from a W2K8 server</p><p>Does it seem strange that there's a crazy amount of IPv6 traffic?<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wshark.JPG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/wshark2.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '14, 19:51</strong></p><img src="https://secure.gravatar.com/avatar/bbe1f3ac2df917c217e1a952b87a8a55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buefordTJ&#39;s gravatar image" /><p><span>buefordTJ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buefordTJ has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-34935" class="comments-container"><span id="34937"></span><div id="comment-34937" class="comment"><div id="post-34937-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Does it seem strange that there's a crazy amount of IPv6 traffic?</p></blockquote><p>no, as IPV6 is enabled by default on Windows &gt;= Vista.</p><p>But besides that IPv6 question. What is your question regarding the <strong>severe</strong> network latency issue?</p></div><div id="comment-34937-info" class="comment-info"><span class="comment-age">(27 Jul '14, 20:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34950"></span><div id="comment-34950" class="comment"><div id="post-34950-score" class="comment-score"></div><div class="comment-text"><p>IPv6 itself being enabled isn't odd, but for a 11 second trace that's about 280 Kbps and 3200 pps of IPv6 payload to the server, which <em>is</em> kind of odd if you're not intending to use that stack at all.</p><p>bueford, what is being carried in those packets (eg: TCP/UDP port number if it is one of those)? What is the response (the two other MACs look like they're load-balancing the other direction)?</p><p>There's really not a lot to go on here in diagnosing why the network is slow but if you can upload the actual packet capture that might be helpful also (<a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> )</p></div><div id="comment-34950-info" class="comment-info"><span class="comment-age">(28 Jul '14, 17:41)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-34935" class="comment-tools"></div><div class="clear"></div><div id="comment-34935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34952"></span>

<div id="answer-container-34952" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34952-score" class="post-score" title="current number of votes">0</div><span id="post-34952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Kurt, it just seems like there are way too many IPv6 packets being sent out, the result being the entire network slows down, our ERP system reponsiveness slows to a snails pace, wireless connections are dropped.<br />
</p><p>Quadratic, i've uploaded a subset of those IPv6 packets to <a href="https://www.cloudshark.org/captures/4cc4188f573d">https://www.cloudshark.org/captures/4cc4188f573d</a></p><p>I think i might have found the source of the problem. Googling the same symptoms i found this thread <a href="https://communities.intel.com/thread/48051">https://communities.intel.com/thread/48051</a> Seems like there is a known issue with Intel I217-LM network cards. When the PC went to sleep these cards would flood the network with IPv6 mutlicast traffic. 4 weeks ago we just purchased 5 Lenovo desktops to replace some old XP workstations and yes, they all had the same Intel I217-LM network card. Upgraded the firmware today and the PCs have been "asleep" since 5:00PM ... no sign of the IPv6 flood so far. Keeping fingers crossed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '14, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/bbe1f3ac2df917c217e1a952b87a8a55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buefordTJ&#39;s gravatar image" /><p><span>buefordTJ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buefordTJ has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-34952" class="comments-container"><span id="34953"></span><div id="comment-34953" class="comment"><div id="post-34953-score" class="comment-score"></div><div class="comment-text"><p>Ah, that makes sense. One suggestion though - disable the IPv6 protocol stack altogether on these machines if you have no use-case for it. Unused protocols on the network only add to the noise, take up bandwidth and in some cases increase the network's attack surface unneccessarily.</p></div><div id="comment-34953-info" class="comment-info"><span class="comment-age">(28 Jul '14, 20:37)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="34963"></span><div id="comment-34963" class="comment"><div id="post-34963-score" class="comment-score"></div><div class="comment-text"><p>FWIW, Microsoft do not recommend disabling IPv6. See their IPv6 FAQ <a href="http://technet.microsoft.com/en-us/network/cc987595.aspx">here</a>.</p></div><div id="comment-34963-info" class="comment-info"><span class="comment-age">(29 Jul '14, 01:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-34952" class="comment-tools"></div><div class="clear"></div><div id="comment-34952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

