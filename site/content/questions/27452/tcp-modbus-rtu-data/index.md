+++
type = "question"
title = "TCP Modbus RTU Data"
description = '''When monitoring Modbus TCP, Wireshark seems to attempt to break down the data. It incorrectly interprets an ieee float as two UINT16 values. What configuration controls how the datagram is dissected? Likewise when monitoring encapsulated or wrapped Modbus Rtu, the datagram shows the raw data. I have...'''
date = "2013-11-26T14:28:00Z"
lastmod = "2013-12-13T01:41:00Z"
weight = 27452
keywords = [ "modbus", "datagram", "tcp" ]
aliases = [ "/questions/27452" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Modbus RTU Data](/questions/27452/tcp-modbus-rtu-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27452-score" class="post-score" title="current number of votes">0</div><span id="post-27452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When monitoring Modbus TCP, Wireshark seems to attempt to break down the data. It incorrectly interprets an ieee float as two UINT16 values. What configuration controls how the datagram is dissected? Likewise when monitoring encapsulated or wrapped Modbus Rtu, the datagram shows the raw data. I have not figured out how to apply the correct data intrepretation within TCP.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-datagram" rel="tag" title="see questions tagged &#39;datagram&#39;">datagram</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/68c400a866c09aef420d295e17c1777c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="btanner&#39;s gravatar image" /><p><span>btanner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="btanner has no accepted answers">0%</span></p></div></div><div id="comments-container-27452" class="comments-container"><span id="28055"></span><div id="comment-28055" class="comment"><div id="post-28055-score" class="comment-score"></div><div class="comment-text"><p>Looks like the Lua scripting language is what I was looking for for creating easy dissectors.</p></div><div id="comment-28055-info" class="comment-info"><span class="comment-age">(12 Dec '13, 08:53)</span> <span class="comment-user userinfo">btanner</span></div></div><span id="28070"></span><div id="comment-28070" class="comment"><div id="post-28070-score" class="comment-score"></div><div class="comment-text"><p>You could also look at <a href="http://wsgd.free.fr/">WSGD</a> that generates a dissector from a text file. Modbus traffic should be OK to handle with WSGD.</p></div><div id="comment-28070-info" class="comment-info"><span class="comment-age">(13 Dec '13, 01:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-27452" class="comment-tools"></div><div class="clear"></div><div id="comment-27452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27455"></span>

<div id="answer-container-27455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27455-score" class="post-score" title="current number of votes">0</div><span id="post-27455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What configuration controls how the datagram is dissected?</p></blockquote><p>The source code that's compiled into Wireshark; we currently don't have anything such as <a href="http://wsgd.free.fr">the Wireshark Generic Dissector</a> built into Wireshark and thus aren't using anything such as that to describe protocols in a fashion that would let users fix protocol dissection by editing a text file and restarting Wireshark. Instead, bugs in dissection need to be fixed by changing the source code for the dissector and recompiling.</p><p>Please file a bug on this on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, and please attach capture files (not screenshots, actually capture files) that demonstrate this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27455" class="comments-container"></div><div id="comment-tools-27455" class="comment-tools"></div><div class="clear"></div><div id="comment-27455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27465"></span>

<div id="answer-container-27465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27465-score" class="post-score" title="current number of votes">0</div><span id="post-27465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark?</p><p>This is not a bug. The Modbus protocol has no indication that two registers are to be treated as a 32 bit float, that is known only at the originating and receiving ends. This is a limitation in the Modbus protocol that is built around the simple data types of a single bit digital (coil) and a 16 bit register. Modbus isn't known as the lowest common denominator of the telemetry world for nothing.</p><p>However, some preferences and logic have been put into the Modbus data dissector such that if the function is either; Read Holding Registers (03), Read Input Registers (04) or Write Multiple Registers (16) and the number of data bytes is a multiple of 4, and the dissector preferences have been set to interpret data as a 32 bit value (32 bit uint, 32 bit IEEE float, 32 bit Modicon float), then the data will be dissected as such.</p><p>Note that there are separate data format dissector preferences for Modbus TCP and Modbus RTU.</p><p>Note that the preferences and logic are all or nothing, so that you can't have one of the function codes above, with the number of data bytes a multiple of 4 and the data containing a mix of 16 bit and 32 bit values interpreted correctly.</p><p>There have also been other additions to Wireshark so that if Modbus RTU (which is normally used over a serial line) is transmitted over a network (usually via a terminal server to the RTU), then the Modbus dissector will attempt to decode that data as well. In this case you must set the Modbus RTU Port value in the Modbus RTU dissector preferences, as there is no standard port for this, unlike Modbus TCP (502).</p><p>What do you mean by "encapsulated or wrapped Modbus RTU"?</p><p>I tested both these aspects today with Wireshark 1.10.3 64 bit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27465" class="comments-container"></div><div id="comment-tools-27465" class="comment-tools"></div><div class="clear"></div><div id="comment-27465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

