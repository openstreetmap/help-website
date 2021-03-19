+++
type = "question"
title = "HEX Interpretation"
description = '''Excuse me if this sounds like a stupid question or maybe i need a revision lesson. I have a HEX printout in Wireshark 0C27  Am i right that this is reversed to interpret as 270C or have i got this wrong. I ask because when converting using HEX calculator my result is 3111 Yet i am expecting the resu...'''
date = "2011-09-29T22:47:00Z"
lastmod = "2011-09-30T07:25:00Z"
weight = 6647
keywords = [ "hex" ]
aliases = [ "/questions/6647" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [HEX Interpretation](/questions/6647/hex-interpretation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6647-score" class="post-score" title="current number of votes">0</div><span id="post-6647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Excuse me if this sounds like a stupid question or maybe i need a revision lesson. I have a HEX printout in Wireshark 0C27 Am i right that this is reversed to interpret as 270C or have i got this wrong. I ask because when converting using HEX calculator my result is 3111 Yet i am expecting the result 9996</p><p>Thanks in Advance Sven</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '11, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/d113fbc61e0985b6f6c7b2cd6e8d6103?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sven&#39;s gravatar image" /><p><span>Sven</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sven has no accepted answers">0%</span></p></div></div><div id="comments-container-6647" class="comments-container"></div><div id="comment-tools-6647" class="comment-tools"></div><div class="clear"></div><div id="comment-6647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6648"></span>

<div id="answer-container-6648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6648-score" class="post-score" title="current number of votes">2</div><span id="post-6648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Welcome to <a href="http://en.wikipedia.org/wiki/Gulliver%27s_Travels">Gulliver’s Travels</a>, the confusing world of <a href="http://en.wikipedia.org/wiki/Endianness">endianess</a>. When you have a sequence of symbols it's always required to know in which order to interpret them.</p><p>Least significant bit vs. most significant, the bit order in an octet (8 bit sequence).</p><p>Least significant byte vs. most significant byte, the byte order in a word, long word, quad word, etc.</p><p>In your case it's the endianess of a 2 byte number that confuses you. You interpret it as big endian, which results in 0c27(hex) = 3111(dec). But since you know it's 9996(dec) = 270c(hex) you now know to interpret it little endian.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '11, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6648" class="comments-container"><span id="6651"></span><div id="comment-6651" class="comment"><div id="post-6651-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the advice the tips</p></div><div id="comment-6651-info" class="comment-info"><span class="comment-age">(30 Sep '11, 00:52)</span> <span class="comment-user userinfo">Sven</span></div></div></div><div id="comment-tools-6648" class="comment-tools"></div><div class="clear"></div><div id="comment-6648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6649"></span>

<div id="answer-container-6649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6649-score" class="post-score" title="current number of votes">2</div><span id="post-6649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Whether some part of the hex data is interpreted as <a href="http://en.wikipedia.org/wiki/Endianness">big-endian or little-endian</a> all depends on the protocol and sometimes even on the application or OS.</p><p>If you look at the sequence numbers in icmp echo packets. Although each ping program will count 1,2,3,4,etc, on the network it looks like 0x0001, 0x0002, 0x0003, 0x0004 for some systems and 0x0100, 0x0200, 0x0300, 0x0400 for others.</p><p>For well defined protocols, the protocol description should tell you how the values are put on the network. So in your case, it all depends on the definition of the protocol at hand.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '11, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6649" class="comments-container"><span id="6650"></span><div id="comment-6650" class="comment"><div id="post-6650-score" class="comment-score"></div><div class="comment-text"><p>Thanks what confuses me is that in the same message i get 52F020 which translates as 5435424 which is correct. Think i will have to do some reading this weekend.</p></div><div id="comment-6650-info" class="comment-info"><span class="comment-age">(30 Sep '11, 00:51)</span> <span class="comment-user userinfo">Sven</span></div></div><span id="6654"></span><div id="comment-6654" class="comment"><div id="post-6654-score" class="comment-score">1</div><div class="comment-text"><p>Many protocol make a blanket statement about endianess, like "the packets will be transmitted in network order". This means big endian, by the way, see RFC1700.</p><p>The host could be big or little endian in it's memory access. Hence any portable software must, before sending / receiving packets, be aware of this and convert multibyte fields between the two using hton<a href="">l|s</a> / ntoh<a href="">s|l</a> respectively. These macro's are empty on big endian architectures, and swap on little endian architectures.</p><p>This is where the ICMP count issue comes from.</p><p>In your example it seems there's a mix in endianess.</p></div><div id="comment-6654-info" class="comment-info"><span class="comment-age">(30 Sep '11, 07:25)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-6649" class="comment-tools"></div><div class="clear"></div><div id="comment-6649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

