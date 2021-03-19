+++
type = "question"
title = "tshark: write packets matching a filter"
description = '''Greetings. On a production system, I&#x27;m using &quot;dumpcap -i any -b ...&quot; to capture all network traffic on the machine and write it to a rotating set of files, so I have a set of files containing all of the network traffic for the previous few hours. I need to know how to read one or more of these files...'''
date = "2012-10-02T12:47:00Z"
lastmod = "2012-10-02T20:06:00Z"
weight = 14645
keywords = [ "filter", "mergecap", "tshark" ]
aliases = [ "/questions/14645" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: write packets matching a filter](/questions/14645/tshark-write-packets-matching-a-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings.</p><p>On a production system, I'm using "dumpcap -i any -b ..." to capture all network traffic on the machine and write it to a rotating set of files, so I have a set of files containing all of the network traffic for the previous few hours.</p><p>I need to know how to read one or more of these files, filter out specific types of traffic (based on client IP address), and write the matching packets to a new pcap file which contains only the matching packets.</p><p>The closest I have so far is this:</p><p>mergecap -w- live*.pcap | tshark -i- -R 'ip.addr==1.2.3.4' -w 1.2.3.4.pcap</p><p>What I have found is that, without the "-w" option, the output (lines of text describing each packet) contains only the selected packets. However, with the "-w" option, the output contains every packet from the input, whether it matches the filter or not.</p><p>How can I get just the packets which match a specific filter?</p></div><div id="question-tags" class="tags-container tags">filter mergecap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/ce59c91e99c16b1583a4c61c95b61928?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jms1&#39;s gravatar image" /><p>jms1<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jms1 has one accepted answer">100%</span></p></div></div><div id="comments-container-14645" class="comments-container"></div><div id="comment-tools-14645" class="comment-tools"></div><div class="clear"></div><div id="comment-14645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14652"></span>

<div id="answer-container-14652" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14652-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is the CentOS 6 "base" yum repository, which is hideously out of date. It contains wireshark version 1.0.15.</p><p>I just tried it with wireshark 1.8.3, and the following command line works:</p><p>mergecap -a -F libpcap -w- live*.pcap | tshark -r- -R 'ip.addr==1.2.3.4' -w 1.2.3.4.pcap</p><p>Note that I also tried it with 1.8.2 on a laptop where wireshark had been installed previously, the same command fails with this error message:</p><p>tshark: The file "-" could not be opened: Illegal seek.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '12, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/ce59c91e99c16b1583a4c61c95b61928?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jms1&#39;s gravatar image" /><p>jms1<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jms1 has one accepted answer">100%</span></p></div></div><div id="comments-container-14652" class="comments-container"><span id="14660"></span><div id="comment-14660" class="comment"><div id="post-14660-score" class="comment-score"></div><div class="comment-text"><p>The code used by Wireshark and TShark to read capture files tries to determine the file type by having code for all the file types it understands read some of the file and indicate whether it's of that type or not. This involves each of those code modules rewinding the file and reading from it; pipes do not support seeks, so it might fail.</p><p>1.8.0 and later allow seeking within buffered data read into memory, so it might work in some cases (cases where not <em>too</em> much data was read); what does "tshark -v" print on the machine where you got "Illegal seek"?</p></div><div id="comment-14660-info" class="comment-info"><span class="comment-age">(03 Oct '12, 01:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14652" class="comment-tools"></div><div class="clear"></div><div id="comment-14652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

