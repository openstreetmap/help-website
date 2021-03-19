+++
type = "question"
title = "Need to convert a tcpdump text file to pcap file"
description = '''Hi All, I searched through and did not find this question asked aleady. Yesterday I received my very first tcpdump.txt file - up to this point all my captures were .pcap so I did not know what to do with that. Some research shows we have text2pcap... and I thought OK GREAT I will convert it...The co...'''
date = "2014-06-20T04:55:00Z"
lastmod = "2014-06-20T17:28:00Z"
weight = 33987
keywords = [ "text2pcap", "text", "pcap", "tcpdump" ]
aliases = [ "/questions/33987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need to convert a tcpdump text file to pcap file](/questions/33987/need-to-convert-a-tcpdump-text-file-to-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I searched through and did not find this question asked aleady. Yesterday I received my very first tcpdump.txt file - up to this point all my captures were .pcap so I did not know what to do with that. Some research shows we have text2pcap... and I thought OK GREAT I will convert it...The commands I have tried ..text2pcap tcpdump.txt tcpdump.pcap this actually returns Input from: tcpdump.txt Output to: tcpdump.pcap Output format: PCAP Read 170 potential packets, wrote 0 packets (24 bytes).</p><p>I have also tried adding in -a and some of the other options but nothing seems to work for me .. every time it returns a file it is 1KB. Can someone tell me if this is the correct tool to use for this and possibly how to use it? Or if there is a better way ..I have never worked with this type of file before.</p></div><div id="question-tags" class="tags-container tags">text2pcap text pcap tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/36c7386e74755c5bb1f8fc300a739ee2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bz6djs&#39;s gravatar image" /><p>bz6djs<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bz6djs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '14, 17:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-33987" class="comments-container"><span id="33990"></span><div id="comment-33990" class="comment"><div id="post-33990-score" class="comment-score"></div><div class="comment-text"><p>Hi,please look at this article, it may solve your problem ,<a href="http://ask.wireshark.org/questions/19054/tcpdump-to-pcap.">http://ask.wireshark.org/questions/19054/tcpdump-to-pcap.</a></p></div><div id="comment-33990-info" class="comment-info"><span class="comment-age">(20 Jun '14, 06:41)</span> kishan pandey</div></div></div><div id="comment-tools-33987" class="comment-tools"></div><div class="clear"></div><div id="comment-33987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34005"></span>

<div id="answer-container-34005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34005-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>text2pcap turns text in the form of <em>hex dumps</em> of packet contents into pcap files.</p><p>Unfortunately, that's probably not what you have; you probably have the result of tcpdump dissecting packets and, as <a href="http://ask.wireshark.org/questions/19054/tcpdump-to-pcap.">the article that was suggested as possibly "[solving] your problem"</a> says, the tcpdump dissection has probably <em>permanently discarded</em> data from the packet, so you probably will not be able to get a pcap file from it (i.e., it "solves" your problem by telling you it's insoluble).</p><p>In the future, make sure whoever makes captures with tcpdump for you to analyze uses the <code>-w</code> flag, so that tcpdump writes a pcap file with raw packet data rather than a text file with dissected packets.</p><p>In the present, learn the format of tcpdump output and see whether the text file tells you enough to let you analyze the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '14, 17:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34005" class="comments-container"></div><div id="comment-tools-34005" class="comment-tools"></div><div class="clear"></div><div id="comment-34005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

