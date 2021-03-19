+++
type = "question"
title = "Can tshark display textual HTTP content during capture?"
description = '''Hi SYN-bit I posted this question on ask.wireshark.org: http://ask.wireshark.org/questions/17961/display-http-content-as-text-using-tshark Jasper suggested I ask you whether you can help here. The question basically is, is it possible to get tshark to emit the content of a (textual) HTTP conversatio...'''
date = "2013-01-27T11:19:00Z"
lastmod = "2013-03-04T11:31:00Z"
weight = 17987
keywords = [ "live", "http", "tshark" ]
aliases = [ "/questions/17987" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can tshark display textual HTTP content during capture?](/questions/17987/can-tshark-display-textual-http-content-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17987-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi SYN-bit I posted this question on ask.wireshark.org: <a href="http://ask.wireshark.org/questions/17961/display-http-content-as-text-using-tshark">http://ask.wireshark.org/questions/17961/display-http-content-as-text-using-tshark</a> Jasper suggested I ask you whether you can help here. The question basically is, is it possible to get tshark to emit the content of a (textual) HTTP conversation live, that is not on a set of packets that have already been captured? Thanks! David</p></div><div id="question-tags" class="tags-container tags">live http tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '13, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/0b0ac57ffe8e8e5747c4b0f5595a521f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sackstein&#39;s gravatar image" /><p>David Sackstein<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sackstein has no accepted answers">0%</span></p></div></div><div id="comments-container-17987" class="comments-container"></div><div id="comment-tools-17987" class="comment-tools"></div><div class="clear"></div><div id="comment-17987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18032"></span>

<div id="answer-container-18032" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18032-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, I don't think that's (easily) possible. But I'm sure there are other specific http tools that will spit out the http objects for you while receiving them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18032" class="comments-container"></div><div id="comment-tools-18032" class="comment-tools"></div><div class="clear"></div><div id="comment-18032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19134"></span>

<div id="answer-container-19134" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19134-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi SYN-bit,</p><p>I was able to get what I needed in the end, so I will share my findings:</p><p>This is the command line I am using:</p><p>tshark.exe -i3 -l -f "tcp port 80" -O http -d tcp.port==80,http -o "ip.use_geoip:FALSE" -R "not tcp.analysis.duplicate_ack" -T fields -e ip.host -e tcp.port -e http.request.full_uri -e http.request.method -e http.response.code -e http.response.phrase -e http.content_length -e data -e text -E separator=;2&gt;&amp;0</p><p>-e data gets me the POST parameters and -e text gets me the content of the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '13, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/0b0ac57ffe8e8e5747c4b0f5595a521f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sackstein&#39;s gravatar image" /><p>David Sackstein<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sackstein has no accepted answers">0%</span></p></div></div><div id="comments-container-19134" class="comments-container"></div><div id="comment-tools-19134" class="comment-tools"></div><div class="clear"></div><div id="comment-19134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

