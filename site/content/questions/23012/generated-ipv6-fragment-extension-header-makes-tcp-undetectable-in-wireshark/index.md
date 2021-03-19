+++
type = "question"
title = "Generated IPV6 Fragment Extension Header makes TCP undetectable in wireshark"
description = '''Hello, I am trying to create random packets using a TCL script. I have encountered the following problem: When creating a TCP packet inside a IPV6 header that has a Fragment Extension Header, Wireshark no longer analyses the data containing the TCP packet (it is labeled simply as &quot;data&quot;). You can fi...'''
date = "2013-07-16T06:34:00Z"
lastmod = "2013-07-17T01:06:00Z"
weight = 23012
keywords = [ "fragment", "tcp", "ipv6" ]
aliases = [ "/questions/23012" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Generated IPV6 Fragment Extension Header makes TCP undetectable in wireshark](/questions/23012/generated-ipv6-fragment-extension-header-makes-tcp-undetectable-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23012-score" class="post-score" title="current number of votes">0</div><span id="post-23012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to create random packets using a TCL script. I have encountered the following problem: When creating a TCP packet inside a IPV6 header that has a Fragment Extension Header, Wireshark no longer analyses the data containing the TCP packet (it is labeled simply as "data").</p><p>You can find here an example of a file that I import into Wireshark to check if my generated packets are correct:</p><p>This file contains packets with fragment extension header - those with the mentioned issue: /6UzxGbgi</p><p>Here is a line from this file:</p><pre><code>000000 3E 7D 55 E9 27 1F EA 96 43 D7 B1 1B 08 00 60 09 16 A8 01 14 00 D2 30 07 52 D7 E0 8E 93 81 36 75 29 B8 CB 3F 54 03 66 6A 99 6D 3B 57 E0 2B 39 4B 96 52 52 68 B2 43 3C 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2B 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2C 00 01 05 68 43 21 00 33 00 00 01 3F B3 C1 FE 3C 08 00 00 8a 85 e6 b8 5a 8e 59 e9 49 84 12 39 87 46 51 38 74 86 91 35 48 31 52 38 74 53 43 81 73 47 51 96 70 00 00 00 06 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 6F ED 09 07 15 C6 F6 A4 00 00 00 00 51 00 1E 0B 85 1F 00 00 F4 66 97 BE 5B 85 A5 B1 F5 8B 1B A4 B3 55 25 4E F9 8E F7 FA 5B E2 03 76 FD 52 4F CE 30 42 8F A4 D0 CB BA C7 6B C7 D7 C5 AF BF 53 F6 4C 1E F2 2A 00 B5 E7 AA 18 D9 15 46 9B 29 AC 3D D0 34 29 60 A2 90 5F 1E 7D AA D7 5C 41 E7 3A D2 47 73 7F 67 89 35 E8 17 56 3A 44 3A 28 BF C7 6C 1A 21 B3 1B 26 C7 4C C7 B1 8E 45 35 A1 CA 63 13 0D 65 49 EC A4 C4 C5 F9 00 82 12 95 DB 61 9D 8E 38 E4 8E F9 D2 19 76 56 F3 10 21 EB D2 95 15 6C 0E BF 7D 8C 09 5A 6E B8 4A 24 65 7D</code></pre><p>This file contains packets without fragment extension header - maybe these also help you understand the issue: /mYTdisYy</p><p>Here is a line from this second file:</p><pre><code>000000 D8 57 96 65 C1 14 BE 6E AF 5E 45 47 08 00 60 05 1C FD 01 0C 00 0F B2 3A F2 3E 59 3B 9D C8 5D 82 23 15 71 8C AC E9 44 F2 E5 4D 2B 3B 20 AB B6 2A 8C E0 2E B7 26 A9 3C 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2B 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 33 00 01 05 68 43 21 00 3C 08 00 00 8a 85 e6 b8 5a 8e 59 e9 49 84 12 39 87 46 51 38 74 86 91 35 48 31 52 38 74 53 43 81 73 47 51 96 70 00 00 00 06 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 DC 79 A6 5A 23 07 0F 05 00 00 00 00 51 00 8A F2 47 BB 00 00 1B C5 78 1D 94 D1 8A 15 1D 1B AB CE 90 D5 19 87 23 70 82 6D 00 24 C4 55 E0 E4 60 9A 32 7B 7C 05 99 47 E6 84 B8 1D 32 53 BE CD 9D 6A E3 77 39 74 7E 0B 3A 13 C6 9E 28 41 74 24 8A 3C E2 1A 5A 9D 58 EF 7E 2D 40 F6 D4 91 9B 2C D4 C9 27 52 49 68 AB F0 13 67 E2 E3 A0 76 E8 93 47 57 F4 E6 AF AB 60 3B A9 4B BD 97 0B 98 09 E5 B0 82 28 61 C4 DA 67 30 D0 39 12 0D 5C 11 4A 06 EC 80 20 1E 1A E7 67 52 64 F5 E3 7E F2 60 B2 B8 80 29 FB 3F E6 18 2F A7 12 CB C1 0E 67 E7</code></pre><p>Both files are on Pastebin.</p><p>I am not asking for lines of code, I want to know what is wrong. I couldn't find anything about fragment headers interfering with tcp online, maybe you could direct me to somewhere I can find the answer.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/b68fad6a138a4a8e90f659020ff5b705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maio&#39;s gravatar image" /><p><span>Maio</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maio has no accepted answers">0%</span></p></div></div><div id="comments-container-23012" class="comments-container"></div><div id="comment-tools-23012" class="comment-tools"></div><div class="clear"></div><div id="comment-23012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23013"></span>

<div id="answer-container-23013" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23013-score" class="post-score" title="current number of votes">2</div><span id="post-23013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Maio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you've got the Ethertype wrong. If my hex reading skills are not totally off you're using Ethertype 0x0800, which is IPv4, not IPv6. You need to use 0x86dd instead.</p><p>Wireshark will decode the IPv6 layer nonetheless because the dissector also checks the IPv6 version nibble, but it may break further dissection. Fix your ethertype and try again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23013" class="comments-container"><span id="23014"></span><div id="comment-23014" class="comment"><div id="post-23014-score" class="comment-score"></div><div class="comment-text"><p>If I don't add the Fragment Extension Header, it detects the TCP packet.</p><p>I have fixed the Ethertype and it behaves the same way.</p></div><div id="comment-23014-info" class="comment-info"><span class="comment-age">(16 Jul '13, 06:47)</span> <span class="comment-user userinfo">Maio</span></div></div><span id="23015"></span><div id="comment-23015" class="comment"><div id="post-23015-score" class="comment-score">2</div><div class="comment-text"><p>Got it. You set the "more fragments" flag, and Wireshark tries to reassemble the packet before displaying the content. Turn off "Reassemble fragmented IPv6 datagrams" in your Wireshark's IPv6 preferences, and it will work.</p></div><div id="comment-23015-info" class="comment-info"><span class="comment-age">(16 Jul '13, 07:05)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="23062"></span><div id="comment-23062" class="comment"><div id="post-23062-score" class="comment-score"></div><div class="comment-text"><p>Yep, setting off "Reassemble fragmented IPv6 datagrams" worked. Thank you very much!</p></div><div id="comment-23062-info" class="comment-info"><span class="comment-age">(17 Jul '13, 01:06)</span> <span class="comment-user userinfo">Maio</span></div></div></div><div id="comment-tools-23013" class="comment-tools"></div><div class="clear"></div><div id="comment-23013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23028"></span>

<div id="answer-container-23028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23028-score" class="post-score" title="current number of votes">2</div><span id="post-23028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You probably have the IPv6 <em>"Reassemble fragmented IPv6 datagrams"</em> preference enabled, but you don't have all the IPv6 fragments in the capture file. If you don't have all the fragments but want to see the first fragment dissected by Wireshark, you need to turn off that preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23028" class="comments-container"></div><div id="comment-tools-23028" class="comment-tools"></div><div class="clear"></div><div id="comment-23028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

