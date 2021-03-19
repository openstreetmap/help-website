+++
type = "question"
title = "4 Errors in Expert Infos"
description = '''Hi recently we have been suffering from an ever increasing amount of timeouts to our database server during peak times. This issue had previously been put down to the SQL server being under high load and queries timing out due to server resource issues. Since the timeouts have become more frequent, ...'''
date = "2015-06-23T06:03:00Z"
lastmod = "2015-06-24T09:20:00Z"
weight = 43475
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/43475" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [4 Errors in Expert Infos](/questions/43475/4-errors-in-expert-infos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43475-score" class="post-score" title="current number of votes">0</div><span id="post-43475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi recently we have been suffering from an ever increasing amount of timeouts to our database server during peak times. This issue had previously been put down to the SQL server being under high load and queries timing out due to server resource issues. Since the timeouts have become more frequent, even during weekends when traffic is low I've turned my attention to the network as the source of the problem.</p><p>This morning I've ran a wireshark trace for 30 mins on a monitor port which was mirroring traffic from our primary database, and the following was displayed in the Expert Infos screen.</p><p><img src="http://oi57.tinypic.com/2nbuir7.jpg" alt="alt text" /></p><p>The Ethernet Bad checksum issue is being caused by the STP protocol messages coming from the switch, not sure if this one is actually a major issue.</p><p>The Malformed packets and retransmissions is what I'm more concerned with. I've been through and checked the following;</p><ul><li>All network cards are running at full duplex</li><li>All servers are connected at 1Gbit</li><li>No QoS services enabled on the switch</li></ul><p>Is there anything else obvious to check?</p><p>We have around 15 Windows 2003 servers, mix of physical and virtual (VMware ESX), plugged into a single 1Gbit HP switch. The storage network is plugged into a separate isolated switch.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/6683a2e04d93a62a03feec8f9991ce4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="siu07&#39;s gravatar image" /><p><span>siu07</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="siu07 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43475" class="comments-container"></div><div id="comment-tools-43475" class="comment-tools"></div><div class="clear"></div><div id="comment-43475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43510"></span>

<div id="answer-container-43510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43510-score" class="post-score" title="current number of votes">0</div><span id="post-43510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With a lot of guessing (without seeing the real capture) I would say that the reported errors have nothing to do with your real problem. The Bad checksumm on ethernet can mostly be ignored - depending on where the trace was taken - on an endpoint vs. in the network - it might not be correct (anymore) . So disable the checksumm validation under Protocol Preferences to get rid of those ... The TDS (and DCERPC) errors: wireshark is trying to dissect packets as TDS Tabular Data Stream when the payload is not carrying this protocol. You can disable the TDS protocol via Analyze -&gt; Enabled Protocols</p><p>That leaves the New Fragment overlaps ... an indication of packet loss and retransmissions occuring. These are not a red herring and might be related to a problem...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-269.png" alt="alt text" /></p><p>Just saw the "monitor port which was mirroring traffic from our primary database" - so if this was really a trace taken on a mirroring port the checksum better be correct or the packet will validly be dropped ...</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '15, 09:22</strong> </span></p></div></div><div id="comments-container-43510" class="comments-container"></div><div id="comment-tools-43510" class="comment-tools"></div><div class="clear"></div><div id="comment-43510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

