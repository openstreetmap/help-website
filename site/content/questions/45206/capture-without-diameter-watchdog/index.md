+++
type = "question"
title = "Capture without diameter watchdog"
description = '''Hi, I want to run a tcpdump capture for all diameter messages (port 3868). But I do not want the Watchdog request/response in the output pcap file. What kind of filter expression can I use ? Advice appreciated ; rgds'''
date = "2015-08-18T10:05:00Z"
lastmod = "2015-08-19T13:48:00Z"
weight = 45206
keywords = [ "diameter", "capture-filter", "pcap" ]
aliases = [ "/questions/45206" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture without diameter watchdog](/questions/45206/capture-without-diameter-watchdog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45206-score" class="post-score" title="current number of votes">0</div><span id="post-45206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to run a tcpdump capture for all diameter messages (port 3868). But I do not want the Watchdog request/response in the output pcap file. What kind of filter expression can I use ?</p><p>Advice appreciated ; rgds</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/a313dab3de560d801422d25e01518338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karhong&#39;s gravatar image" /><p><span>karhong</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karhong has no accepted answers">0%</span></p></div></div><div id="comments-container-45206" class="comments-container"></div><div id="comment-tools-45206" class="comment-tools"></div><div class="clear"></div><div id="comment-45206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45210"></span>

<div id="answer-container-45210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45210-score" class="post-score" title="current number of votes">0</div><span id="post-45210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is the display filter after you finished capturing:</p><p>(diameter) &amp;&amp; !(diameter.cmd.code == 280)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-45210" class="comments-container"><span id="45211"></span><div id="comment-45211" class="comment"><div id="post-45211-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>That is the display filter. What I am looking is the filtering out of diameter Watchdog request/responses <em>during</em> the capturing phase. I have taken a look at the manpage of 'pcap-filter'. Those filters have different syntax from the display filters.</p><p>Thanks in advance ; rgds.</p></div><div id="comment-45211-info" class="comment-info"><span class="comment-age">(18 Aug '15, 11:15)</span> <span class="comment-user userinfo">karhong</span></div></div><span id="45217"></span><div id="comment-45217" class="comment"><div id="post-45217-score" class="comment-score"></div><div class="comment-text"><p>You can use the above display filter, then export your capture file out using only the displayed packets (File - Export Specified Packets - Under Packet Range just make sure the displayed column is selected and all packets).</p><p>You would then have a capture file that only contains the diameter messages, but no watchdog requests and responses. If you are inspecting the capture live, it should only matter what is displayed and then later you are done and want to review it later the exported file would contain only the data you wanted.</p></div><div id="comment-45217-info" class="comment-info"><span class="comment-age">(18 Aug '15, 15:54)</span> <span class="comment-user userinfo">NiCe85</span></div></div><span id="45240"></span><div id="comment-45240" class="comment"><div id="post-45240-score" class="comment-score"></div><div class="comment-text"><p>Capture filters have a much more restricted view of the traffic, they're built for efficiency, and as such they don't understand the diameter protocol.</p><p>If the required values are always at the same offset in the capture you can use a capture offset filter using the slicing notation, e.g. tcp[x] = 280, where x is the offset of the diameter.cmd.code field.</p></div><div id="comment-45240-info" class="comment-info"><span class="comment-age">(19 Aug '15, 06:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-45210" class="comment-tools"></div><div class="clear"></div><div id="comment-45210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45248"></span>

<div id="answer-container-45248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45248-score" class="post-score" title="current number of votes">0</div><span id="post-45248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>HINT</strong>: If you remove single frames from a TCP stream, Wireshark will display error message, because it looks like packet loss, so please ignore error messages like ("TCP ACKed unseen segment" or similar), after you apply my capture filter!!</p><p>BTW: There might be better, more elegant capture filters to achieve your goal, but I have no time to optimize anything. It works, so it's good enough for me ;-)</p><p><strong>Option #1:</strong></p><p>Remove frames that are not Watchdog Request/Answer frames.</p><blockquote><p>dumpcap -ni eth0 -w diameter.pcap -f "port 3868 and not ((tcp[36:4] &amp; 0x80FFFFFF) = 0x00000118 or (tcp[36:4] &amp; 0x80FFFFFF) = 0x80000118)"</p></blockquote><p><strong>However</strong> this will also remove (most) ACK frames, as they don't have any data at position tcp[36:4], so you will see TCP error messages in Wireshark if you open the resulting pcap file.</p><p><strong>Option #2:</strong></p><p>Remove frames that are not Watchdog Request/Answer frames, but also keep ACK frames.</p><blockquote><p>dumpcap -ni eth0 -w diameter.pcap -f "port 3868 and ((ip[2:2]) &lt; 0x40 or not ((tcp[36:4] &amp; 0x80FFFFFF) = 0x00000118 or (tcp[36:4] &amp; 0x80FFFFFF) = 0x80000118))"</p></blockquote><p><strong>However</strong> this will also keep the ACK frames for the removed Watchdog frames, so again: error messages in Wireshark about missing frames!</p><p><strong>Option #3:</strong></p><p>Remove everything without TCP payload and frames that are not Watchdog Request/Answer frames.</p><blockquote><p>dumpcap -ni eth0 -w diameter.pcap -f "port 3868 and ((ip[2:2]) &gt; 0x40 and not ((tcp[36:4] &amp; 0x80FFFFFF) = 0x00000118 or (tcp[36:4] &amp; 0x80FFFFFF) = 0x80000118))"</p></blockquote><p><strong>However</strong> this will also remove the ACK frames for the remaining diameter frames, so again: error messages in Wireshark!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45248" class="comments-container"></div><div id="comment-tools-45248" class="comment-tools"></div><div class="clear"></div><div id="comment-45248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

