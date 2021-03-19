+++
type = "question"
title = "how to capture vlan tag on osx 10.6 (lion)?"
description = '''i installed wireshark (64bits) on my macbook pro(2011 edition). but i found i couldn&#x27;t see vlan tag information. every packets were UNtagged. :( any idea?'''
date = "2012-05-29T08:34:00Z"
lastmod = "2012-05-31T11:09:00Z"
weight = 11446
keywords = [ "osx", "lion", "vlan" ]
aliases = [ "/questions/11446" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture vlan tag on osx 10.6 (lion)?](/questions/11446/how-to-capture-vlan-tag-on-osx-106-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i installed wireshark (64bits) on my macbook pro(2011 edition). but i found i couldn't see vlan tag information. every packets were UNtagged. :(</p><p>any idea?</p></div><div id="question-tags" class="tags-container tags">osx lion vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/c57f4e3aff3ceca6a1e4a1940360d390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itsmecho&#39;s gravatar image" /><p>itsmecho<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itsmecho has no accepted answers">0%</span></p></div></div><div id="comments-container-11446" class="comments-container"></div><div id="comment-tools-11446" class="comment-tools"></div><div class="clear"></div><div id="comment-11446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11455"></span>

<div id="answer-container-11455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11455-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you capturing by connecting the Macbook to the span port of a switch? Or are you trying to monitor the traffic originating and terminating on the Mac?</p><p>The VLAN tag is only part of the switched network packets, not the source or destination endpoint packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-11455" class="comments-container"><span id="11457"></span><div id="comment-11457" class="comment"><div id="post-11457-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to capture vlan tagged packets from switch by port mirroring (SPAN)</p></div><div id="comment-11457-info" class="comment-info"><span class="comment-age">(29 May '12, 19:06)</span> itsmecho</div></div><span id="11465"></span><div id="comment-11465" class="comment"><div id="post-11465-score" class="comment-score"></div><div class="comment-text"><p>Take a look at this question: (<a href="http://ask.wireshark.org/questions/10868/adding-vlan-tag-on-wireshark-capture)">http://ask.wireshark.org/questions/10868/adding-vlan-tag-on-wireshark-capture)</a> And confirm that A. The span port of your switch is including VLAN tags, and B. The NIC in your Macbook is not stripping the VLAN tags or rejecting VLAN tagged packets.</p></div><div id="comment-11465-info" class="comment-info"><span class="comment-age">(29 May '12, 23:13)</span> inetdog</div></div></div><div id="comment-tools-11455" class="comment-tools"></div><div class="clear"></div><div id="comment-11455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11500"></span>

<div id="answer-container-11500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11500-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What network interface are you capturing on? <code>en0</code>, or some other interface? If it's some other interface, try capturing on <code>en0</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-11500" class="comments-container"></div><div id="comment-tools-11500" class="comment-tools"></div><div class="clear"></div><div id="comment-11500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

