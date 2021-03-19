+++
type = "question"
title = "reading pcap file in C# or C++"
description = '''in general, I want to analyze a tcp packet ,first I should read the pcap file in c++(this is my first problem), after that I want to analyze just the tcp packets in the flow of packets, and find it&#x27;s header details such that &quot;syn&quot;,&quot;ack&quot;,&quot;fin&quot;,&quot;source ip&quot;,&quot;destination ip&quot; and etc ,for this I read som...'''
date = "2014-01-16T08:22:00Z"
lastmod = "2015-06-02T11:21:00Z"
weight = 28965
keywords = [ "c#", "tcp.stream", "pcap", "c++" ]
aliases = [ "/questions/28965" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [reading pcap file in C\# or C++](/questions/28965/reading-pcap-file-in-c-or-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in general, I want to analyze a tcp packet ,first I should read the pcap file in c++(this is my first problem), after that I want to analyze just the tcp packets in the flow of packets, and find it's header details such that "syn","ack","fin","source ip","destination ip" and etc ,for this I read something a bout "pcap" that I found it here, but it doesn't give me enough information, it doesn't give me any thing about "syn" or "ack",.....and now I don't know how and with which program in c++ or c# I can do it??? that is my big problem! thank you so much for your attention</p></div><div id="question-tags" class="tags-container tags">c# tcp.stream pcap c++</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '14, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/2ace83a7e6598144111a2c23b5564113?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mesmslampanah&#39;s gravatar image" /><p>mesmslampanah<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mesmslampanah has no accepted answers">0%</span></p></div></div><div id="comments-container-28965" class="comments-container"></div><div id="comment-tools-28965" class="comment-tools"></div><div class="clear"></div><div id="comment-28965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28967"></span>

<div id="answer-container-28967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28967-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is a c++/c# 'wrapper library' for libpcap. There are two candidates I know of:</p><p>Pcap.Net</p><blockquote><p><a href="http://pcapdotnet.codeplex.com/">http://pcapdotnet.codeplex.com/</a></p></blockquote><p>SharpPcap<br />
</p><blockquote><p><a href="http://sourceforge.net/apps/mediawiki/sharppcap/index.php?title=Main_Page">http://sourceforge.net/apps/mediawiki/sharppcap/index.php?title=Main_Page</a></p></blockquote><p>For both you need</p><ul><li>some c++/c# programming experience. Nothing we can help you with</li><li>some understanding of TCP/IP and networking. Something you can only learn yourself, by reading the right books, like: <a href="http://www.amazon.com/TCP-Illustrated-Volume-Addison-Wesley-Professional/dp/0321336313/ref=sr_1_1?ie=UTF8&amp;qid=1389895782&amp;sr=8-1&amp;keywords=tcp%2Fip+illustrated">TCP/IP Illustrated Volume 1</a></li><li>a rough idea how to use the libpcap libraries. See their docs.</li></ul><blockquote><p>and now I don't know how and with which program in c++ or c# I can do it???</p></blockquote><p>If you don't know how to program in c++/c# you will have a hard time to finish your task. Maybe you'll find some example code in one of the wrapper libraries above, that does similar things you need.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '14, 10:15</p></div></div><div id="comments-container-28967" class="comments-container"><span id="28992"></span><div id="comment-28992" class="comment"><div id="post-28992-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help,I know C# programming and C++,but i dont know what's of their is easier to do this? I saw a sample written by Perl,but it had some functions(read byte and byte) and Data Type (like hash)</p></div><div id="comment-28992-info" class="comment-info"><span class="comment-age">(17 Jan '14, 08:10)</span> mesmslampanah</div></div><span id="28997"></span><div id="comment-28997" class="comment"><div id="post-28997-score" class="comment-score"></div><div class="comment-text"><blockquote><p>what's of their is easier to do this?</p></blockquote><p>Well, that's something you should decide for yourself, as it mainly depends on your skills and your personal preferences...</p></div><div id="comment-28997-info" class="comment-info"><span class="comment-age">(17 Jan '14, 10:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28967" class="comment-tools"></div><div class="clear"></div><div id="comment-28967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42832"></span>

<div id="answer-container-42832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42832-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a>. It has all that you need and more...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '15, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p>seladb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-42832" class="comments-container"></div><div id="comment-tools-42832" class="comment-tools"></div><div class="clear"></div><div id="comment-42832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

