+++
type = "question"
title = "Same source and destination MAC address"
description = '''What will the Ethernet switch do, if my NIC transmits an Ethernet frame with same source and destination MAC address?'''
date = "2013-02-14T04:01:00Z"
lastmod = "2013-02-14T09:02:00Z"
weight = 18632
keywords = [ "ethernet", "mac", "switch", "address" ]
aliases = [ "/questions/18632" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Same source and destination MAC address](/questions/18632/same-source-and-destination-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18632-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What will the Ethernet switch do, if my NIC transmits an Ethernet frame with same source and destination MAC address?</p></div><div id="question-tags" class="tags-container tags">ethernet mac switch address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2b3f99b46ca3d6fa9894d76c5fb9377f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssp&#39;s gravatar image" /><p>ssp<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssp has no accepted answers">0%</span></p></div></div><div id="comments-container-18632" class="comments-container"></div><div id="comment-tools-18632" class="comment-tools"></div><div class="clear"></div><div id="comment-18632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18636"></span>

<div id="answer-container-18636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18636-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally a switch will never forward a packet out a port on which it was received, whether it was destined for the same mac address or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18636" class="comments-container"><span id="18708"></span><div id="comment-18708" class="comment"><div id="post-18708-score" class="comment-score"></div><div class="comment-text"><p>There is a nice flash video (hosted on cisco.com - apparently from howstuffworks.com) that shows the working of a switch, including <strong>filtering</strong>. The setup is slightly different but still the same 'problem'.</p><blockquote><p><code>http://www.cisco.com/image/gif/paws/10607/lan-switch-transparent.swf</code><br />
</p></blockquote><p>Maybe that helps the OP to better understand...</p><p>BTW: Works will in IE not so well in Firefox !?!</p></div><div id="comment-18708-info" class="comment-info"><span class="comment-age">(18 Feb '13, 09:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18636" class="comment-tools"></div><div class="clear"></div><div id="comment-18636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

