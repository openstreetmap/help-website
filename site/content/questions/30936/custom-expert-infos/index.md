+++
type = "question"
title = "Custom Expert-infos"
description = '''Won&#x27;t lie, not too good with coding, so here&#x27;s what I&#x27;m trying to do: Make a custom expert-info (or color-rule otherwise) so that it will highlight a packet with a specific DS status (0x01, 0x02, 0x03 etc.) Highlight it in the Packet list, as well as in the Packet Details pane. I&#x27;ve gotten as far as...'''
date = "2014-03-18T16:13:00Z"
lastmod = "2014-03-18T16:13:00Z"
weight = 30936
keywords = [ "color-rules", "expert-info" ]
aliases = [ "/questions/30936" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Expert-infos](/questions/30936/custom-expert-infos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Won't lie, not too good with coding, so here's what I'm trying to do:</p><p>Make a custom expert-info (or color-rule otherwise) so that it will highlight a packet with a specific DS status (0x01, 0x02, 0x03 etc.) Highlight it in the Packet list, as well as in the Packet Details pane.</p><p>I've gotten as far as getting the wireshark sources, and looking at the epan/expert.x and epan/proto.h files, but at this point I'm out of my depth regarding the code. If someone could provide what format I would use, or if they knew a way to add a custom color rule that highlights it in both panes. So far, the only thing I've been able to accomplish is getting a custom color to highlight in the packet list, but not in the packet details.</p><p>Any help is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">color-rules expert-info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '14, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/a2115c753aa5ada76ef542f5350e0fc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reginald&#39;s gravatar image" /><p>Reginald<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reginald has no accepted answers">0%</span></p></div></div><div id="comments-container-30936" class="comments-container"><span id="30939"></span><div id="comment-30939" class="comment"><div id="post-30939-score" class="comment-score"></div><div class="comment-text"><p>No coding is necessary to highlight the packet in the packet list; that's what coloring rules are for.</p><p>What is it you want to highlight in the packet details? The field containing the DS status?</p></div><div id="comment-30939-info" class="comment-info"><span class="comment-age">(18 Mar '14, 20:47)</span> Guy Harris ♦♦</div></div><span id="30945"></span><div id="comment-30945" class="comment"><div id="post-30945-score" class="comment-score"></div><div class="comment-text"><p>I want it to highlight the field with the DS status.</p><p>I have seen the expert-infos do it, so I figured if I add a custom expert-info to the 802.11 dissector I would be able to highlight it in one of clothe currently established groups. (Ie yellow for PI_WARN)</p></div><div id="comment-30945-info" class="comment-info"><span class="comment-age">(19 Mar '14, 04:31)</span> Reginald</div></div><span id="30986"></span><div id="comment-30986" class="comment"><div id="post-30986-score" class="comment-score"></div><div class="comment-text"><p>I did suggest making it possible to associate expert info with a colouring rule in this post <a href="http://www.wireshark.org/lists/wireshark-dev/201308/msg00033.html">http://www.wireshark.org/lists/wireshark-dev/201308/msg00033.html</a></p><p>I never did implement it though.</p></div><div id="comment-30986-info" class="comment-info"><span class="comment-age">(20 Mar '14, 06:34)</span> MartinM</div></div></div><div id="comment-tools-30936" class="comment-tools"></div><div class="clear"></div><div id="comment-30936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

