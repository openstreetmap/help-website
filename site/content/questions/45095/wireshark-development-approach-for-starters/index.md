+++
type = "question"
title = "Wireshark Development Approach For starters"
description = '''Hello, I just completed a course in &quot;C on Linux&quot;, Data Structures, Linux user space programming and Linux Device Drivers. Now I find myself a little confused and in the middle of nowhere. I would like to learn &amp;amp; make tools such as Wireshark (I understand its a very complex tool with years of man...'''
date = "2015-08-14T01:00:00Z"
lastmod = "2015-08-15T02:37:00Z"
weight = 45095
keywords = [ "development", "packets", "protocol", "tcp", "wireshark" ]
aliases = [ "/questions/45095" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Development Approach For starters](/questions/45095/wireshark-development-approach-for-starters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45095-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I just completed a course in "<strong>C on Linux", Data Structures, Linux user space programming and Linux Device Drivers</strong>. Now I find myself a <strong>little confuse</strong>d and in the middle of nowhere. I would like to learn &amp; make tools such as Wireshark (I understand its a very complex tool with years of man hours effort gone into it...but all newbies have to start somewhere :-) )</p><p>So my dilemma is as follows :</p><ul><li><p>To learn to develop a tool like Wire shark do I need to focus on <strong>"user space"</strong> programming -APIs and protocols or I need to focus on <strong>Linux Internals, Linux Kernel Network Internals &amp; Linux Kernel programming</strong> as well</p></li><li><p>If I need to focus on Linux Internals, Network Internals &amp; Kernel programming as well then what do developers do when they deal with "Windows" as its a closed source software. Don't developers face challenges when working with Windows in the absence of windows source code.</p></li><li><p>lastly, I can learn about protocols such as TCP/IP (and functions &amp; APIs) using "unix socket programming" book but I do I learn about other protocols and the APIs they extend</p></li></ul><p>PS: Kindly do answer these questions as I am confused at the moment. I am trying to look for answers n google too.</p><p>Thanks !</p></div><div id="question-tags" class="tags-container tags">development packets protocol tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '15, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/e74d8ecace804379f67c14c9af33695d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monu&#39;s gravatar image" /><p>Monu<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monu has no accepted answers">0%</span></p></div></div><div id="comments-container-45095" class="comments-container"></div><div id="comment-tools-45095" class="comment-tools"></div><div class="clear"></div><div id="comment-45095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="45100"></span>

<div id="answer-container-45100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45100-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Start with user space programming</li><li>There's all kinds of technical info available, even for Windows</li><li>Look at <a href="http://tools.ietf.org/rfc/index">RFCs</a></li></ol><p>Here a list of resources you can pull information from:</p><ul><li><a href="https://www.wireshark.org/develop.html">Wireshark develop</a></li><li><a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developer guide</a></li><li><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=doc;hb=HEAD">README.dissector</a></li><li><a href="http://tools.ietf.org/rfc/index">A good reference on various protocols</a></li><li><a href="http://linux.die.net/man/">Manual pages</a></li><li><a href="http://wiki.qt.io/Basic_Qt_Programming_Tutorial">Qt</a></li><li><a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ff818516%28v=vs.85%29.aspx">Windows API (if you must)</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '15, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-45100" class="comments-container"></div><div id="comment-tools-45100" class="comment-tools"></div><div class="clear"></div><div id="comment-45100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45101"></span>

