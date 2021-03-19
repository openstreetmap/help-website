+++
type = "question"
title = "Timestamps drift from real time"
description = '''I&#x27;ve been using Wireshark/Ethereal for several years and now I observe a very odd behaviour (Wireshark 1.4.2/1.4.6 and PCap 4.1.2) on a HP Compaq 8000 Elite CMT with Windows XP SP3 32bit. When I start the capture, the timestamp of the immediately captured packet is okay. The more time passes, the mo...'''
date = "2011-05-03T02:26:00Z"
lastmod = "2011-05-04T00:14:00Z"
weight = 3893
keywords = [ "timestamp" ]
aliases = [ "/questions/3893" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Timestamps drift from real time](/questions/3893/timestamps-drift-from-real-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3893-score" class="post-score" title="current number of votes">0</div><span id="post-3893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using Wireshark/Ethereal for several years and now I observe a very odd behaviour (Wireshark 1.4.2/1.4.6 and PCap 4.1.2) on a HP Compaq 8000 Elite CMT with Windows XP SP3 32bit.</p><p>When I start the capture, the timestamp of the immediately captured packet is okay. The more time passes, the more does the timestamp deviate from the real time. That is, after 10 seconds of real time passed, Wireshark will timestamp that only 4 seconds passed - no matter what the timeview format is. The clocks completely differ after some time (the OS clock will show something like 11:42:15 and when I provoke a packet then, the timestamp might say 11:40:57 or in the Seconds since Capture view, the first packet has 0 seconds, then I wait 10 seconds, send a packet and the packet has just 4 seconds as timestamp).</p><p>I've other software that timestamps received packets and this other software works though - the timestamps are correct. I can run them simultaneously, too and see the difference between the timestamps for the very same packet, up to minutes, if I let Wireshark run long enough. (As far as I can tell, Wireshark/PCap seems to retrieve the current time once and then internally counts the time while the capture is running - and this does not work properly on this machine for whatever reason).</p><p>I've reinstalled Wireshark and PCap, deinstalled nearly every other software etc. I've checked the BIOS if there are time related settings... right now I'm at a loss what else I can do. Wireshark works fine on my other computers (be it XP or Linux).</p><p>Additional: This is not just a timestamp delay due to performance issues or network traffic. The timestamps are plain wrong. It happens with single packets, name resolutions disabled etc. I've two network cards in the machine and the behaviour is the same for both.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/05aa584fbeb890a9bbd3e43e0e23a1f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Iyanga&#39;s gravatar image" /><p><span>Iyanga</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Iyanga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '11, 02:34</strong> </span></p></div></div><div id="comments-container-3893" class="comments-container"></div><div id="comment-tools-3893" class="comment-tools"></div><div class="clear"></div><div id="comment-3893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3909"></span>

<div id="answer-container-3909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3909-score" class="post-score" title="current number of votes">1</div><span id="post-3909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="http://seclists.org/wireshark/2010/Aug/297">this thread</a> on the wireshark mailing-list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 00:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3909" class="comments-container"></div><div id="comment-tools-3909" class="comment-tools"></div><div class="clear"></div><div id="comment-3909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3908"></span>

<div id="answer-container-3908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3908-score" class="post-score" title="current number of votes">0</div><span id="post-3908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark gets it frames, timestamped and all, from the WinPcap driver. Somehow that driver isn't able to track time, maybe due to the way it integrates with your network driver and or network stack. You could try running in a different mode (NPF driver of not), try a previous WinPcap version. Otherwise the WinPcap mailing list may be of help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '11, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3908" class="comments-container"></div><div id="comment-tools-3908" class="comment-tools"></div><div class="clear"></div><div id="comment-3908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

