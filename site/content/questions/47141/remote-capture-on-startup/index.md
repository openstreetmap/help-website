+++
type = "question"
title = "Remote Capture on startup"
description = '''Hi all, I have managed to get the remote capture feature working on the target machine, however every time I need to shut down the target/my own PC, I need to manually re-enter the connection details. Is there a way to make it so it saves the details I have previously entered, so I can start capturi...'''
date = "2015-11-02T03:06:00Z"
lastmod = "2015-11-02T05:00:00Z"
weight = 47141
keywords = [ "remote-capture", "startup", "details" ]
aliases = [ "/questions/47141" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Remote Capture on startup](/questions/47141/remote-capture-on-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have managed to get the remote capture feature working on the target machine, however every time I need to shut down the target/my own PC, I need to manually re-enter the connection details. Is there a way to make it so it saves the details I have previously entered, so I can start capturing data on startup without any intervention on my part?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">remote-capture startup details</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/1b0111f78e1f65adab7dde8313aea857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MWMWMW&#39;s gravatar image" /><p>MWMWMW<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MWMWMW has no accepted answers">0%</span></p></div></div><div id="comments-container-47141" class="comments-container"></div><div id="comment-tools-47141" class="comment-tools"></div><div class="clear"></div><div id="comment-47141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47153"></span>

<div id="answer-container-47153" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47153-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you're hitting a know problem, depending on your Wireshark version.</p><blockquote><p><a href="https://ask.wireshark.org/questions/17898/remote-interfaces-does-not-save">https://ask.wireshark.org/questions/17898/remote-interfaces-does-not-save</a><br />
</p></blockquote><p>possible solution:</p><p>Run Wirshark with a commandline to tell it the remote interface</p><blockquote><p><a href="https://ask.wireshark.org/questions/23393/manually-enter-remote-capture-line">https://ask.wireshark.org/questions/23393/manually-enter-remote-capture-line</a></p></blockquote><p>Example:</p><blockquote><p>wireshark -i <span>rpcap://ip.address/eth0</span></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47153" class="comments-container"><span id="47157"></span><div id="comment-47157" class="comment"><div id="post-47157-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I will give this a try</p></div><div id="comment-47157-info" class="comment-info"><span class="comment-age">(02 Nov '15, 08:45)</span> MWMWMW</div></div><span id="47159"></span><div id="comment-47159" class="comment"><div id="post-47159-score" class="comment-score"></div><div class="comment-text"><p>good luck!</p></div><div id="comment-47159-info" class="comment-info"><span class="comment-age">(02 Nov '15, 08:49)</span> Kurt Knochner ♦</div></div><span id="56513"></span><div id="comment-56513" class="comment"><div id="post-56513-score" class="comment-score"></div><div class="comment-text"><p>When will this be "fixed"? At least in version 2.2.1 there is a disclaimer stating interfaces won't be saved. (See screenshot.)</p><p>Note to developers: This is very inconvenient especially when you have multiple devices to track.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Cant_Save_Remote_Settings_Uqd4yDt.png" alt="alt text" /></p></div><div id="comment-56513-info" class="comment-info"><span class="comment-age">(19 Oct '16, 13:59)</span> Jollyrgr</div></div><span id="56737"></span><div id="comment-56737" class="comment"><div id="post-56737-score" class="comment-score"></div><div class="comment-text"><p>FWIW this request is tracked as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8557">bug 8557</a>.</p></div><div id="comment-56737-info" class="comment-info"><span class="comment-age">(27 Oct '16, 06:34)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-47153" class="comment-tools"></div><div class="clear"></div><div id="comment-47153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

