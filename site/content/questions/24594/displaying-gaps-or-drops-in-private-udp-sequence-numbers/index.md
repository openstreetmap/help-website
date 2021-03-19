+++
type = "question"
title = "Displaying gaps or drops in private UDP sequence numbers"
description = '''I&#x27;ve seen several topics here that relate to this issue, but none of the solutions have worked for me so far, so hopefully someone can point out where I&#x27;m going wrong. I have a capture with 4 separate UDP streams being received on 4 well known ports, 30300 - 30303. The UDP packets have a private &quot;se...'''
date = "2013-09-11T16:09:00Z"
lastmod = "2014-02-06T07:57:00Z"
weight = 24594
keywords = [ "lua", "udp", "dissector", "tap", "sequence" ]
aliases = [ "/questions/24594" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Displaying gaps or drops in private UDP sequence numbers](/questions/24594/displaying-gaps-or-drops-in-private-udp-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've seen several topics here that relate to this issue, but none of the solutions have worked for me so far, so hopefully someone can point out where I'm going wrong.</p><p>I have a capture with 4 separate UDP streams being received on 4 well known ports, 30300 - 30303.</p><p>The UDP packets have a private "sequence number" that increments monotonically for each port.</p><p>I've been able to write a dissector in Lua that highlights that sequence number, but want to go to the next step: highlighting or somehow calling out packets just after a packet drop has been detected, indicated by a break in the sequence.</p><p>Here's my attempt so far: <a href="http://pastebin.com/nL9TCPWq">http://pastebin.com/nL9TCPWq</a></p><p>I've seen discussions indicating a Tap may be more appropriate for this purpose, but haven't found any Lua examples as yet.</p></div><div id="question-tags" class="tags-container tags">lua udp dissector tap sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/c24f943b37470fb3c3ad80d4cbb1a919?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gordon%20Marler&#39;s gravatar image" /><p>Gordon Marler<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gordon Marler has no accepted answers">0%</span></p></div></div><div id="comments-container-24594" class="comments-container"></div><div id="comment-tools-24594" class="comment-tools"></div><div class="clear"></div><div id="comment-24594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24617"></span>

<div id="answer-container-24617" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24617-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The code looks like it could work. So, what is your question?</p><p>BTW: why</p><blockquote><p>port_seq[port_str] = { seq }</p></blockquote><p>instead of</p><blockquote><p>port_seq[port_str] = seq</p></blockquote><p>??</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24617" class="comments-container"><span id="24660"></span><div id="comment-24660" class="comment"><div id="post-24660-score" class="comment-score"></div><div class="comment-text"><p>That was a mistake, probably an attempt to build a nested table initially, which wasn't necessary. I've corrected it as you've shown.</p><p>As to my question, through various trial and error, the script seems to just stop at this line, where I try to increment the last sequence number and store it in expected:</p><blockquote>local expected = port_seq[port_str] + 1</blockquote><p>I'm wondering if the value I extracted from the packet with buffer(8,8) as the sequence number is actually being interpreted as an integer.</p></div><div id="comment-24660-info" class="comment-info"><span class="comment-age">(13 Sep '13, 15:35)</span> Gordon Marler</div></div><span id="24671"></span><div id="comment-24671" class="comment"><div id="post-24671-score" class="comment-score"></div><div class="comment-text"><blockquote><p>as the sequence number is actually being interpreted as an integer.</p></blockquote><p>good question. Impossible to answer without a sample capture file ;-) Can you please post one on google drive, dropbox or cloudshark?</p></div><div id="comment-24671-info" class="comment-info"><span class="comment-age">(14 Sep '13, 04:20)</span> Kurt Knochner ♦</div></div><span id="24809"></span><div id="comment-24809" class="comment"><div id="post-24809-score" class="comment-score"></div><div class="comment-text"><p>That makes sense - here's a sample capture:</p><p><a href="http://www.cloudshark.org/captures/78f060054941">dropped-test.pcapng</a></p></div><div id="comment-24809-info" class="comment-info"><span class="comment-age">(17 Sep '13, 04:26)</span> Gordon Marler</div></div><span id="24812"></span><div id="comment-24812" class="comment not_top_scorer"><div id="post-24812-score" class="comment-score"></div><div class="comment-text"><p>The first 8 bytes are not a counter in any way, as the bytes are the same for every frame, and I can't see any other byte sequence that increments in a detectable/predictable way.</p><p>So, where exactly is that sequence number within the frame?</p></div><div id="comment-24812-info" class="comment-info"><span class="comment-age">(17 Sep '13, 05:22)</span> Kurt Knochner ♦</div></div><span id="24822"></span><div id="comment-24822" class="comment"><div id="post-24822-score" class="comment-score">1</div><div class="comment-text"><p>hold on. My mistake. I was looking at the beginning of the UDP payload, whereas in the code it says: at byte 8. O.K. then there is an increasing seq number. I'll have to check how that gets read by the lua code.</p></div><div id="comment-24822-info" class="comment-info"><span class="comment-age">(17 Sep '13, 07:17)</span> Kurt Knochner ♦</div></div><span id="24826"></span><div id="comment-24826" class="comment not_top_scorer"><div id="post-24826-score" class="comment-score"></div><div class="comment-text"><p>strange thing.</p><p>If you change the code to this:</p><pre><code>                    warn(&quot;P#1&quot;)
                local expected = port_seq[port_str] + 1;
                warn(&quot;P#2&quot;)</code></pre><p>and then run tshark like this:</p><blockquote><p>tshark -nr input.pcap -Xlua_script:udprecv-info.lua</p></blockquote><p>The output look like this:</p><pre><code>  1 0.000000000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
P#1
  2 0.000275000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
P#1
  3 0.000277000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
P#1
  4 0.000278000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301</code></pre><p>So, P#1 gets printed, but not P#2, as if code execution stops after (or with) the declaration of <strong>local expected</strong>. Currently I have no idea what's going wrong (maybe a bug), but if code execution really stops there, your code to analyze the sequence number will not be executed either!</p><p>If you remove the declaration of <strong>local expected</strong>, the output looks like this.</p><pre><code>  1 0.000000000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
P#1
P#2
not sequential
  2 0.000275000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
P#1
P#2
not sequential</code></pre><p>So, now P#2 gets printed and the rest of the code gets executed as well, although with wrong result, due to the missing variable.</p><p>Looks like a strange bug to me.</p><p>BTW: The <strong>seq</strong> is extracted correctly by the code.</p></div><div id="comment-24826-info" class="comment-info"><span class="comment-age">(17 Sep '13, 07:38)</span> Kurt Knochner ♦</div></div><span id="24831"></span><div id="comment-24831" class="comment not_top_scorer"><div id="post-24831-score" class="comment-score"></div><div class="comment-text"><p>O.K. the problem is the data type of seq. It gets extracted as type <strong>userdata</strong> (see: warn("Seq type: " .. type(seq)). Even if you make it a uint64, it's type is still <strong>userdata</strong></p><blockquote><p>local seq = buffer(8, 8):uint64()</p></blockquote><p>Apparently there is no + operator defined for that data type and thus the code</p><blockquote><p>local expected = port_seq[port_str] + 1</p></blockquote><p>fails.</p><p>So, we need to find a way to make <strong>seq</strong> a number object. Unfortunately I have not found a way to do that yet. tonumber() does not work.</p></div><div id="comment-24831-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:06)</span> Kurt Knochner ♦</div></div><span id="24832"></span><div id="comment-24832" class="comment"><div id="post-24832-score" class="comment-score">1</div><div class="comment-text"><p>well, there seems to be a problem with unit64(). If I change the code to this</p><blockquote><p>local seq = buffer(12, 4):uint()</p></blockquote><p>it works well, as the data type of <strong>seq</strong> is then a <strong>number</strong> instead of <strong>userdata</strong> (with uint64())</p><p>HOWEVER: That's just 4 bytes of your sequence!!</p><p>Test:</p><blockquote><p>tshark -nr input.pcap -Xlua_script:udprecv-info.lua</p></blockquote><p>Output:</p><pre><code>  1 0.000000000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
not sequential
  2 0.000275000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
it was equal
  3 0.000277000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
it was equal
  4 0.000278000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
it was equal
  5 0.000279000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
not sequential
  6 0.000281000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
it was equal
  7 0.000282000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
it was equal
  8 0.000283000 10.126.45.147 -&gt; 239.255.6.82 UDP 1066 0x0000 (0) Source port: 53486  Destination port: 30301
</code></pre><p>I don't know if this is a bug or if there are internal representation problems with 64 bit values in Lua !?! Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> with a reference to this question and my 'findings'.</p></div><div id="comment-24832-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:19)</span> Kurt Knochner ♦</div></div><span id="24871"></span><div id="comment-24871" class="comment not_top_scorer"><div id="post-24871-score" class="comment-score"></div><div class="comment-text"><p>Excellent troubleshooting! Thanks for taking the time.</p><p>I've submitted <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9162">Bug ID 9162</a></p></div><div id="comment-24871-info" class="comment-info"><span class="comment-age">(17 Sep '13, 17:51)</span> Gordon Marler</div></div><span id="24881"></span><div id="comment-24881" class="comment not_top_scorer"><div id="post-24881-score" class="comment-score"></div><div class="comment-text"><p>Thanks for submitting the bug.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-24881-info" class="comment-info"><span class="comment-age">(18 Sep '13, 00:25)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24617" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-24617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29491"></span>

<div id="answer-container-29491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29491-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Support for 64-bt integers in Lua has now been added in Wireshark 1.11.3, and should be in the latest <a href="http://www.wireshark.org/download/automated/">nightly builds</a>. It provides Int64/UInt64 objects with abilities to use math and comparison operators and such. See <a href="http://wiki.wireshark.org/LuaAPI/Int64">wiki.wireshark.org/LuaAPI/Int64</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '14, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29491" class="comments-container"></div><div id="comment-tools-29491" class="comment-tools"></div><div class="clear"></div><div id="comment-29491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

