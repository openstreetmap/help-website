+++
type = "question"
title = "How do I get the packet detail text using tshark?"
description = '''In Wireshark, fields are shown in the packet details pane using some particular text rendering, but tshark shows a different rendering. For example, ip.version is rendered as 0100 .... = Version: 4 for a particular packet in Wireshark. Invoking tshark -r myPacket.pcap -T fields -e &quot;ip.version&quot; outpu...'''
date = "2015-03-05T13:24:00Z"
lastmod = "2015-03-05T17:34:00Z"
weight = 40301
keywords = [ "development", "text", "dissector", "tshark", "display" ]
aliases = [ "/questions/40301" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I get the packet detail text using tshark?](/questions/40301/how-do-i-get-the-packet-detail-text-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40301-score" class="post-score" title="current number of votes">1</div><span id="post-40301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark, fields are shown in the packet details pane using some particular text rendering, but tshark shows a different rendering.</p><p>For example, <code>ip.version</code> is rendered as <code>0100 .... = Version: 4</code> for a particular packet in Wireshark. Invoking <code>tshark -r myPacket.pcap -T fields -e "ip.version"</code> outputs <code>4</code>.</p><p><strong>Is there a way to extract the text using tshark?</strong></p><p>I have a field in one of my dissectors that is added to the tree using <code>proto_tree_add_int_format_value</code>, and I'd like to be able to capture some parts of that formatted output using tshark in a script. I know I could export the packet to pdml using the "all expanded" format, but that gets to be very large for even moderately-sized files. As an alternative, can I add another field to my protocol and set it's value explicitly somehow so I can use tshark to extract that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-40301" class="comments-container"><span id="40312"></span><div id="comment-40312" class="comment"><div id="post-40312-score" class="comment-score"></div><div class="comment-text"><p>What parts do you want? <code>0100 .... = Version: 4</code> has a lot of cruft in it, and pretty much all but "4" is uninteresting, but <code>Opcode: request (1)</code> in an ARP packet contains both the raw numeric value of the field <em>and</em> its interpretation, and some might want to get the latter or both.</p><p>Not that there's any way to get that <em>now</em>, but that would be something useful to think about as an extension to, for example, the <code>-e</code> flag, so that you can, for a given field, request the raw value, the interpreted value, or both.</p></div><div id="comment-40312-info" class="comment-info"><span class="comment-age">(05 Mar '15, 17:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-40301" class="comment-tools"></div><div class="clear"></div><div id="comment-40301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40303"></span>

<div id="answer-container-40303" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40303-score" class="post-score" title="current number of votes">1</div><span id="post-40303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="multipleinterfaces has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think you can do that currently with -T fields, as it only outputs the exact field contents, e.g. the 4 for ip.version.</p><p>In your own protocol you could add format up the text you want and add a generated text field and tshark should output that verbatim.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40303" class="comments-container"><span id="40305"></span><div id="comment-40305" class="comment"><div id="post-40305-score" class="comment-score"></div><div class="comment-text"><p>can you point me to an example of how to create the <code>generated text field</code>?</p></div><div id="comment-40305-info" class="comment-info"><span class="comment-age">(05 Mar '15, 14:06)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-40303" class="comment-tools"></div><div class="clear"></div><div id="comment-40303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

