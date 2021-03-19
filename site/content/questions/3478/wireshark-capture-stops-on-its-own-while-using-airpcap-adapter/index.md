+++
type = "question"
title = "Wireshark capture stops on its own while using AirPcap adapter"
description = '''While running Wireshark capture using AirPcap Adapters, the capture will stop on its own, so I can&#x27;t capture data for long periods of time. This has been an on going problem for me, and I have already gone through CACE Technologies for help, but they insist that it is a Wireshark issue. Is this a kn...'''
date = "2011-04-13T05:04:00Z"
lastmod = "2013-06-10T12:11:00Z"
weight = 3478
keywords = [ "capture", "airpcap", "stop" ]
aliases = [ "/questions/3478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture stops on its own while using AirPcap adapter](/questions/3478/wireshark-capture-stops-on-its-own-while-using-airpcap-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3478-score" class="post-score" title="current number of votes">0</div><span id="post-3478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While running Wireshark capture using AirPcap Adapters, the capture will stop on its own, so I can't capture data for long periods of time. This has been an on going problem for me, and I have already gone through CACE Technologies for help, but they insist that it is a Wireshark issue. Is this a known issue and is there a solution to this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/9e867fc366253a3f0fde8bdaa091c505?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SigmaEng&#39;s gravatar image" /><p><span>SigmaEng</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SigmaEng has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '12, 19:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3478" class="comments-container"></div><div id="comment-tools-3478" class="comment-tools"></div><div class="clear"></div><div id="comment-3478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3481"></span>

<div id="answer-container-3481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3481-score" class="post-score" title="current number of votes">3</div><span id="post-3481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a>, wireshark has not been written for long time capture purposes.</p><p>The best way to capture for a long time is to use command line tool <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> (which wireshark also uses to do the capturing). Have a look at the "-b" options of dumpcap in particular.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '11, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3481" class="comments-container"><span id="3482"></span><div id="comment-3482" class="comment"><div id="post-3482-score" class="comment-score"></div><div class="comment-text"><p>I understand your answer, but it will capture much longer from a wired network vs over the air with AirPcap adapters. I can only capture data for about a half hour with AirPcap (at the most), but with a wired network from an Ethernet card I can capture for much longer. Why shorter time period with AirPcap?</p></div><div id="comment-3482-info" class="comment-info"><span class="comment-age">(13 Apr '11, 08:23)</span> <span class="comment-user userinfo">SigmaEng</span></div></div><span id="3489"></span><div id="comment-3489" class="comment"><div id="post-3489-score" class="comment-score">1</div><div class="comment-text"><p>It may have to do with the amount and kind of packets. For example: on wireless captures you often have tons of beacon frames which might get you into trouble sooner than on a wired link that doesn't have those.</p></div><div id="comment-3489-info" class="comment-info"><span class="comment-age">(13 Apr '11, 13:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21897"></span><div id="comment-21897" class="comment"><div id="post-21897-score" class="comment-score"></div><div class="comment-text"><p>SYN-bit, you said that wireshark is not for long time capture. Is this true even if I use multiple file to capture example next every 200MB? and will I loose some data if i used multiple file ??</p></div><div id="comment-21897-info" class="comment-info"><span class="comment-age">(10 Jun '13, 12:11)</span> <span class="comment-user userinfo">Ashraf</span></div></div></div><div id="comment-tools-3481" class="comment-tools"></div><div class="clear"></div><div id="comment-3481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

