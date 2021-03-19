+++
type = "question"
title = "Wireshark display bug"
description = '''In the attached test.pcapng file Ethernet source address of all packets should cyclically change from 0 to 3 in the first byte like that:   00.00.00.00.01   01.00.00.00.01   02.00.00.00.01   03.00.00.00.01   00.00.00.00.01   01.00.00.00.01    .....   I see these addresses properly in my program, but...'''
date = "2014-09-05T11:33:00Z"
lastmod = "2014-09-05T12:23:00Z"
weight = 36029
keywords = [ "bug", "wireshark" ]
aliases = [ "/questions/36029" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark display bug](/questions/36029/wireshark-display-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36029-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the attached test.pcapng file Ethernet source address of all packets should cyclically change from 0 to 3 in the first byte like that:</p><ul><li><p>00.00.00.00.01</p></li><li><p>01.00.00.00.01</p></li><li><p>02.00.00.00.01</p></li><li><p>03.00.00.00.01</p></li><li><p>00.00.00.00.01</p></li><li><p>01.00.00.00.01</p></li><li><p>.....</p></li></ul><p>I see these addresses properly in my program, but Wireshark shows them incorrectly:</p><ul><li><p>00.00.00.00.01</p></li><li><p><strong>00</strong>.00.00.00.01</p></li><li><p>02.00.00.00.01</p></li><li><p>03.00.00.00.01</p></li><li><p>00.00.00.00.01</p></li><li><p><strong>00</strong>.00.00.00.01</p></li><li><p>.....</p></li></ul><p>and also for reason I don't understand why it specifically displays the "NETBIOS-" word for the packets with 03.00.00.00.01 address and not for others. I think that either it should not display this word (preferably) or should display it for all packets in the same way.</p></div><div id="question-tags" class="tags-container tags">bug wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '14, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/9b46c715cf0bfeca20dd3927c55be5fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravil&#39;s gravatar image" /><p>Ravil<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '14, 11:40</p></div></div><div id="comments-container-36029" class="comments-container"><span id="36033"></span><div id="comment-36033" class="comment"><div id="post-36033-score" class="comment-score"></div><div class="comment-text"><p>With which version of Wireshark does this happen? The MAC addresses look OK when I read it with a version built recently from the trunk and with 1.12.0.</p></div><div id="comment-36033-info" class="comment-info"><span class="comment-age">(05 Sep '14, 12:45)</span> Guy Harris ♦♦</div></div><span id="36035"></span><div id="comment-36035" class="comment"><div id="post-36035-score" class="comment-score"></div><div class="comment-text"><p>I see it on both 1.12.0 and 1.10.9. MAC address name resolution has to be on to see the error, otherwise the MAC address displays correctly.</p></div><div id="comment-36035-info" class="comment-info"><span class="comment-age">(05 Sep '14, 14:31)</span> Jim Aragon</div></div><span id="36037"></span><div id="comment-36037" class="comment"><div id="post-36037-score" class="comment-score"></div><div class="comment-text"><p>This is probably another side effect of bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10344">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10344</a> that is fixed in the upcoming 1.12.1 and 1.10.10 releases.</p></div><div id="comment-36037-info" class="comment-info"><span class="comment-age">(05 Sep '14, 15:59)</span> Pascal Quantin</div></div></div><div id="comment-tools-36029" class="comment-tools"></div><div class="clear"></div><div id="comment-36029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36030"></span>

<div id="answer-container-36030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36030-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let's take the second problem first.</p><pre><code>and also for reason I don&#39;t understand why it specifically displays the &quot;NETBIOS-&quot; word for the packets with 03.00.00.00.01 address and not for others. I think that either it should not display this word (preferably) or should display it for all packets in the same way.</code></pre><p>Click on "View" &gt; "Name Resolution" and then uncheck "Enable for MAC Layer" if you don't want to see that. No, it should not display it for all packets. Wireshark is attempting to display the friendly name for the OUI (Organizational Unit Identifier), which is the first three bytes of the MAC address. Since the first three bytes are different, Wireshark should not display the same thing for all packets.</p><p>I suggest opening the <em>manuf</em> file, which is in the Wireshark program files directory, searching for "NETBIOS-" (which you will find down on line 24,869) and read the note immediately above.</p><p>And now for the first problem:</p><pre><code>I see these addresses properly in my program, but Wireshark shows them incorrectly.</code></pre><p>You seem to have encountered a Wireshark display bug. If you turn off MAC address name resolution, as I suggest above, it will also fix this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '14, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-36030" class="comments-container"><span id="36031"></span><div id="comment-36031" class="comment"><div id="post-36031-score" class="comment-score"></div><div class="comment-text"><p>Yes, exactly! The problem is solved. Thank you!</p></div><div id="comment-36031-info" class="comment-info"><span class="comment-age">(05 Sep '14, 12:34)</span> Ravil</div></div></div><div id="comment-tools-36030" class="comment-tools"></div><div class="clear"></div><div id="comment-36030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

