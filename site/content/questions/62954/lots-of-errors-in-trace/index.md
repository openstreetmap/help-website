+++
type = "question"
title = "Lots of errors in trace"
description = '''In the attached trace there are a lots of errors, which are not true. Some of them are below. https://drive.google.com/file/d/0B7Io9WiIN49VazZnZjJ4c2hwNTA/view?usp=sharing  Why does relative sequence numbers  not work. Why does tcp.time_delta display  values which are not at all true  (#6). There ar...'''
date = "2017-07-21T01:00:00Z"
lastmod = "2017-07-21T02:41:00Z"
weight = 62954
keywords = [ "retransmissions" ]
aliases = [ "/questions/62954" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lots of errors in trace](/questions/62954/lots-of-errors-in-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62954-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the attached trace there are a lots of errors, which are not true. Some of them are below.</p><p><a href="https://drive.google.com/file/d/0B7Io9WiIN49VazZnZjJ4c2hwNTA/view?usp=sharing">https://drive.google.com/file/d/0B7Io9WiIN49VazZnZjJ4c2hwNTA/view?usp=sharing</a></p><ol><li>Why does relative sequence numbers not work.</li><li>Why does tcp.time_delta display values which are not at all true (#6).</li><li>There are a lot of retransmission's and acked unseen segments which are also not true.</li><li>why does filtering with stream indexes not work. Stream index 0 only has 443-&gt;24891 traffic.</li></ol></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '17, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/5de3f05c3183608f6986dd68fa7eb0f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soochi&#39;s gravatar image" /><p>soochi<br />
<span class="score" title="57 reputation points">57</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soochi has no accepted answers">0%</span></p></div></div><div id="comments-container-62954" class="comments-container"><span id="62960"></span><div id="comment-62960" class="comment"><div id="post-62960-score" class="comment-score">1</div><div class="comment-text"><p>How was the capture made, i.e. on-host, tap, mirror or span port or something else?</p></div><div id="comment-62960-info" class="comment-info"><span class="comment-age">(21 Jul '17, 01:57)</span> grahamb ♦</div></div><span id="62962"></span><div id="comment-62962" class="comment"><div id="post-62962-score" class="comment-score"></div><div class="comment-text"><p>it was made on different devices on the path. example by dumping on the firewall, dumping on LB, and also via mirror port... all of them shows the same errors.</p></div><div id="comment-62962-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:01)</span> soochi</div></div><span id="62964"></span><div id="comment-62964" class="comment"><div id="post-62964-score" class="comment-score"></div><div class="comment-text"><p>If they show the same errors there's something with your capture platform. It is known that hardware offloading features may interfere with proper capturing of these protocol streams.</p></div><div id="comment-62964-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:22)</span> Jaap ♦</div></div><span id="62966"></span><div id="comment-62966" class="comment"><div id="post-62966-score" class="comment-score"></div><div class="comment-text"><p>error in capture platforms from many different vendors? all at the same time and all for the same IP pair combinations. highly unlikely!</p></div><div id="comment-62966-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:26)</span> soochi</div></div><span id="62975"></span><div id="comment-62975" class="comment"><div id="post-62975-score" class="comment-score"></div><div class="comment-text"><p>You never told <em>how</em> these captures were made, only <em>where</em>. It still can be the same laptop connected to different equipment in the network, either directly or via (possibly virtual) span or mirror.</p></div><div id="comment-62975-info" class="comment-info"><span class="comment-age">(21 Jul '17, 04:36)</span> Jaap ♦</div></div></div><div id="comment-tools-62954" class="comment-tools"></div><div class="clear"></div><div id="comment-62954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62969"></span>

<div id="answer-container-62969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62969-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps Wireshark is confused about which packets belong to which TCP connection. It looks as if packet 1 is the last packet of one TCP connection (an RST+ACK) and packet 2 is the initial SYN of a new TCP connection between the same endpoints (IP addresses+TCP ports), with packet 3 being the SYN+ACK, packet 4 being the ACK of the SYN+ACK, and packet 5 being the first data packet. That could cause various forms of confusion, including all of the symptoms reported above; stripping out the first packet seems to make at least some things work better.</p><p>Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, with your capture attached to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62969" class="comments-container"></div><div id="comment-tools-62969" class="comment-tools"></div><div class="clear"></div><div id="comment-62969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

