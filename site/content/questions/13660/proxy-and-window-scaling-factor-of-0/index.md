+++
type = "question"
title = "Proxy and Window scaling factor of 0"
description = '''I was wondering if anyone had any advice for what i&#x27;m seeing in our network. I was looking at some captures and noticed that the window scale factor for anything coming back through the blue coat was a scale factor of 0. Which means I support it..but I wont scale.. That was just odd me to and I star...'''
date = "2012-08-15T13:17:00Z"
lastmod = "2012-08-15T20:00:00Z"
weight = 13660
keywords = [ "scaling", "window", "zero", "size" ]
aliases = [ "/questions/13660" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Proxy and Window scaling factor of 0](/questions/13660/proxy-and-window-scaling-factor-of-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13660-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if anyone had any advice for what i'm seeing in our network.</p><p>I was looking at some captures and noticed that the window scale factor for anything coming back through the blue coat was a scale factor of 0. Which means I support it..but I wont scale.. That was just odd me to and I started to do some digging. I couldn’t see how every site coming back had a scale factor of zero. Which made me thing the bluecoat was doing something fishy.</p><p>I setup a small http webserver on my home laptop just so I can connect and get the 3-way handshake and see what was really going on. And what I saw was, in fact when the server sends a response to back to the client its not zero at all, it sent a scale factor but when it went through the blue coat and back to the client, the bluecoat told the client the scale factor was zero, so it stripped it. I’m thinking scaling is turned off on the bluecoats or it’s a bug..</p><p>Example:</p><p>Host A / Window scale 4 &gt; Bluecoat / Strips windows scale 4 makes it 0 &gt; Server B = sees client window scale 0 but sends its own scale factor of 7</p><p>Server B / Window scale 7 &gt; Bluecoat / Strips window scale 7 makes it 0 &gt; Host A = sees server window scale 0 but sends its own scale factor of 4</p><p>So Host a sent window scale of 4, blue coat stripped it and made it 0, when server get the packet with the window scale its now 0 instead of 4. Same thing with Server B, instead of Host A seeing Window scale of 7 it sees that it’s a window scale of 0.</p><p>So my question is.. Is Window scaling happening at all? One side believes its has a window scale factor of X and is telling the other end, but that end only sees 0. I see the calculated window size on the client end goes above 65k as the captures go on, but ofcourse the return traffic end doesnt go above 65k.</p></div><div id="question-tags" class="tags-container tags">scaling window zero size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '12, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/e9ce15add76dd3cab7a823b4b761a0a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HCA1234&#39;s gravatar image" /><p>HCA1234<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HCA1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Aug '12, 13:21</p></div></div><div id="comments-container-13660" class="comments-container"><span id="13661"></span><div id="comment-13661" class="comment"><div id="post-13661-score" class="comment-score"></div><div class="comment-text"><p>I actually looked at the other end a bit better and saw this.</p><p>What i said here is still correct : "I see the calculated window size on the client end goes above 65k as the captures go on, but ofcourse the return traffic end doesnt go above 65k."</p><p>But if i look at that window size as it comes across to the server..the window size is actually 65k or less, so before it leaves the proxy i.e the client will say my window size is above 65k such as 131920, but after the server gets it, the window size is 65k or less after the proxy sends it to the server.</p><p>So i'm quite sure Window scaling has been interrupted because of the proxy, and most likely its disabled on the proxy end. Thoughts?</p></div><div id="comment-13661-info" class="comment-info"><span class="comment-age">(15 Aug '12, 14:23)</span> HCA1234</div></div></div><div id="comment-tools-13660" class="comment-tools"></div><div class="clear"></div><div id="comment-13660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13668"></span>

<div id="answer-container-13668" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13668-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't say what Bluecoat device you have, but yes, it sounds like window scaling is disabled on the Bluecoat proxy. I suggest you search the Bluecoat Knowledge Base for "window scale" or "rfc 1323". <a href="https://kb.bluecoat.com/index?page=content&amp;id=FAQ1006">This link</a> is for the Bluecoat ProxySG and it describes exactly what you're seeing: The Bluecoat device changing the window scale factor to 0 because window scaling is disabled. The article gives the commands for enabling and disabling window scaling, at least on the ProxySG, and it says that when window scaling is enabled, the ProxySG will use a scale factor of 6 by default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 20:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13668" class="comments-container"><span id="13672"></span><div id="comment-13672" class="comment"><div id="post-13672-score" class="comment-score"></div><div class="comment-text"><p>I find it strange that the window scaling option value is set to 0. That means both sides are not aware of the real receive buffer on the other side. Instead the BlueCoat should just remove the window scale option from the TCP header altogether. I would consider this a bug and would file it to BlueCoat support.</p><p>Are you able to share the captures of both sides of the BlueCoat on <a href="http://www.cloudshark.org">www.cloudshark.org</a>? I'd like to see this peculiar behavior myself :-)</p></div><div id="comment-13672-info" class="comment-info"><span class="comment-age">(15 Aug '12, 23:47)</span> SYN-bit ♦♦</div></div><span id="13674"></span><div id="comment-13674" class="comment"><div id="post-13674-score" class="comment-score"></div><div class="comment-text"><p>It's a waste of time to argue with Blue Coat support about RFC feature interpretation/implementation. I've done it a few times and never got anywhere. Perhaps their installed base is to big to make fundamental changes to the system, which allways carries the risk of breaking things that used to work in most environments.</p><p>In this special case, they will refuse start a discussion, as RFC 1323 states:</p><blockquote><p>The value 'shift.cnt' may be zero offering to scale, while applying a scale factor of 1 to the receive window).</p></blockquote><p>So, what they do is RFC compliant, but may cause problems with other devices.</p></div><div id="comment-13674-info" class="comment-info"><span class="comment-age">(16 Aug '12, 01:18)</span> Kurt Knochner ♦</div></div><span id="13675"></span><div id="comment-13675" class="comment"><div id="post-13675-score" class="comment-score"></div><div class="comment-text"><p>Whether it is RFC compliant depends on the working of the BlueCoat. If it is an application layer proxy having it's own TCP buffers on both sides of the connection, than indeed it is RFC compliant (I was not fully awake when writing my last comment I guess). So if it is a ProxySG, then it is compliant.</p><p>When it is a non-buffering device that does this, it is not RFC compliant. I don't know what kind of BlueCoat device it is, I can imagine their trafficshaper to not buffer so that could be a problem.</p></div><div id="comment-13675-info" class="comment-info"><span class="comment-age">(16 Aug '12, 01:32)</span> SYN-bit ♦♦</div></div><span id="13678"></span><div id="comment-13678" class="comment"><div id="post-13678-score" class="comment-score"></div><div class="comment-text"><p>I assume it is a ProxySG, as it is mentioned in the title of the question.</p></div><div id="comment-13678-info" class="comment-info"><span class="comment-age">(16 Aug '12, 02:47)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13668" class="comment-tools"></div><div class="clear"></div><div id="comment-13668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

