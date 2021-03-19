+++
type = "question"
title = "How to bind both RTP streams of a VoIP communication (MGCP/SDP)"
description = '''I have several Pcaps, some of them with only one communication (2 RTP streams), some of them with several communications (several streams). I&#x27;m trying to figure how can I bind RTP stream A and B of each communications. I&#x27;ve found in SDP packets the field mgcp.param.connectionid (2 bytes) that GENERA...'''
date = "2015-09-17T07:59:00Z"
lastmod = "2015-09-17T07:59:00Z"
weight = 45920
keywords = [ "mgcp", "voip", "rtp" ]
aliases = [ "/questions/45920" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to bind both RTP streams of a VoIP communication (MGCP/SDP)](/questions/45920/how-to-bind-both-rtp-streams-of-a-voip-communication-mgcpsdp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45920-score" class="post-score" title="current number of votes">0</div><span id="post-45920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have several Pcaps, some of them with only one communication (2 RTP streams), some of them with several communications (several streams).</p><p>I'm trying to figure how can I bind RTP stream A and B of each communications.</p><p>I've found in SDP packets the field mgcp.param.connectionid (2 bytes) that GENERALLY can help me for that, but in some pcaps one of the SDP has not this field.</p><p>I've also found a couple of pcaps with 3 RTP streams with the same connectionid field (one forward and two reverse)</p><p>I've also found a way in tshark with this command line to bind both ssrc</p><p>tshark -n -r xxxxxxx.pcap -2 -R rtcp -T fields -e rtcp.ssrc.identifier -Eseparator=, | sort -u | awk -F, {'print $1, $2'} | sort -u</p><p>but I can't reproduce the same in pyshark, rtcp.ssrc.identifier field does'nt have the list of ssrc. I'm not even sure that each stream HAS at least one RTCP packet for taking this approach.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mgcp" rel="tag" title="see questions tagged &#39;mgcp&#39;">mgcp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/47164287da0e0d6aec8ee380f9237932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qsebas&#39;s gravatar image" /><p><span>qsebas</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qsebas has one accepted answer">100%</span></p></div></div><div id="comments-container-45920" class="comments-container"></div><div id="comment-tools-45920" class="comment-tools"></div><div class="clear"></div><div id="comment-45920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

