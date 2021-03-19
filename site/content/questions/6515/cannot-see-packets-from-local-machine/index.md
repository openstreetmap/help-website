+++
type = "question"
title = "Cannot see packets from local machine"
description = '''Hi All, I am running Wireshark 1.6.2 on a Windows 2008 server. However, I am unable to see any packets originating from the server. If I ping a remote host, I can see the return packets but not packets sent from the local host. Any clues? Bashment'''
date = "2011-09-23T08:47:00Z"
lastmod = "2011-10-11T03:34:00Z"
weight = 6515
keywords = [ "windows", "capture" ]
aliases = [ "/questions/6515" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see packets from local machine](/questions/6515/cannot-see-packets-from-local-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6515-score" class="post-score" title="current number of votes">0</div><span id="post-6515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am running Wireshark 1.6.2 on a Windows 2008 server. However, I am unable to see any packets originating from the server. If I ping a remote host, I can see the return packets but not packets sent from the local host.</p><p>Any clues?</p><p>Bashment</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '11, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/ea29c1dedd300a048eb75014b5d0ef73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BASHMENTY2K&#39;s gravatar image" /><p><span>BASHMENTY2K</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BASHMENTY2K has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '11, 15:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6515" class="comments-container"><span id="6806"></span><div id="comment-6806" class="comment"><div id="post-6806-score" class="comment-score"></div><div class="comment-text"><p>Has this server more than one network adpater?</p></div><div id="comment-6806-info" class="comment-info"><span class="comment-age">(08 Oct '11, 08:31)</span> <span class="comment-user userinfo">harper</span></div></div><span id="6808"></span><div id="comment-6808" class="comment"><div id="post-6808-score" class="comment-score"></div><div class="comment-text"><p>The configuration of the server is: Physical NIC = 2, However,one card is disabled IP Addresses: 1 + 3 virtual addresses used by the Microsoft NLB cluster, of which this server is a member OS: Windows 2008 Web Server</p><p>Note that the other cluster members are of similar hardware and software config, but wirshark works just fine on these servers.</p><p>Bashment</p></div><div id="comment-6808-info" class="comment-info"><span class="comment-age">(08 Oct '11, 11:07)</span> <span class="comment-user userinfo">BASHMENTY2K</span></div></div><span id="6843"></span><div id="comment-6843" class="comment"><div id="post-6843-score" class="comment-score"></div><div class="comment-text"><p>Try to check on every adapter wireshark provides as capture source and search for your outgoing traffic. In some cases e.g. two adapters in the same IP subnet, windows is theoretically able to send traffic out of a different card that the one designed as recipient for the answers</p></div><div id="comment-6843-info" class="comment-info"><span class="comment-age">(11 Oct '11, 03:34)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-6515" class="comment-tools"></div><div class="clear"></div><div id="comment-6515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

