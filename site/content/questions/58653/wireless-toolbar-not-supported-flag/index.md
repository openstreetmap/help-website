+++
type = "question"
title = "Wireless toolbar not supported flag"
description = '''Have installed 2.2.3 and when I tried to open a wireless capture with the wireless toolbar it says &quot;Wireless controls are not supported in this version of Wireshark&quot; Just started using WS 2.X - have been a long time user of WS 1.X Thanks for any guidance'''
date = "2017-01-10T20:35:00Z"
lastmod = "2017-01-15T10:57:00Z"
weight = 58653
keywords = [ "wireless_toolbar" ]
aliases = [ "/questions/58653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless toolbar not supported flag](/questions/58653/wireless-toolbar-not-supported-flag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58653-score" class="post-score" title="current number of votes">0</div><span id="post-58653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have installed 2.2.3 and when I tried to open a wireless capture with the wireless toolbar it says "Wireless controls are not supported in this version of Wireshark"</p><p>Just started using WS 2.X - have been a long time user of WS 1.X Thanks for any guidance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless_toolbar" rel="tag" title="see questions tagged &#39;wireless_toolbar&#39;">wireless_toolbar</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '17, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-58653" class="comments-container"><span id="58654"></span><div id="comment-58654" class="comment"><div id="post-58654-score" class="comment-score"></div><div class="comment-text"><p>What operating system is Wireshark running on?</p></div><div id="comment-58654-info" class="comment-info"><span class="comment-age">(10 Jan '17, 20:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="58660"></span><div id="comment-58660" class="comment"><div id="post-58660-score" class="comment-score"></div><div class="comment-text"><p>On my systems, only Mac shows that now:</p><p>Windows V2.2.3:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Win_2.2.3_60Hf7BZ.png" alt="alt text" /></p><hr /><p>Linux V2.0.4:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Linux_2.0.4_wDfJEYM.png" alt="alt text" /></p><hr /><p>MacOS V2.2.3:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/MAC_2.2.3_f8pxnaD.png" alt="alt text" /></p></div><div id="comment-58660-info" class="comment-info"><span class="comment-age">(11 Jan '17, 03:15)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="58662"></span><div id="comment-58662" class="comment"><div id="post-58662-score" class="comment-score"></div><div class="comment-text"><p>Yup! That's the error I'm getting. Any thoughts as to why? Getting the same thing on my laptop too. My PC = W10, laptop = W7. Thanks</p><p>Eric</p></div><div id="comment-58662-info" class="comment-info"><span class="comment-age">(11 Jan '17, 05:54)</span> <span class="comment-user userinfo">EricKnaus</span></div></div></div><div id="comment-tools-58653" class="comment-tools"></div><div class="clear"></div><div id="comment-58653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58665"></span>

<div id="answer-container-58665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58665-score" class="post-score" title="current number of votes">1</div><span id="post-58665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any thoughts as to why?</p></blockquote><p>Because the wireless toolbar isn't yet supported on macOS. Sorry. Fixing that will require writing support code for it.</p><p>The only platform on which it's currently supported is Linux; on Windows, instead of the standard wireless toolbar, Wireshark has an AirPcap toolbar, which works only with AirPcap adapters. The regular wireless toolbar couldn't be supported on Windows, with regular wireless adapters, with WinPcap, but it might be possible to support it on Windows Vista and later with Npcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '17, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-58665" class="comments-container"><span id="58670"></span><div id="comment-58670" class="comment"><div id="post-58670-score" class="comment-score"></div><div class="comment-text"><p>Guy - Thanks for the response.<br />
So in order to even read a pcap file using the wireless tool bar on my Windows machines I will need to do ... what?</p><p>Eric</p></div><div id="comment-58670-info" class="comment-info"><span class="comment-age">(11 Jan '17, 14:06)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="58677"></span><div id="comment-58677" class="comment"><div id="post-58677-score" class="comment-score"></div><div class="comment-text"><p>Open it with Wireshark.</p><p>The wireless toolbar isn't something used when reading <em>existing</em> captures, it's something that's used when you're using Wireshark to <em>capture</em> traffic. It lets you choose what channel(s) you're capturing on, but once the traffic's been captured, it's not necessary.</p></div><div id="comment-58677-info" class="comment-info"><span class="comment-age">(11 Jan '17, 14:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="58683"></span><div id="comment-58683" class="comment"><div id="post-58683-score" class="comment-score"></div><div class="comment-text"><p>Guy - Got it - thanks! Guess I'll be picking up an AirPcap adapter shortly!</p></div><div id="comment-58683-info" class="comment-info"><span class="comment-age">(11 Jan '17, 17:21)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="58684"></span><div id="comment-58684" class="comment"><div id="post-58684-score" class="comment-score"></div><div class="comment-text"><p>Well, you'll only need it if 1) you have a Windows box and want to <em>capture</em> Wi-Fi traffic on it, 2) you are running Windows XP or earlier or don't want to experiment with using <a href="http://www.npcap.org">Npcap</a> rather than WinPcap, and 3) want to be able to control the Wi-Fi channel on which you're capturing through the GUI (I think there might be some command-line tools that come with Npcap, but there's no wireless toolbar in Wireshark for Npcap).</p><p>On macOS, you can capture Wi-Fi traffic using built-in AirPort adapters, but you can't control the channel from the GUI (you may be able to use <code>/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport</code> to control the channel).</p><p>On <em>all</em> those OSes, you can read a Wi-Fi capture file.</p><p>So if "open a wireless capture" means "start <em>capturing</em> Wi-Fi traffic with Wireshark", on most UN*Xes (Linux, macOS, *BSD) you should be able to do it, but you'll only be able to control the channel on which you're capturing from the GUI on Linux; on Windows, you'll either need an AirPcap adapter, with which you'll be able to control the channel from the GUI, or Windows Vista-or-later+Npcap, with which you won't be able to control the channel from the GUI.</p><p>If "open a wireless capture" means "open a file containing traffic that's already been captured on Wi-Fi", you can do that on any OS, and don't need an AirPcap adapter or, in fact, <em>any</em> Wi-Fi adapter.</p></div><div id="comment-58684-info" class="comment-info"><span class="comment-age">(11 Jan '17, 18:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="58781"></span><div id="comment-58781" class="comment"><div id="post-58781-score" class="comment-score"></div><div class="comment-text"><p>I fall under Category 1 of your above scenarios. It does come up all that often but when it does it's usually to clear myself of any "you totally screwed up our network" charges leveled at us by hyper-sensitive, trigger happy network fascists (just sayin'!). How's that for a label?! Thanks for your guidance. E</p></div><div id="comment-58781-info" class="comment-info"><span class="comment-age">(15 Jan '17, 10:57)</span> <span class="comment-user userinfo">EricKnaus</span></div></div></div><div id="comment-tools-58665" class="comment-tools"></div><div class="clear"></div><div id="comment-58665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

