+++
type = "question"
title = "Format of data"
description = '''What is the format of data in wireshark capture file? The data is 18 bytes in my file. How to find another data with the help of this.'''
date = "2013-12-05T11:55:00Z"
lastmod = "2013-12-06T02:19:00Z"
weight = 27839
keywords = [ "data", "format" ]
aliases = [ "/questions/27839" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Format of data](/questions/27839/format-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27839-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the format of data in wireshark capture file? The data is 18 bytes in my file. How to find another data with the help of this.</p></div><div id="question-tags" class="tags-container tags">data format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/b0aee001bed393362d749d82a1f71d2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="R%C3%AC%C3%BD%C3%A0%20%C3%90ash%C3%B6R%C3%AC%C3%BD%C3%A3&#39;s gravatar image" /><p>Rìýà ÐashöRìýã<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rìýà ÐashöRìýã has no accepted answers">0%</span></p></div></div><div id="comments-container-27839" class="comments-container"><span id="27844"></span><div id="comment-27844" class="comment"><div id="post-27844-score" class="comment-score"></div><div class="comment-text"><p>Not sure I understand your question. You want to programmatically extract 'data' from a packet capture file? And you need the layout of the pcap file format? Can you upload your file to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and explain what you need to achieve in more detail?</p></div><div id="comment-27844-info" class="comment-info"><span class="comment-age">(05 Dec '13, 23:03)</span> mrEEde</div></div><span id="27845"></span><div id="comment-27845" class="comment"><div id="post-27845-score" class="comment-score"></div><div class="comment-text"><p>Yes! I need the layout probably! Actually the main question was to see one packet and write about its Ethernet frame. That will be my data 1. Next they asked data 2 is embedded in data 1. How to find this thing?</p></div><div id="comment-27845-info" class="comment-info"><span class="comment-age">(05 Dec '13, 23:09)</span> Rìýà ÐashöRìýã</div></div><span id="27852"></span><div id="comment-27852" class="comment"><div id="post-27852-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Next they asked data 2 is embedded in data 1. How to find this thing?</p></blockquote><p>Could you please add more details about the questions asked? Maybe just post the original question here. Otherwise it is hard to understand what you really need.</p></div><div id="comment-27852-info" class="comment-info"><span class="comment-age">(06 Dec '13, 02:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27839" class="comment-tools"></div><div class="clear"></div><div id="comment-27839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27849"></span>

<div id="answer-container-27849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27849-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the pcap file format description helps? I guess you're trying to parse frame content from a file in pcap format, which means that you need to read the file and frame headers, too. It's not just frame data in the files.</p><p>See this page: <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">http://wiki.wireshark.org/Development/LibpcapFileFormat</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '13, 01:07</p></div></div><div id="comments-container-27849" class="comments-container"></div><div id="comment-tools-27849" class="comment-tools"></div><div class="clear"></div><div id="comment-27849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27851"></span>

<div id="answer-container-27851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27851-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What is the format of data in wireshark capture file?</p></blockquote><p><a href="http://www.tcpdump.org/manpages/pcap-savefile.5.html">Pcap</a> and <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">pcap-ng</a> are the native file formats in Wireshark, although it can read a number of other file formats.</p><p>Libpcap and WinPcap can read pcap files; libpcap 1.1 and later (but not WinPcap) can also read some pcap-ng files. Most programs that need to read pcap or pcap-ng files should use libpcap or WinPcap rather than trying to handle the file formats themselves.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27851" class="comments-container"></div><div id="comment-tools-27851" class="comment-tools"></div><div class="clear"></div><div id="comment-27851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

