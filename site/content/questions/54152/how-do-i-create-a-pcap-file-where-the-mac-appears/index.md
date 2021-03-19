+++
type = "question"
title = "¿How do I create a PCAP file where the MAC appears?"
description = '''try to create a pcap file from ubntu with dumpcap tool, but not the mac and I get priate time I turn the pcap in csv . help me please'''
date = "2016-07-18T23:30:00Z"
lastmod = "2016-07-19T04:19:00Z"
weight = 54152
keywords = [ "pcap", "dumpcap", "wireshark" ]
aliases = [ "/questions/54152" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [¿How do I create a PCAP file where the MAC appears?](/questions/54152/how-do-i-create-a-pcap-file-where-the-mac-appears)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54152-score" class="post-score" title="current number of votes">0</div><span id="post-54152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>try to create a pcap file from ubntu with dumpcap tool, but not the mac and I get priate time I turn the pcap in csv . help me please</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '16, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/cd94b0fac95d9efc8fd35a32533577db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrip&#39;s gravatar image" /><p><span>adrip</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrip has no accepted answers">0%</span></p></div></div><div id="comments-container-54152" class="comments-container"><span id="54153"></span><div id="comment-54153" class="comment"><div id="post-54153-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure we understand the question.</p><p>"PCAP file where the MAC appears" what does that mean?</p><p>"..., but not the mac", what does that mean?</p><p>"... I get priate time ...." what does that mean?</p></div><div id="comment-54153-info" class="comment-info"><span class="comment-age">(19 Jul '16, 01:59)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="54155"></span><div id="comment-54155" class="comment"><div id="post-54155-score" class="comment-score"></div><div class="comment-text"><p>Hello Jaap ,</p><p>When I am writing in the terminal dumpcap and apply filters and parameters , I am writing the route to be saved to a file with nombre.pcap .</p><p>when I convert that file to csv to see all GET port 80 IP 's shown me , and pages .</p><p>I want to see the MAC of computers on the network hacinedo GET requests and time that have been made. please</p></div><div id="comment-54155-info" class="comment-info"><span class="comment-age">(19 Jul '16, 03:12)</span> <span class="comment-user userinfo">adrip</span></div></div></div><div id="comment-tools-54152" class="comment-tools"></div><div class="clear"></div><div id="comment-54152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54156"></span>

<div id="answer-container-54156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54156-score" class="post-score" title="current number of votes">0</div><span id="post-54156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The CVS output only gives you the packet overview lines, so a single line per packet. This includes all columns you have configured (in the Default profile that is "No", "Time", "Source", "Destination", "Protocol", "Length" and "Info"). The "Time" column is already there. You can add a column to that, set the name to "MAC" and the type to "HW src addr". This gives you both a MAC address and a Timestamp in the CSV output.</p><p>Notes:</p><ol><li>The timestamp is of the moment the frame is timestamped on the capture interface.</li><li>The MAC address is that of the last IP node sending the frame, either the original host, or last intermediate router.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54156" class="comments-container"></div><div id="comment-tools-54156" class="comment-tools"></div><div class="clear"></div><div id="comment-54156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

