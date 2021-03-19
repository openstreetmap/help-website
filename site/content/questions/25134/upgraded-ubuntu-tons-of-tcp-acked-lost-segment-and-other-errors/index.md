+++
type = "question"
title = "upgraded Ubuntu, tons of &#x27;TCP ACKed lost segment&#x27; and other errors..."
description = '''I couldn&#x27;t find a similar thread, sorry if this is a dup... I recently upgraded my Ubuntu 12.04 system, running the standard Wireshark 1.6.7, and am betting boatloads of &quot;TCP ACKed lost segment&quot; messages, as well as &quot;TCP Previous segment lost&quot;, and sometimes I&#x27;ve even seen FCS errors. Some details a...'''
date = "2013-09-23T15:14:00Z"
lastmod = "2013-09-24T08:36:00Z"
weight = 25134
keywords = [ "ack", "errors", "tcp", "ubuntu" ]
aliases = [ "/questions/25134" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [upgraded Ubuntu, tons of 'TCP ACKed lost segment' and other errors...](/questions/25134/upgraded-ubuntu-tons-of-tcp-acked-lost-segment-and-other-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I couldn't find a similar thread, sorry if this is a dup...</p><p>I recently upgraded my Ubuntu 12.04 system, running the standard Wireshark 1.6.7, and am betting boatloads of "TCP ACKed lost segment" messages, as well as "TCP Previous segment lost", and sometimes I've even seen FCS errors. Some details about my environment:</p><ul><li>Running VirtualBox for my Ubuntu systems</li><li>Host OS is Windows 8, Wireshark there runs fine without errors</li><li>Updated VMs are showing the errors above</li><li>On my lone un-updated Ubuntu system, it runs fine without errors</li><li>I've uninstalled and reinstalled multiple times with the same issue</li><li>I've compiled from the latest source on an updated system but have the same issue</li></ul><p>I'm going to try installing a brand new Ubuntu 13.04 system, and will post the results, but if anybody has any ideas of what might be causing this, please send them my way. Thanks!</p></div><div id="question-tags" class="tags-container tags">ack errors tcp ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '13, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/c4df2966640e6bdf8dfacdbae3bdb8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chuck-tallac&#39;s gravatar image" /><p>chuck-tallac<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chuck-tallac has no accepted answers">0%</span></p></div></div><div id="comments-container-25134" class="comments-container"></div><div id="comment-tools-25134" class="comment-tools"></div><div class="clear"></div><div id="comment-25134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25148"></span>

<div id="answer-container-25148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25148-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This might be caused by 'offload' features enabled. Try disabling LRO TSO and GSO using the ethtool -k command</p><p>A nice writeup on the ethtool can be found <a href="http://securityonion.blogspot.de/2011/10/when-is-full-packet-capture-not-full.html">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '13, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '13, 22:56</p></div></div><div id="comments-container-25148" class="comments-container"><span id="25160"></span><div id="comment-25160" class="comment"><div id="post-25160-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestion mrEEde - plus I now know a lot about ethtool that I didn't know before. Unfortunately though, turning off all the offloads, even some you didn't mention explicitly, has not resolved the issue. I'm still getting these errors. Thanks for the info however.</p></div><div id="comment-25160-info" class="comment-info"><span class="comment-age">(24 Sep '13, 08:29)</span> chuck-tallac</div></div></div><div id="comment-tools-25148" class="comment-tools"></div><div class="clear"></div><div id="comment-25148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25161"></span>

<div id="answer-container-25161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25161-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Running VirtualBox for my Ubuntu systems<br />
Host OS is Windows 8, Wireshark there runs fine without errors</p></blockquote><p>Based on that information, I assume you're capturing on the bridged interface of VirtualBox on Windows 8.</p><p>If so, I'd like to refer you to similar problems posted here and in other forums.</p><blockquote><p><a href="https://www.google.com/?q=site:ask.wireshark.org+virtualbox">https://www.google.com/?q=site:ask.wireshark.org+virtualbox</a><br />
<a href="https://www.google.com/?q=virtualbox%20bridged%20wireshark">https://www.google.com/?q=virtualbox%20bridged%20wireshark</a><br />
</p></blockquote><p>There seems to be an ever recurring problem with VirtualBox and sniffing on the bridged interface. Maybe the update of your virtual machine (including kernel and network driver) broke something (like the internal handling of the VM traffic by the VirtualBox bridged interface) and thus you don't see some packets in Wireshark, if you capture on the bridged interface.</p><p>Usually it works very well to use Wireshark within the virtual machine.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Sep '13, 08:38</p></div></div><div id="comments-container-25161" class="comments-container"><span id="25163"></span><div id="comment-25163" class="comment"><div id="post-25163-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for the tip and pointers to those articles about wireshark and virtualbox. I suspect that you are correct regarding the updating of my VM causing some internal driver change that broke something in wireshark.</p><p>I am stuck in that I must use bridged mode since I'm running services on my VMs that require communication from other external devices. I will keep poking around and reading more hints like the ones you posted to see if there is a reasonable workaround.</p><p>Thanks again for the help!</p></div><div id="comment-25163-info" class="comment-info"><span class="comment-age">(24 Sep '13, 08:51)</span> chuck-tallac</div></div><span id="25171"></span><div id="comment-25171" class="comment"><div id="post-25171-score" class="comment-score"></div><div class="comment-text"><blockquote><p>some internal driver change that broke something in wireshark.</p></blockquote><p>It did not break Wireshark. Most certainly it broke some functionality of the VirtualBox bridged interface ;-)</p><blockquote><p>I will keep poking around and reading more hints like the ones you posted <strong>to see if there is a reasonable workaround</strong>.</p></blockquote><p>I've never found or heard of a reliable workaround, except capturing <strong>within</strong> the virtual machine.</p></div><div id="comment-25171-info" class="comment-info"><span class="comment-age">(24 Sep '13, 13:11)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25161" class="comment-tools"></div><div class="clear"></div><div id="comment-25161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

