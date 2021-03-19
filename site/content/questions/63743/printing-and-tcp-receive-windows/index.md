+++
type = "question"
title = "Printing and TCP Receive Windows"
description = '''Hi all !! So I have the following scenario. A print server in Sydney Australia and Ricoh MP 5054 printers in a number of sites in Singapore. At one site, for all four printers, users were complaining that a large print job ( 26M ) was taking up to 3 mins to be sent from Sydney to start printing. The...'''
date = "2017-10-08T14:17:00Z"
lastmod = "2017-10-12T20:58:00Z"
weight = 63743
keywords = [ "printer", "tcp", "tcpwindowsize" ]
aliases = [ "/questions/63743" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Printing and TCP Receive Windows](/questions/63743/printing-and-tcp-receive-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63743-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all !!</p><p>So I have the following scenario. A print server in Sydney Australia and Ricoh MP 5054 printers in a number of sites in Singapore. At one site, for all four printers, users were complaining that a large print job ( 26M ) was taking up to 3 mins to be sent from Sydney to start printing. The same model printer at other sites took in the order of 20-30 seconds.</p><p>Latency is about 100ms between Sydney and SG. I have a NetShark in Sydney and so ran captures to all 5054 printers. According to both WireShark and Riverbed Packet Analyser, all four printers at the slow site were advertising a maximum TCP window size of 16KB. The other sites showed TCP RWIN of 196KB, thus explaining the dramatic difference in job transfer times. These values are completely different to the Printer IO buffer settings on the device itself which seem to bear no resemblance to what I am actually seeing on the wire ;-)</p><p>Before I go asking the remote team to start shifting a huge printer from one site to the other to prove my point, and making me look stupid if it doesnt fix the problem, 1 basic question... Can anything in the network change the advertised TCP window size that I am seeing from the printer in the captures ?</p><p>I capture the 3 way handshake, so scaling is not the issue, WS on the printers is 1. Or is this really a bad coincidence and case of a whole bad batch of printers at this site ? All firmware and settings are identical across all sites.</p><p>The TCP Receive Window size in a packet capture, provided scaling is catered for, doesnt lie right ;-)</p><p>Thanks all.</p></div><div id="question-tags" class="tags-container tags">printer tcp tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '17, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/bc94271046d66620f4be0a8dc1e58ad5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seandavies&#39;s gravatar image" /><p>Seandavies<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seandavies has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '17, 03:27</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63743" class="comments-container"></div><div id="comment-tools-63743" class="comment-tools"></div><div class="clear"></div><div id="comment-63743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63745"></span>

<div id="answer-container-63745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63745-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I agree that the TCP window size seems to be the problem here. Do you have captures close to the printers, or is all you have on the print server site? That would be required to prove that some device in the path messes up the receive window size. Or, to answer your question: yes, there may be devices that change the window size, e.g. load balancers, traffic shapers and other black boxes.</p><p>My recommendation would be to try to get a capture on the printer side, as close as possible to the printer itself (e.g. TAP on the cable to the printer, or SPAN on the same switch) to see if the device itself sends such a low window size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '17, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63745" class="comments-container"><span id="63775"></span><div id="comment-63775" class="comment"><div id="post-63775-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response Jasper !. Yes. That was the next thing I requested last Friday ( I posted this before getting the results ) ... I mirrored the printer port to another port on the same switch and got a capture from there. The results actually show the same result as the printer server side ( 16KB TCP RWIN ). Short of the switch itself doing something weird ( very unlikely ), I can only assume that eliminated any possible window size change by a random device. (UPDATE - the ack from the printer showing the 16KB RWIN actually comes from the Ricoh MAC address itself - so surely nothing would be changing the TCP RWIN size and not the source MAC address ? ;-) ) Next step today or tomorrow is to do exactly the same at another 'fast' site with the same printer and capture at the printer side again. If that result is as expected ( ie 196KB TCP RWIN ), then I am going to have to bite the bullet and get one of these working printers shipped over to the 'slow' site. Thank you for the sanity check and clarifying my thought process on this ;-) I am just watching your SF '13 Trace File Sanitisation preso just in case I need to post a capture file ;-) I will let you know what happens. Of course I hope its the printers and we have a bug, but I can see that the RWIN surely must be the issue here - the RWIN / latency almost exactly matches the throughput and transfer time experienced by the users - bandwidth is not problem ;-)</p></div><div id="comment-63775-info" class="comment-info"><span class="comment-age">(09 Oct '17, 14:45)</span> Seandavies</div></div></div><div id="comment-tools-63745" class="comment-tools"></div><div class="clear"></div><div id="comment-63745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63860"></span>

<div id="answer-container-63860" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63860-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So I discovered the answer ;-) After performing packet captures on a mirrored port of a printer at the 'fast' site I saw something interesting in the delta between the SYN/ACK from the printer and the ACK from the 'Print Server'. The delta was 0.07ms !! With a RTT between Sydney and Singapore of 150ms thats impossible right ?! ;-) So something on the LAN at the fast site was answering on behalf of the print server. That something happened to be WANx !! I thought of WANx initially but was lookng at things the wrong way round. I elimiated WANx from the equation because the slow site didnt have WANx ( I know my bad ). ALL the printers in fact have a TCP Receive window of 16KB ONLY, but WANx was effectively masking/fixing this inherent problem. Short of rolling out WANx to every single site just to fix print times - which is not cost effective for me - I have to go back to the vendor to persuade them to fix their issue. Looks like these printers are designed for local printing only and are extremely inefficient over high speed high latency links.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '17, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/bc94271046d66620f4be0a8dc1e58ad5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seandavies&#39;s gravatar image" /><p>Seandavies<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seandavies has no accepted answers">0%</span></p></div></div><div id="comments-container-63860" class="comments-container"></div><div id="comment-tools-63860" class="comment-tools"></div><div class="clear"></div><div id="comment-63860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

