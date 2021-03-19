+++
type = "question"
title = "How to block DoS attacks using protocol SIGCOMP"
description = '''I captured a DoS attack against my gameserver. Always using protocol sigcomp. Only from one IP adress. The adress seems to be spoofed because a block in firewall doesn&#x27;t help! It causes some lag for my players on the server. I search a way to block incoming SIGCOMP Traffic. (on WINDOWS 2012 SERVER)....'''
date = "2015-01-18T04:55:00Z"
lastmod = "2015-01-18T09:12:00Z"
weight = 39240
keywords = [ "sigcomp" ]
aliases = [ "/questions/39240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to block DoS attacks using protocol SIGCOMP](/questions/39240/how-to-block-dos-attacks-using-protocol-sigcomp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a DoS attack against my gameserver. Always using protocol sigcomp. Only from one IP adress. The adress seems to be spoofed because a block in firewall doesn't help! It causes some lag for my players on the server.</p><p>I search a way to block incoming SIGCOMP Traffic. (on WINDOWS 2012 SERVER). This compression protocol is used/abused to perform the attack, because I don't have a chance to ban the IP.</p><p>How to block DoS attacks using protocol SIGCOMP</p></div><div id="question-tags" class="tags-container tags">sigcomp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '15, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/33f35d7902cb0190229646e7ce7d9b1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="appreciated&#39;s gravatar image" /><p>appreciated<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="appreciated has no accepted answers">0%</span></p></div></div><div id="comments-container-39240" class="comments-container"></div><div id="comment-tools-39240" class="comment-tools"></div><div class="clear"></div><div id="comment-39240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39247"></span>

<div id="answer-container-39247" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39247-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That all depends on your setup and the actual DoS traffic.</p><ul><li>If the (D)DoS traffic is filling up your bandwidth, filtering the packets just before they reach your server will not help you, as your uplink is still saturated by the traffic. You will need the help of your (upstream) provider or a (D)DoS scrubbing center to remove the (D)DoS traffic</li><li>If the SIGCOMP traffic is actually just overloading your server and it is not part of your normal traffic, you can filter the traffic on your router with an access-list using the port number of the traffic.</li></ul><p>Any other scenario needs further analysis and careful action to not block legitimate traffic while trying out to filter the (D)DoS traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39247" class="comments-container"><span id="39259"></span><div id="comment-39259" class="comment"><div id="post-39259-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to block that traffic with Snort for example?</p><p>OVH already got my Wireshark logs [at] antiddos but they even doesn't answer since weeks. DDOS attacks are mitigated by DDOS protection, but this "smaller" attacks get not mitigated and I can't ban the IP (I think it's spoofed 90% IPs from China or Russia). I don't have access to router or hardware firewall, it is a dedicated windows 2012 server with ddos protection/mitigation included. The attacks use protocol SIGCOMP or QUIC. (Quic is the protocol which is used with "LOIC" for example too.</p></div><div id="comment-39259-info" class="comment-info"><span class="comment-age">(18 Jan '15, 20:47)</span> appreciated</div></div><span id="39268"></span><div id="comment-39268" class="comment"><div id="post-39268-score" class="comment-score">1</div><div class="comment-text"><p>(I converted your "answer" to a "comment", please refer to the FAQ)</p><p>Are you able to share a capture file with the presumed DoS traffic in it? Different attacks call for different anti-ddos measures. You can upload a tracefile to www.cloudshark.org and paste the link here in a comment.</p></div><div id="comment-39268-info" class="comment-info"><span class="comment-age">(19 Jan '15, 01:22)</span> SYN-bit ♦♦</div></div><span id="39307"></span><div id="comment-39307" class="comment"><div id="post-39307-score" class="comment-score">1</div><div class="comment-text"><p>Since it is all UDP traffic, it can be spoofed very easily. The traffic you think is SIGCOMP is just interpreted by Wireshark as SIGCOMP as it is sent to a port that Wireshark dissects as SIGCOMP. In fact the data part of the packet to port 6666 (dissected as SIGCOMP) and port 6688 is 0xffffffff55 in both cases. If this is not normal traffic to your game server, then you could block udp traffic with exactly this payload (on any port).</p><p>If this can be valid traffic, then you need something more advanced like threshold based blocking or maybe even something that can follow the state of a session to your server and if a session is not established within a certain time limit, block the IP for a while.</p><p>Whether you will be able to do this with the tools at hand is another question. You might need to invest in a more advanced infrastructure to be able to protect your game-server.</p></div><div id="comment-39307-info" class="comment-info"><span class="comment-age">(19 Jan '15, 14:10)</span> SYN-bit ♦♦</div></div><span id="39311"></span><div id="comment-39311" class="comment"><div id="post-39311-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your analyse!</p><p>Your wrote: "If this is not normal traffic to your game server, then you could block udp traffic with exactly this payload (on any port."</p><p>That's the way I would like to try first!</p><p>The problem is the attack is to "small" so the DDOS protection from OVH can't block it. (It's a dedicated server even with DDOS protection.</p><p>Do you think "Snort" is the right tool for that or know another way to do so?</p><p>I thought first I could make an ACL Rule with Wireshark but I don't think this will block the special payload?</p><p>==&gt; I am searching for a way to block special payloads or data send to some ports SINCE WEEKS! It would help a lot because some older game engines can be easily crashed while sending special sequences to some ports belonging to the game.</p><p>This for example is deadly for me. Sending to UDP Port and gameserver will crash... or reboot. It's an attack against the game engine.</p><p>\secure\aaaaaaaaaaaaaaaaa</p><p>(and some letters more I don't want to write all in public because I have no fix and can't block it now)</p><p>So a solution to block special payloads or traffic would help in both cases I think. (at least the last one)</p></div><div id="comment-39311-info" class="comment-info"><span class="comment-age">(19 Jan '15, 16:27)</span> appreciated</div></div><span id="39321"></span><div id="comment-39321" class="comment"><div id="post-39321-score" class="comment-score">1</div><div class="comment-text"><p>Yes, snort should be able to block specific payload patterns like the one in the tracefile or the one you mentioned in your last comment.</p></div><div id="comment-39321-info" class="comment-info"><span class="comment-age">(20 Jan '15, 10:18)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-39247" class="comment-tools"></div><div class="clear"></div><div id="comment-39247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

