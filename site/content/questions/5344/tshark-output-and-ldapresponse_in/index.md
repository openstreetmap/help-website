+++
type = "question"
title = "tshark output and ldap.response_in"
description = '''I have configured my Default profile to include a custom field for the ldap.response_in value. In Wireshark, it works great, but in tshark, the values are empty. This Windows command line returns empty lines for the 6 hits on &quot;ldap.request || ldap.response&quot; filter: &amp;gt; tshark.exe -r ldap.pcap &quot;ldap...'''
date = "2011-07-28T08:23:00Z"
lastmod = "2011-07-28T11:18:00Z"
weight = 5344
keywords = [ "windows", "display-filter", "tshark", "ldap" ]
aliases = [ "/questions/5344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark output and ldap.response\_in](/questions/5344/tshark-output-and-ldapresponse_in)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have configured my Default profile to include a custom field for the <strong>ldap.response_in</strong> value. In Wireshark, it works great, but in tshark, the values are empty. This Windows command line returns empty lines for the 6 hits on <strong>"ldap.request || ldap.response"</strong> filter:</p><pre><code>&gt; tshark.exe -r ldap.pcap &quot;ldap.bindRequest || ldap.bindResponse&quot; -o column.format:&quot;&quot;Response&quot; &quot;In&quot;, &quot;%Cus:ldap.response_in&quot;&quot;</code></pre><p>Ideas?</p></div><div id="question-tags" class="tags-container tags">windows display-filter tshark ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '11, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/922af96c76c020661f416be82856de3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanh&#39;s gravatar image" /><p>ivanh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '11, 15:59</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5344" class="comments-container"></div><div id="comment-tools-5344" class="comment-tools"></div><div class="clear"></div><div id="comment-5344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5349"></span>

<div id="answer-container-5349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5349-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark does one pass through the tracefile while wireshark displays packets only after analysing them all first. That's why Wireshark knows when (in the future) a response will be given to a paricular request. tshark however has no knowledge about "the future", so it does not know which packet the response will be in.</p><p>There is an undocumented option in tshark to make it do a 2-pass analysis, just like Wireshark. But I'm not sure how complete that functionality is at the moment (I have never used it myself). You can always try of course... The command line option that you have to use is "-P".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '11, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5349" class="comments-container"><span id="5351"></span><div id="comment-5351" class="comment"><div id="post-5351-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply SYNbit. No joy with -P, ERROR:dfvm.c:400:???: assertion failed: (tree)</p><p>When I use the -V the values for ldap_response_in and response_to are both present. I could use this but runtimes are greatly extended and so much extra noise in the output.... ... Lightweight Directory Access Protocol LDAPMessage bindResponse(1) success messageID: 1 protocolOp: bindResponse (1) bindResponse resultCode: success (0) matchedDN: errorMessage: [Response To: 7365] [Time: 0.004628000 seconds]</p></div><div id="comment-5351-info" class="comment-info"><span class="comment-age">(28 Jul '11, 11:25)</span> ivanh</div></div><span id="5360"></span><div id="comment-5360" class="comment"><div id="post-5360-score" class="comment-score"></div><div class="comment-text"><p>On close inspection of the -V output I saw that there were only Response to: values, no Response in: are present. Armed with this observation I twiddled my script and configuration and was able to obtain ldap.response_to values with single pass parsing. This makes good sense actually. We should be able to look behind at messageID to determine response_to value with only one pass.</p></div><div id="comment-5360-info" class="comment-info"><span class="comment-age">(29 Jul '11, 07:53)</span> ivanh</div></div></div><div id="comment-tools-5349" class="comment-tools"></div><div class="clear"></div><div id="comment-5349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

