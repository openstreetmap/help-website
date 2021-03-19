+++
type = "question"
title = "Mapping a Packet in Wireshark to the Application that sent that packet"
description = '''Does anyone know of a good way and/or tool that can be used to match a packet in Wireshark with the local application that sent or received that packet? It would be used with Wireshark capturing on the local machine. I believe I heard something from Laura C about one for Windows. I&#x27;m looking for wha...'''
date = "2015-07-15T14:57:00Z"
lastmod = "2015-07-22T11:41:00Z"
weight = 44192
keywords = [ "application" ]
aliases = [ "/questions/44192" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping a Packet in Wireshark to the Application that sent that packet](/questions/44192/mapping-a-packet-in-wireshark-to-the-application-that-sent-that-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44192-score" class="post-score" title="current number of votes">0</div><span id="post-44192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know of a good way and/or tool that can be used to match a packet in Wireshark with the local application that sent or received that packet? It would be used with Wireshark capturing on the local machine.</p><p>I believe I heard something from Laura C about one for Windows. I'm looking for what that was and one that could be used for OSX as well.</p><p>Thanks in advance. Let me know if anyone needs to know the exact use case for this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '15, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/4a4df10c701372e5dbbb8015a1d6b67b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_harrold&#39;s gravatar image" /><p><span>patrick_harrold</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_harrold has no accepted answers">0%</span></p></div></div><div id="comments-container-44192" class="comments-container"></div><div id="comment-tools-44192" class="comment-tools"></div><div class="clear"></div><div id="comment-44192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="44196"></span>

<div id="answer-container-44196" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44196-score" class="post-score" title="current number of votes">2</div><span id="post-44196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="patrick_harrold has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The poor man's way in Windows (probably applicable to other OSs as well) is to use netstat to determine which process is using a port. Of course this can be difficult to actually tie up with a capture as netstat shows the current (instantaneous) state of ports.</p><p>On Windows you can capture using MS Message Analyzer which can record the process involved in the traffic.</p><p>There is a (old) <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">feature request</a> on the Wireshark Bugzilla to add process ID capability but it's languished for a long time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '15, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44196" class="comments-container"><span id="44217"></span><div id="comment-44217" class="comment"><div id="post-44217-score" class="comment-score"></div><div class="comment-text"><p>Until Windows 7: Network Monitor 3.4 has this feature.</p><p>The combination of two CLI commands could be used since WinXP to match the window name to the port.</p><p>netstat -ano and tasklist /v</p><p>At MacOS you can use the Activity Monitor to support your analyze. <a href="https://support.apple.com/en-us/HT201464">https://support.apple.com/en-us/HT201464</a></p></div><div id="comment-44217-info" class="comment-info"><span class="comment-age">(16 Jul '15, 12:17)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44223"></span><div id="comment-44223" class="comment"><div id="post-44223-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help Graham.</p><p>That is a way for it to work: matching the source port in wireshark with netstat on either OSX or Windows. Then match that PID with the application.</p><p>I'll wait a day or two before marking this as the answer just in case someone else has a better answer or an app out there that can show this.</p></div><div id="comment-44223-info" class="comment-info"><span class="comment-age">(16 Jul '15, 15:13)</span> <span class="comment-user userinfo">patrick_harrold</span></div></div><span id="44233"></span><div id="comment-44233" class="comment"><div id="post-44233-score" class="comment-score"></div><div class="comment-text"><p>On Windows &gt; XP SP2, <code>netstat -b</code> in an elevated shell will show the process name as well as the PID.</p></div><div id="comment-44233-info" class="comment-info"><span class="comment-age">(17 Jul '15, 02:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-44196" class="comment-tools"></div><div class="clear"></div><div id="comment-44196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44231"></span>

<div id="answer-container-44231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44231-score" class="post-score" title="current number of votes">1</div><span id="post-44231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Patrick,</p><p>I tend to leave a tcpview (Sysinternals) window open, it updates in 1 second bursts and you can pause it using SPACE when your data comes, you can then Save the file out as a text file for records if required.</p><p>It's not a whole lot more modern than netstat, but it's a little easier to use in my opinion:</p><p>start tcpview, sort on the ports you want to see and just wait.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44231" class="comments-container"><span id="44291"></span><div id="comment-44291" class="comment"><div id="post-44291-score" class="comment-score"></div><div class="comment-text"><p>Thanks Darren. I'll look into this as well.</p></div><div id="comment-44291-info" class="comment-info"><span class="comment-age">(18 Jul '15, 23:58)</span> <span class="comment-user userinfo">patrick_harrold</span></div></div></div><div id="comment-tools-44231" class="comment-tools"></div><div class="clear"></div><div id="comment-44231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44383"></span>

<div id="answer-container-44383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44383-score" class="post-score" title="current number of votes">0</div><span id="post-44383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may find some usefulness with Dtrace - from Sun - ported to OSX etc.</p><p><a href="https://en.wikipedia.org/wiki/DTrace">https://en.wikipedia.org/wiki/DTrace</a> Great info from Brendan Gregg on his site, linked off the dtrace.org site - <a href="https://en.wikipedia.org/wiki/Brendan_Gregg">https://en.wikipedia.org/wiki/Brendan_Gregg</a> I met him when he was giving a talk about ZFS a few years ago.</p><p><a href="http://dtrace.org/blogs/about/">http://dtrace.org/blogs/about/</a> <a href="http://dtrace.org/blogs/brendan/2011/10/10/top-10-dtrace-scripts-for-mac-os-x/">http://dtrace.org/blogs/brendan/2011/10/10/top-10-dtrace-scripts-for-mac-os-x/</a> <a href="http://www.brendangregg.com/USEmethod/use-macosx.html">http://www.brendangregg.com/USEmethod/use-macosx.html</a></p><p>e.g. soconnect_mac.d tcpio.d trace TCP connections -</p><p>At least get the tarball of dtrace scripts from dtrace.org - maybe worth the price of his book also - I have the Kindle edition.</p><p>Hope this helps -</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/52ff5d6b59bd5798a667a6f346a52421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetlevel&#39;s gravatar image" /><p><span>packetlevel</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetlevel has no accepted answers">0%</span></p></div></div><div id="comments-container-44383" class="comments-container"></div><div id="comment-tools-44383" class="comment-tools"></div><div class="clear"></div><div id="comment-44383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

