+++
type = "question"
title = "Issues with virtual machines"
description = '''One of our clients had previously used two computers to monitor SIP traffic, one before the firewall, and one internally. The hardware being in use all the time has meant that errors are occurring. So, we decided to implement server 2012 R2 to on a HPE ProLiant DL180 Gen9, two virtual machines, with...'''
date = "2016-11-28T03:19:00Z"
lastmod = "2017-01-04T10:45:00Z"
weight = 57674
keywords = [ "captureerror", "sip", "virtual" ]
aliases = [ "/questions/57674" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Issues with virtual machines](/questions/57674/issues-with-virtual-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57674-score" class="post-score" title="current number of votes">0</div><span id="post-57674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of our clients had previously used two computers to monitor SIP traffic, one before the firewall, and one internally. The hardware being in use all the time has meant that errors are occurring. So, we decided to implement server 2012 R2 to on a HPE ProLiant DL180 Gen9, two virtual machines, with two network cards, each one with two ports one for the connectivity of the server to the LAN, others for internal / external monitoring. We have a 3rd party that does the monitoring of the SIP traffic, they couldn't use the virtual machines to see the traffic, however if we run two instances of wireshark on the host the traffic is visible.</p><p>Are there any known issues with using virtual interfaces and wire shark ?</p><p>Are there any issues with SIP traffic and virtual machines ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureerror" rel="tag" title="see questions tagged &#39;captureerror&#39;">captureerror</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-virtual" rel="tag" title="see questions tagged &#39;virtual&#39;">virtual</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '16, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/5451bb4448fd0e632fa89aa0d5e8b3d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jordan_patrick_SS&#39;s gravatar image" /><p><span>jordan_patri...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jordan_patrick_SS has no accepted answers">0%</span></p></div></div><div id="comments-container-57674" class="comments-container"></div><div id="comment-tools-57674" class="comment-tools"></div><div class="clear"></div><div id="comment-57674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58509"></span>

<div id="answer-container-58509" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58509-score" class="post-score" title="current number of votes">0</div><span id="post-58509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In my experience it is always possible, in a VM, to capture traffic going into/out of that VM (using Wireshark or tcpdump).</p><p>If you're saying that the VM is dedicated for capturing other traffic (i.e., the traffic is <strong>not</strong> <em>naturally</em> going in/out of the VM) then you will need to arrange with the virtualization software and/or host to:</p><ol><li>Put the physical NICs in promiscuous mode</li><li>Allow the VMs to get copies of that monitored data (presumably by binding them to the physical NICs and configuring the virtual NICs into promiscuous mode)</li></ol><p>How you do that is probably specific to the virtualization software you're running.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58509" class="comments-container"></div><div id="comment-tools-58509" class="comment-tools"></div><div class="clear"></div><div id="comment-58509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

