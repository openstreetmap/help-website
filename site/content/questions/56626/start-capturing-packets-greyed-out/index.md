+++
type = "question"
title = "Start capturing packets greyed out"
description = '''I have used Wireshark in the distant past, but now have a Win10 PC on which I have installed Wireshark 2.2.1 and Win10Pcap, but the &quot;Start capturing packets&quot; toolbar icon is greyed out. If I try to start NPF manually from a Cmd window running as Administrator I get: OpenService FAILED 1060: The spec...'''
date = "2016-10-24T19:25:00Z"
lastmod = "2016-10-26T03:55:00Z"
weight = 56626
keywords = [ "start", "capture" ]
aliases = [ "/questions/56626" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Start capturing packets greyed out](/questions/56626/start-capturing-packets-greyed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56626-score" class="post-score" title="current number of votes">0</div><span id="post-56626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have used Wireshark in the distant past, but now have a Win10 PC on which I have installed Wireshark 2.2.1 and Win10Pcap, but the "Start capturing packets" toolbar icon is greyed out.</p><p>If I try to start NPF manually from a Cmd window running as Administrator I get: OpenService FAILED 1060: The specified service does not exist as an installed service.</p><p>Can anyone guide to get this resolved me please, Graham</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-start" rel="tag" title="see questions tagged &#39;start&#39;">start</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '16, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/de963d3ce1f3f0cad75514255a8b00a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graham&#39;s gravatar image" /><p><span>Graham</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graham has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '16, 00:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56626" class="comments-container"></div><div id="comment-tools-56626" class="comment-tools"></div><div class="clear"></div><div id="comment-56626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56631"></span>

<div id="answer-container-56631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56631-score" class="post-score" title="current number of votes">0</div><span id="post-56631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Win10Pcap isn't supported for use with Wireshark, it's an entirely separate project that you'll have to contact for support.</p><p>WinPcap 4.1.3 that is provided by the 2.2.1 installer runs on Win 10 as well as older versions if Windows, so to get help here, please uninstall Win10Pcap, reboot, and then re-install Wireshark, this time allowing it to install WinPcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '16, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56631" class="comments-container"><span id="56632"></span><div id="comment-56632" class="comment"><div id="post-56632-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your input, I installed Win10Pcap after I could not get the "Start capturing packets" toolbar icon to be enabled first time round, and saw someone in this form had used it.</p><p>Anyhow, I have uninstalled all the components, rebooted, and reinstalled Wireshark with the embedded WinPcap 4.1.3, and still the "Start capturing packets" toolbar icon is greyed out.</p></div><div id="comment-56632-info" class="comment-info"><span class="comment-age">(25 Oct '16, 00:33)</span> <span class="comment-user userinfo">Graham</span></div></div><span id="56637"></span><div id="comment-56637" class="comment"><div id="post-56637-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-56637-info" class="comment-info"><span class="comment-age">(25 Oct '16, 03:01)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="56641"></span><div id="comment-56641" class="comment"><div id="post-56641-score" class="comment-score">1</div><div class="comment-text"><p>Have you selected an interface to capture on in the interface list under the Capture filter field? The selected interface(s) are highlighted in blue.</p></div><div id="comment-56641-info" class="comment-info"><span class="comment-age">(25 Oct '16, 05:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56673"></span><div id="comment-56673" class="comment"><div id="post-56673-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I did not realize with just one interface you could double click on it to start capturing.</p></div><div id="comment-56673-info" class="comment-info"><span class="comment-age">(26 Oct '16, 00:16)</span> <span class="comment-user userinfo">Graham</span></div></div><span id="56681"></span><div id="comment-56681" class="comment"><div id="post-56681-score" class="comment-score"></div><div class="comment-text"><p>You can Ctrl + click to select multiple interfaces as well.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-56681-info" class="comment-info"><span class="comment-age">(26 Oct '16, 03:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56631" class="comment-tools"></div><div class="clear"></div><div id="comment-56631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

