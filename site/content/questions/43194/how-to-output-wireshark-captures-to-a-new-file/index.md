+++
type = "question"
title = "how to output wireshark captures to a new file ?"
description = '''i am using linux and i&#x27;m trying through the command line to capture certain number of packets and save them to a pcap file in a certain directory, i used this command but something is wrong it&#x27;s not being saved ! wireshark -f tcp -i eth1 -k -c 700 -w ~/dev/shm/new.pcap any help?'''
date = "2015-06-15T10:21:00Z"
lastmod = "2015-06-15T10:40:00Z"
weight = 43194
keywords = [ "output", "linux", "pcap", "wireshark" ]
aliases = [ "/questions/43194" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to output wireshark captures to a new file ?](/questions/43194/how-to-output-wireshark-captures-to-a-new-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am using linux and i'm trying through the command line to capture certain number of packets and save them to a pcap file in a certain directory, i used this command but something is wrong it's not being saved !</p><p>wireshark -f tcp -i eth1 -k -c 700 -w ~/dev/shm/new.pcap</p><p>any help?</p></div><div id="question-tags" class="tags-container tags">output linux pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '15, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-43194" class="comments-container"></div><div id="comment-tools-43194" class="comment-tools"></div><div class="clear"></div><div id="comment-43194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43195"></span>

<div id="answer-container-43195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43195-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please use dumpcap or tcpdump to capture frames on the CLI.</p><blockquote><p>dumpcap -ni eth1 -c 700 -w ~/new.pcap -f "tcp"<br />
tcpdump -ni eth1 -c 700 -w ~/new.pcap "tcp"</p></blockquote><p>BTW: If you are using the capture filter "tcp" and there is no TCP traffic on eth1, you won't see anything!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '15, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-43195" class="comments-container"></div><div id="comment-tools-43195" class="comment-tools"></div><div class="clear"></div><div id="comment-43195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

