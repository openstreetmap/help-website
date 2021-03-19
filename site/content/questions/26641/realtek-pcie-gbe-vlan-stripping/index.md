+++
type = "question"
title = "Realtek PCIe GBE vlan stripping"
description = '''I am trying to turn off vlan stripping on my Realtek PCIe GBE Family Controller, although not for Wireshark. I am working on INE labs and using the cloud connector to bridge from my GNS3 routers to my physical switches. I followed prior instructions and set the &quot;Priority &amp;amp; VLAN disabled&quot; option ...'''
date = "2013-11-03T11:47:00Z"
lastmod = "2013-11-04T05:20:00Z"
weight = 26641
keywords = [ "realtek", "vlan" ]
aliases = [ "/questions/26641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Realtek PCIe GBE vlan stripping](/questions/26641/realtek-pcie-gbe-vlan-stripping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26641-score" class="post-score" title="current number of votes">0</div><span id="post-26641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to turn off vlan stripping on my Realtek PCIe GBE Family Controller, although not for Wireshark. I am working on INE labs and using the cloud connector to bridge from my GNS3 routers to my physical switches. I followed prior instructions and set the "Priority &amp; VLAN disabled" option on the NIC driver. Was monitoring the registry key for the device and noticed the registry DWORD "*PriorityVLANTag=0" was created upon configuring this option, similar to the Marvell Yukon NIC. However, I am still unable to PING from my GNS3 virtual router with a subinterface dot1q tag to the SVI of the physical switch with matching VLAN #. Even tried setting the SkDisableVlanStrip value to 1 but to no avail.</p><p>One thing I did notice, while PING fails from both directions, the physical switch is able to complete ARP resolution and MAC of virtual router populates the Switch's MAC Add table, but NOT vice versa.</p><p>Any help you could offer would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-realtek" rel="tag" title="see questions tagged &#39;realtek&#39;">realtek</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '13, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/9385066850ce9688d3a8a2e6a01754d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tajikidc&#39;s gravatar image" /><p><span>tajikidc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tajikidc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>04 Nov '13, 03:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26641" class="comments-container"><span id="26654"></span><div id="comment-26654" class="comment"><div id="post-26654-score" class="comment-score"></div><div class="comment-text"><p>Converted "answer" to <a href="http://ask.wireshark.org/questions/5996/how-to-configure-realtek-pcie-gbe-family-controller-to-capture-vlan-tag-packet">this</a> question.</p></div><div id="comment-26654-info" class="comment-info"><span class="comment-age">(04 Nov '13, 03:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26658"></span><div id="comment-26658" class="comment"><div id="post-26658-score" class="comment-score"></div><div class="comment-text"><p>unless you can provide a capture file of the 'failing' ping, this is (kind of) unrelated to Wireshark and more a GNS3 configuration problem.</p></div><div id="comment-26658-info" class="comment-info"><span class="comment-age">(04 Nov '13, 05:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26641" class="comment-tools"></div><div class="clear"></div><div id="comment-26641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

