+++
type = "question"
title = "SSH Remote Capture TCPdump"
description = '''Would be awesome if Wireshark had native/built-in SSH tunnel support for remote tcpdump packet capturing instead of having to use a third party SSH app and the limitations such as not being able to stop/restart a capture, and not being able to use the Wireshark GUI to set the capture filter. Maybe h...'''
date = "2017-01-12T02:36:00Z"
lastmod = "2017-01-12T03:14:00Z"
weight = 58696
keywords = [ "capture", "remote", "ssh", "tcpdump" ]
aliases = [ "/questions/58696" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSH Remote Capture TCPdump](/questions/58696/ssh-remote-capture-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58696-score" class="post-score" title="current number of votes">0</div><span id="post-58696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would be awesome if Wireshark had native/built-in SSH tunnel support for remote tcpdump packet capturing instead of having to use a third party SSH app and the limitations such as not being able to stop/restart a capture, and not being able to use the Wireshark GUI to set the capture filter.</p><p>Maybe have Wireshark be able to load plink.exe and use it as though it is it's natively built-in SSH tunnel app.</p><p>Instead of having to execute plink to set up the pipe to redirect Unix/Linux tcpdump into Wireshark. Have Wireshark handle the whole thing. Tell Wireshark what SSH app to use (plink.exe), provide credentials/key file for SSH access, the remote app to run (tcpdump), and configure the capture filter for tcpdump to use.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '17, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/fb0be57cb38cb228c08b34a06872ee0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NOYB&#39;s gravatar image" /><p><span>NOYB</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NOYB has no accepted answers">0%</span></p></div></div><div id="comments-container-58696" class="comments-container"></div><div id="comment-tools-58696" class="comment-tools"></div><div class="clear"></div><div id="comment-58696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58697"></span>

<div id="answer-container-58697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58697-score" class="post-score" title="current number of votes">1</div><span id="post-58697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is being worked in with the extcap utility sshdump which gives a pseudo-interface "SSH remote capture". I'm not sure of the state of this in the stable (2.2.x) releases but you can try a development release (2.3.x) from the <a href="https://www.wireshark.org/download/automated/">automated builds</a> site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '17, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58697" class="comments-container"></div><div id="comment-tools-58697" class="comment-tools"></div><div class="clear"></div><div id="comment-58697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

