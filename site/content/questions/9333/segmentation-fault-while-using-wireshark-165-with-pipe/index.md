+++
type = "question"
title = "Segmentation Fault while using Wireshark 1.6.5 with PIPE"
description = '''I am using Wireshark 1.6.5 in Ubuntu and here is my capture setting: I start Wireshark from the command line as: ./wireshark -k -i /tmp/pipe After starting Wireshark I dump the contents of a capture file (in libpcap format) into the pipe on which Wireshark listens.  Wireshark displays the packets he...'''
date = "2012-03-03T12:30:00Z"
lastmod = "2012-03-05T07:56:00Z"
weight = 9333
keywords = [ "pipe", "virtualbox", "ubuntu" ]
aliases = [ "/questions/9333" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Segmentation Fault while using Wireshark 1.6.5 with PIPE](/questions/9333/segmentation-fault-while-using-wireshark-165-with-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9333-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.6.5 in Ubuntu and here is my capture setting:</p><p>I start Wireshark from the command line as: <code>./wireshark -k -i /tmp/pipe</code></p><p>After starting Wireshark I dump the contents of a capture file (in libpcap format) into the pipe on which Wireshark listens.</p><p>Wireshark displays the packets here but at the end it throws segmentation fault? I have used older version of Wireshark in similar fashion and it worked perfectly fine.</p><p>So could some one tell me if there is a bug or am I going wrong somewhere here?</p><p>Adding to my question: I found about <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6002">this bug</a> in Wireshark 1.6.1 change log : "Cannot Live-capture VirtualBox network packets with Wireshark; pipe problem."</p><p>I am running Ubuntu on a Virtual Box. Does this have anything to do with the error I'm getting?</p></div><div id="question-tags" class="tags-container tags">pipe virtualbox ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '12, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/83e04f89cabcf71f8efd2238a88905ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v%20j&#39;s gravatar image" /><p>v j<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v j has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '12, 22:35</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-9333" class="comments-container"><span id="9347"></span><div id="comment-9347" class="comment"><div id="post-9347-score" class="comment-score"></div><div class="comment-text"><p>How do you dump the capture file contents into the pipe?</p></div><div id="comment-9347-info" class="comment-info"><span class="comment-age">(04 Mar '12, 22:36)</span> Jaap ♦</div></div></div><div id="comment-tools-9333" class="comment-tools"></div><div class="clear"></div><div id="comment-9333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9360"></span>

<div id="answer-container-9360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9360-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5939">bug 5939</a>, and is fixed in the 1.6 branch, so the fix should be in a future 1.6.6 release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9360" class="comments-container"></div><div id="comment-tools-9360" class="comment-tools"></div><div class="clear"></div><div id="comment-9360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

