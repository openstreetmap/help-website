+++
type = "question"
title = "Multiple Messages in single frame causing problems while converting to csv using tshark"
description = '''Hi, I am trying to extract some information from a wireshark capture using tshark. the problem is that within a single packet there are multiple messages. The messages are of different types and hence all the messages do not contain all the parameters.  Due to this I am not able to figure out which ...'''
date = "2013-08-22T23:18:00Z"
lastmod = "2013-08-24T23:29:00Z"
weight = 23972
keywords = [ "tcpdump", "tshark", "wireshark" ]
aliases = [ "/questions/23972" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple Messages in single frame causing problems while converting to csv using tshark](/questions/23972/multiple-messages-in-single-frame-causing-problems-while-converting-to-csv-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23972-score" class="post-score" title="current number of votes">0</div><span id="post-23972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to extract some information from a wireshark capture using tshark. the problem is that within a single packet there are multiple messages. The messages are of different types and hence all the messages do not contain all the parameters. Due to this I am not able to figure out which parameter belongs to which message type.</p><p>The expression used by me is :</p><p>tshark -V -T fields -r "E:\Traces\IUPS-CP.pcap" -E separator=, -E header=y -e frame.time -e frame.number -e frame.len -e vlan.id -e ip.src -e ip.dst -e sctp.srcport -e sctp.dstport -e ip.proto -e m3ua.protocol_data_opc -e m3ua.protocol_data_dpc -e ranap.imsi_digits -e gsm_a.dtap_msg_sm_type -e gsm_a.dtap_msg_gmm_type -e ranap.lAC -e ranap.RAC -e ranap.sAC -e ranap.rNC_ID -e gsm_a.imsi -e ranap.radioNetwork -e gsm_a.sm.cause -e ranap.nAS -e &gt; c:\IUPS-SM.csv</p><p>Is there any expression which can be used in tshark to resolve this or any other way to resolve this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/799782db18884c8f445a7d7522d2551d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vishal%20Pathak&#39;s gravatar image" /><p><span>Vishal Pathak</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vishal Pathak has no accepted answers">0%</span></p></div></div><div id="comments-container-23972" class="comments-container"></div><div id="comment-tools-23972" class="comment-tools"></div><div class="clear"></div><div id="comment-23972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24016"></span>

<div id="answer-container-24016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24016-score" class="post-score" title="current number of votes">0</div><span id="post-24016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By multiple messages do you mean multiple applications in a single M3UA packet (Camel, MAP, RANAP, etc.), or multiple RANAP messages in a packet, or just multiple containers within the RANAP message (eg: the NAS container you care about)? Is your IuPS control interface deployed via an STP, or is this M3UA association direct from RNC to SGSN (where pure RANAP can be safely assumed)?</p><p>If you actually have multiple occurrences of RANAP messages in the same packet,or even multiple NAS containers, unfortunately since those values you want printed can occur at different times in different messages there's no way to just do a -T occurrences check, or to map the values to message containers with -T fields. The only solution for that that I've come up with so far is to use the '-O RANAP' option and read the output through a perl script to map out what values correspond to what RANAP message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-24016" class="comments-container"></div><div id="comment-tools-24016" class="comment-tools"></div><div class="clear"></div><div id="comment-24016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

