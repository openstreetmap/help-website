+++
type = "question"
title = "VLAN capture filter with DumpCap"
description = '''I&#x27;ve been trying to sniff a trunk running multiple VLANs with DumpCap, and would like to filter out all VLAN traffic except the VoIP VLAN, which is VLAN 11. I have tried using the filter qualifier such as -f vlan 11 or -f &quot;vlan 11&quot; or -f vlan:11 None of these permutations have worked. Anyone out the...'''
date = "2014-01-17T08:58:00Z"
lastmod = "2014-01-27T10:56:00Z"
weight = 28995
keywords = [ "filter", "capture", "vlan" ]
aliases = [ "/questions/28995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VLAN capture filter with DumpCap](/questions/28995/vlan-capture-filter-with-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28995-score" class="post-score" title="current number of votes">0</div><span id="post-28995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to sniff a trunk running multiple VLANs with DumpCap, and would like to filter out all VLAN traffic except the VoIP VLAN, which is VLAN 11. I have tried using the filter qualifier such as -f vlan 11 or -f "vlan 11" or -f vlan:11 None of these permutations have worked. Anyone out there had any success with using a VLAN capture filter? If so, can you elaborate?</p><p>Here is my full command-line:</p><p>dumpcap -i 2 -b files:144 -b duration:600 -f "vlan 11" -w dumptest.pcap</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/3d1f94fd059d26805abac57ed6299bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyp&#39;s gravatar image" /><p><span>randyp</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyp has no accepted answers">0%</span></p></div></div><div id="comments-container-28995" class="comments-container"><span id="29002"></span><div id="comment-29002" class="comment"><div id="post-29002-score" class="comment-score">1</div><div class="comment-text"><p>Are you actually capturing vlan-tagged frames? See the <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">VLAN</a> wiki page.</p></div><div id="comment-29002-info" class="comment-info"><span class="comment-age">(17 Jan '14, 12:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="29009"></span><div id="comment-29009" class="comment"><div id="post-29009-score" class="comment-score"></div><div class="comment-text"><p>On which OS is this?</p></div><div id="comment-29009-info" class="comment-info"><span class="comment-age">(18 Jan '14, 13:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29029"></span><div id="comment-29029" class="comment"><div id="post-29029-score" class="comment-score"></div><div class="comment-text"><p>Running WinXP. VLAN tagged packets show up when I run it through the WireShark GUI--but I will doublecheck this. I see from the DumpCap website that anytime you use a filter that contains a space, you must enclose it with quotation marks--when I do this, it acts like it takes the command, but never captures anything. Problem is, for an extended capture and for the amount of traffic, I have to use DumpCap to keep it from locking up.</p></div><div id="comment-29029-info" class="comment-info"><span class="comment-age">(20 Jan '14, 07:28)</span> <span class="comment-user userinfo">randyp</span></div></div></div><div id="comment-tools-28995" class="comment-tools"></div><div class="clear"></div><div id="comment-28995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29201"></span>

<div id="answer-container-29201" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29201-score" class="post-score" title="current number of votes">0</div><span id="post-29201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Finally figured this one out for myself.</p><p>tshark -i1 -c 5000 -f "vlan 11" -w filname.pcapng</p><p>This syntax works just fine with the -f filter; problem was that my company laptop was running Symantec Endpoint Protection in the background. Once I turned it off, the VLANs showed up!</p><p>I was having the same issue trying to do a capture filter for certain TCP or UDP ports--that also works fine now.</p><p>dumpcap -i1 -c 5000 -f "tcp port 443" -w filename.pcapng</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/3d1f94fd059d26805abac57ed6299bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyp&#39;s gravatar image" /><p><span>randyp</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyp has no accepted answers">0%</span></p></div></div><div id="comments-container-29201" class="comments-container"></div><div id="comment-tools-29201" class="comment-tools"></div><div class="clear"></div><div id="comment-29201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

