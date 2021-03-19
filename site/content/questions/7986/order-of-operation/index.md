+++
type = "question"
title = "Order-of-operation"
description = '''I am trying to solve a problem in an ESXi/XP environment. The VM is running XP and Wireshark, The host is running Solaris. Wireshark shows a packet leaving the VM but the Solaris server never sees the packet, nor does the span port on the Cisco switch. The vendor of the VM installed an Intel driver ...'''
date = "2011-12-15T07:24:00Z"
lastmod = "2012-01-10T11:40:00Z"
weight = 7986
keywords = [ "nic", "vm", "order" ]
aliases = [ "/questions/7986" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Order-of-operation](/questions/7986/order-of-operation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7986-score" class="post-score" title="current number of votes">0</div><span id="post-7986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to solve a problem in an ESXi/XP environment. The VM is running XP and Wireshark, The host is running Solaris.</p><p>Wireshark shows a packet leaving the VM but the Solaris server never sees the packet, nor does the span port on the Cisco switch. The vendor of the VM installed an Intel driver and right now that is where our suspicions are focused. He will fix that today.</p><p>But the question I have is where does Wireshark 'pick-up' the packet, if it actually never leaves the Intel NIC? This information would be useful to know so I could confidently rule out the NIC in this case and in other cases too.</p><p>I am planning to install Cisco 1000V to test the virtual switch but was hoping someone knew of documentation of Wireshark/tcpdump/snoop order-of-operation.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-vm" rel="tag" title="see questions tagged &#39;vm&#39;">vm</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '11, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/f5107f490d89ecc8b78f9d282e61f6a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ttpm&#39;s gravatar image" /><p><span>ttpm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ttpm has no accepted answers">0%</span></p></div></div><div id="comments-container-7986" class="comments-container"><span id="8306"></span><div id="comment-8306" class="comment"><div id="post-8306-score" class="comment-score"></div><div class="comment-text"><p>I have a similar issue. Have you found a resolution to your issue yet?</p></div><div id="comment-8306-info" class="comment-info"><span class="comment-age">(10 Jan '12, 11:40)</span> <span class="comment-user userinfo">jc931r</span></div></div></div><div id="comment-tools-7986" class="comment-tools"></div><div class="clear"></div><div id="comment-7986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7989"></span>

<div id="answer-container-7989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7989-score" class="post-score" title="current number of votes">0</div><span id="post-7989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand your question correctly you're running Wireshark inside the VM and capture the packet, but you do not see it outside the ESXi?</p><p>Wireshark picks up packets before it actually goes out onto the "wire" (or to the vSwitch of the ESXi, in this case), so seeing it in a capture done inside the VM does not mean it actually left it. You might want to enable promiscuous mode on the vSwitch and attach another VM with Wireshark running to see if the vSwitch got the packet at all (a vSwitch in promiscuous mode will forward all incoming packets to all ports, just like a hub does).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7989" class="comments-container"></div><div id="comment-tools-7989" class="comment-tools"></div><div class="clear"></div><div id="comment-7989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

