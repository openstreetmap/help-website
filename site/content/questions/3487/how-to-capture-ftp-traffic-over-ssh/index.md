+++
type = "question"
title = "How to capture ftp traffic over ssh?"
description = '''I am new to wireshark. I have downloaded wireshark in my machine and I am using Windows Vista. I am trying to capture ftp traffic between 2 local hosts by executing some ftp commands in SSH terminal. I need wireshark in my machine to capture that traffic. How to configure wireshark for that. Kindly ...'''
date = "2011-04-13T09:52:00Z"
lastmod = "2011-04-14T06:30:00Z"
weight = 3487
keywords = [ "ftp", "ssh" ]
aliases = [ "/questions/3487" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture ftp traffic over ssh?](/questions/3487/how-to-capture-ftp-traffic-over-ssh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3487-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark. I have downloaded wireshark in my machine and I am using Windows Vista. I am trying to capture ftp traffic between 2 local hosts by executing some ftp commands in SSH terminal. I need wireshark in my machine to capture that traffic. How to configure wireshark for that. Kindly help.</p></div><div id="question-tags" class="tags-container tags">ftp ssh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/ccc174888d92711e12f6967df51b4e40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajan&#39;s gravatar image" /><p>rajan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '11, 10:52</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3487" class="comments-container"></div><div id="comment-tools-3487" class="comment-tools"></div><div class="clear"></div><div id="comment-3487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3498"></span>

<div id="answer-container-3498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3498-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are issuing ftp commands from within an ssh session, you will not see any FTP traffic. You will only see SSH traffic. From the <a href="http://wiki.wireshark.org/SSH">SSH</a> wiki page, <em>"The SSH dissector is, unlike the <a href="http://wiki.wireshark.org/SSL">SSL</a> dissector, not able to decrypt the encrypted packets/payload."</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '11, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3498" class="comments-container"></div><div id="comment-tools-3498" class="comment-tools"></div><div class="clear"></div><div id="comment-3498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3491"></span>

<div id="answer-container-3491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3491-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark would need to invoke promiscuous mode. You probably won't have any issues with that, it is simply a checkbox when you choose capture. You probably will only have luck on a wired connection. The second thing is that you must get the traffic to the NIC in the PC with Wireshark installed. This could be done if all pc's are connected to a hub. Alternatively, most managed switches have a span or monitor mode that could copy traffic to the capture pc's port. The third option would be to use a TAP inline to duplicate the signals to the capture pc.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '11, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-3491" class="comments-container"></div><div id="comment-tools-3491" class="comment-tools"></div><div class="clear"></div><div id="comment-3491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

