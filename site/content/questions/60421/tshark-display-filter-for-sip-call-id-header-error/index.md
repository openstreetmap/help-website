+++
type = "question"
title = "TSHARK Display Filter for SIP Call-ID Header Error"
description = '''I am trying to extract the SIP dialog (call) with a specific SIP Call-ID header value. For example, I am trying to run the following command with the noted display filter.  tshark -r Full_SIP-ISDN-GW.pcap -Y &quot;(sip.Call-ID == &quot;8005551212_45087863@xxx.xxx.xxx.xxx&quot;) or (udp.port==24116 and udp.port==80...'''
date = "2017-03-29T12:33:00Z"
lastmod = "2017-03-29T13:58:00Z"
weight = 60421
keywords = [ "error", "sip", "tshark", "display-filter" ]
aliases = [ "/questions/60421" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TSHARK Display Filter for SIP Call-ID Header Error](/questions/60421/tshark-display-filter-for-sip-call-id-header-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60421-score" class="post-score" title="current number of votes">0</div><span id="post-60421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to extract the SIP dialog (call) with a specific SIP Call-ID header value. For example, I am trying to run the following command with the noted display filter.</p><p><strong>tshark -r Full_SIP-ISDN-GW.pcap -Y "(sip.Call-ID == "<span class="__cf_email__" data-cfemail="ccf4fcfcf9f9f9fdfefdfe93f8f9fcf4fbf4faff8cb4b4b4e2b4b4b4e2b4b4b4e2b4b4b4">[email protected]</span>") or (udp.port==24116 and udp.port==8030)" -w extracted_call.pcap</strong></p><p>This display filter works fine in Wireshark, but I am getting the following error when running using in tshark.</p><p><strong>tshark: "@" was unexpected in this context.</strong></p><p>Does anyone have any ideas on how to get around this?</p><p>Thanks in advance.</p><p>Travis</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-60421" class="comments-container"><span id="60422"></span><div id="comment-60422" class="comment"><div id="post-60422-score" class="comment-score"></div><div class="comment-text"><p>TShark (Wireshark) 2.2.5 (v2.2.5-0-g440fd4d)</p></div><div id="comment-60422-info" class="comment-info"><span class="comment-age">(29 Mar '17, 12:38)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-60421" class="comment-tools"></div><div class="clear"></div><div id="comment-60421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60428"></span>

<div id="answer-container-60428" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60428-score" class="post-score" title="current number of votes">1</div><span id="post-60428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rooster_50 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely you need to escape the quotes for the string. Please give a try to:</p><pre><code>tshark -r Full_SIP-ISDN-GW.pcap -Y &quot;(sip.Call-ID == \&quot;[email protected]\&quot;) or (udp.port==24116 and udp.port==8030)&quot; -w extracted_call.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '17, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-60428" class="comments-container"><span id="60429"></span><div id="comment-60429" class="comment"><div id="post-60429-score" class="comment-score"></div><div class="comment-text"><p>That was it Pascal, many thanks!</p></div><div id="comment-60429-info" class="comment-info"><span class="comment-age">(29 Mar '17, 13:58)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-60428" class="comment-tools"></div><div class="clear"></div><div id="comment-60428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

