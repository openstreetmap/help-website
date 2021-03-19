+++
type = "question"
title = "Tshark statistics to show port numbers?"
description = '''My apologies if this comes off as an overly newb question. I have been tasked by coworker to take a repository of pcaps and provide output from them in the form of... src ip:src port dst ip:dst port # of packets  I played around with piping tcpdump to grep for a while before figuring out that tshark...'''
date = "2011-08-25T14:15:00Z"
lastmod = "2011-08-25T14:56:00Z"
weight = 5875
keywords = [ "statistics", "tshark", "ports" ]
aliases = [ "/questions/5875" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark statistics to show port numbers?](/questions/5875/tshark-statistics-to-show-port-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5875-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My apologies if this comes off as an overly newb question. I have been tasked by coworker to take a repository of pcaps and provide output from them in the form of...</p><pre><code>src ip:src port    dst ip:dst port    # of packets</code></pre><p>I played around with piping tcpdump to grep for a while before figuring out that tshark might be far easier, and I've managed to get the output that I need with the exception of the source and destination ports.</p><p>The command that I've used is...</p><pre><code>tshark -r file.pcap -z conv,ip -q</code></pre><p>The output would be perfect if I could get it to display ports numbers beside each IP. I've been digging through the man pages with little luck so far. If anyone can recommend a solution, I would be most appreciative.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">statistics tshark ports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '11, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/52c23a5bff4bdbfe732d41509c7392b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark&#39;s gravatar image" /><p>Mark<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark has no accepted answers">0%</span></p></div></div><div id="comments-container-5875" class="comments-container"></div><div id="comment-tools-5875" class="comment-tools"></div><div class="clear"></div><div id="comment-5875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5876"></span>

<div id="answer-container-5876" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5876-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simple: (assuming you're referring to TCP ports) try</p><pre><code>tshark -r file.pcap -z conv,tcp -q</code></pre><p>:)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Aug '11, 14:57</p></div></div><div id="comments-container-5876" class="comments-container"><span id="5877"></span><div id="comment-5877" class="comment"><div id="post-5877-score" class="comment-score"></div><div class="comment-text"><p>The TShark command to do this for UDP ports is left as an exercise for the reader. :-)</p></div><div id="comment-5877-info" class="comment-info"><span class="comment-age">(25 Aug '11, 17:53)</span> Guy Harris ♦♦</div></div><span id="5886"></span><div id="comment-5886" class="comment"><div id="post-5886-score" class="comment-score"></div><div class="comment-text"><p>Ever have one of those head-to-desk moments? I had one when I read that. Thank you, Bill! As an aside, is it possible to display multiple protocols with this? Something like...</p><p>-z conv,tcp&amp;udp</p></div><div id="comment-5886-info" class="comment-info"><span class="comment-age">(26 Aug '11, 08:17)</span> Mark</div></div><span id="5888"></span><div id="comment-5888" class="comment"><div id="post-5888-score" class="comment-score">2</div><div class="comment-text"><p>$ tshark -r http.pcap -q -z conv,tcp -z conv,udp<br />
<br />
See the TShark man-page for more information:<br />
http://www.wireshark.org/docs/man-pages/tshark.html</p></div><div id="comment-5888-info" class="comment-info"><span class="comment-age">(26 Aug '11, 10:27)</span> joke</div></div></div><div id="comment-tools-5876" class="comment-tools"></div><div class="clear"></div><div id="comment-5876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

