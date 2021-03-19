+++
type = "question"
title = "Building Display Filter Using Conversations"
description = '''Good day all! I&#x27;m trying to build a comprehensive list of hosts and ports talking within a network so I can begin to build a firewall ACL as we begin to compartmentalize the network a bit. I&#x27;m using WS 1.4.6 where I start by simply capture &amp;gt;&amp;gt; start &amp;gt;&amp;gt; and select interface. I then apply a...'''
date = "2011-05-20T10:29:00Z"
lastmod = "2011-05-20T15:43:00Z"
weight = 4164
keywords = [ "conversation", "display-filter" ]
aliases = [ "/questions/4164" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building Display Filter Using Conversations](/questions/4164/building-display-filter-using-conversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4164-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good day all! I'm trying to build a comprehensive list of hosts and ports talking within a network so I can begin to build a firewall ACL as we begin to compartmentalize the network a bit. I'm using WS 1.4.6 where I start by simply capture &gt;&gt; start &gt;&gt; and select interface. I then apply a display filter of ((tcp.flags.syn == 1) &amp;&amp; (tcp.seq == 0)) &amp;&amp; !(tcp.flags.ack == 1) which (I believe) will only display the initial syn of each conversation. I do this because I never know when I start my trace files if I'm catching conversations some in the middle so I want to ensure my firewall ACLs are correct so I need the correct conversation flow.</p><p>I then go to Statistics &gt;&gt; Conversations and check the box for "Limit to Display Filter." I now want to filter out each conversation once I note it on my spreadsheet so I go to prepare a filter and chose not selected A&lt;-&gt;B. This starts to eliminate each conversation from the trace file as I note it on my spreadsheet. The thing that is happening though is the conversation in the Conversations &gt;&gt; TCP (TCP tab) window is backwards from what appears to be actually happening. For example in the tracefile I'm seeing host A doing a syn to host B on port 1234 but the Conversations list has it listed as host B sending to host A. So now of course when I build my filter it turns out backwards. Not every instance/conversation line in the Conversations list is backwards but it causes me to double check each time.</p><p>Any thoughts on what I could be doing wrong here? Or, if there is an easier way to acccomplish this, I'm eagerly all ears :)</p><p>Have a great day! Garry</p></div><div id="question-tags" class="tags-container tags">conversation display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '11, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/8b4f310967492da86d13424f06be9b4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfrizz17&#39;s gravatar image" /><p>gfrizz17<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfrizz17 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 27 May '11, 20:56</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4164" class="comments-container"></div><div id="comment-tools-4164" class="comment-tools"></div><div class="clear"></div><div id="comment-4164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4165"></span>

<div id="answer-container-4165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4165-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have no idea why the conversations would appear reversed, so can't address that part of your question, but here's a way to accomplish what you want that sidesteps that issue and may be a bit simpler:</p><p>First, simplify your filter to "tcp.flags == 0x02". This will show you the initial SYN of each conversation.</p><p>Second, don't go to the Conversations display. Stay on the main Wireshark screen with your display filter in place. Each line of the packet list display represents one conversation. As you enter each conversation in your spreadsheet, highlight that line and press Ctrl-D, or right-click and select Ignore Packet. This will cause that line to disappear from the display.</p><p>It will be clear from the packet list display which side initiated the conversation, and this will be simpler than building an exclusion filter for each conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '11, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4165" class="comments-container"></div><div id="comment-tools-4165" class="comment-tools"></div><div class="clear"></div><div id="comment-4165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4166"></span>

<div id="answer-container-4166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4166-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way to get a list of conversations to turn into a firewall rulebase is (IMHO) to use tshark:</p><pre><code>tshark -C Default-Sake -r ipad.cap -nl -R &quot;tcp.flags==2&quot; -T fields -e ip.src -e ip.dst -e tcp.dstport | sort | uniq 
192.168.1.22    192.168.1.29    59548
192.168.1.29    17.152.17.80    443
192.168.1.29    17.172.236.21   5223
192.168.1.29    184.73.184.162  80
192.168.1.29    194.134.4.233   110
192.168.1.29    2.20.93.15  80
[...]</code></pre><p>Or if you want it sorted by the amount of conversations:</p><pre><code>tshark -C Default-Sake -r ipad.cap -nl -R &quot;tcp.flags==2&quot; -T fields -e ip.src -e ip.dst -e tcp.dstport | sort | uniq -c | sort -rn
  18 192.168.1.29   216.39.58.249   80
   7 192.168.1.29   72.233.96.254   80
   3 192.168.1.29   93.184.220.20   80
   3 192.168.1.29   83.163.163.55   993
  [...]</code></pre><p>Of course you can pipe this outpur through sed and awk to even build the commands needed to implement the FW rules (assuming your firewall has a CLI through which new rules can be added).</p><p>Hope this helps!</p><p>(Oh BTW, if you use Windows, you can use <a href="http://www.cygwin.com">Cygwin</a> to get a shell in which you are able to do this)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '11, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4166" class="comments-container"><span id="4167"></span><div id="comment-4167" class="comment"><div id="post-4167-score" class="comment-score"></div><div class="comment-text"><p><code>Cygwin == molasses</code></p></div><div id="comment-4167-info" class="comment-info"><span class="comment-age">(20 May '11, 16:07)</span> helloworld</div></div></div><div id="comment-tools-4166" class="comment-tools"></div><div class="clear"></div><div id="comment-4166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

