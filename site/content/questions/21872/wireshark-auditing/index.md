+++
type = "question"
title = "wireshark auditing"
description = '''Hi, i have dedicated linux server for running wireshark in order to do network analysis when needed. It has very restrictive access but anyway we would like to achieve some sort of logging of what and when are users capturing using wireshark on this machine. Since wireshark and its utilites are not ...'''
date = "2013-06-10T04:24:00Z"
lastmod = "2013-06-11T20:55:00Z"
weight = 21872
keywords = [ "security", "auditing", "logging" ]
aliases = [ "/questions/21872" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark auditing](/questions/21872/wireshark-auditing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21872-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i have dedicated linux server for running wireshark in order to do network analysis when needed. It has very restrictive access but anyway we would like to achieve some sort of logging of what and when are users capturing using wireshark on this machine. Since wireshark and its utilites are not providing any logging capabilities i wonder how can we achieve logging.</p><p>I was thinking about writing warpper around /usb/bin/dumpcap in order to generate syslog messages and spawn the real dumpcap binary. I think that would be stupid but simple solution so im looking for something more elegant.</p><p>It would be the best if wireshark would provide logging functionalities so I appeal to wireshark developers to think about it while im looking for alternatives.</p><p>Thank you in advance for tips and hints. klodovic</p></div><div id="question-tags" class="tags-container tags">security auditing logging</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '13, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/0817cf7965ef06a56ada1be48a4244bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klodovic&#39;s gravatar image" /><p>klodovic<br />
<span class="score" title="42 reputation points">42</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klodovic has no accepted answers">0%</span></p></div></div><div id="comments-container-21872" class="comments-container"></div><div id="comment-tools-21872" class="comment-tools"></div><div class="clear"></div><div id="comment-21872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21876"></span>

<div id="answer-container-21876" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21876-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I was thinking about writing <strong>wrapper around /usb/bin/dumpcap</strong></p></blockquote><p>Any wrapper solution can be bypassed by the users, by calling the binary itself, instead of the wrapper script.</p><p>I suggest to use the Linux auditing system: <code>http://doc.opensuse.org/products/draft/SLES/SLES-security_sd_draft/cha.audit.comp.html</code><br />
</p><blockquote><p>i have dedicated linux server for <strong>running wireshark</strong> in order <strong>to do network analysis</strong> when needed. It has very restrictive access</p></blockquote><p>As you mentioned, Wireshark is a network <strong>analysis/troubleshooting tool</strong>. Why would you want to restrict or log the use of Wireshark?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '13, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '13, 03:07</p></div></div><div id="comments-container-21876" class="comments-container"><span id="21883"></span><div id="comment-21883" class="comment"><div id="post-21883-score" class="comment-score"></div><div class="comment-text"><p>Network monitoring sessions are privacy concern of many users who are being monitored. So the process of monitoring has to be approved and supervised by person who is not network analyst itself and session must be covered with auditing logs in order to satisfy user's privacy concern and to let network analysts know that they have been supervised.</p></div><div id="comment-21883-info" class="comment-info"><span class="comment-age">(10 Jun '13, 09:15)</span> klodovic</div></div><span id="21888"></span><div id="comment-21888" class="comment"><div id="post-21888-score" class="comment-score"></div><div class="comment-text"><p>Thank you, auditd is the right thing!</p></div><div id="comment-21888-info" class="comment-info"><span class="comment-age">(10 Jun '13, 10:39)</span> klodovic</div></div><span id="21889"></span><div id="comment-21889" class="comment"><div id="post-21889-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Network monitoring sessions are privacy concern of many users who are being monitored</p></blockquote><p>be careful not to make a 'logical error' by believing that restricted or logged access to wireshark will solve your security issues! In fact that kind of logging/restriction will not stop a user to sniff the network with a private laptop, <strong>unless</strong> you have appropriate security solutions in place in your network that prevent it (as far as possible).</p></div><div id="comment-21889-info" class="comment-info"><span class="comment-age">(10 Jun '13, 11:30)</span> Kurt Knochner ♦</div></div><span id="21891"></span><div id="comment-21891" class="comment"><div id="post-21891-score" class="comment-score"></div><div class="comment-text"><p>Im aware of that. Thank you anyway for pointing out!</p></div><div id="comment-21891-info" class="comment-info"><span class="comment-age">(10 Jun '13, 11:45)</span> klodovic</div></div><span id="21945"></span><div id="comment-21945" class="comment"><div id="post-21945-score" class="comment-score"></div><div class="comment-text"><p>I think the key there is that it's a dedicated server. Most likely it's the only system in the line of path to receive the sensitive data in question, so it becomes a matter of securing access to capturing data on that server, not sniffing the network on a laptop. Of course, plugging a laptop into the server's network cables physically is going to be possible, but physical security is always a hard thing to account for.</p></div><div id="comment-21945-info" class="comment-info"><span class="comment-age">(11 Jun '13, 20:44)</span> Quadratic</div></div></div><div id="comment-tools-21876" class="comment-tools"></div><div class="clear"></div><div id="comment-21876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21946"></span>

<div id="answer-container-21946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21946-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One solution is that you could limit dumpcap to only be executable by root and a system account, write your wrapper with your log file push, and set the wrapper with a sticky bit to run as that special system user when calling dumpcap. That way the binary is locked down for direct access and you force the wrapper on people.</p><p>I think the key for those other security concerns in comments is that it's a dedicated server. Most likely it's the only system in the line of path to receive the sensitive data in question, so it becomes a matter of securing access to capturing data on that server, not sniffing the network on a laptop. If that's the case, especially since you already have an approval process you might even consider disabling the feeds into the server that have the sensitive data and enable them (taps, span ports, whatever) as part of the approval process for performing the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21946" class="comments-container"></div><div id="comment-tools-21946" class="comment-tools"></div><div class="clear"></div><div id="comment-21946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

