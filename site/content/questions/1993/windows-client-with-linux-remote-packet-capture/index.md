+++
type = "question"
title = "Windows client with Linux remote packet capture"
description = '''I&#x27;ve got my headless Linux box in the cabinet where I need to capture my packets, but I&#x27;d rather use the fancy GUI instead of tshark over ssh. Since all my client systems run Windows I&#x27;m trying to setup a Windows Wireshark instance to display remotely captured packets from a Linux host. I looked and...'''
date = "2011-01-28T10:29:00Z"
lastmod = "2016-03-27T15:55:00Z"
weight = 1993
keywords = [ "windows", "rpcapd", "linux" ]
aliases = [ "/questions/1993" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Windows client with Linux remote packet capture](/questions/1993/windows-client-with-linux-remote-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1993-score" class="post-score" title="current number of votes">0</div><span id="post-1993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got my headless Linux box in the cabinet where I need to capture my packets, but I'd rather use the fancy GUI instead of tshark over ssh. Since all my client systems run Windows I'm trying to setup a Windows Wireshark instance to display remotely captured packets from a Linux host. I looked and rpcapd doesn't appear to be a part of the Ubuntu Wireshark package that I am using. Online I could only find Windows copies of the program. Is this just a configuration that not a lot of people use? Or am I missing an obvious link that puts this puzzle together nicely?</p><p>Thanks! -Matt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-rpcapd" rel="tag" title="see questions tagged &#39;rpcapd&#39;">rpcapd</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '11, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/e447339af8aa611777b751f9d77b4019?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mra&#39;s gravatar image" /><p><span>mra</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mra has no accepted answers">0%</span></p></div></div><div id="comments-container-1993" class="comments-container"></div><div id="comment-tools-1993" class="comment-tools"></div><div class="clear"></div><div id="comment-1993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2003"></span>

<div id="answer-container-2003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2003-score" class="post-score" title="current number of votes">0</div><span id="post-2003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That is a configuration not a lot of people use.</p><p>It can be made to work though, if you're willing to compile it yourself.</p><p>Get the <a href="http://www.winpcap.org/devel.htm">WinPcap source code</a>, extract it and follow what's said in winpcap/wpcap/libpcap/readme-rpcap.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '11, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2003" class="comments-container"></div><div id="comment-tools-2003" class="comment-tools"></div><div class="clear"></div><div id="comment-2003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51226"></span>

<div id="answer-container-51226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51226-score" class="post-score" title="current number of votes">0</div><span id="post-51226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>i currently use tshark/wireshark on linux, but also over two years i created tools from the ground up using tshark(since tshark can do everything that the GUI can do), i redirected stdin/stdout/stderr streams into c# winform applications. i did have numerous linux packet sniffer boxes in small network with windows host. the packet sniffers in this case were pcmcia cards on the linux boxes. also i used Mono at that time as well. mono by now is much more capable than that time, 2007 to 2008 time frame.<br />
</p><p>best of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '16, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/26fe25a5ae59042b33999d85ec52deae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ron%20Harding&#39;s gravatar image" /><p><span>Ron Harding</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ron Harding has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-51226" class="comments-container"></div><div id="comment-tools-51226" class="comment-tools"></div><div class="clear"></div><div id="comment-51226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

