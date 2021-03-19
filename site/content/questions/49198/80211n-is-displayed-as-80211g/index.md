+++
type = "question"
title = "802.11n is displayed as 802.11g."
description = '''I&#x27;m new to Wireshark, so I&#x27;m really hard to suppose why this happens. The connection between my PC and AP is certainly 802.11n, but the packets which is captured through AirPcap shows that PHY type is 802.11g. Is there any problem in my PC or AirPcap?'''
date = "2016-01-13T23:28:00Z"
lastmod = "2016-01-14T19:46:00Z"
weight = 49198
keywords = [ "802.11n" ]
aliases = [ "/questions/49198" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11n is displayed as 802.11g.](/questions/49198/80211n-is-displayed-as-80211g)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark, so I'm really hard to suppose why this happens.</p><p>The connection between my PC and AP is certainly 802.11n, but the packets which is captured through AirPcap shows that PHY type is 802.11g.</p><p>Is there any problem in my PC or AirPcap?</p></div><div id="question-tags" class="tags-container tags">802.11n</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '16, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/b97f6c2166d44cfec3e394149a408bf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chen0641&#39;s gravatar image" /><p>Chen0641<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chen0641 has no accepted answers">0%</span></p></div></div><div id="comments-container-49198" class="comments-container"><span id="49205"></span><div id="comment-49205" class="comment"><div id="post-49205-score" class="comment-score">1</div><div class="comment-text"><p>Maybe this article could give a small help: <a href="http://crnetpackets.com/2015/11/16/how-to-validate-the-wi-fi-information-within-wireshark-part-i-determining-the-wlan-capabilities/">http://crnetpackets.com/2015/11/16/how-to-validate-the-wi-fi-information-within-wireshark-part-i-determining-the-wlan-capabilities/</a></p></div><div id="comment-49205-info" class="comment-info"><span class="comment-age">(14 Jan '16, 01:35)</span> Christian_R</div></div><span id="49237"></span><div id="comment-49237" class="comment"><div id="post-49237-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Now I understand what was wrong!</p></div><div id="comment-49237-info" class="comment-info"><span class="comment-age">(14 Jan '16, 19:18)</span> Chen0641</div></div><span id="49238"></span><div id="comment-49238" class="comment"><div id="post-49238-score" class="comment-score">1</div><div class="comment-text"><p>Note, by the way, that Wireshark 2.x shows, in addition to the radiotap or PPI or... header, a "radio" header which is constructed from the radiotap or PPI or... header and that should show, for <em>all</em> header types (radiotap, PPI, or any of the other formats in non-pcap/pcapng capture files), radio information in a form that's easier to read than any of the raw headers. (It doesn't currently handle signal or noise levels from multiple antennas, but I plan to fix that.) That should, for most people, mean that it won't matter whether the headers are radiotap or PPI or something else.</p></div><div id="comment-49238-info" class="comment-info"><span class="comment-age">(14 Jan '16, 19:38)</span> Guy Harris ♦♦</div></div><span id="49241"></span><div id="comment-49241" class="comment"><div id="post-49241-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris: Thanks, Good to know.</p></div><div id="comment-49241-info" class="comment-info"><span class="comment-age">(14 Jan '16, 22:27)</span> Christian_R</div></div></div><div id="comment-tools-49198" class="comment-tools"></div><div class="clear"></div><div id="comment-49198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49239"></span>

<div id="answer-container-49239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49239-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The connection between my PC and AP is certainly 802.11n, but the packets which is captured through AirPcap shows that PHY type is 802.11g.</p></blockquote><p>The connection between my Mac and the AP is 802.11n, but if I do a capture, I see plenty of 802.11g packets as well as 802.11n packets. The 11g packets (which are really only 11b or even legacy 802.11 packets!) are sent from or to my ancient (first-generation!) iPhone.</p><p>So don't <em>assume</em> that all the packets on your network will be 11n.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '16, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49239" class="comments-container"></div><div id="comment-tools-49239" class="comment-tools"></div><div class="clear"></div><div id="comment-49239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

