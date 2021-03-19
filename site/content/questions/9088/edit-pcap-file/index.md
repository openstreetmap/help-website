+++
type = "question"
title = "Edit PCAP file"
description = '''Hello, I need to modify a pcap file. For example, I need to edit the IP address, timestamp, URL, ... fields. How can I do it? Do I have to write a new software application, or is one available in the network? Thanks Paolino'''
date = "2012-02-17T05:25:00Z"
lastmod = "2015-07-24T14:40:00Z"
weight = 9088
keywords = [ "edit", "pcap" ]
aliases = [ "/questions/9088" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Edit PCAP file](/questions/9088/edit-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9088-score" class="post-score" title="current number of votes">0</div><span id="post-9088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need to modify a pcap file. For example, I need to edit the IP address, timestamp, URL, ... fields. How can I do it? Do I have to write a new software application, or is one available in the network?</p><p>Thanks Paolino</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/9b0c75ce40880c709f41c1182bd3d8ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paolino&#39;s gravatar image" /><p><span>Paolino</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paolino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 20:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-9088" class="comments-container"></div><div id="comment-tools-9088" class="comment-tools"></div><div class="clear"></div><div id="comment-9088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

6 Answers:

</div>

</div>

<span id="9091"></span>

<div id="answer-container-9091" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9091-score" class="post-score" title="current number of votes">1</div><span id="post-9091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you need are tools that are usually used for anonymization and/or packet replay of trace files. You might want to take a look at tcprewrite, bittwiste, pktanon and other tools. You can also download the Sharkfest 2011 presentation (A-11) I did at the retrospective page:</p><p><a href="http://sharkfest.wireshark.org/sharkfest.11/index.html">http://sharkfest.wireshark.org/sharkfest.11/index.html</a></p><p><strong>Update:</strong> since 2013, you can also use <a href="https://www.tracewrangler.com">TraceWrangler</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '12, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Mar '15, 01:58</strong> </span></p></div></div><div id="comments-container-9091" class="comments-container"></div><div id="comment-tools-9091" class="comment-tools"></div><div class="clear"></div><div id="comment-9091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40574"></span>

<div id="answer-container-40574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40574-score" class="post-score" title="current number of votes">0</div><span id="post-40574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try WireEdit (wireedit.com). You can edit any field on any network layer for supported protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '15, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/bfcf401da9fc7c09faf43c83e4e7ce7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msukhar&#39;s gravatar image" /><p><span>msukhar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msukhar has no accepted answers">0%</span></p></div></div><div id="comments-container-40574" class="comments-container"></div><div id="comment-tools-40574" class="comment-tools"></div><div class="clear"></div><div id="comment-40574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40586"></span>

<div id="answer-container-40586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40586-score" class="post-score" title="current number of votes">0</div><span id="post-40586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If it's for a single packet and you want to edit some of the deeper application stuff, there's actually a custom compile option for wireshark that enables you to do that within Wireshark itself. That is, in a manual compile you can add "--enable-packet-editor" when doing a ./configure, allowing you to edit the packet fields in the GUI after Wireshark has decoded them: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9234">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9234</a></p><p>The catch there is that it's per-packet, GUI-based, so if you need to change many headers you're much better off with the other tools suggested. Only advantage to this method is that you have the power of Wireshark's dissectors to decode down into the application-specific field values for editing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '15, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Mar '15, 10:43</strong> </span></p></div></div><div id="comments-container-40586" class="comments-container"><span id="40588"></span><div id="comment-40588" class="comment"><div id="post-40588-score" class="comment-score"></div><div class="comment-text"><p>Also, the last time I checked, edited packets could not be saved. So it's use case was mainly to test how dissectors respond. Has that been changed since then and can edited packets be saved now?</p></div><div id="comment-40588-info" class="comment-info"><span class="comment-age">(15 Mar '15, 12:05)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="40595"></span><div id="comment-40595" class="comment"><div id="post-40595-score" class="comment-score"></div><div class="comment-text"><p>Ah, that's a good point. I just tested it, and while it will let you edit and save it won't reflect the actual edits in the new saved file.</p></div><div id="comment-40595-info" class="comment-info"><span class="comment-age">(15 Mar '15, 13:31)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-40586" class="comment-tools"></div><div class="clear"></div><div id="comment-40586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40645"></span>

<div id="answer-container-40645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40645-score" class="post-score" title="current number of votes">0</div><span id="post-40645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I use scapy (<a href="http://www.secdev.org/projects/scapy/).">http://www.secdev.org/projects/scapy/).</a> It's an extensible python tool that can capture and modify packets. However, tcprewrite is also a great choice, albeit more limited.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '15, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/0bd470f6c157ba727d5c2a68595d007e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="howlingcat&#39;s gravatar image" /><p><span>howlingcat</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="howlingcat has no accepted answers">0%</span></p></div></div><div id="comments-container-40645" class="comments-container"></div><div id="comment-tools-40645" class="comment-tools"></div><div class="clear"></div><div id="comment-40645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41716"></span>

<div id="answer-container-41716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41716-score" class="post-score" title="current number of votes">0</div><span id="post-41716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>if you want to write new application,you can write a c# program using pcap.net library.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/ffdb11952a5028d43a89614d8cad5983?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fateme&#39;s gravatar image" /><p><span>Fateme</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fateme has no accepted answers">0%</span></p></div></div><div id="comments-container-41716" class="comments-container"></div><div id="comment-tools-41716" class="comment-tools"></div><div class="clear"></div><div id="comment-41716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44453"></span>

<div id="answer-container-44453" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44453-score" class="post-score" title="current number of votes">0</div><span id="post-44453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use packet crafting libraries. I can recommend a library I'm developing: <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a>. It's a C++ library where you can open a pcap file, parse and edit the packets ini it and save them back to the pcap file. You didn't say which OS you'd like to use, but this library supports Windows, Linux and Mac OS</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p><span>seladb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-44453" class="comments-container"></div><div id="comment-tools-44453" class="comment-tools"></div><div class="clear"></div><div id="comment-44453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

