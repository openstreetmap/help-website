+++
type = "question"
title = "Use of call_dissector ?"
description = '''I am total newbie in wireshark plugin development and i was curious about precise use case of this function , some &quot;packet-xx.c&quot; don&#x27;t use it and some use it but still i am not able to make out difference. I am under impression that even if we don&#x27;t use it , dissectors get called by default from epa...'''
date = "2012-06-04T02:57:00Z"
lastmod = "2012-06-04T03:08:00Z"
weight = 11608
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/11608" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Use of call\_dissector ?](/questions/11608/use-of-call_dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am total newbie in wireshark plugin development and i was curious about precise use case of this function , some "packet-xx.c" don't use it and some use it but still i am not able to make out difference. I am under impression that even if we don't use it , dissectors get called by default from epan/dissectors for all basic protocols.Please point some source file for more understanding of this function.</p></div><div id="question-tags" class="tags-container tags">plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '12, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11608" class="comments-container"></div><div id="comment-tools-11608" class="comment-tools"></div><div class="clear"></div><div id="comment-11608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11611"></span>

<div id="answer-container-11611" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11611-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general, the "call_dissector()" function is called whenever a dissector knows that it's payload is of a certain type for which wireshark has a dissector.</p><p>For instance, in the http-dissector, many different types of payload might be encountered. Depending on the type of data, the http-dissestor will call the appropriate (sub-)dissector.</p><p>An example is when the http dissector encounters a base64-encoded kerberos object. It will then decode the object first and then hand it over to the kerberos dissector for further dissection:</p><pre><code>kerberos_tvb = base64_to_tvb(tvb, line + 9); /* skip &#39;Kerberos &#39; which is 9 chars */
add_new_data_source(pinfo, kerberos_tvb, &quot;Kerberos Data&quot;);
call_dissector(gssapi_handle, kerberos_tvb, pinfo, tree);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '12, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11611" class="comments-container"><span id="11612"></span><div id="comment-11612" class="comment"><div id="post-11612-score" class="comment-score"></div><div class="comment-text"><p>ok , and what if we don't call it ? won't wireshark call the relevant dissector on its own ?</p></div><div id="comment-11612-info" class="comment-info"><span class="comment-age">(04 Jun '12, 03:11)</span> yogeshg</div></div><span id="11613"></span><div id="comment-11613" class="comment"><div id="post-11613-score" class="comment-score"></div><div class="comment-text"><p>those are different things.</p><ol><li><p>You can call another dissector yourself WITHIN your own dissector with call_dissector (as described by @SYN-bit).</p></li><li><p>YOUR dissector will be called after you told wireshark it exists. See skeleton code in README.developer.</p></li></ol></div><div id="comment-11613-info" class="comment-info"><span class="comment-age">(04 Jun '12, 03:20)</span> Kurt Knochner ♦</div></div><span id="11704"></span><div id="comment-11704" class="comment"><div id="post-11704-score" class="comment-score"></div><div class="comment-text"><p>@SYN-bit , in your example we know for sure that we have only kerberos object ,but what if suppose there is something else also appended to kerberos object and that something else happens to be your protocol relevant data (for which you are writing dissector)? Same is the case with me. I can call kerberos dissector which wireshark knows but after this call , will the tvb point to that extra appended data ? .. How to approach this problem</p></div><div id="comment-11704-info" class="comment-info"><span class="comment-age">(05 Jun '12, 22:12)</span> yogeshg</div></div></div><div id="comment-tools-11611" class="comment-tools"></div><div class="clear"></div><div id="comment-11611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

