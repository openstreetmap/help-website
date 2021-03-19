+++
type = "question"
title = "Ip Checksum offload in Vmware VMs."
description = '''Hello Experts. My Windows File server is so slow and it is Virtualized on Vmware ESXi 5.5. I capture some packets via Wireshark and it show me &quot;Ip Checksum offload&quot;. How can I solve it?link text link text I attached two photos and I&#x27;m thankful if you help me. Thank you.'''
date = "2015-05-09T07:42:00Z"
lastmod = "2015-05-14T15:50:00Z"
weight = 42254
keywords = [ "checksum", "offload" ]
aliases = [ "/questions/42254" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ip Checksum offload in Vmware VMs.](/questions/42254/ip-checksum-offload-in-vmware-vms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42254-score" class="post-score" title="current number of votes">0</div><span id="post-42254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts. My Windows File server is so slow and it is Virtualized on Vmware ESXi 5.5. I capture some packets via Wireshark and it show me "Ip Checksum offload". How can I solve it?<a href="https://osqa-ask.wireshark.org/upfiles/Wireshark-1.png">link text</a></p><p><a href="https://osqa-ask.wireshark.org/upfiles/Wireshark-2.png">link text</a></p><p>I attached two photos and I'm thankful if you help me.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-offload" rel="tag" title="see questions tagged &#39;offload&#39;">offload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '15, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/1f1d393403ea997213960ee852d8f897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hack3rcon&#39;s gravatar image" /><p><span>hack3rcon</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hack3rcon has no accepted answers">0%</span></p></div></div><div id="comments-container-42254" class="comments-container"></div><div id="comment-tools-42254" class="comment-tools"></div><div class="clear"></div><div id="comment-42254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42405"></span>

<div id="answer-container-42405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42405-score" class="post-score" title="current number of votes">2</div><span id="post-42405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You really should not solve this!</p><p>Because Wireshark told you something different.</p><p>Wireshark has seen a wrong IP Checksum (0x0000) and not (0x6460). So far so good. But the main cause for this behaviour is the feature Checksum offload and this fact is Wireshark telling you.</p><p>With this feature enabled network interface makes the checksum calculations and not the CPU. So if the checksum calculation is donne in the interface, Wireshark has no chance to see the Checksums.</p><p>My recommendation for your analysis is to disable the coloring rule with (fcs_bad).<br />
</p><p>And this has nothing to do with your slow connections. The root cause of your slow connection problem is a different. But this root cause I really can´t tell you with nothing more than this screenshots.</p><p>If you want further assistance you should upload a trace on cloudshark.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '15, 15:52</strong> </span></p></div></div><div id="comments-container-42405" class="comments-container"></div><div id="comment-tools-42405" class="comment-tools"></div><div class="clear"></div><div id="comment-42405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

