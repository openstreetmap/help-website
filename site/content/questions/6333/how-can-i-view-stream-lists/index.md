+++
type = "question"
title = "How can I view stream lists"
description = '''I like to see the list of TCP streams from my packet capture. Something like this: Source Dest Prot Port Start End 1.1.1.1 -&amp;gt; 2.2.2.2 TCP 445 12:00:00.000 12:00:03.000 1.1.1.1 -&amp;gt; 3.3.3.3 TCP 80 12:00:04.000 12:00:05.000 1.1.1.1 -&amp;gt; 2.2.2.2 TCP 445 12:00:07.000 12:00:09.000 (a different strea...'''
date = "2011-09-13T15:14:00Z"
lastmod = "2011-09-13T23:50:00Z"
weight = 6333
keywords = [ "list", "group", "stream", "tcp", "conversation" ]
aliases = [ "/questions/6333" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I view stream lists](/questions/6333/how-can-i-view-stream-lists)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6333-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I like to see the list of TCP streams from my packet capture. Something like this:</p><pre><code>Source     Dest    Prot Port Start        End
1.1.1.1 -&gt; 2.2.2.2 TCP   445 12:00:00.000 12:00:03.000
1.1.1.1 -&gt; 3.3.3.3 TCP    80 12:00:04.000 12:00:05.000
1.1.1.1 -&gt; 2.2.2.2 TCP   445 12:00:07.000 12:00:09.000 (a different stream than the first)</code></pre>I looked at Statistics/FlowGraphs, but that seems to show all the SYN/ACK details in each stream (too much information to go though). I looked at Statistics/ConversationList, but that appears to combine the first and the third in the example above (not enough information).<p>This would be so I can document the traffic going between my application servers. For instance: workstation A talks to server B, which starts server B talking to server C, etc. Is there a way to do this in Wireshare, or am I incorrect in my assumptions? Thanks!</p></div><div id="question-tags" class="tags-container tags">list group stream tcp conversation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '11, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/859c3afbe716eeec3c3c9201f02d56c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris&#39;s gravatar image" /><p>Chris<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '11, 23:17</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6333" class="comments-container"></div><div id="comment-tools-6333" class="comment-tools"></div><div class="clear"></div><div id="comment-6333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6336"></span>

<div id="answer-container-6336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6336-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The functionality that matches your request the most is "Statistics -&gt; Conversations" and then the TCP tab, it will show you the details of every single TCP session in the tracefile.</p><p>If you need the output to be exactly like the table you included in your question, then you would need to do some scripting or programming yourself. You can either use <a href="http://wiki.wireshark.org/Lua">LUA</a> within Wireshark or use tshark with some shell scripting (or perl or ...).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '11, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6336" class="comments-container"><span id="6372"></span><div id="comment-6372" class="comment"><div id="post-6372-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That is what I was looking for. I copied it from there to Excel after that for further analysis. It looks like your suggestion will reduce my work from looking at 100,000 packets to looking at 1,000 conversations :).</p></div><div id="comment-6372-info" class="comment-info"><span class="comment-age">(14 Sep '11, 14:12)</span> Chris</div></div></div><div id="comment-tools-6336" class="comment-tools"></div><div class="clear"></div><div id="comment-6336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

