+++
type = "question"
title = "Still getting header checksum errors after disabling"
description = '''I understand why I was getting so many header checksum errors so I went to Edit &amp;gt; Preferences &amp;gt; Protocols and chose IPv4 as well as TCP and deselected &#x27;Validate the IPv4 checksum if possible&#x27; I&#x27;m still getting lots of header checksum errors, however. I would think they would be taken care of b...'''
date = "2012-07-24T08:45:00Z"
lastmod = "2012-07-24T12:41:00Z"
weight = 12958
keywords = [ "header", "recurring", "checksum" ]
aliases = [ "/questions/12958" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Still getting header checksum errors after disabling](/questions/12958/still-getting-header-checksum-errors-after-disabling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12958-score" class="post-score" title="current number of votes">0</div><span id="post-12958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand why I was getting so many header checksum errors so I went to Edit &gt; Preferences &gt; Protocols and chose IPv4 as well as TCP and deselected 'Validate the IPv4 checksum if possible'</p><p>I'm still getting lots of header checksum errors, however. I would think they would be taken care of by making those setting changes.</p><p>Anyone have any ideas?</p><p>Regards, Joe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-recurring" rel="tag" title="see questions tagged &#39;recurring&#39;">recurring</span> <span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '12, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/b2cdf181f709cd05d5fa9afb725a7355?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoeyJoeJoe1970&#39;s gravatar image" /><p><span>JoeyJoeJoe1970</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoeyJoeJoe1970 has no accepted answers">0%</span></p></div></div><div id="comments-container-12958" class="comments-container"></div><div id="comment-tools-12958" class="comment-tools"></div><div class="clear"></div><div id="comment-12958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12959"></span>

<div id="answer-container-12959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12959-score" class="post-score" title="current number of votes">0</div><span id="post-12959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are they by any chance UDP packets? You might want to disable checksum checking in the UDP protocol preferences too...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12959" class="comments-container"><span id="12960"></span><div id="comment-12960" class="comment"><div id="post-12960-score" class="comment-score"></div><div class="comment-text"><p>Nope. Checksum validation was turned off for IPv4, TCP and UDP.</p><p>The error I see is 'Header checksum: 0x000 [incorrect, should be 0xf9dc (maybe caused by "IP checksum offload"?)].</p><p>It's not for every packet but definitely every third one or so.</p></div><div id="comment-12960-info" class="comment-info"><span class="comment-age">(24 Jul '12, 09:23)</span> <span class="comment-user userinfo">JoeyJoeJoe1970</span></div></div><span id="12961"></span><div id="comment-12961" class="comment"><div id="post-12961-score" class="comment-score"></div><div class="comment-text"><p>Incoming or outgoing packets?</p></div><div id="comment-12961-info" class="comment-info"><span class="comment-age">(24 Jul '12, 09:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-12959" class="comment-tools"></div><div class="clear"></div><div id="comment-12959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12964"></span>

<div id="answer-container-12964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12964-score" class="post-score" title="current number of votes">0</div><span id="post-12964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Nope. Checksum validation was turned off for IPv4, TCP and UDP. The error I see is 'Header checksum: 0x000 [incorrect, should be 0xf9dc (maybe caused by "IP checksum offload"?)].</p></blockquote><p>sounds like IP checksum checking is not disabled, although you say so.</p><p>The code in epan/dissectors/packet-ip.c (Wireshark 1.8.0) will only print that specific error message, if the IP preference "Validate the IPv4 checksum if possible" is set (Default: yes/true).</p><blockquote><p><code>http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-ip.c</code><br />
</p></blockquote><p>What is the output of the following command?</p><blockquote><p><code>windows: tshark -G currentprefs  | find "ip.check"</code><br />
<code>unix: tshark -G currentprefs  | grep -i "ip.check"</code></p></blockquote><p>What is your Wireshark version?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jul '12, 12:27</strong> </span></p></div></div><div id="comments-container-12964" class="comments-container"><span id="12969"></span><div id="comment-12969" class="comment"><div id="post-12969-score" class="comment-score"></div><div class="comment-text"><p>command: tshark -G currentprefs | find "ip.check" results: ip.check_checksum: FALSE</p><p>Version 1.8.1 (SVN Rev 43946 from /trunk-1.8)</p><p>Puzzling</p></div><div id="comment-12969-info" class="comment-info"><span class="comment-age">(24 Jul '12, 12:27)</span> <span class="comment-user userinfo">JoeyJoeJoe1970</span></div></div><span id="12970"></span><div id="comment-12970" class="comment"><div id="post-12970-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Puzzling</p></blockquote><p>yep. Can you please post a screenshot (and possibly a sample capture file)?</p></div><div id="comment-12970-info" class="comment-info"><span class="comment-age">(24 Jul '12, 12:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12971"></span><div id="comment-12971" class="comment"><div id="post-12971-score" class="comment-score"></div><div class="comment-text"><p>I just tested with 1.8.1 on Windows 7 (32 Bit) and it works as expected. I modified the IP checksum with a HEX editor.</p><p>IP checksum checking: OFF</p><blockquote><p><code>Header checksum: 0x0000 [validation disabled]</code><br />
</p></blockquote><p>IP checksum checking: ON</p><blockquote><p><code>Header checksum: 0x0000 [incorrect, should be 0x267a (may be caused by "IP checksum offload"?)]</code><br />
</p></blockquote><p>If you run it on Windows as well, I recommend to uninstall Wireshark (delete preferences - ONLY if you don't need them) and then reinstall.</p></div><div id="comment-12971-info" class="comment-info"><span class="comment-age">(24 Jul '12, 12:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12964" class="comment-tools"></div><div class="clear"></div><div id="comment-12964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

