+++
type = "question"
title = "Using BPF on a .pcap file"
description = '''So I have a whatever.pcap file and load it into Wireshark. I do not want to use the native Wireshark display filters, but use BPF to filter through my traffic. I know I can use BPF to filter traffic during the capture, but I want to be able to use it after the capture as well.  Is there a way to do ...'''
date = "2012-06-06T12:45:00Z"
lastmod = "2012-06-06T18:49:00Z"
weight = 11723
keywords = [ "filtering", "bpf" ]
aliases = [ "/questions/11723" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Using BPF on a .pcap file](/questions/11723/using-bpf-on-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11723-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I have a whatever.pcap file and load it into Wireshark. I do not want to use the native Wireshark display filters, but use BPF to filter through my traffic.</p><p>I know I can use BPF to filter traffic during the capture, but I want to be able to use it after the capture as well.</p><p>Is there a way to do this?</p></div><div id="question-tags" class="tags-container tags">filtering bpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/52ed6c357139a816973503834d804ce2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wormy638&#39;s gravatar image" /><p>wormy638<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wormy638 has no accepted answers">0%</span></p></div></div><div id="comments-container-11723" class="comments-container"></div><div id="comment-tools-11723" class="comment-tools"></div><div class="clear"></div><div id="comment-11723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11728"></span>

<div id="answer-container-11728" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>tcpdump -r {your pcap file} -w {a filtered pcap file} {libpcap-style filter expression}</code></pre><p>and then read the filtered file in Wireshark. There's no way to do that in Wireshark, and there probably never will be, for the reasons noted in the other answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jun '12, 18:50</p></div></div><div id="comments-container-11728" class="comments-container"><span id="11737"></span><div id="comment-11737" class="comment"><div id="post-11737-score" class="comment-score">1</div><div class="comment-text"><p>Well, this could be an applicable real-life problem: I'm making a capture at one point in the network (using a capture filter to get rid of uninteresting stuff), while my co-worker does it at his end. After a lot of testing we've been able to reproduce the problem (Yeah!). Now I have two files to compare, where the co-workers' file has all this extra 'crap' in it, because he forgot to apply the agreed capture filter (#&amp;$#%*!). Now I want to post-BPF it before starting my comparison.</p></div><div id="comment-11737-info" class="comment-info"><span class="comment-age">(07 Jun '12, 04:33)</span> Jaap ♦</div></div><span id="11767"></span><div id="comment-11767" class="comment"><div id="post-11767-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Now I want to post-BPF it before starting my comparison.</p></blockquote><p>The code to filter on BPF is already there and if one adds a file read option to dumpcap (-r, pcap_open_offline()), it would be possible to have that functionality in wireshark/tshark too, right? Would such an option break something in dumpcap?</p></div><div id="comment-11767-info" class="comment-info"><span class="comment-age">(08 Jun '12, 06:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11728" class="comment-tools"></div><div class="clear"></div><div id="comment-11728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11725"></span>

<div id="answer-container-11725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11725-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there is no way to do this within the Wireshark GUI. The only place you can enter filters in BPF syntax is in the capture filter field.</p><p>This sounds like a solution in search of a problem. The only reason I can think of to avoid display filter syntax is to avoid the learning curve. However, a little time invested in learning display filter syntax is well worth the effort. Wireshark display filters have many, many more options than capture filters and are much more flexible and powerful.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-11725" class="comments-container"></div><div id="comment-tools-11725" class="comment-tools"></div><div class="clear"></div><div id="comment-11725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

