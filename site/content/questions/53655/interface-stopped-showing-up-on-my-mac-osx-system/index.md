+++
type = "question"
title = "Interface stopped showing up on my MAC OSX system"
description = '''When I originally installed Wireshark a few months ago, the active interface showed up and I was able to collect and analyze packets with no problem. Then, out of the blue, the interface stopped showing up and I cannot get it to show.  Doing an &quot;ifconfig&quot; reveals the interface just fine: en1: flags=...'''
date = "2016-06-26T08:44:00Z"
lastmod = "2016-06-27T08:43:00Z"
weight = 53655
keywords = [ "interface", "en1", "macosx" ]
aliases = [ "/questions/53655" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interface stopped showing up on my MAC OSX system](/questions/53655/interface-stopped-showing-up-on-my-mac-osx-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53655-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I originally installed Wireshark a few months ago, the active interface showed up and I was able to collect and analyze packets with no problem. Then, out of the blue, the interface stopped showing up and I cannot get it to show.<br />
</p><p>Doing an "ifconfig" reveals the interface just fine:</p><pre><code>en1: flags=8863&lt;up,broadcast,smart,running,simplex,multicast&gt; mtu 1500
    ether 88:63:df:c7:1b:37 
    inet6 fe80::8a63:dfff:fec7:1b37%en1 prefixlen 64 scopeid 0x5 
    inet 192.168.1.16 netmask 0xffffff00 broadcast 192.168.1.255
    nd6 options=1&lt;performnud&gt;
    media: autoselect
    status: active</code></pre>I am using Version 2.0.4 (v2.0.4-0-gdd7746e from master-2.0)<p>Thanks</p></div><div id="question-tags" class="tags-container tags">interface en1 macosx</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '16, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/b427b7af4aadff36df6847c58f9d846e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Frush&#39;s gravatar image" /><p>Andy Frush<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Frush has one accepted answer">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '16, 12:13</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-53655" class="comments-container"></div><div id="comment-tools-53655" class="comment-tools"></div><div class="clear"></div><div id="comment-53655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53676"></span>

<div id="answer-container-53676" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53676-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found the problem. In the preferences-&gt;advanced dialog there is an attribute called "capture.devices_hide". It was set to en1. (I don't know how it got set) I reset it to the default, (blank), and that fixed the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '16, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/b427b7af4aadff36df6847c58f9d846e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Frush&#39;s gravatar image" /><p>Andy Frush<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Frush has one accepted answer">100%</span></p></div></div><div id="comments-container-53676" class="comments-container"><span id="53686"></span><div id="comment-53686" class="comment"><div id="post-53686-score" class="comment-score"></div><div class="comment-text"><p>@Andy Frush, although it may seem funny, the next step is to accept your own Answer using the checkmark icon next to it. Questions with an accepted Answer are shown in green in the list to indicate they have been usefully answered. And the only person who can Accept an Answer is the author of the Question.</p></div><div id="comment-53686-info" class="comment-info"><span class="comment-age">(28 Jun '16, 00:46)</span> sindy</div></div></div><div id="comment-tools-53676" class="comment-tools"></div><div class="clear"></div><div id="comment-53676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

