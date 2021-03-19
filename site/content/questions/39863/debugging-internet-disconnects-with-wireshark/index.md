+++
type = "question"
title = "Debugging internet disconnects with wireshark"
description = '''Hello, we have been experiencing problems with our home network and I am now reaching out for help in tracing the problem. The problem is that atleast two computers on the home network are getting disconnected on a regular basis (some days it happens more frequently and some days it doesn&#x27;t happen a...'''
date = "2015-02-14T13:30:00Z"
lastmod = "2015-02-15T01:46:00Z"
weight = 39863
keywords = [ "arp", "isatap", "disconnected", "nbns" ]
aliases = [ "/questions/39863" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Debugging internet disconnects with wireshark](/questions/39863/debugging-internet-disconnects-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39863-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, we have been experiencing problems with our home network and I am now reaching out for help in tracing the problem. The problem is that <strong>atleast</strong> two computers on the home network are getting disconnected on a regular basis (some days it happens more frequently and some days it doesn't happen at all. By disconnected I mean that the internet stops working (e.g. a YouTube video stops playing, a game loses connection to the server etc, but it never says that the computer was disconnected from the router network name). When a computer gets disconnected, it still works on all the other computers (not every device on the network is affected by each disconnect).</p><p>Today the problem happened when I watched a YouTube video (the video stopped playing with an error message). I opened up WireShark and started capturing and this is what I got:</p><p>Below are links to 4 images from the capture (I'm sorry to have to link to these instead of embedding them as images, but the image size looked weird when I tried to do that).</p><p>My computer sends ARP requests asking for the owner of the routers IP (192.168.1.9): <a href="http://i.imgur.com/4IDr8uQ.png">imgur</a></p><p>There's also some NBNS (netbios?) packets from the other computer which also experiences the problems (but <strong>not</strong> at the time of this capture) - Another fact: we tried disabling Netbios on that computer but we still get these ISATAP messages: <a href="http://i.imgur.com/PEuk3GV.png">imgur</a></p><p>After a while, lets say 30 seconds, the router responds to my ARP requests and I can then use the internet again: <a href="http://i.imgur.com/No3Tcf9.png">imgur</a></p><p>The NBNS packets still continues after the ARP respond: <a href="http://i.imgur.com/HkCLXRK.png">imgur</a></p><p>To clarify:</p><p>192.168.1.236 was the computer experiencing the problem and the machine which captured the logs with WireShark (runs a linux distribution)</p><p>192.168.1.34 the machine sending the NBNS packets (which may not be related to the problem at all) (runs Windows 7)</p><p>My question is: Is it possible to draw any conclusion from this log as to what the problem may be? Is it possible to narrow down the search to finding the problem? What else can I do to track the problem?</p><p>Thank you in advance for any information you can share on this subject!</p></div><div id="question-tags" class="tags-container tags">arp isatap disconnected nbns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '15, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/859ee129ae90ce828f9d59fcaa913223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steelman&#39;s gravatar image" /><p>steelman<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steelman has no accepted answers">0%</span></p></div></div><div id="comments-container-39863" class="comments-container"></div><div id="comment-tools-39863" class="comment-tools"></div><div class="clear"></div><div id="comment-39863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39866"></span>

<div id="answer-container-39866" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39866-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ARP is used to find the mac-address (ethernet hardware address) of a system. If 192.168.1.9 is your router to the rest of the world. When your system 192.168.1.236 is ARPing for 192.168.1.9, it means it timed out the entry for 192.168.1.9 from its cache (this is normal behavior to make sure you have the right address in the cache even when the network has changed). So far, so good.</p><p>The fact that your router is not quickly responding to the ARP request is the source of your disconnects. Without the ARP response, you system does not know anymore where to send the data destined to the Internet anymore. Since YouTube works with TCP, your system still needs to send ACK frames telling YouTube that it received data packets.</p><p>Have a look at the router firmware version and check whether there is a newer version available that might solve this issue. If there is not, you might want to raise a support call with the vendor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '15, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39866" class="comments-container"></div><div id="comment-tools-39866" class="comment-tools"></div><div class="clear"></div><div id="comment-39866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

