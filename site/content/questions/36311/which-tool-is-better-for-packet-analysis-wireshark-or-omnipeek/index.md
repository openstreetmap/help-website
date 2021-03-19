+++
type = "question"
title = "Which tool is better for packet analysis Wireshark or OmniPeek ?"
description = '''I am new in packet analysis, The team I work with is having a big argument about which tool is better. so I decided to make it an open discussion and see your responses. thank you '''
date = "2014-09-14T10:12:00Z"
lastmod = "2015-04-21T06:37:00Z"
weight = 36311
keywords = [ "omnipeek", "wireshark" ]
aliases = [ "/questions/36311" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Which tool is better for packet analysis Wireshark or OmniPeek ?](/questions/36311/which-tool-is-better-for-packet-analysis-wireshark-or-omnipeek)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36311-score" class="post-score" title="current number of votes">0</div><span id="post-36311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new in packet analysis, The team I work with is having a big argument about which tool is better. so I decided to make it an open discussion and see your responses. thank you<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-omnipeek" rel="tag" title="see questions tagged &#39;omnipeek&#39;">omnipeek</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '14, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/c3b2db7f09e56fda1ee5f516d0e677f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Almeida&#39;s gravatar image" /><p><span>Almeida</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Almeida has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '14, 14:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36311" class="comments-container"></div><div id="comment-tools-36311" class="comment-tools"></div><div class="clear"></div><div id="comment-36311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36312"></span>

<div id="answer-container-36312" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36312-score" class="post-score" title="current number of votes">4</div><span id="post-36312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Almeida has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Which tools is better" is the same as asking about "PC vs. Mac", "Windows vs. Linux", "iPhone vs. Android", etc. - not really a good question to ask, because it depends on what you need.</p><p>Both Wireshark and Omnipeek are good tools, both have their strength and weaknesses. The two things where nobody will ever be able to beat Wireshark are</p><ol><li>Price (it's free)</li><li>Dissectors - the packet dissectors are too numerous to count and decode things most other tools have never thought about</li></ol><p>Things were Wireshark can be less optimal to use for are</p><ol><li>high speed packet capture (with "high speed" starting at about 300MBit/s) - other commercial tools come with specialized capture hardware, but to be fair you can use some of those cards with Wireshark, too</li><li>protocols that are proprietary and no documentation available. Some commercial analyzers like Omnipeek are able to decode some of them (with an NDA) e.g. Citrix ICA</li><li>fancy graphics - Wireshark is very technical and does not really produce eye candy (meaning: things that you can put in a report that the CEO has to understand, at least partially)</li><li>Advanced diagnostics, e.g. when comparing multi point captures</li></ol><p>There are probably more things, but any network analyst worth her/his salt will tell you that they combine different tools to get their results. Usually, Wireshark is the most trusted tool when it comes to decodes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '14, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36312" class="comments-container"><span id="41606"></span><div id="comment-41606" class="comment"><div id="post-41606-score" class="comment-score"></div><div class="comment-text"><p>nice thanks a lot.</p></div><div id="comment-41606-info" class="comment-info"><span class="comment-age">(20 Apr '15, 18:44)</span> <span class="comment-user userinfo">zhiying678</span></div></div><span id="41607"></span><div id="comment-41607" class="comment"><div id="post-41607-score" class="comment-score"></div><div class="comment-text"><p>Another advantage of Wireshark over OmniPeek:</p><p>If you're running some flavor of UN*X (Linux, OS X, *BSD, Solaris, AIX, HP-UX, etc.) rather than Windows, and don't have a virtual machine running Windows, and don't have a tool such as Wine that lets you run Windows binaries on your operating system, you can run Wireshark but you can't run OmniPeek. :-)</p></div><div id="comment-41607-info" class="comment-info"><span class="comment-age">(20 Apr '15, 18:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41608"></span><div id="comment-41608" class="comment"><div id="post-41608-score" class="comment-score"></div><div class="comment-text"><p>Another advantage of OmniPeek over Wireshark:</p><p>On Windows, OmniPeek can, with popular Wi-Fi adapters, capture in "monitor mode" and see traffic to or from other hosts and get radio information; Wireshark can't, because it uses WinPcap, which (currently) can't capture in monitor mode.</p></div><div id="comment-41608-info" class="comment-info"><span class="comment-age">(20 Apr '15, 18:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-36312" class="comment-tools"></div><div class="clear"></div><div id="comment-36312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41630"></span>

<div id="answer-container-41630" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41630-score" class="post-score" title="current number of votes">0</div><span id="post-41630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think there <strong><em>IS</em></strong> a major difference between Wireshark and OmniPeek especially when it comes to the question of "What is the purpose of performing the capture over WiFi?" Over the last year I asked a similar question on a blog regarding WiFi. After receiving many responses from across the industry (including IT Professionals, developers, education professionals, and hobbyists), there seems to be two different types of thinking when it comes to WiFi capturing:</p><ol><li><p>Macro-capturing = the need to capture all traffic and analyze a large amount of data. This type of capturing is done by IT departments to ensure connectivity across the network. There are many solutions for this need, including OmniPeek, Eye P.A., AirMagnet, etc.</p></li><li><p>Micro-capturing = the need to capture specific traffic between two devices and analyze the stream from a particular device. This type of capturing is mainly done by development and testing teams to ensure proper communication and protocol analysis. The best and cheapest solution for this type of need is Wireshark.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41630" class="comments-container"></div><div id="comment-tools-41630" class="comment-tools"></div><div class="clear"></div><div id="comment-41630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

