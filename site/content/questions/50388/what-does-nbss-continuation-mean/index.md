+++
type = "question"
title = "What does NBSS continuation mean?"
description = '''opensuse v42.1 linux 4.1.15-8-default x86_64 wireshark 1.12.9 virtualbox 5.0.14 Wireshark is running on the linux side. I have been having difficulty with netbios and tcp writes from an ancient OS/2 system running in VirtualBox. Sometimes the writes perform as expected; other times they stall. I hav...'''
date = "2016-02-21T13:57:00Z"
lastmod = "2016-02-22T17:19:00Z"
weight = 50388
keywords = [ "dropped_packet", "tcp" ]
aliases = [ "/questions/50388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What does NBSS continuation mean?](/questions/50388/what-does-nbss-continuation-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>opensuse v42.1 linux 4.1.15-8-default x86_64 wireshark 1.12.9 virtualbox 5.0.14</p><p>Wireshark is running on the linux side.</p><p>I have been having difficulty with netbios and tcp writes from an ancient OS/2 system running in VirtualBox. Sometimes the writes perform as expected; other times they stall.</p><p>I have some PCAPs that capture both success and failure to write to the network. In one case it is a netbios send; in another it is a TCP connection from SVN. I do not know (yet) what is expected in this forum for displaying packet info.</p><p>In both cases it proceeds normally until, well, <em>something</em>, happens. Instead of proceeding with the data transfer, the resulting packet proclaims "[TCP Previous segment not captured] NBSS" rather than the expected data packet.</p><p>11 2016-02-21 12:40:28.433429 192.168.69.236 192.168.69.245 NBSS [TCP Previous segment not captured] NBSS Continuation Message</p><p>Shortly thereafter is a packet indicating "[TCP Dup ACK 10#1] 139→51555 [ACK] Seq=389". Sometimes there is another DUP packet. By this time the session is a mess, and eventually times out.</p><p>The SVN failure packet is</p><p>19 2016-02-21 14:50:10.913572 192.168.69.236 74.101.171.114 TCP [TCP Previous segment not captured] 51560→3690 [PSH, ACK] Seq=3342 Ack=401 Win=33580 Len=1176</p><p>Does this imply a fault on the sender's side (OS/2), trying to recover from a dropped packet? And failing?</p><p>Or is it a Wireshark error, failing to capture the packet?</p><p>Or ...?</p></div><div id="question-tags" class="tags-container tags">dropped_packet tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '16, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/730b660be92239491830262053868575?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimoe&#39;s gravatar image" /><p>jimoe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimoe has no accepted answers">0%</span></p></div></div><div id="comments-container-50388" class="comments-container"></div><div id="comment-tools-50388" class="comment-tools"></div><div class="clear"></div><div id="comment-50388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50422"></span>

<div id="answer-container-50422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50422-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can't say for certain, but, in this case, given the networking problems you're describing, "NBSS Continuation Message" probably means that the "previous segment" wasn't captured because it didn't make it to the machine running Wireshark, i.e. a packet got lost in transit between 192.168.69.236 and 192.168.69.245.</p><p>Wireshark couldn't reassemble the message (NetBIOS Session Service, "NBSS", over TCP - port 139 - which is used to transport SMB in older systems such as OS/2) because the chunk was missing, but it inferred from port 139 that it's NBSS, so it assumed it was a continuation of an earlier message as it didn't begin with an SMB header. It probably <em>was</em> a continuation, but there was a piece missing before it.</p><p>I suspect that if you look at the TCP layer of those packets, there will be some TCP analysis information indicating a missing packet.</p><p>Is Linux the host and OS/2 the guest? Or are they both guests on the same host talking to each other? Or is there actual communication over a physical network? If it's host &lt;-&gt; guest or guest &lt;-&gt; guest, there's no physical network, so packet drops at the "physical" layer are just VirtualBox issues. However, there might instead be a problem with one of the TCP layers.</p><blockquote><p>Does this imply a fault on the sender's side (OS/2), trying to recover from a dropped packet? And failing?</p></blockquote><p>We'd probably have to see the full dissection of the packets in question, but I suspect from the duplicate ACKs that something's going on at the TCP layer.</p><blockquote><p>I do not know (yet) what is expected in this forum for displaying packet info.</p></blockquote><p>It's probably best to upload the raw capture to some online storage service and post the URL here, <em>if</em> you're willing and able to make the capture public; that way, we can see all the details without having to deal with a big text dump or screenshot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 17:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50422" class="comments-container"><span id="50424"></span><div id="comment-50424" class="comment"><div id="post-50424-score" class="comment-score"></div><div class="comment-text"><p>Here is a link to two PCAPs for a file transfer, a write from local os/2 to the remote system. One is the successful transfer, the other when it failed.</p><p><a href="https://www.dropbox.com/sh/b6t28azor5x6swv/AACwEycyRdj5I27KDkztVZ1aa?dl=0">https://www.dropbox.com/sh/b6t28azor5x6swv/AACwEycyRdj5I27KDkztVZ1aa?dl=0</a></p><p>linux is hosting VirtualBox; os/2 is a guest. As a side note, we have 4 other similar installations that are also displaying this issue. And one that does not: an OSX host with a os/2 guest; it runs fine.</p><p>The connection is very short: os/2 to host to destination (a linux-based NAS unit). Because the OSX setup functions normally, it has made me suspect something about the vbox network interface. Which is why I am investigating this with wireshark.</p><p>Wireshark is running on the host, linux OS. I would presume, then, that the packet is somehow being lost from the destination to the host. It would seem almost impossible given how little hardware is in between.</p></div><div id="comment-50424-info" class="comment-info"><span class="comment-age">(22 Feb '16, 20:39)</span> jimoe</div></div><span id="50425"></span><div id="comment-50425" class="comment"><div id="post-50425-score" class="comment-score"></div><div class="comment-text"><p>It looks as if, in the failing case, the first two TCP segments of an SMB Write are getting lost, and the server is sending two duplicate ACKs to try to trigger a <a href="https://en.wikipedia.org/wiki/Fast_retransmit">"fast retransmit"</a>.</p><p>So Wireshark is running on the machine in the middle (the host), and it's <em>not</em> seeing the packets, so they're <em>probably</em> getting out somewhere between the OS/2 box and the host. Whether that's an OS/2 problem or a VirtualBox problem - or a Linux problem, or a VirtualBox-on-Linux problem, as it's not happening with an OS X host - I don't know.</p></div><div id="comment-50425-info" class="comment-info"><span class="comment-age">(22 Feb '16, 22:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-50422" class="comment-tools"></div><div class="clear"></div><div id="comment-50422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

