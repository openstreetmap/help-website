+++
type = "question"
title = "Running Wireshark from Red Hat command line?"
description = '''I am running Red Hat Enterprise Linux Server release 5.6 (x86_64), and I installed Wireshark 1.0.15. I installed Wireshark by: yum install wireshark  Now when I try running following command line: wireshark -c 100 -k -Q -w –  I receive: (wireshark:25796): Gtk-WARNING **: cannot open display:  Any id...'''
date = "2013-03-11T12:18:00Z"
lastmod = "2013-03-11T23:41:00Z"
weight = 19361
keywords = [ "command", "line", "hat", "gui", "red" ]
aliases = [ "/questions/19361" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Running Wireshark from Red Hat command line?](/questions/19361/running-wireshark-from-red-hat-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19361-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Red Hat Enterprise Linux Server release 5.6 (x86_64), and I installed Wireshark 1.0.15.</p><p>I installed Wireshark by:</p><pre><code>yum install wireshark</code></pre><p>Now when I try running following command line:</p><pre><code>wireshark -c 100 -k -Q -w –</code></pre><p>I receive:</p><pre><code>(wireshark:25796): Gtk-WARNING **: cannot open display:</code></pre><p>Any ideas why it won't run from the command line? Do you need the GUI for Wireshark to work from the command line?</p></div><div id="question-tags" class="tags-container tags">command line hat gui red</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '13, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/7ddc340fc30c3dd8e9a6cec5f320e573?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakeland&#39;s gravatar image" /><p>lakeland<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakeland has no accepted answers">0%</span></p></div></div><div id="comments-container-19361" class="comments-container"></div><div id="comment-tools-19361" class="comment-tools"></div><div class="clear"></div><div id="comment-19361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19365"></span>

<div id="answer-container-19365" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19365-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you even have a $DISPLAY defined? Or do you intend to run it from a workstation? If you do you should make sure that the user running Wireshark (don't go with root here) has access right to the display server. Or allow the access at the workstation with <code>xhost</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19365" class="comments-container"><span id="19366"></span><div id="comment-19366" class="comment"><div id="post-19366-score" class="comment-score"></div><div class="comment-text"><p>and on a sidenote: yes, you do need the GUI to run Wireshark, no matter if by icon click, file association or command line. If you want a command line tool, run tshark instead.</p></div><div id="comment-19366-info" class="comment-info"><span class="comment-age">(11 Mar '13, 15:55)</span> Jasper ♦♦</div></div></div><div id="comment-tools-19365" class="comment-tools"></div><div class="clear"></div><div id="comment-19365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19369"></span>

<div id="answer-container-19369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>yum install wireshark</p></blockquote><p>As far as I know, the GUI version package is called <strong>wireshark-gnome</strong> on RHEL 5.6, whereas the package <strong>wireshark</strong> contains only the CLI tools (tshark, dumpcap, etc.). So, please run this command</p><blockquote><p><code>yum install wireshark-gnome</code><br />
</p></blockquote><p>Then you should be able to start wireshark from the CLI.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '13, 23:42</p></div></div><div id="comments-container-19369" class="comments-container"></div><div id="comment-tools-19369" class="comment-tools"></div><div class="clear"></div><div id="comment-19369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

