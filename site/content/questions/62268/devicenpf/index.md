+++
type = "question"
title = "Device/npf"
description = '''I keep receiving a snooping device in my network using Device/NPf interface, and i don&#x27;t know what that means or how to stop it, to stay private, and it flags red alerts all the time, so what Device/npf stands for and how to stop it ?'''
date = "2017-06-23T11:03:00Z"
lastmod = "2017-06-23T22:54:00Z"
weight = 62268
keywords = [ "wireshark" ]
aliases = [ "/questions/62268" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Device/npf](/questions/62268/devicenpf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62268-score" class="post-score" title="current number of votes">0</div><span id="post-62268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I keep receiving a snooping device in my network using Device/NPf interface, and i don't know what that means or how to stop it, to stay private, and it flags red alerts all the time, so what Device/npf stands for and how to stop it ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '17, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/d07f3e773cfe9a0aa6ee062321fb9420?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shawer6&#39;s gravatar image" /><p><span>shawer6</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shawer6 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jun '17, 11:04</strong> </span></p></div></div><div id="comments-container-62268" class="comments-container"></div><div id="comment-tools-62268" class="comment-tools"></div><div class="clear"></div><div id="comment-62268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62269"></span>

<div id="answer-container-62269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62269-score" class="post-score" title="current number of votes">0</div><span id="post-62269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A npf (network packet filter) device is not an external device somewhere in your network, it is a piece of software in your PC provided by WinPcap, the library which Wireshark uses to capture packets. So it appeared in your system because you (or someone else who can install software to your PC) have installed Wireshark along with WinPcap. See details <a href="https://www.winpcap.org/docs/docs_412/html/group__NPF.html">here</a>.</p><p>So it is something you can use to monitor the traffic of your own PC, not something that someone else would use to spy on you (unless they can control your PC and run packet capture in the background without your knowledge, but if they can, packet capture is one of the least harmful activities they could do).</p><p>Regarding</p><blockquote><p>it flags red alerts</p></blockquote><p>can you be more specific and possibly provide a screenshot of what you have in mind?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '17, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62269" class="comments-container"><span id="62274"></span><div id="comment-62274" class="comment"><div id="post-62274-score" class="comment-score"></div><div class="comment-text"><p>another device in my network shares Device/NPF data with my machine and i discovered it using wireshark and previously was sharing information using UPnp before i blocked it.. now i see communication between my device and the same device using UDP and TCP ?</p></div><div id="comment-62274-info" class="comment-info"><span class="comment-age">(23 Jun '17, 17:05)</span> <span class="comment-user userinfo">shawer6</span></div></div><span id="62278"></span><div id="comment-62278" class="comment"><div id="post-62278-score" class="comment-score"></div><div class="comment-text"><p>In that case please capture that traffic, look for a couple of frame numbers of these susicious packets, and then use <code>File -&gt; Export specified packets</code>, fill these numbers comma-separated into the <code>Range</code> window, choose a destination folder and fill in some file name, and press [Save].</p><p>Then open this new file using Wireshark to check that it really contains those packets, and if yes, publish it at Cloudshark or any ordinary file sharing service and edit your question with a link to it.</p><p>Without seeing what kind of traffic you talk about it is hard to provide you with any useful feedback.</p></div><div id="comment-62278-info" class="comment-info"><span class="comment-age">(23 Jun '17, 22:54)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62269" class="comment-tools"></div><div class="clear"></div><div id="comment-62269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

