+++
type = "question"
title = "Wireshark and Linux"
description = '''I am trying to open Wireshark in the command prompt using sudo -i Wireshark, but it keeps telling me command not found. When I type in just Wireshark, the program will open. Any idea why I cannot open Wireshark via sudo command?'''
date = "2013-09-25T13:38:00Z"
lastmod = "2013-09-25T14:01:00Z"
weight = 25242
keywords = [ "sudo", "wireshark", "linux" ]
aliases = [ "/questions/25242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and Linux](/questions/25242/wireshark-and-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25242-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to open Wireshark in the command prompt using sudo -i Wireshark, but it keeps telling me command not found. When I type in just Wireshark, the program will open. Any idea why I cannot open Wireshark via sudo command?</p></div><div id="question-tags" class="tags-container tags">sudo wireshark linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/abe541c78b1c639c6b2fbf7750095d5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renee&#39;s gravatar image" /><p>Renee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '13, 14:04</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-25242" class="comments-container"></div><div id="comment-tools-25242" class="comment-tools"></div><div class="clear"></div><div id="comment-25242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25243"></span>

<div id="answer-container-25243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25243-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>sudo -i Wireshark</p></blockquote><p>You write Wireshark with an uppercase W, while the binary is called <strong>wireshark</strong>. If that was just a typo in your question, what is the output of the following commands?</p><blockquote><p>which wireshark<br />
sudo wireshark<br />
sudo which wireshark</p></blockquote><p>I suspect the binary <strong>wireshark</strong> is not in the search path of the root user.</p><p>BTW: You should not run Wireshark as root. See here: <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p><p>If you don't see any interfaces as non-root, please run the following command (on Linux):</p><blockquote><p>sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap</p></blockquote><p>Please adjust the path, if dumpcap is not installed to /usr/bin.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '13, 15:14</p></div></div><div id="comments-container-25243" class="comments-container"></div><div id="comment-tools-25243" class="comment-tools"></div><div class="clear"></div><div id="comment-25243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

