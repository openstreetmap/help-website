+++
type = "question"
title = "Unexpected TCP retransmissions"
description = '''I am trying to debug a network using wireshark. I have a few VMs running on virtualbox. One of the VM is connected to the host using a &quot;host only&quot; interface. The host runs OVS through which all the VMs communicate. I ran wireshark on one of the VMs and the corresponding port on OVS and I see a numbe...'''
date = "2012-08-13T17:13:00Z"
lastmod = "2012-08-14T03:28:00Z"
weight = 13600
keywords = [ "retransmissions", "tcp", "wireshark" ]
aliases = [ "/questions/13600" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unexpected TCP retransmissions](/questions/13600/unexpected-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13600-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to debug a network using wireshark. I have a few VMs running on virtualbox. One of the VM is connected to the host using a "host only" interface. The host runs OVS through which all the VMs communicate. I ran wireshark on one of the VMs and the corresponding port on OVS and I see a number of TCP retransmissions. What can cause this?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_2.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">retransmissions tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 17:13</strong></p><img src="https://secure.gravatar.com/avatar/3fee5e731e44c6a77001f580ed181f34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhishek%20Chanda&#39;s gravatar image" /><p>Abhishek Chanda<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhishek Chanda has no accepted answers">0%</span></p></img></div></div><div id="comments-container-13600" class="comments-container"></div><div id="comment-tools-13600" class="comment-tools"></div><div class="clear"></div><div id="comment-13600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13605"></span>

<div id="answer-container-13605" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13605-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I see the following, possible reasons:</p><ul><li>a bug in the OpenFlow dissector (see also error message in the screenshot)</li><li>a bug in Open vSwitch</li><li>some kind of overload in your virtual environment, leading to drops within the Open vSwitch or one of the VMs</li><li>a bug in yor OS/application that handles the HTTP connection</li><li>any other strange problem, wich is unpredictable without further information about your system and software versions used.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13605" class="comments-container"><span id="13852"></span><div id="comment-13852" class="comment"><div id="post-13852-score" class="comment-score"></div><div class="comment-text"><p>This turned out to be a problem with Virtualbox. I changed to KVM and its gone.</p></div><div id="comment-13852-info" class="comment-info"><span class="comment-age">(23 Aug '12, 16:06)</span> Abhishek Chanda</div></div></div><div id="comment-tools-13605" class="comment-tools"></div><div class="clear"></div><div id="comment-13605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

