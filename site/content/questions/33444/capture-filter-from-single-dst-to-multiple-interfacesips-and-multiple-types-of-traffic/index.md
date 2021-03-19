+++
type = "question"
title = "Capture Filter from single dst to multiple interfaces/ips and multiple types of traffic"
description = '''Hello, I am trying to create a capture filter....  I have a Source Host, IP-A I have two Destination Host&#x27;s, IP-B and IP-C IP-B and IP-C are on two different NIC interfaces locally  I want to capture:  All UDP to IP-B from IP-A All TCP on port 5061 to IP-C from IP-A  Any help would be fantastic! Tha...'''
date = "2014-06-05T07:34:00Z"
lastmod = "2014-06-05T07:44:00Z"
weight = 33444
keywords = [ "multiple-interfaces", "capture-filter" ]
aliases = [ "/questions/33444" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture Filter from single dst to multiple interfaces/ips and multiple types of traffic](/questions/33444/capture-filter-from-single-dst-to-multiple-interfacesips-and-multiple-types-of-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to create a capture filter....</p><ul><li>I have a Source Host, IP-A</li><li>I have two Destination Host's, IP-B and IP-C</li><li>IP-B and IP-C are on two different NIC interfaces locally</li></ul><p>I want to capture:</p><ol><li>All UDP to IP-B from IP-A</li><li>All TCP on port 5061 to IP-C from IP-A</li></ol><p>Any help would be fantastic! Thanks all..</p></div><div id="question-tags" class="tags-container tags">multiple-interfaces capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/f82da48ff71e54dfa161705787d93c95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cwinchell&#39;s gravatar image" /><p>cwinchell<br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cwinchell has no accepted answers">0%</span></p></div></div><div id="comments-container-33444" class="comments-container"></div><div id="comment-tools-33444" class="comment-tools"></div><div class="clear"></div><div id="comment-33444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33446"></span>

<div id="answer-container-33446" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33446-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try:</p><p><code>(udp and src B and dst A) or (tcp and src port 5061 and src C and dst A)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33446" class="comments-container"><span id="33451"></span><div id="comment-33451" class="comment"><div id="post-33451-score" class="comment-score"></div><div class="comment-text"><p>Thank you grahamb!</p><p>I made a slight modify to your rule: (udp and <strong>src A</strong> and <strong>dst B</strong>) or (<strong>tcp port 5061</strong> and <strong>src A</strong> and <strong>dst C</strong>)</p></div><div id="comment-33451-info" class="comment-info"><span class="comment-age">(05 Jun '14, 07:55)</span> cwinchell</div></div><span id="33452"></span><div id="comment-33452" class="comment"><div id="post-33452-score" class="comment-score"></div><div class="comment-text"><p>Ok, my brain interpreted your clear statements the other way around for some odd reason, e.g from B to A.</p></div><div id="comment-33452-info" class="comment-info"><span class="comment-age">(05 Jun '14, 07:57)</span> grahamb ♦</div></div></div><div id="comment-tools-33446" class="comment-tools"></div><div class="clear"></div><div id="comment-33446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

