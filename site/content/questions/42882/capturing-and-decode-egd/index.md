+++
type = "question"
title = "Capturing and Decode EGD"
description = '''Hi, I need to capture and decode EGD (Ethernet Global Data,) exchanged between number of PLCs (non window machines).  I tried to connect a laptop (window machine) with Window 7pro and Wireshark 1.12.5 to that EGD network switch of the PLCs and tried to capture the EGD message packs. I typed the IP o...'''
date = "2015-06-04T05:09:00Z"
lastmod = "2015-06-09T02:52:00Z"
weight = 42882
keywords = [ "egd" ]
aliases = [ "/questions/42882" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing and Decode EGD](/questions/42882/capturing-and-decode-egd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42882-score" class="post-score" title="current number of votes">0</div><span id="post-42882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to capture and decode EGD (Ethernet Global Data,) exchanged between number of PLCs (non window machines). I tried to connect a laptop (window machine) with Window 7pro and Wireshark 1.12.5 to that EGD network switch of the PLCs and tried to capture the EGD message packs. I typed the IP of a PLC in Remote Interface under Interface management. But an error messaging is coming mentioned connection is refused.</p><p>Kindly mention how I can collect the exchanged EGD message.</p><p>Thanks and Regards, Sandeep Maitra</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-egd" rel="tag" title="see questions tagged &#39;egd&#39;">egd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '15, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/84169ce4abbbe71a6e352ebcc211f0d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="san_mai&#39;s gravatar image" /><p><span>san_mai</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="san_mai has no accepted answers">0%</span></p></div></div><div id="comments-container-42882" class="comments-container"></div><div id="comment-tools-42882" class="comment-tools"></div><div class="clear"></div><div id="comment-42882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42884"></span>

<div id="answer-container-42884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42884-score" class="post-score" title="current number of votes">0</div><span id="post-42884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Remote Interface for Wireshark is for a remote host running rpcap, and your PLC's are unlikely to be running this.</p><p>Instead you need to learn about capturing on a switched network, see the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture</a>. What is the model of your switch?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '15, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jun '15, 02:58</strong> </span></p></div></div><div id="comments-container-42884" class="comments-container"><span id="42997"></span><div id="comment-42997" class="comment"><div id="post-42997-score" class="comment-score"></div><div class="comment-text"><p>Dear Mr Graham, Thanks for replying. Other than Remote interface, is there any other way to capture EGD telegrams. Is there anything called EGD plugins which need to be installed separately!!</p><p>Regards, Sandeep Maitra</p></div><div id="comment-42997-info" class="comment-info"><span class="comment-age">(09 Jun '15, 00:14)</span> <span class="comment-user userinfo">san_mai</span></div></div><span id="43006"></span><div id="comment-43006" class="comment"><div id="post-43006-score" class="comment-score"></div><div class="comment-text"><p>I think your conflating two things here, capturing and dissecting.</p><p>To capture, you must arrange for your capture interface to be able to see the traffic of interest. This is likely to involve spanning or mirroring a switch port in your environment.</p><p>To dissect, after you have a captured traffic of interest, you need a program with knowledge of the protocols involved. Fortunately, Wireshark is such a program, it has an egd dissector built-in that expects EGD traffic to be run over UDP on port 18246. If your EGD traffic is different you might need to use the "Decode As..." facility in Wireshark to cause the traffic to be dissected as EGD.</p></div><div id="comment-43006-info" class="comment-info"><span class="comment-age">(09 Jun '15, 02:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43008"></span><div id="comment-43008" class="comment"><div id="post-43008-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Other than Remote interface, is there any other way to capture EGD telegrams.</p></blockquote><p>as <span></span><span>@grahamb</span> wrote: take a look at the "Ethernet Capture Setup" (link in his answer). In short: The easiest way would be a switch with port mirroring capabilities.</p></div><div id="comment-43008-info" class="comment-info"><span class="comment-age">(09 Jun '15, 02:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42884" class="comment-tools"></div><div class="clear"></div><div id="comment-42884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

