+++
type = "question"
title = "Filter Incoming Connection Attempts"
description = '''With tcpdump if I want to capture all TCP connection attempts (whether successful or not) I use the following capture filter: tcp[tcpflags] &amp;amp; (tcp-syn) != 0 and if I want capture the start and end packetes (The SYN and FIN packets) of each TCP conversation that involves a non-local host I use: t...'''
date = "2013-03-08T10:30:00Z"
lastmod = "2013-03-15T04:57:00Z"
weight = 19306
keywords = [ "filtering", "capture", "capture-filter", "tcpdump", "filters" ]
aliases = [ "/questions/19306" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Incoming Connection Attempts](/questions/19306/filter-incoming-connection-attempts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19306-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With tcpdump if I want to capture all TCP connection attempts (whether successful or not) I use the following capture filter: <strong>tcp[tcpflags] &amp; (tcp-syn) != 0</strong> and if I want capture the start and end packetes (The SYN and FIN packets) of each TCP conversation that involves a non-local host I use: <strong>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst net localnet</strong> How can I do these examples using Wireshark GUI (Creating capture filters)? Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">filtering capture capture-filter tcpdump filters</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/a334020eacdd8a7faf0f3e9d0d1cf678?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zig69&#39;s gravatar image" /><p>zig69<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zig69 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Mar '13, 10:32</p></div></div><div id="comments-container-19306" class="comments-container"></div><div id="comment-tools-19306" class="comment-tools"></div><div class="clear"></div><div id="comment-19306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19307"></span>

<div id="answer-container-19307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19307-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you're running Wireshark 1.8.x, you can open the capture options and double click on the interface you want to capture on. This will open another dialog where you can specify the capture filter.</p><p>On older versions, you'll see the capture filter input field right after opening the capture options dialog.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19307" class="comments-container"><span id="19309"></span><div id="comment-19309" class="comment"><div id="post-19309-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer, but I already knew that, is trivial! I meant how to create the filters (syntax) for doing the same thing that I do with tcpdump...</p></div><div id="comment-19309-info" class="comment-info"><span class="comment-age">(08 Mar '13, 11:12)</span> zig69</div></div><span id="19315"></span><div id="comment-19315" class="comment"><div id="post-19315-score" class="comment-score">1</div><div class="comment-text"><p>Not sure what you're aiming at, but THAT capture filter box takes <strong>tcpdump</strong> syntax... just put it in there, just as you would for tcpdump. Did you ever try? It's trivial! ;-)</p></div><div id="comment-19315-info" class="comment-info"><span class="comment-age">(08 Mar '13, 13:59)</span> Jasper ♦♦</div></div><span id="19356"></span><div id="comment-19356" class="comment"><div id="post-19356-score" class="comment-score"></div><div class="comment-text"><p>Yes, It's trivial but does not work! The filter: tcp[tcpflags] &amp; (tcp-syn) != 0 works well but when I add the expression "and not src and dst net localnet" the capture filter field appears in red color and does not work (Of course) :-(</p></div><div id="comment-19356-info" class="comment-info"><span class="comment-age">(11 Mar '13, 10:42)</span> zig69</div></div><span id="19371"></span><div id="comment-19371" class="comment"><div id="post-19371-score" class="comment-score"></div><div class="comment-text"><p>Wireshark does not know the term <strong>localnet</strong></p></div><div id="comment-19371-info" class="comment-info"><span class="comment-age">(11 Mar '13, 23:52)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19307" class="comment-tools"></div><div class="clear"></div><div id="comment-19307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19536"></span>

<div id="answer-container-19536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19536-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>localnet is not a libpcap keyword, it is looked up by your system in /etc/networks. Even though you can add an entry to /etc/networks, it does not seem to be CIDR compatible, so if you are on a network that is not classfull, you will be out of luck anyway.</p><p>See also: <a href="http://www.winpcap.org/pipermail/winpcap-users/2011-November/004522.html">http://www.winpcap.org/pipermail/winpcap-users/2011-November/004522.html</a></p><p>You will have to contruct the network address for your network yourself and can then use it like this (for 192.168.1.0/25):</p><pre><code>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst net 192.168.1.0/25</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19536" class="comments-container"></div><div id="comment-tools-19536" class="comment-tools"></div><div class="clear"></div><div id="comment-19536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

