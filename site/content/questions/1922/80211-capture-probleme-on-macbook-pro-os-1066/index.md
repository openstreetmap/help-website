+++
type = "question"
title = "802.11 capture probleme on MacBook Pro (os 10.6.6)"
description = '''I&#x27;ve just changed may MacBook Pro. I have the same Airport chipset and firmware than my old one.  With my old MacBook Pro and old Wireshark version, the Link-Layer header type for my airport interface proposed me different option: Ethernet, 802.11, ... With my new MacBook and Wireshark 1.4.3, i have...'''
date = "2011-01-25T07:22:00Z"
lastmod = "2011-01-25T15:01:00Z"
weight = 1922
keywords = [ "airport", "802.11", "macbook", "pro" ]
aliases = [ "/questions/1922" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 capture probleme on MacBook Pro (os 10.6.6)](/questions/1922/80211-capture-probleme-on-macbook-pro-os-1066)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1922-score" class="post-score" title="current number of votes">0</div><span id="post-1922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just changed may MacBook Pro. I have the same Airport chipset and firmware than my old one. With my old MacBook Pro and old Wireshark version, the Link-Layer header type for my airport interface proposed me different option: Ethernet, 802.11, ... With my new MacBook and Wireshark 1.4.3, i have only Ethernet option. However there is a new topic "Capture packets in monitor mode". In this mode I can choose 802.11. However only the 66 first byte of frames data are captured. Same probleme with tcpdump:</p><blockquote><p>tcpdump -y ieee802_11_radio -s 256 -i en1 tcpdump: IEEE802_11_RADIO is not one of the DLTs supported by this device How can i capture complete 802.11 traffic on my MacBook pro, as I did before ?</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-macbook" rel="tag" title="see questions tagged &#39;macbook&#39;">macbook</span> <span class="post-tag tag-link-pro" rel="tag" title="see questions tagged &#39;pro&#39;">pro</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/bd19860db193f4952d58e883d3415d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Serge%20Botkine&#39;s gravatar image" /><p><span>Serge Botkine</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Serge Botkine has no accepted answers">0%</span></p></div></div><div id="comments-container-1922" class="comments-container"></div><div id="comment-tools-1922" class="comment-tools"></div><div class="clear"></div><div id="comment-1922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1936"></span>

<div id="answer-container-1936" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1936-score" class="post-score" title="current number of votes">0</div><span id="post-1936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>802.11 adapters can capture in a number of modes, including <a href="https://secure.wikimedia.org/wikipedia/en/wiki/Monitor_mode">monitor mode</a>. The way monitor mode is selected is, at the low level, different in different OSes; in OS X 10.5.x and 10.6.x, the way to ask the driver to run in monitor mode is to select an 802.11 link-layer type when capturing - and if you select one of those link-layer types, the adapter will go into monitor mode.</p><p>Libpcap 1.0 added programming interfaces to select monitor mode; Wireshark 1.4 supports those APIs, if present. When using those APIs, Wireshark lets you select monitor mode by checking the "Capture packets in monitor mode" check box, and only shows the link-layer types available in the mode you select - if you're not in monitor mode, you can only get Ethernet headers on 802.11 devices.</p><p>OS X 10.6.x includes libpcap 1.0.x - and tcpdump 4.x. This means that, to capture in monitor mode, you have to use the "-I" flag to tcpdump:</p><pre><code>tcpdump -I -s 256 -i en1</code></pre><p>Note that monitor mode defaults to IEEE802_11_RADIO, so you don't need a -y flag. Note also that the "256" includes the Radiotap header.</p><p>The Wireshark dmg for Snow Leopard uses the new APIs, so, to capture in monitor mode with TShark, you must specify the -I flag, and, to capture in monitor mode with Wireshark, you must check the "Capture packets in monitor mode" checkbox. As noted, if you want 802.11 headers, you must capture in monitor mode.</p><p>As for only seeing the first 66 bytes of packet data, try not specifying the "-s" flag to tcpdump or TShark, or selecting "Limit each packet to {XXX} bytes" in Wireshark. If you don't get the full packet, that's probably an OS X bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-1936" class="comments-container"></div><div id="comment-tools-1936" class="comment-tools"></div><div class="clear"></div><div id="comment-1936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

