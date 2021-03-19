+++
type = "question"
title = "Wireshark install"
description = '''Can I run wireshark without doing an install? We have some prod servers that we cannot install the program until the weekend and need to run it without an install? Thank you, Dario'''
date = "2011-11-02T14:14:00Z"
lastmod = "2011-11-03T18:30:00Z"
weight = 7209
keywords = [ "install", "wireshark" ]
aliases = [ "/questions/7209" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark install](/questions/7209/wireshark-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7209-score" class="post-score" title="current number of votes">0</div><span id="post-7209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I run wireshark without doing an install? We have some prod servers that we cannot install the program until the weekend and need to run it without an install?</p><p>Thank you, Dario</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '11, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/6bd4b15a44704811da76fb39caefcc14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lastcall1969&#39;s gravatar image" /><p><span>lastcall1969</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lastcall1969 has no accepted answers">0%</span></p></div></div><div id="comments-container-7209" class="comments-container"></div><div id="comment-tools-7209" class="comment-tools"></div><div class="clear"></div><div id="comment-7209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7211"></span>

<div id="answer-container-7211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7211-score" class="post-score" title="current number of votes">0</div><span id="post-7211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can <a href="http://www.wireshark.org/download.html">download</a> the sources and compile Wireshark yourself, then you can run it from the build directory without doing an install. Or, if your production servers are running Windows, then it might be easier for you to download and install either the U3 or portableapps versions on a compatible USB flash drive and run it from there instead.</p><p>If your production servers are running Windows and you want to capture live traffic as opposed to only reading existing capture files, then you will still have to install <a href="http://www.winpcap.org/">WinPcap</a> though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '11, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-7211" class="comments-container"></div><div id="comment-tools-7211" class="comment-tools"></div><div class="clear"></div><div id="comment-7211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7230"></span>

<div id="answer-container-7230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7230-score" class="post-score" title="current number of votes">0</div><span id="post-7230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the production servers have, for example, tcpdump or snoop installed on them (many UN*Xes may have tcpdump installed; Solaris machines might have snoop installed), you could use tcpdump with <code>-s 0 -w</code> or snoop with <code>-o</code> to capture the network traffic, and then copy it to a machine that has Wireshark installed on it and open the capture there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '11, 18:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7230" class="comments-container"></div><div id="comment-tools-7230" class="comment-tools"></div><div class="clear"></div><div id="comment-7230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

