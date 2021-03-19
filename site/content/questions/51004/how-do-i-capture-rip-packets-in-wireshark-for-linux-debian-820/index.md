+++
type = "question"
title = "How do I capture RIP packets in Wireshark for Linux (Debian 8.2.0)?"
description = '''I am running Wireshark and have configured it so that non-superusers can capture packets. I also capture on all interfaces in &quot;Promiscuous Mode.&quot; I followed the instructions below to configure Wireshark:  https://wiki.wireshark.org/CaptureSetup/CapturePrivileges  I have installed Quagga and have con...'''
date = "2016-03-17T06:49:00Z"
lastmod = "2016-03-18T11:03:00Z"
weight = 51004
keywords = [ "quagga", "capture", "rip", "linux" ]
aliases = [ "/questions/51004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture RIP packets in Wireshark for Linux (Debian 8.2.0)?](/questions/51004/how-do-i-capture-rip-packets-in-wireshark-for-linux-debian-820)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51004-score" class="post-score" title="current number of votes">0</div><span id="post-51004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark and have configured it so that non-superusers can capture packets. I also capture on all interfaces in "Promiscuous Mode." I followed the instructions below to configure Wireshark:</p><ul><li><a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges">https://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></li></ul><p>I have installed Quagga and have configured both zebra and ripd according to instructions in the two links below:</p><ul><li><a href="http://computechtips.com/578/install-and-configure-quagga-in-ubuntu">http://computechtips.com/578/install-and-configure-quagga-in-ubuntu</a></li><li><a href="https://opensourcecentre.wordpress.com/article/install-quagga-as-linux-router/">https://opensourcecentre.wordpress.com/article/install-quagga-as-linux-router/</a></li></ul><p>I have checked the process list using "ps -ef | grep quagga" in the Linux Terminal, and it shows that Quagga is running and both zebra and ripd are running when my computer starts up. Therefore, I know that I should be seeing RIP packets sent over the network about every 30 seconds. <strong>No matter how long I leave Wireshark running, it does not capture any RIP packets.</strong></p><p>I have considered that the issue may be with my Quagga configuration, so if anyone can also speak to that here, I appreciate any and all advice. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-quagga" rel="tag" title="see questions tagged &#39;quagga&#39;">quagga</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-rip" rel="tag" title="see questions tagged &#39;rip&#39;">rip</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '16, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/5f22c96b6d4ea8b2238742702c88c7e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NetworkAnalyzer&#39;s gravatar image" /><p><span>NetworkAnalyzer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NetworkAnalyzer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '16, 08:48</strong> </span></p></div></div><div id="comments-container-51004" class="comments-container"><span id="51008"></span><div id="comment-51008" class="comment"><div id="post-51008-score" class="comment-score"></div><div class="comment-text"><p>Do you use any capture filter? If yes, what one? Can you see other than RIP packets?</p></div><div id="comment-51008-info" class="comment-info"><span class="comment-age">(17 Mar '16, 08:25)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51009"></span><div id="comment-51009" class="comment"><div id="post-51009-score" class="comment-score"></div><div class="comment-text"><p>No, I am not using any capture filters. I am seeing many other packets, especially when I use ping. But I never see any RIP packets.</p></div><div id="comment-51009-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:03)</span> <span class="comment-user userinfo">NetworkAnalyzer</span></div></div><span id="51010"></span><div id="comment-51010" class="comment"><div id="post-51010-score" class="comment-score">1</div><div class="comment-text"><p>OK, in that case it is not a Wireshark question any more and the packets are really not there, unless you have by miracle disabled the RIP dissector and thus you can the RIP packets are shown as plain UDP ones in the packet list pane.</p></div><div id="comment-51010-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:14)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51013"></span><div id="comment-51013" class="comment"><div id="post-51013-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I will double check the status of the RIP dissector, and will seek some additional advice on how Quagga/zebra/ripd is configured. I ask because I am setting up a Linux computer as a router, and I need to examine some RIP packets.</p></div><div id="comment-51013-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:41)</span> <span class="comment-user userinfo">NetworkAnalyzer</span></div></div><span id="51014"></span><div id="comment-51014" class="comment"><div id="post-51014-score" class="comment-score">1</div><div class="comment-text"><p>Somewhere in the chain of the comments to your two quagga-related links I've seen that it won't work without configuring at least an IP address using quagga's command line (as if quagga wouldn't inherit anything from the system), that might be the issue.</p></div><div id="comment-51014-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:45)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51015"></span><div id="comment-51015" class="comment not_top_scorer"><div id="post-51015-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I see. I just did a search on setting the IP address in Quagga, and came across this website: <a href="http://openmaniak.com/quagga_tutorial.php">http://openmaniak.com/quagga_tutorial.php</a></p><p>It seems to be a good guide to setting up Quagga, so I will try out what it says later and report back here for the sake of anyone else reading this post.</p></div><div id="comment-51015-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:54)</span> <span class="comment-user userinfo">NetworkAnalyzer</span></div></div></div><div id="comment-tools-51004" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-51004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51040"></span>

<div id="answer-container-51040" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51040-score" class="post-score" title="current number of votes">0</div><span id="post-51040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Along with the websites and information posted in my question above, I discovered two things that enabled me to capture RIP packets in Wireshark on Linux Debian 8.2.0.</p><p>1) My Linux workstation did not have IPv4 Forwarding enabled. A quick search on how to enable IPv4 Forwarding fixed that issue.</p><p>2) The .conf file for ripd needed to be filled in, not just left empty as one website suggested. I simply had to enter network information into the ripd.conf file and store that file in "/etc/quagga." The information in the ripd.conf file looks like:</p><pre><code>  Network 199.234.24.0/24
  Network 199.234.25.0/24
  Network eth0
  Network eth1</code></pre><p>In other words, I had to specify the networks that ripd would be working on.</p><p>Thanks to <em>sindy</em> for the advice as I sought an answer to this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '16, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/5f22c96b6d4ea8b2238742702c88c7e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NetworkAnalyzer&#39;s gravatar image" /><p><span>NetworkAnalyzer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NetworkAnalyzer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '16, 08:49</strong> </span></p></div></div><div id="comments-container-51040" class="comments-container"></div><div id="comment-tools-51040" class="comment-tools"></div><div class="clear"></div><div id="comment-51040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

