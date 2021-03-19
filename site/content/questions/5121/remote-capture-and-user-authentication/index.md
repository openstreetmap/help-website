+++
type = "question"
title = "Remote capture and user authentication"
description = '''Hi, i&#x27;m using Wireshark to monitor traffic of a windows machine (using Winpcap). everything works fine but any user account which exists on the target machine is allowed to do a remote capture. how could i specify allowed user or groups ?'''
date = "2011-07-19T06:57:00Z"
lastmod = "2011-07-19T07:29:00Z"
weight = 5121
keywords = [ "winpcap", "remote" ]
aliases = [ "/questions/5121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture and user authentication](/questions/5121/remote-capture-and-user-authentication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i'm using Wireshark to monitor traffic of a windows machine (using Winpcap). everything works fine but any user account which exists on the target machine is allowed to do a remote capture. how could i specify allowed user or groups ?</p></div><div id="question-tags" class="tags-container tags">winpcap remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '11, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/966011a769960ea852447ac46f2e8de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sos00&#39;s gravatar image" /><p>sos00<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sos00 has no accepted answers">0%</span></p></div></div><div id="comments-container-5121" class="comments-container"></div><div id="comment-tools-5121" class="comment-tools"></div><div class="clear"></div><div id="comment-5121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5125"></span>

<div id="answer-container-5125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5125-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All you can do is limit the hosts which may connect. Run <code>rpcapd.exe -help</code> to see the options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '11, 07:29</p></div></div><div id="comments-container-5125" class="comments-container"><span id="5128"></span><div id="comment-5128" class="comment"><div id="post-5128-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap, I'm using third-party vpn for connecting to server so using the host file may causes some more problems.</p></div><div id="comment-5128-info" class="comment-info"><span class="comment-age">(19 Jul '11, 09:08)</span> sos00</div></div></div><div id="comment-tools-5125" class="comment-tools"></div><div class="clear"></div><div id="comment-5125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

