+++
type = "question"
title = "tvbuff_t* tvb_new_real_data()"
description = '''void tvb_set_real_data(tvbuff_t* tvb, const guint8* data, const guint length, const gint reported_length)  Hi all, could i use the above function to create a tvb by passing a packet in hex string into its parameters?  Thanks Regards, Eddie Choo'''
date = "2011-08-04T00:49:00Z"
lastmod = "2011-08-04T01:14:00Z"
weight = 5483
keywords = [ "development" ]
aliases = [ "/questions/5483" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tvbuff\_t\* tvb\_new\_real\_data()](/questions/5483/tvbuff_t-tvb_new_real_data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>void
tvb_set_real_data(tvbuff_t* tvb, const guint8* data, const guint length, const gint reported_length)</code></pre><p>Hi all, could i use the above function to create a tvb by passing a packet in hex string into its parameters?</p><p>Thanks</p><p>Regards,</p><p>Eddie Choo</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '11, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p>eddie choo<br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '11, 16:14</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5483" class="comments-container"><span id="5509"></span><div id="comment-5509" class="comment"><div id="post-5509-score" class="comment-score">1</div><div class="comment-text"><p>duplicate: <a href="http://ask.wireshark.org/questions/5422/feed-a-packet-in-hex-string-format-into-a-dissecctor">feed a packet in hex string format into a dissecctor</a></p></div><div id="comment-5509-info" class="comment-info"><span class="comment-age">(04 Aug '11, 16:16)</span> helloworld</div></div><span id="5514"></span><div id="comment-5514" class="comment"><div id="post-5514-score" class="comment-score"></div><div class="comment-text"><p>Hi helloworld, i was thinking that i should open a new question because i wanted to be more specified in getting response only for this <code>tvb_set_real_data</code> function.Thanks</p><p>Eddie Choo</p></div><div id="comment-5514-info" class="comment-info"><span class="comment-age">(04 Aug '11, 19:11)</span> eddie choo</div></div></div><div id="comment-tools-5483" class="comment-tools"></div><div class="clear"></div><div id="comment-5483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5484"></span>

<div id="answer-container-5484" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5484-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean by a "hex string"? Do you mean the ASCII hex representation of some 8 bit binary values, e.g. given the values 01, 66, 255, you have a string "0142FF"?</p><p>If so, it all depends on what the consumer of the tvb is expecting. If the consumer is expecting a hex string, all will be OK, if the consumer is expecting the binary values that the hex string represents then things won't go so well.</p><p>However if your "hex string" is in fact a pointer to the binary representation then you should be OK.</p><p>An example would help to clarify your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5484" class="comments-container"><span id="5515"></span><div id="comment-5515" class="comment"><div id="post-5515-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham, I wanted to use the wireshark dissectors to dissect the packet in hex string format, which is something like this: <code>03b1682daa0980030e160b12950012042618061003020812060012045649734162 3f4804ba1411b66b1e281c060700118605010101a011600f80020780a1090607040 000010 002036c17a115020100020103a30d040825054373236300f50a0100</code> I have now found a temporary solution, which is to explore deeper in the <code>tvb_get_uintX()</code> function and modified slightly so that it only deals with the <code>real_data</code> parameter of the <code>tvb</code>, in which i hope is in the hex format. Thanks for your reply</p><p>Eddie Choo</p></div><div id="comment-5515-info" class="comment-info"><span class="comment-age">(04 Aug '11, 19:15)</span> eddie choo</div></div></div><div id="comment-tools-5484" class="comment-tools"></div><div class="clear"></div><div id="comment-5484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

