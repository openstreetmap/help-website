+++
type = "question"
title = "Export data for all received pacekts"
description = '''Hello I&#x27;ve got a capture from a device that has sent me 64K worth of data, and I&#x27;d like to export all of the data bytes to a bin file, or something of the like. Right now I have my filter set to ip.addr == 192.168.111.110  and I&#x27;d like to get all the data of each packet exported to a file. I don&#x27;t w...'''
date = "2013-02-26T14:17:00Z"
lastmod = "2013-02-26T14:29:00Z"
weight = 18896
keywords = [ "export" ]
aliases = [ "/questions/18896" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export data for all received pacekts](/questions/18896/export-data-for-all-received-pacekts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18896-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I've got a capture from a device that has sent me 64K worth of data, and I'd like to export all of the data bytes to a bin file, or something of the like.</p><p>Right now I have my filter set to ip.addr == 192.168.111.110</p><p>and I'd like to get all the data of each packet exported to a file.</p><p>I don't want to go to the data portion of each packet and select File --&gt; Export --&gt; Selected pacekt bytes. There must be a better way to do this.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/0d360038e03ff48b37e40b74e74caabf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="william256&#39;s gravatar image" /><p>william256<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="william256 has no accepted answers">0%</span></p></div></div><div id="comments-container-18896" class="comments-container"></div><div id="comment-tools-18896" class="comment-tools"></div><div class="clear"></div><div id="comment-18896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18897"></span>

<div id="answer-container-18897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18897-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>right click any packet, then "Follow TCP Stream" or "Follow UDP Stream" (depends on your protocol). Then: Save As (Raw).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '13, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '13, 14:29</p></div></div><div id="comments-container-18897" class="comments-container"></div><div id="comment-tools-18897" class="comment-tools"></div><div class="clear"></div><div id="comment-18897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

