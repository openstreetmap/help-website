+++
type = "question"
title = "Why does Wireshark not decode SIP-TLS packets?"
description = '''Hello,  I have a capture in which SIP-TLS is being used. When I look at the packets, I see the TCP port being used for SIP-TLS = 5061. When I go to Preferences -&amp;gt; Protocols -&amp;gt; SIP, the SIP-TLS port = 5061. However, Wireshark only shows the packet as TCP and not SIP-TLS. Why is Wireshark not di...'''
date = "2015-04-22T06:55:00Z"
lastmod = "2015-04-22T07:58:00Z"
weight = 41685
keywords = [ "sip" ]
aliases = [ "/questions/41685" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does Wireshark not decode SIP-TLS packets?](/questions/41685/why-does-wireshark-not-decode-sip-tls-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41685-score" class="post-score" title="current number of votes">0</div><span id="post-41685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a capture in which SIP-TLS is being used. When I look at the packets, I see the TCP port being used for SIP-TLS = 5061. When I go to Preferences -&gt; Protocols -&gt; SIP, the SIP-TLS port = 5061. However, Wireshark only shows the packet as TCP and not SIP-TLS. Why is Wireshark not displaying the packets with TCP port 5061 as SIP-TLS?</p><p>I have performed the following in Wireshark: 1. Preferences -&gt; Protocols -&gt; TCP -&gt; "Allow subdissector to reassemble TCP streams". I tried enabling and disabling this setting. It had no effect on decoding the SIP-TLS packets. 2. At first RTP packets were also not being decoded by Wireshark. After going to Preferences -&gt; Protocols -&gt; RTP, I enabled the setting "Try to decode RTP outside of conversation" and the RTP packets were properly decoded.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41685" class="comments-container"></div><div id="comment-tools-41685" class="comment-tools"></div><div class="clear"></div><div id="comment-41685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41688"></span>

<div id="answer-container-41688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41688-score" class="post-score" title="current number of votes">1</div><span id="post-41688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Amato_C has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, Wireshark only shows the packet as TCP and not SIP-TLS. Why is <strong>Wireshark not displaying</strong> the packets with <strong>TCP port 5061 as SIP-TLS</strong>?</p></blockquote><p>because it will never do that, as there is no protocol "SIP-TLS" in Wireshark, that's why you see either TCP or SSL (or TLSxxx) in the protocol column.</p><p>There is however a "translation/resolution" of port 5061 to <strong>sips</strong> and you will see that in the Info column, if you enable transport name resolution.</p><blockquote><p>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve transport names</p></blockquote><p>So, what you should see is TCP and SSL/TLS (as soon as the client starts the handshake) in the protocol column. If you only see TCP, then there is no SSL/TLS encryption in that session.</p><p>For any further analysis, we would need a capture file. Can you please upload a sample capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41688" class="comments-container"><span id="41690"></span><div id="comment-41690" class="comment"><div id="post-41690-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. When I enabled the Transport name resolution, I see "sips" in the Info column. I was mistakenly expecting SIP-TLS to be presented in the Protocol column.</p></div><div id="comment-41690-info" class="comment-info"><span class="comment-age">(22 Apr '15, 07:58)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-41688" class="comment-tools"></div><div class="clear"></div><div id="comment-41688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

