+++
type = "question"
title = "see UDP data with tshark"
description = '''i have this pcap file  in wireshark i can see data (click packet and goto floww UDP stream..) but when i show data in tshark, tshark print empty line, my command is this: tshark -r dns.cap -T fields -e data  i want see data in packet as HEX format'''
date = "2014-12-31T03:32:00Z"
lastmod = "2015-01-01T11:34:00Z"
weight = 38818
keywords = [ "tshark" ]
aliases = [ "/questions/38818" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [see UDP data with tshark](/questions/38818/see-udp-data-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38818-score" class="post-score" title="current number of votes">0</div><span id="post-38818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have <a href="https://www.cloudshark.org/captures/c32b074b2091">this pcap file</a></p><p>in <code>wireshark</code> i can see <code>data</code> (click packet and goto floww UDP stream..)</p><p>but when i show data in <code>tshark</code>, <code>tshark</code> print empty line,</p><p>my command is this:</p><pre><code>tshark -r dns.cap -T fields -e data</code></pre><p>i want see <code>data</code> in packet as <code>HEX</code> format</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '14, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/1cb87595461ed35a34557221c8805759?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Babyy&#39;s gravatar image" /><p><span>Babyy</span><br />
<span class="score" title="476 reputation points">476</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Babyy has no accepted answers">0%</span></p></div></div><div id="comments-container-38818" class="comments-container"></div><div id="comment-tools-38818" class="comment-tools"></div><div class="clear"></div><div id="comment-38818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38834"></span>

<div id="answer-container-38834" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38834-score" class="post-score" title="current number of votes">2</div><span id="post-38834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Babyy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your question you called it "<code>data</code>", but there is no "<code>data</code>" field in your captured packets, and you did this command:</p><pre><code>tshark -r dns.cap -T fields -e data</code></pre><p>That command will print out the value of the <code>data</code> field - "<code>data</code>" is a real name of a field in Wireshark/tshark, and it usually represents un-parsed payload bytes in the packet. But your capture of a DNS query and response has no <code>data</code> field in it, so you see nothing print out when you run that command. The same happens if you put "<code>data</code>" in the display filter of Wireshark: you won't see any packets displayed because no packet in your capture has a <code>data</code> field.</p><p>When you select "Follow UDP stream" in Wireshark, it shows you the raw UDP payload bytes of the UDP packet(s) of the UDP conversation, but they're not a "<code>data</code>" field.</p><p>I don't know of any tshark command which will print the UDP payload as raw bytes/hex directly. There are other, indirect, ways of getting the payload. One way is to follow the directions given in the answer to <a href="https://ask.wireshark.org/questions/38759/using-tshark-to-save-filtered-packets-to-file">this previous question</a>, by using the Lua script shown in <a href="https://ask.wireshark.org/questions/38759/using-tshark-to-save-filtered-packets-to-file/38799">that answer</a> and using the following command for your case:</p><pre><code>tshark -r dns2.cap -X lua_script:extract.lua -X lua_script1:dns -T fields -e extractor.value.hex</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-38834" class="comments-container"><span id="38840"></span><div id="comment-38840" class="comment"><div id="post-38840-score" class="comment-score"></div><div class="comment-text"><p>This command also prints a blank line :|</p></div><div id="comment-38840-info" class="comment-info"><span class="comment-age">(01 Jan '15, 09:45)</span> <span class="comment-user userinfo">Babyy</span></div></div><span id="38841"></span><div id="comment-38841" class="comment"><div id="post-38841-score" class="comment-score">1</div><div class="comment-text"><p>Doesn't for me - I get the following two lines:</p><pre><code>F8F401000001000000000000057961686F6F03636F6D0000010001
F8F481800001000300000000057961686F6F03636F6D0000010001C00C00010001000002430004628BB718C00C00010001000002430004CEBE242DC00C00010001000002430004628AFD6D</code></pre></div><div id="comment-38841-info" class="comment-info"><span class="comment-age">(01 Jan '15, 10:07)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="38842"></span><div id="comment-38842" class="comment"><div id="post-38842-score" class="comment-score"></div><div class="comment-text"><p>What version of shark do you have? Run: "<code>tshsark -v</code>" and paste the output here.</p></div><div id="comment-38842-info" class="comment-info"><span class="comment-age">(01 Jan '15, 10:08)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="38843"></span><div id="comment-38843" class="comment"><div id="post-38843-score" class="comment-score"></div><div class="comment-text"><p>thank you, my t shark version is : <code>TShark 1.6.7</code></p></div><div id="comment-38843-info" class="comment-info"><span class="comment-age">(01 Jan '15, 11:23)</span> <span class="comment-user userinfo">Babyy</span></div></div><span id="38844"></span><div id="comment-38844" class="comment"><div id="post-38844-score" class="comment-score"></div><div class="comment-text"><p>Oh wow. Version 1.6.7 is ancient history. That won't even run the Lua script. You should upgrade - version 1.12.2 is the most recent stable release. Get it from the <a href="https://www.wireshark.org/download.html">Wireshark downloads page</a>.</p></div><div id="comment-38844-info" class="comment-info"><span class="comment-age">(01 Jan '15, 11:34)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-38834" class="comment-tools"></div><div class="clear"></div><div id="comment-38834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38825"></span>

<div id="answer-container-38825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38825-score" class="post-score" title="current number of votes">0</div><span id="post-38825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which bit of the "data" do you want, the Ethernet header, the IP header, the UDP Header or the DNS query and response?</p><p>You can get all of the hex bytes with <code>-x</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '14, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38825" class="comments-container"><span id="38833"></span><div id="comment-38833" class="comment"><div id="post-38833-score" class="comment-score"></div><div class="comment-text"><p>i want see UDP data both query and response</p></div><div id="comment-38833-info" class="comment-info"><span class="comment-age">(31 Dec '14, 10:52)</span> <span class="comment-user userinfo">Babyy</span></div></div></div><div id="comment-tools-38825" class="comment-tools"></div><div class="clear"></div><div id="comment-38825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

