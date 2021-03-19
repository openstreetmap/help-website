+++
type = "question"
title = "Remote Capture with fifo -- Windows?"
description = '''Is it possible to do this: $ mkfifo /tmp/sharkfin  $ wireshark -k -i /tmp/sharkfin &amp;amp; $ ssh user@remote-host &quot;dumpcap -w - not port 22&quot; &amp;gt; /tmp/sharkfin On a linux box, connecting via SSH to a Windows box? ie, the Windows box is the one performing the actual capture and passing the traffic back...'''
date = "2012-09-01T20:02:00Z"
lastmod = "2013-08-08T07:59:00Z"
weight = 13985
keywords = [ "windows", "remote", "ssh", "linux" ]
aliases = [ "/questions/13985" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Capture with fifo -- Windows?](/questions/13985/remote-capture-with-fifo-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13985-score" class="post-score" title="current number of votes">0</div><span id="post-13985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to do this:</p><p><em>$ mkfifo /tmp/sharkfin<br />
$ wireshark -k -i /tmp/sharkfin &amp;<br />
$ ssh <span class="__cf_email__" data-cfemail="94e1e7f1e6d4e6f1f9fbe0f1b9fcfbe7e0">[email protected]</span> "dumpcap -w - not port 22" &gt; /tmp/sharkfin</em><br />
</p><p>On a linux box, connecting via SSH to a Windows box? ie, the Windows box is the one performing the actual capture and passing the traffic back to the Linux box.</p><p>Any reason why it wouldn't work?</p><p>As a side note, yes, I know about rpcap, but I don't want to use it if I can help it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '12, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/a6bfd9657bcf28e0b72e4bc8873fbf03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DefensiveDepth&#39;s gravatar image" /><p><span>DefensiveDepth</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DefensiveDepth has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-13985" class="comments-container"></div><div id="comment-tools-13985" class="comment-tools"></div><div class="clear"></div><div id="comment-13985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13996"></span>

<div id="answer-container-13996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13996-score" class="post-score" title="current number of votes">0</div><span id="post-13996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I tried it UN*X-to-UN*X , and it worked, as long as I quoted the filter in the dumpcap command <em>and</em> told it to dump in pcap rather than pcap-NG format (this is with the version on the trunk, but the same applies to 1.8.x), i.e.</p><pre><code>ssh [email protected] &quot;dumpcap -P -w - &#39;not port 22&#39;&quot; &gt; /tmp/sharkfin</code></pre><p>If it's pre-1.8, you can, and need to, leave the <code>-P</code> flag out.</p><p>For Windows, it'll probably work too, but you'd have to have an ssh daemon on the Windows box <em>and</em> arrange that, if you try to ssh to the Windows box and run dumpcap, it finds dumpcap - you might have to explicitly specify the path to dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '12, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-13996" class="comments-container"></div><div id="comment-tools-13996" class="comment-tools"></div><div class="clear"></div><div id="comment-13996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23651"></span>

<div id="answer-container-23651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23651-score" class="post-score" title="current number of votes">0</div><span id="post-23651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>$ ssh <span class="__cf_email__" data-cfemail="1e6b6d7b6c5e6c7b73716a7b3376716d6a">[email protected]</span> "dumpcap -w - not port 22" &gt; /tmp/sharkfin Any reason why it wouldn't work?</p></blockquote><p>You did not specify the interface number for dumpcap, so it will use the first interface. That might <strong>not</strong> be your LAN interface (depends on the configuration of your windows system).</p><p>Please run this command from the Linux box.</p><blockquote><p>$ ssh <span class="__cf_email__" data-cfemail="5c292f392e1c2e39313328397134332f28">[email protected]</span> "dumpcap -D -M"</p></blockquote><p>It will show you two things:</p><p>First: if <code>dumpcap</code> is found, without specifying the full path. If not, run the following command:</p><blockquote><p>$ ssh <span class="__cf_email__" data-cfemail="13666076615361767e7c67763e7b7c6067">[email protected]</span> "%PROGRAMFILES%\Wireshark\dumpcap -D -M"</p></blockquote><p>Second: if the first interface (Interface ID 1), is the one you want to capture on. If not, please run this command, by specifying the interface number.</p><blockquote><p>$ ssh <span class="__cf_email__" data-cfemail="6d181e081f2d1f08000219084005021e19">[email protected]</span> "dumpcap -ni 2 -w - not port 22" &gt; /tmp/sharkfin</p></blockquote><p>BTW: The SSH Daemon on Windows may have problems forwarding the binary data through the SSH tunnel. That's unlikely but not impossible. What is the SSH daemon you were using on Windows?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23651" class="comments-container"></div><div id="comment-tools-23651" class="comment-tools"></div><div class="clear"></div><div id="comment-23651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

