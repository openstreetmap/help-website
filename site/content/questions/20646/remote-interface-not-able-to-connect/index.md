+++
type = "question"
title = "Remote interface Not Able to connect"
description = '''I am Trying to connect My PABX in wire shark using Remote Interface with Port number 5060 , But It&#x27;s not connection . Can any one help me , how to connect PABX network card.'''
date = "2013-04-19T17:15:00Z"
lastmod = "2013-04-20T05:04:00Z"
weight = 20646
keywords = [ "interface", "remote" ]
aliases = [ "/questions/20646" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote interface Not Able to connect](/questions/20646/remote-interface-not-able-to-connect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20646-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am Trying to connect My PABX in wire shark using Remote Interface with Port number 5060 , But It's not connection .</p><p>Can any one help me , how to connect PABX network card.</p></div><div id="question-tags" class="tags-container tags">interface remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '13, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/57bfe9fcc4d8d7efd8576cb7a2248974?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raamc&#39;s gravatar image" /><p>Raamc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raamc has no accepted answers">0%</span></p></div></div><div id="comments-container-20646" class="comments-container"></div><div id="comment-tools-20646" class="comment-tools"></div><div class="clear"></div><div id="comment-20646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20650"></span>

<div id="answer-container-20650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20650-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to start <strong>rpcapd</strong> on the remote machine (if it is a windows system). See the following article.</p><blockquote><p><code>http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</code><br />
</p></blockquote><p>In your case, you need to configure rpcapd to listen on port 5060. However, please see my hints.</p><p><strong>HINTS</strong></p><ol><li>I'm not sure if it is possible at all to run rpcapd on your PBX system.</li><li>If the system that runs rpcapd is a VoIP PBX, port 5060 could be used by the SIP Listener. In that case it's not a good idea to run rpcapd on that port.</li><li>If your PBX system is linux based, please have a look at the following question: <a href="http://ask.wireshark.org/questions/13217/remote-packet-capture-on-remote-linux-machine">http://ask.wireshark.org/questions/13217/remote-packet-capture-on-remote-linux-machine</a></li><li>If your PBX system is a proprietary system, then you can't use the remote capturing feature.</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '13, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Apr '13, 05:39</p></div></div><div id="comments-container-20650" class="comments-container"></div><div id="comment-tools-20650" class="comment-tools"></div><div class="clear"></div><div id="comment-20650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

