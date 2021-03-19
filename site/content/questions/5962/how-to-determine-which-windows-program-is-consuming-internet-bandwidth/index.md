+++
type = "question"
title = "How to determine which  Windows program is consuming Internet bandwidth"
description = '''I have a client that is on a limited Bandwith residential ISP with a daily allocation of 250MB up/down. The user has a PC running WIN 7 Home Premium. She has turned off all known &quot;automatic update&quot; configurations in all of the programs that are installed. But the bandwidth is still being consumed at...'''
date = "2011-08-30T10:37:00Z"
lastmod = "2011-08-30T11:30:00Z"
weight = 5962
keywords = [ "windows", "windows7", "traffic", "troubleshooting" ]
aliases = [ "/questions/5962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine which Windows program is consuming Internet bandwidth](/questions/5962/how-to-determine-which-windows-program-is-consuming-internet-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5962-score" class="post-score" title="current number of votes">1</div><span id="post-5962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client that is on a limited Bandwith residential ISP with a daily allocation of 250MB up/down. The user has a PC running WIN 7 Home Premium. She has turned off all known "automatic update" configurations in all of the programs that are installed. But the bandwidth is still being consumed at an unacceptable rate. The PC was recently restored back to its out of box new condition and fresh copies of Windows 7 and Avast Internet Security were installed.</p><p>Can Wireshark help her determine which Windows program(s) is the culprit?</p><p>For the record, only one PC is connected to the home network and the ISP is HughesNet in Texas.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '11, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/c87cb0632313e1bb754eed89f560b06a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wtg1953&#39;s gravatar image" /><p><span>wtg1953</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wtg1953 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Aug '11, 12:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5962" class="comments-container"></div><div id="comment-tools-5962" class="comment-tools"></div><div class="clear"></div><div id="comment-5962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5964"></span>

<div id="answer-container-5964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5964-score" class="post-score" title="current number of votes">3</div><span id="post-5964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark could be used to identify what traffic is being transferred and at what rate, but doesn't directly point to the process that is causing the traffic. You may be able to infer that from the traffic content.</p><p>As you'll be likely to want this to run for some time, you may want to use dumpcap to do the capture so that the Wireshark UI isn't available for user "experimentation".</p><p>Microsoft's <a href="http://www.microsoft.com/download/en/details.aspx?displaylang=en&amp;id=4865">Network Monitor</a> can show you the process causing the traffic, and you can also use other tools such as <a href="http://technet.microsoft.com/en-us/sysinternals/bb897437">TCPView</a> or netstat to find out what process is using a port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Aug '11, 13:36</strong> </span></p></div></div><div id="comments-container-5964" class="comments-container"><span id="5965"></span><div id="comment-5965" class="comment"><div id="post-5965-score" class="comment-score"></div><div class="comment-text"><p>I second <strong>TCPView</strong>.</p></div><div id="comment-5965-info" class="comment-info"><span class="comment-age">(30 Aug '11, 11:30)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-5964" class="comment-tools"></div><div class="clear"></div><div id="comment-5964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

