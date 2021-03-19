+++
type = "question"
title = "dns request duplicating"
description = '''everytime i make a dns request, it sends 2 requests insted of just 1 quest, is there a bug somewhere in wireshark/computer or did i not configure sometnig right screenshot http://imgur.com/hjYVT95'''
date = "2016-07-12T18:45:00Z"
lastmod = "2016-07-12T23:45:00Z"
weight = 54013
keywords = [ "request", "duplicating", "dns", "wireshark" ]
aliases = [ "/questions/54013" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dns request duplicating](/questions/54013/dns-request-duplicating)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>everytime i make a dns request, it sends 2 requests insted of just 1 quest, is there a bug somewhere in wireshark/computer or did i not configure sometnig right</p><p>screenshot <a href="http://imgur.com/hjYVT95">http://imgur.com/hjYVT95</a></p></div><div id="question-tags" class="tags-container tags">request duplicating dns wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '16, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/2df223dbb5ae1c84fb713cc591195742?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monstermatt2&#39;s gravatar image" /><p>Monstermatt2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monstermatt2 has no accepted answers">0%</span></p></div></div><div id="comments-container-54013" class="comments-container"></div><div id="comment-tools-54013" class="comment-tools"></div><div class="clear"></div><div id="comment-54013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54017"></span>

<div id="answer-container-54017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54017-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This most likely has to do with your capture setup. If you capture both ingress and egress traffic on a span you'll see frames twice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54017" class="comments-container"><span id="54033"></span><div id="comment-54033" class="comment"><div id="post-54033-score" class="comment-score"></div><div class="comment-text"><p>anyway to fix that?? or u cant</p></div><div id="comment-54033-info" class="comment-info"><span class="comment-age">(13 Jul '16, 06:29)</span> Monstermatt2</div></div><span id="54037"></span><div id="comment-54037" class="comment"><div id="post-54037-score" class="comment-score"></div><div class="comment-text"><p>Yes, editcap options -d / -D can be used to remove duplicates from a capture file.</p></div><div id="comment-54037-info" class="comment-info"><span class="comment-age">(13 Jul '16, 07:31)</span> Jaap ♦</div></div></div><div id="comment-tools-54017" class="comment-tools"></div><div class="clear"></div><div id="comment-54017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

