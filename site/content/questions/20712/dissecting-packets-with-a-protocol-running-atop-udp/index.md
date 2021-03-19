+++
type = "question"
title = "Dissecting packets with a protocol running atop UDP"
description = '''Wireshark semi-noob here.  I have two devices that talk to each other over 802.11, and I need to reverse engineer the protocol (we are emulating one of the devices, and don&#x27;t have full docs).  The protocol is more or less ASCII strings over UDP over wireless, i. e. text strings, SQL queries, etc.  I...'''
date = "2013-04-22T08:28:00Z"
lastmod = "2013-04-22T19:17:00Z"
weight = 20712
keywords = [ "filtering", "dissector" ]
aliases = [ "/questions/20712" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting packets with a protocol running atop UDP](/questions/20712/dissecting-packets-with-a-protocol-running-atop-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20712-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark semi-noob here.</p><p>I have two devices that talk to each other over 802.11, and I need to reverse engineer the protocol (we are emulating one of the devices, and don't have full docs).</p><p>The protocol is more or less ASCII strings over UDP over wireless, i. e. text strings, SQL queries, etc.</p><p>I am able to sniff packets that I know are part of the dialog between client and server. I can search captured packets for known strings and see them; I can search for hex values of IP addresses and find them.</p><p>I cannot (but would like to): - Filter by IP address - Filter by port number - Filter out data payload from header, etc.</p><p>Does wireshark even have a way to make this easy?</p><p>And (should be simple): How to log raw binary packet captures?</p><p>Thanks lots</p><p>Eric</p></div><div id="question-tags" class="tags-container tags">filtering dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/741628fb897b52c2efdab6720c63265c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricFowler&#39;s gravatar image" /><p>EricFowler<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricFowler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 18:09</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20712" class="comments-container"></div><div id="comment-tools-20712" class="comment-tools"></div><div class="clear"></div><div id="comment-20712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20717"></span>

<div id="answer-container-20717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20717-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does wireshark even have a way to make this easy?</p></blockquote><p>There are several ways. Some are easier than others.</p><ul><li>Write your own dissector in C (rather hard)</li><li>Write your own dissector in Lua (easier than in C)</li><li>Use the generic dissector: <a href="http://wsgd.free.fr/">http://wsgd.free.fr/</a> (rather simple)</li></ul><p>I'm not sure if the generic dissector will solve all your problems/requirements, but it is for sure easy to start with.</p><blockquote><p>And (should be simple): How to <strong>log raw binary packet captures</strong>?</p></blockquote><p>What do you mean by that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 13:33</p></div></div><div id="comments-container-20717" class="comments-container"></div><div id="comment-tools-20717" class="comment-tools"></div><div class="clear"></div><div id="comment-20717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20722"></span>

<div id="answer-container-20722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20722-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I cannot (but would like to): - Filter by IP address - Filter by port number - Filter out data payload from header, etc.</p></blockquote><p>What do you mean by "filter"?</p><p>"Filter by IP address" and "Filter by port number" sound as if they mean either "capture only packets to/from/both a particular IP address/port number" or "in a capture I have, show me only the packets to/from/both a particular IP address/port number". Both of those should be possible with Wireshark, e.g. a capture filter of <code>host XXX.XXX.XXX.XXX</code> to capture traffic to or from IP address XXX.XXX.XXX.XXX or <code>udp port YYY</code> to capture traffic to or from UDP port YYY, or a display filter of <code>ip.addr == XXX.XXX.XXX.XXX</code> to show traffic to or from IP address XXX.XXX.XXX.XXX or <code>udp.port == YYY</code> to show traffic to or from UDP port YYY.</p><p>You can also search for packets to or from a particular IP address or UDP port - "Find packet by display filter", in the "Find Packet" dialog, lets you search for packets that match an arbitrary display filter address, such as <code>ip.addr == XXX.XXX.XXX.XXX</code> or <code>udp.port == YYY</code>, just as that dialog lets you search by strings and hex data.</p><p>"Filter out data payload from header" is a completely different type of filtering; Wireshark shows complete packets, so there's no way to do that. What you can do, however, is, in the packet detail pane, not open up anything other than the bottommost tree item, which, for the packets you're interested in, will probably just be "Data", below "UDP", unless some other dissector happens to claim those packets.</p><p>You could also, as Kurt suggests, write your own dissector for that protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 19:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20722" class="comments-container"></div><div id="comment-tools-20722" class="comment-tools"></div><div class="clear"></div><div id="comment-20722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

