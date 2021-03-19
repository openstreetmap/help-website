+++
type = "question"
title = "How to extract smpp.message using tshark?"
description = '''I am trying to extract SMPP message content using tshark. But when I use -T fields -e &quot;smpp.message&quot; it only prints 1 and not the actual message. C:&#92;Program Files&#92;Wireshark&amp;gt;tshark -r SMPP.pcap -2 -R &quot;(smpp.command_id == 0x00000004)&quot; -T fields -e smpp.message -E header=y smpp.message 1 1 1 1 1 1 1...'''
date = "2017-01-27T06:37:00Z"
lastmod = "2017-01-30T07:19:00Z"
weight = 59106
keywords = [ "smpp", "tshark" ]
aliases = [ "/questions/59106" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract smpp.message using tshark?](/questions/59106/how-to-extract-smppmessage-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59106-score" class="post-score" title="current number of votes">0</div><span id="post-59106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to extract SMPP message content using tshark.</p><p>But when I use -T fields -e "smpp.message" it only prints 1 and not the actual message.</p><pre><code>C:\Program Files\Wireshark&gt;tshark -r SMPP.pcap -2 -R &quot;(smpp.command_id == 0x00000004)&quot; -T fields -e         smpp.message -E header=y
smpp.message
1
1
1
1
1
1
1
1
1</code></pre><p>If I use -T text -x parameters it shows the actual message, but I cant filter to only shows the smpp message.</p><p>When i consult tshark -G it shows:</p><pre><code>F   Message smpp.message    FT_NONE smpp    The actual message or data.</code></pre><p>What I am doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '17, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/8c07f4b8d119d231205e2472d78ff4fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bricio&#39;s gravatar image" /><p><span>Bricio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bricio has no accepted answers">0%</span></p></div></div><div id="comments-container-59106" class="comments-container"></div><div id="comment-tools-59106" class="comment-tools"></div><div class="clear"></div><div id="comment-59106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59112"></span>

<div id="answer-container-59112" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59112-score" class="post-score" title="current number of votes">0</div><span id="post-59112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bricio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The latest version of <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-smpp.c;h=48b1ba8517749133920b2e8e6765de91bb300edc;hb=HEAD#l2951">packet-smpp.c</a> shows <code>FT_BYTES</code>, not <code>FT_NONE</code>. <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=76cf240a0bbe142829083189f943dcc85c7f1223">Here</a>'s the exact change.</p><p>Try upgrading Wireshark. You can even get a very recent <a href="https://www.wireshark.org/download/automated/">automated</a> version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '17, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59112" class="comments-container"><span id="59129"></span><div id="comment-59129" class="comment"><div id="post-59129-score" class="comment-score"></div><div class="comment-text"><p>TY, is there a way, inside wireshark, to return this field as STRING? My smpp messages is always strings. I don't have c or c++ compiler to change the file and recompile.</p></div><div id="comment-59129-info" class="comment-info"><span class="comment-age">(29 Jan '17, 04:28)</span> <span class="comment-user userinfo">Bricio</span></div></div><span id="59149"></span><div id="comment-59149" class="comment"><div id="post-59149-score" class="comment-score"></div><div class="comment-text"><p>Without modifying the Wireshark sources and recompiling it, you can <em>probably</em> achieve this with some scripting, removing the <code>:</code>'s and converting each hex byte to its ASCII-equivalent character.</p></div><div id="comment-59149-info" class="comment-info"><span class="comment-age">(30 Jan '17, 07:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-59112" class="comment-tools"></div><div class="clear"></div><div id="comment-59112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

