+++
type = "question"
title = "Attach wireshark to guest(virual machines) node"
description = '''Please guys, how do I attach wireshark to a virtual machine node? I am using NAT for 2 machines and using Internal Network to connect the 2 machines as well. I want to attach wireshark to the internal network node. Thanks'''
date = "2015-11-07T06:17:00Z"
lastmod = "2015-11-08T14:30:00Z"
weight = 47358
keywords = [ "node", "virtualbox", "wireshark" ]
aliases = [ "/questions/47358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Attach wireshark to guest(virual machines) node](/questions/47358/attach-wireshark-to-guestvirual-machines-node)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47358-score" class="post-score" title="current number of votes">0</div><span id="post-47358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please guys, how do I attach wireshark to a virtual machine node? I am using NAT for 2 machines and using Internal Network to connect the 2 machines as well. I want to attach wireshark to the internal network node. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '15, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/45d1ee0122f5cb72677fcedcdf92ac77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kelex&#39;s gravatar image" /><p><span>Kelex</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kelex has no accepted answers">0%</span></p></div></div><div id="comments-container-47358" class="comments-container"><span id="47415"></span><div id="comment-47415" class="comment"><div id="post-47415-score" class="comment-score"></div><div class="comment-text"><p>Is the VM host ESX, VMware Workstation, Hyper-V or something else?</p><p>I understand that VMNET on VMware workstation operates like a hub. In which case you would need to:</p><ul><li>Setup a VM to run Wireshark or dumpcap</li><li>Set the virtual NIC of that VM in promiscuous mode</li><li>Start capture</li></ul><p>For ESX both Jasper Bongertz and I covered this at Sharkfest 15. So you might want to view:</p><ul><li>Jasper's slides - <a href="http://sharkfest.wireshark.org/assets/presentations15/34.pdf">http://sharkfest.wireshark.org/assets/presentations15/34.pdf</a></li><li>My presentation - <a href="https://youtu.be/pb1yb1eUlgY">https://youtu.be/pb1yb1eUlgY</a> at 54:50</li></ul><p>Best regards...Paul</p></div><div id="comment-47415-info" class="comment-info"><span class="comment-age">(08 Nov '15, 14:30)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-47358" class="comment-tools"></div><div class="clear"></div><div id="comment-47358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

