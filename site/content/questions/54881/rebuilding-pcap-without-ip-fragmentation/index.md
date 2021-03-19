+++
type = "question"
title = "Rebuilding PCAP without IP Fragmentation"
description = '''Can Wireshark rebuild an HTTP PCAP that contains IP Fragmentation and rebuild the PCAP so there is no IP Fragmentation present in the PCAP?'''
date = "2016-08-16T13:15:00Z"
lastmod = "2016-08-17T07:27:00Z"
weight = 54881
keywords = [ "ip", "fragmentation", "pcap" ]
aliases = [ "/questions/54881" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rebuilding PCAP without IP Fragmentation](/questions/54881/rebuilding-pcap-without-ip-fragmentation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54881-score" class="post-score" title="current number of votes">1</div><span id="post-54881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Wireshark rebuild an HTTP PCAP that contains IP Fragmentation and rebuild the PCAP so there is no IP Fragmentation present in the PCAP?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/7946b3dc310ab7d1e442e0e480ba47f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LennyB&#39;s gravatar image" /><p><span>LennyB</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LennyB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Aug '16, 03:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54881" class="comments-container"></div><div id="comment-tools-54881" class="comment-tools"></div><div class="clear"></div><div id="comment-54881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54883"></span>

<div id="answer-container-54883" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54883-score" class="post-score" title="current number of votes">0</div><span id="post-54883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark doesn't modify packets. I know of no other tool that can reassemble IP fragments and give you a PCAP with the reassembled packets. Why would you need this feature anyway?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54883" class="comments-container"><span id="54885"></span><div id="comment-54885" class="comment"><div id="post-54885-score" class="comment-score"></div><div class="comment-text"><p>Jasper, Thanks for the answer. The test tool I am using does not support reading in fragmented PCAPs. The PCAPs that I want to use contain IP Fragmentation.</p></div><div id="comment-54885-info" class="comment-info"><span class="comment-age">(16 Aug '16, 13:36)</span> <span class="comment-user userinfo">LennyB</span></div></div><span id="54886"></span><div id="comment-54886" class="comment"><div id="post-54886-score" class="comment-score"></div><div class="comment-text"><p>But the test tool can deal with oversized packets? Because that's what will happen if you reassemble IP fragments.</p><p>Maybe I can add a feature to TraceWrangler to do this kind of reassembly for you - how urgent is this?</p></div><div id="comment-54886-info" class="comment-info"><span class="comment-age">(16 Aug '16, 13:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="54888"></span><div id="comment-54888" class="comment"><div id="post-54888-score" class="comment-score"></div><div class="comment-text"><p>In the development version packet kan be exported on the exported pdu format at the Tcp or udp layer I think. Would that help?</p></div><div id="comment-54888-info" class="comment-info"><span class="comment-age">(16 Aug '16, 14:05)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="54913"></span><div id="comment-54913" class="comment"><div id="post-54913-score" class="comment-score"></div><div class="comment-text"><p>I also have this need, I have a capture of SIP traffic running permanently. When I need to analyse a call I use ngrep to filter a callid. But due to fragmentation, I do not get all the SIP messages. I have tcpdump exporting the fragments, but ngrep does not handle fragments. Thus I need jumbo frames.</p></div><div id="comment-54913-info" class="comment-info"><span class="comment-age">(17 Aug '16, 05:11)</span> <span class="comment-user userinfo">Kjeld Flarup</span></div></div><span id="54920"></span><div id="comment-54920" class="comment"><div id="post-54920-score" class="comment-score"></div><div class="comment-text"><p>At least in the development version you can use tshark to export PDU at OSI Layer 7 to extract the reassembled SIP traffic and then work on the resulting file, you might want to use 2 pass to make sure reassembly is OK.</p><p>tshark with parameters -U "OSI layer 7" -2</p></div><div id="comment-54920-info" class="comment-info"><span class="comment-age">(17 Aug '16, 07:27)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-54883" class="comment-tools"></div><div class="clear"></div><div id="comment-54883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

