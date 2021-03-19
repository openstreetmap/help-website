+++
type = "question"
title = "INVITE seems as &quot;Fragmented IP Protocol&quot;"
description = '''Hi; Whwn we create a SIP call INVITE do not appears in Wireshark trace. When we filter the trace as SIP the flow starts with &quot;100 Trying&quot;. When i search full trace the psition that belongs to INVITE is covered with &quot;Fragmented IP Protocol&quot;. It seems like wireshark can not produce the INVITE Message ...'''
date = "2011-11-29T03:45:00Z"
lastmod = "2014-04-23T00:43:00Z"
weight = 7697
keywords = [ "fragmented_ip" ]
aliases = [ "/questions/7697" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [INVITE seems as "Fragmented IP Protocol"](/questions/7697/invite-seems-as-fragmented-ip-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7697-score" class="post-score" title="current number of votes">0</div><span id="post-7697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi;</p><p>Whwn we create a SIP call INVITE do not appears in Wireshark trace. When we filter the trace as SIP the flow starts with "100 Trying". When i search full trace the psition that belongs to INVITE is covered with "Fragmented IP Protocol". It seems like wireshark can not produce the INVITE Message normally.</p><p>Is there ant option to have INVITE message with correct format with Wireshark?</p><p>Thanks Best Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmented_ip" rel="tag" title="see questions tagged &#39;fragmented_ip&#39;">fragmented_ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '11, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/aeea46dcfcc580a7902e10239d3b75f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m_ayazici&#39;s gravatar image" /><p><span>m_ayazici</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m_ayazici has no accepted answers">0%</span></p></div></div><div id="comments-container-7697" class="comments-container"></div><div id="comment-tools-7697" class="comment-tools"></div><div class="clear"></div><div id="comment-7697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32087"></span>

<div id="answer-container-32087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32087-score" class="post-score" title="current number of votes">1</div><span id="post-32087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>Disable the option "Reassemble fragmented IPv4 datagrams" in wireshark. Edit -&gt; Preferences -&gt; Protocols -&gt; IPv4.</p><p>Once this is done, you will see the pcap correctly.</p><p>Regards Diego</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/7254bfd7f451f232001d3b3ae50b642e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dpombo&#39;s gravatar image" /><p><span>dpombo</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dpombo has no accepted answers">0%</span></p></div></div><div id="comments-container-32087" class="comments-container"></div><div id="comment-tools-32087" class="comment-tools"></div><div class="clear"></div><div id="comment-32087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7702"></span>

<div id="answer-container-7702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7702-score" class="post-score" title="current number of votes">0</div><span id="post-7702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No idea if this helps, but you could try to toggle the "Reassemble fragmented IPv4 datagrams" in the IPv4 protocol preferences setting. Sometimes the Reassembly setting fools around with the decoding, so it might help to try to change it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '11, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7702" class="comments-container"><span id="7706"></span><div id="comment-7706" class="comment"><div id="post-7706-score" class="comment-score"></div><div class="comment-text"><p>"Reassemble fragmented IPv4 datagrams" was selected in the configuration of wireshark as default. I deselect it and tried again but it still seems as "Fragmented IP Protocol"</p><p>I tried it in SIP protocol also but it didn't effect also.</p><p>Thanks a lot for your help</p></div><div id="comment-7706-info" class="comment-info"><span class="comment-age">(29 Nov '11, 13:20)</span> <span class="comment-user userinfo">m_ayazici</span></div></div><span id="7710"></span><div id="comment-7710" class="comment"><div id="post-7710-score" class="comment-score"></div><div class="comment-text"><p>The traffic probably <em>is</em> fragmented, and there's something preventing the IPv4 dissector from reassembling the fragments. such as packets having been cut short by a snapshot length when capturing or IP checksum offloading causing outgoing packets to <em>appear</em> to have bad checksums.</p><p>There's nothing that can be done about the first of those, other than "don't capture with a snapshot length". For the second of those, <em>if</em> the "Fragmented IP Protocol" packets have a bad IP header checksum, turn off the "Validate the IPv4 checksum if possible" preference for IP.</p></div><div id="comment-7710-info" class="comment-info"><span class="comment-age">(29 Nov '11, 14:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7711"></span><div id="comment-7711" class="comment"><div id="post-7711-score" class="comment-score"></div><div class="comment-text"><p>(And if you've turned off "Reassemble fragmented IPv4 datagrams", turn it back on! If it's off, Wireshark won't even <em>try</em> to reassemble fragmented IPv4 datagrams.)</p></div><div id="comment-7711-info" class="comment-info"><span class="comment-age">(29 Nov '11, 14:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7702" class="comment-tools"></div><div class="clear"></div><div id="comment-7702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

