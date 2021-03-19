+++
type = "question"
title = "Not seeing Jumbo Packets in Wireshark"
description = '''Hi All,  I have a hardware board which sends Jumbo packets of around 8192 byte sized packet.My laptop is of following configuration Windows-7 64-Bit Operating System. Wireshark version Version 1.8.0 (SVN Rev 43431 from /trunk-1.8) I followed below steps to change the MTU Size to 9216 bytes. Open a c...'''
date = "2012-10-10T02:39:00Z"
lastmod = "2012-10-10T11:03:00Z"
weight = 14867
keywords = [ "jumbo", "wirehshark" ]
aliases = [ "/questions/14867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not seeing Jumbo Packets in Wireshark](/questions/14867/not-seeing-jumbo-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14867-score" class="post-score" title="current number of votes">0</div><span id="post-14867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I have a hardware board which sends Jumbo packets of around 8192 byte sized <a href="http://packet.My">packet.My</a> laptop is of following configuration Windows-7 64-Bit Operating System. Wireshark version Version 1.8.0 (SVN Rev 43431 from /trunk-1.8)</p><p>I followed below steps to change the MTU Size to 9216 bytes.</p><p>Open a command line window as an Administrator (ie. right click on All Programs &gt; Accessories &gt; Command Prompt and select Run as administrator) ... Type the command netsh and wait for prompt Type the command interface and wait for prompt Type the command ipv4 and wait for prompt Type the command set subinterface "Local Area Connection" mtu=xxxx store=persistent</p><p>Also, in the NIC Interface card, there is JUMBO Packets Option [DISABLED or 4088 bytes], instead of DISABLED (which was default), i set it to 4088 bytes. There was no other option apart from DISABLE/4088 bytes.</p><p>Kindly help as what is to be done further to see wireshark capture the packet.</p><p>Thanks V.Reddy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jumbo" rel="tag" title="see questions tagged &#39;jumbo&#39;">jumbo</span> <span class="post-tag tag-link-wirehshark" rel="tag" title="see questions tagged &#39;wirehshark&#39;">wirehshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/6774b421f816a0c9ba622e492851cdc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vlsireddy&#39;s gravatar image" /><p><span>vlsireddy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vlsireddy has no accepted answers">0%</span></p></div></div><div id="comments-container-14867" class="comments-container"><span id="14876"></span><div id="comment-14876" class="comment"><div id="post-14876-score" class="comment-score"></div><div class="comment-text"><p>If you set the MTU to 4088 bytes, can you capture them with wireshark?</p></div><div id="comment-14876-info" class="comment-info"><span class="comment-age">(10 Oct '12, 04:11)</span> <span class="comment-user userinfo">rakki</span></div></div></div><div id="comment-tools-14867" class="comment-tools"></div><div class="clear"></div><div id="comment-14867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14901"></span>

<div id="answer-container-14901" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14901-score" class="post-score" title="current number of votes">0</div><span id="post-14901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Rakki, Thanks for suggestion. I didn't try that [4088 bytes]. But after i restarted my laptop, it worked fine [i was able to capture 8192 bytes packet on wireshark].</p><p>Thanks V Reddy</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/6774b421f816a0c9ba622e492851cdc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vlsireddy&#39;s gravatar image" /><p><span>vlsireddy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vlsireddy has no accepted answers">0%</span></p></div></div><div id="comments-container-14901" class="comments-container"></div><div id="comment-tools-14901" class="comment-tools"></div><div class="clear"></div><div id="comment-14901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

