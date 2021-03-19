+++
type = "question"
title = "about capturing of Fibre Channel packets"
description = '''As I know about wireshark,It can capture the Ethernet packets by Winpcap。 But now，I want to capture the FC packets, how can I do? And I have find the source code file : &quot;packet-fc.c&quot;, what about it? ps: sorry, My english is poor ,thank you all the time.'''
date = "2012-03-22T00:32:00Z"
lastmod = "2012-05-04T09:07:00Z"
weight = 9687
keywords = [ "capture", "fc" ]
aliases = [ "/questions/9687" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [about capturing of Fibre Channel packets](/questions/9687/about-capturing-of-fibre-channel-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9687-score" class="post-score" title="current number of votes">0</div><span id="post-9687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I know about wireshark,It can capture the Ethernet packets by Winpcap。 But now，I want to capture the FC packets, how can I do?</p><p>And I have find the source code file : "packet-fc.c", what about it?</p><p>ps: sorry, My english is poor ,thank you all the time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-fc" rel="tag" title="see questions tagged &#39;fc&#39;">fc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/2f2143723c2bece1840d64bbd18dc04d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taiyangluoyu&#39;s gravatar image" /><p><span>taiyangluoyu</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taiyangluoyu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '12, 01:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9687" class="comments-container"></div><div id="comment-tools-9687" class="comment-tools"></div><div class="clear"></div><div id="comment-9687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9691"></span>

<div id="answer-container-9691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9691-score" class="post-score" title="current number of votes">3</div><span id="post-9691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't include its own code for capturing packets; it uses libpcap/WinPcap for that. Unfortunately, nobody's contributed code to libpcap/WinPcap to capture Fibre Channel traffic; I'm not sure whether the operating systems on which Wireshark runs support doing so. Perhaps if there's hardware that can capture raw Fibre Channel packets, and drivers for it for an operating system that libpcap/WinPcap supports, somebody could contribute code to capture it in libpcap/WinPcap, but, until then, there's no way to capture Fibre Channel packets in Wireshark.</p><p>The Fibre Channel dissectors in Wireshark are used for various Fibre Channel-in-IP encapsulations and for Network Instruments' Observer captures, not for captures done by Wireshark itself. There's also support for Fibre Channel in pcap files, but I don't know whether any software can write those files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9691" class="comments-container"></div><div id="comment-tools-9691" class="comment-tools"></div><div class="clear"></div><div id="comment-9691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10685"></span>

<div id="answer-container-10685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10685-score" class="post-score" title="current number of votes">0</div><span id="post-10685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only way to capture Fibre Channel packets that I know of is using the JDSU Xgig Analyzer which supports 1-16Gig Fibre Channel. The Xgig is used by almost all storage development vendors and is the best in class analyzer for Fibre Channel, and all other storage protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '12, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/598171a752db2a25d5c09865224cd137?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobFin&#39;s gravatar image" /><p><span>RobFin</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobFin has no accepted answers">0%</span></p></div></div><div id="comments-container-10685" class="comments-container"></div><div id="comment-tools-10685" class="comment-tools"></div><div class="clear"></div><div id="comment-10685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

