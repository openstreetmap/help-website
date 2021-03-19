+++
type = "question"
title = "installing Tshark"
description = '''Hi, I&#x27;m trying to install latest tshark. Currently I&#x27;m using CentOS 5.x and it seems that there&#x27;s no rpm for CentOS. Is there any link for downloading tshark source code or RPM for CentOS? I don&#x27;t need to install wireshark but tshark!! What I want to to is using frame.time_epoch filter but my curren...'''
date = "2012-12-06T10:45:00Z"
lastmod = "2012-12-06T12:22:00Z"
weight = 16646
keywords = [ "tshark" ]
aliases = [ "/questions/16646" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [installing Tshark](/questions/16646/installing-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16646-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to install latest tshark. Currently I'm using CentOS 5.x and it seems that there's no rpm for CentOS. Is there any link for downloading tshark source code or RPM for CentOS? I don't need to install wireshark but tshark!!</p><p>What I want to to is using frame.time_epoch filter but my current version, 1.0.15, doesn't provide this filter.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/2c33bce451fd8dc3844b351b798cbee1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fates&#39;s gravatar image" /><p>fates<br />
<span class="score" title="35 reputation points">35</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fates has no accepted answers">0%</span></p></div></div><div id="comments-container-16646" class="comments-container"></div><div id="comment-tools-16646" class="comment-tools"></div><div class="clear"></div><div id="comment-16646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16654"></span>

<div id="answer-container-16654" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16654-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, CentOS 5 uses a very old Wireshark. To get a newer version you'd have to compile your own. Wireshark 1.8 won't compile on CentOS 5 so you should pick up the latest Wireshark 1.6 source (get it from the <a href="https://www.wireshark.org/download.html">download page</a>).</p><p>When configuring you can disable wireshark (the GUI) by running 'configure' with "--disable-wireshark".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '12, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16654" class="comments-container"><span id="16657"></span><div id="comment-16657" class="comment"><div id="post-16657-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much!!! I'll try it. :)</p></div><div id="comment-16657-info" class="comment-info"><span class="comment-age">(06 Dec '12, 13:36)</span> fates</div></div><span id="16673"></span><div id="comment-16673" class="comment"><div id="post-16673-score" class="comment-score"></div><div class="comment-text"><p>Super!! It works!!! Thank you so much Jeff!!!</p></div><div id="comment-16673-info" class="comment-info"><span class="comment-age">(07 Dec '12, 01:08)</span> fates</div></div><span id="16677"></span><div id="comment-16677" class="comment"><div id="post-16677-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. I marked this answer as Accepted (by clicking the checkbox) for you.</p></div><div id="comment-16677-info" class="comment-info"><span class="comment-age">(07 Dec '12, 06:12)</span> JeffMorriss ♦</div></div><span id="16678"></span><div id="comment-16678" class="comment"><div id="post-16678-score" class="comment-score"></div><div class="comment-text"><p>Oh! I forgot to accept the answer. :)</p></div><div id="comment-16678-info" class="comment-info"><span class="comment-age">(07 Dec '12, 06:31)</span> fates</div></div></div><div id="comment-tools-16654" class="comment-tools"></div><div class="clear"></div><div id="comment-16654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