<div id="answer-container-45101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45101-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a userspace program, and as all such applications it will make use of system\kernel APIs to run. note Wireshark isn't limited to Linux, but runs on multiple platforms.</p><p>Wireshark is a packet analyser, it allows you to analyze traffic made by other applications but has very little internal involvement with network programming as such.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45101" class="comments-container"><span id="45105"></span><div id="comment-45105" class="comment"><div id="post-45105-score" class="comment-score">1</div><div class="comment-text"><p>The level of knowledge needed depends on what you want to, to write a protocol dissector for a simple protocol with no reassembly is a pretty trivial task that could be done with basic programing skills just using Wiresharks APIs(copy paste from other similar dissectors).</p><p>More advanced dissectors require deeper knowledge about the protocol and Wiresharks APIs to do complex operations like reassembly hash maps conversations that may be needed to present the protocol PDUs.</p><p>Decryption requires some knowledge about cryptography and how to use the crypto libraries.</p><p>Doing GUI work requires Qt/GTK knowledge.</p><p>Work on the dissection engine requires a deeper knowledge of Wireshark internals and more advanced programing skills.</p><p>Working on the capturing part and libpcap may requre a deeper knowledge of various OSes network stack and kernel inner workings</p><p>So it all depends on what your goal is and how much time you are prepared to put in.</p></div><div id="comment-45105-info" class="comment-info"><span class="comment-age">(14 Aug '15, 03:52)</span> Anders ♦</div></div><span id="45109"></span><div id="comment-45109" class="comment"><div id="post-45109-score" class="comment-score"></div><div class="comment-text"><p>Sorry to bother again. I have been going through all the stuff listed as above. The work load looks enormous,intimidating and indecipherable.</p><p>In the bigger scheme of things I would want to dissect protocols (work on dissection engine).</p><p>Is there a road map that I could follow perhaps a set of small projects that will gradually help me build up my knowledge base gradually over a period of time for example (A.) which simple protocol should I pick up first to Analyze (B.) what resources/RFCs should I read etc</p><p>I am not expecting to be spoon fed but just seeking a direction and some help so that i don't get lost in this technical maze</p><p>Thanks Again for taking time out !</p></div><div id="comment-45109-info" class="comment-info"><span class="comment-age">(14 Aug '15, 07:07)</span> Monu</div></div><span id="45111"></span><div id="comment-45111" class="comment"><div id="post-45111-score" class="comment-score"></div><div class="comment-text"><p>@Monu</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>For writing dissectors you could look at my <a href="https://sharkfest.wireshark.org/assets/presentations15/03.pptx">presentation</a> for SharkFest on writing a Dissector, although you'll probably be interested in just the C part.</p><p>Finding a protocol that isn't yet dissected by Wireshark is quite hard, for my presentation I created one, and writing the server and client for your own protocol would be a good introduction to network programming itself.</p><p>One way to start with coding and Wireshark is to look at bugs on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, pick one that seems to make sense to you and have a go. Ask on the Wireshark dev mailing list if things aren't clear on a particular bug. You also <strong>must</strong> read the fine documentation that @Jaap listed, in particular the Developers Guide and README.dissector.</p></div><div id="comment-45111-info" class="comment-info"><span class="comment-age">(14 Aug '15, 07:30)</span> grahamb ♦</div></div></div><div id="comment-tools-45101" class="comment-tools"></div><div class="clear"></div><div id="comment-45101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45133"></span>

<div id="answer-container-45133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45133-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now I find myself a little confused and in the middle of nowhere. I would like to learn &amp; make tools such as Wireshark (I understand its a very complex tool with years of man hours effort gone into it...but all newbies have to start somewhere :-) )</p></blockquote><p>Whireshark is way too complex to start with after a C programming course. I guess you don't have much programming experience, so you should look at a task that is achievable in a certain amount of time. If you are interesting in network sniffer, you should probably first start with a <strong>libpcap tutorial</strong> (<a href="https://www.google.com/?q=libpcap+programming+tutorial).">https://www.google.com/?q=libpcap+programming+tutorial).</a> That should teach you:</p><ul><li>more C coding (hopefully)</li><li>a better understanding of network capturing techniques</li><li>the structure of a pcap file</li><li>how to write a small network sniffer</li></ul><p>After you've done that, you can start with more advanced tasks, like trying to <strong>re-write</strong> a dissector for an already existing protocol, like SMTP or something similar, obviously without looking at the existing code ;-)).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '15, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45133" class="comments-container"></div><div id="comment-tools-45133" class="comment-tools"></div><div class="clear"></div><div id="comment-45133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

