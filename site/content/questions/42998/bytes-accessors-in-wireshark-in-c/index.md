+++
type = "question"
title = "Bytes Accessors in wireshark in c"
description = '''I&#x27;ve to access 4 bytes of data from tvb (tvbuff_t *) passed in dissect-protocolname() function. I used 2 functions: 1. data = tvb_get_bits32(tvb, offset, 32, ENC_BIG_ENDIAN); 2. proto_tree_add_item(foo_tree, hf_foo_data, tvb, offset, 4, ENC_BIG_ENDIAN);  the returned value from the first function i&#x27;...'''
date = "2015-06-09T01:42:00Z"
lastmod = "2015-06-09T02:17:00Z"
weight = 42998
keywords = [ "dissect", "dissector", "wireshark" ]
aliases = [ "/questions/42998" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Bytes Accessors in wireshark in c](/questions/42998/bytes-accessors-in-wireshark-in-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42998-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've to access 4 bytes of data from tvb (tvbuff_t *) passed in dissect-protocolname() function. I used 2 functions:<br />
<code>1. data = tvb_get_bits32(tvb, offset, 32, ENC_BIG_ENDIAN); 2. proto_tree_add_item(foo_tree, hf_foo_data, tvb, offset, 4, ENC_BIG_ENDIAN);</code> the returned value from the first function i'm displaying it using</p><pre><code>proto_tree_add_uint(foo_tree, hf_foo_data1, tvb, offset, 4, data);</code></pre><p>Both shows the different result in second display pane of wireshark. I'm not changing the offset too.<br />
since offset does not change in both and both are accessing 4 bytes of data . Then Why do both show different result ?<br />
I need 4 bytes of data in a variable to manipulate which first function is doing but returned value is not correct why ??<br />
second function shows the correct decimal value of 4 bytes in display pane of wireshark whereas first does not, why ?<br />
Is there any other function to access 4 bytes of data from tvb buffer ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">dissect dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/ea74f093a0efe137c7c114da864fa5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sammee%20Sharma&#39;s gravatar image" /><p>Sammee Sharma<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sammee Sharma has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '15, 01:49</p></div></div><div id="comments-container-42998" class="comments-container"></div><div id="comment-tools-42998" class="comment-tools"></div><div class="clear"></div><div id="comment-42998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43000"></span>

<div id="answer-container-43000" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43000-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>data = tvb_get_bits32(tvb, offset, 32, ENC_BIG_ENDIAN);</code></p></blockquote><p>Note that, in that statement, <code>offset</code> is the offset, in <em>bits</em>, not <em>bytes</em>, from the beginning of the tvbuff.</p><blockquote><p><code>proto_tree_add_item(foo_tree, hf_foo_data, tvb, offset, 4, ENC_BIG_ENDIAN);</code></p></blockquote><p>However, in <em>that</em> statement, <code>offset</code> is the offset in <em>bytes</em> from the beginning of the tvbuff.</p><blockquote><p><code>proto_tree_add_uint(foo_tree, hf_foo_data1, tvb, offset, 4, data);</code></p></blockquote><p>And it's the offset in bytes from the beginning of the tvbuff in that call as well.</p><p>So, if you want to use <code>tvb_get_bits32()</code>, you'll have to convert <code>offset</code> to an offset in bits, i.e.</p><pre><code>data = tvb_get_bits32(tvb, offset*8, 32, ENC_BIG_ENDIAN);</code></pre><p>However:</p><blockquote><p>Is there any other function to access 4 bytes of data from tvb buffer ?</p></blockquote><p>Yes - <code>tvb_get_ntohl()</code>, i.e.</p><pre><code>data = tvb_get_ntohl(tvb, offset);</code></pre><p>(No, the name doesn't have "be", for "big-endian", or "32" in it, but, well, BSD, UN*X history, <code>ntohl()</code>, blah blah blah.)</p><p>Unless you're dealing with values <em>not</em> aligned on byte boundaries, i.e. bit-packed values, you don't need to use the <code>tvb_get_bits</code> routines, you can just use routines such as <code>tvb_get_ntohs()</code>, <code>tvb_get_ntohl()</code>, <code>tvb_get_letohs()</code>, <code>tvb_get_letohl()</code>, etc.. Most protocols have byte-aligned values, so the <code>tvb_get_bits</code> routines are less often used than the routines I mentioned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '15, 09:58</p></div></div><div id="comments-container-43000" class="comments-container"><span id="43003"></span><div id="comment-43003" class="comment"><div id="post-43003-score" class="comment-score"></div><div class="comment-text"><p>Thanks, @GuyHarris , it worked. The offset in first function is in bits. so it should be converted to bytes in order to access the same value. just one correction i want to make in your answer is that the offset should be multiplied by 8 not 32. Thanks for the quick answer.</p></div><div id="comment-43003-info" class="comment-info"><span class="comment-age">(09 Jun '15, 02:36)</span> Sammee Sharma</div></div><span id="43005"></span><div id="comment-43005" class="comment"><div id="post-43005-score" class="comment-score"></div><div class="comment-text"><p>And one more thing, i didn't get the function<br />
data = tvb_get_ntohl(tvb, offset);<br />
Can you explain a bit about this function like how it will be used to access the 4 bytes.<br />
Thanks.</p></div><div id="comment-43005-info" class="comment-info"><span class="comment-age">(09 Jun '15, 02:40)</span> Sammee Sharma</div></div><span id="43007"></span><div id="comment-43007" class="comment"><div id="post-43007-score" class="comment-score">1</div><div class="comment-text"><p>The ntohl is an abbreviation for "network to host long", i.e. convert a long from the network representation (which is always big-endian) to host representation. There are similar functions for converting from host to network representations and for many different data types. See <code>epan/tvbuff.h</code> for the full list.</p></div><div id="comment-43007-info" class="comment-info"><span class="comment-age">(09 Jun '15, 02:50)</span> grahamb ♦</div></div><span id="43015"></span><div id="comment-43015" class="comment"><div id="post-43015-score" class="comment-score">1</div><div class="comment-text"><p>...which means that <code>tvb_get_ntohl()</code> is all you need to fetch a 32-bit big-endian quantity that's aligned on a byte boundary; there's no advantage to using <code>tvb_get_bits32()</code> unless you're dealing with data that's not aligned on byte boundaries.</p></div><div id="comment-43015-info" class="comment-info"><span class="comment-age">(09 Jun '15, 09:55)</span> Guy Harris ♦♦</div></div><span id="43017"></span><div id="comment-43017" class="comment"><div id="post-43017-score" class="comment-score">1</div><div class="comment-text"><p>Example fixed.</p></div><div id="comment-43017-info" class="comment-info"><span class="comment-age">(09 Jun '15, 09:55)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43000" class="comment-tools"></div><div class="clear"></div><div id="comment-43000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

