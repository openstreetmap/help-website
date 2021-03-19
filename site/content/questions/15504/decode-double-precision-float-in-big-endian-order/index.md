+++
type = "question"
title = "Decode double-precision float in big-endian order"
description = '''I used WireShark to capture this double-precision float from ethernet: 40 39 64 15 85 15 4f 4f Basic format understanding: [sign bit][11 bit exponent][52 bit mantissa] = 64 bit value I believe it&#x27;s in big-endian order, equivalent to approximately 52,000 decimal. No matter how I order the bytes it ne...'''
date = "2012-11-02T09:30:00Z"
lastmod = "2012-11-02T18:11:00Z"
weight = 15504
keywords = [ "big-endian", "double-precision" ]
aliases = [ "/questions/15504" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Decode double-precision float in big-endian order](/questions/15504/decode-double-precision-float-in-big-endian-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used WireShark to capture this double-precision float from ethernet: 40 39 64 15 85 15 4f 4f Basic format understanding: [sign bit][11 bit exponent][52 bit mantissa] = 64 bit value I believe it's in big-endian order, equivalent to approximately 52,000 decimal. No matter how I order the bytes it never comes out right.<br />
Does the data look reasonable? How to decode properly? Good online tool available? I just need to convert it (and MANY other numbers like it), I don't need to understand the process. Thanks in advance for your help.</p></div><div id="question-tags" class="tags-container tags">big-endian double-precision</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/69e58ab06605d3360fb06a06ceec944c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roy%20L%20Payne&#39;s gravatar image" /><p>Roy L Payne<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roy L Payne has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-15504" class="comments-container"></div><div id="comment-tools-15504" class="comment-tools"></div><div class="clear"></div><div id="comment-15504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15506"></span>

<div id="answer-container-15506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>http://www.binaryconvert.com/result_double.html</code></p></blockquote><p>52000 would be 0x40E9640000000000, so no matter if you use big/little endian, you will not end up with your hex representation.</p><p>So, where did capture that double float and how do you know it's the representation of the double float value 52000?</p><p>Can you post the capture file that contains that value (on <a href="http://cloudshark.org">cloudshark.org</a>)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15506" class="comments-container"><span id="15509"></span><div id="comment-15509" class="comment"><div id="post-15509-score" class="comment-score"></div><div class="comment-text"><p>Kurt, thanks for feedback. I'm Richard (Roy L Payne), and comparing your number with mine, I realized I typo'd part of it ('39' should be 'e9'). So mine starts with "40 e9 64", which matches the start of your number. I'll have to track down what all that other garbage is in my value. About posting files, it won't be possible. Thanks again for your help.</p></div><div id="comment-15509-info" class="comment-info"><span class="comment-age">(02 Nov '12, 09:55)</span> Roy L Payne</div></div><span id="15516"></span><div id="comment-15516" class="comment"><div id="post-15516-score" class="comment-score"></div><div class="comment-text"><p>The "other garbage" may be "it's approximately 52000, not exactly 52000".</p></div><div id="comment-15516-info" class="comment-info"><span class="comment-age">(02 Nov '12, 15:09)</span> Guy Harris ♦♦</div></div><span id="15523"></span><div id="comment-15523" class="comment"><div id="post-15523-score" class="comment-score"></div><div class="comment-text"><p>if you use the online converter (see link above), you will get the decimal representation.</p><blockquote><p><code>http://www.binaryconvert.com/result_double.html?hexadecimal=40E9641585154F4F</code><br />
</p></blockquote><p>Result: 5.20006724955128665897063910961E4</p><p>So, the rest is not really "garbage", but an essential part of the value, <strong>if</strong> it's a double float value. As @Guy Harris said: It's approximately 52000. And that's what you also assumed in your question:</p><blockquote><p><code>I believe it's in big-endian order, equivalent to</code> <strong>approximately 52,000</strong> <code>decimal.</code><br />
</p></blockquote><p>So, I think the puzzle is solved ;-)</p><p>Regards<br />
Kurt</p></div><div id="comment-15523-info" class="comment-info"><span class="comment-age">(04 Nov '12, 01:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15506" class="comment-tools"></div><div class="clear"></div><div id="comment-15506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15513"></span>

<div id="answer-container-15513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15513-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you need the value for some reason other than to simply display it, you can use <code>tvb_get_ntohieee_double()</code>; otherwise, if you're just going to display it in the tree, use <code>proto_tree_add_item()</code> where the <code>hf_</code> field has a type of <code>FT_DOUBLE</code>. Refer to <code>doc/README.developer</code>, <code>epan/tvbuff.[h|c]</code> and various dissector source files for further help and examples.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-15513" class="comments-container"></div><div id="comment-tools-15513" class="comment-tools"></div><div class="clear"></div><div id="comment-15513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15520"></span>

<div id="answer-container-15520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15520-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><h3 id="scripting">Scripting</h3><p>If you have more hex strings than is convenient for manual entry, I would employ scripting. You could even use this <a href="http://codepad.org/B4u96Ybn">Python script</a> directly in <em>codepad</em>.</p><h3 id="ieee-754-analysis-from-cuny">IEEE-754 Analysis from CUNY</h3><p>I like using the <a href="http://babbage.cs.qc.cuny.edu/IEEE-754/">IEEE-754 Analysis page</a> to convert hex strings (copied from Wireshark/Tshark or similar tools) to decimal values. It also converts decimal floating-point to hex string, handles endianness, and displays the conversion in different precisions.</p><p><em>Instructions</em></p><ol><li>Open the page for <a href="http://babbage.cs.qc.cuny.edu/IEEE-754/">IEEE-754 Analysis</a>. Keep the default settings unless you need to tweak them.</li><li>Copy and paste your hex string (<strong><code>40e9641585154f4f</code></strong>) into the textbox for <strong>Value to analyze</strong>.</li><li>Press <strong>Enter</strong>. Assuming you left the <strong>Input Mode</strong> as <strong>auto</strong>, It should automatically convert your hex string into a decimal value (shown in <a href="http://en.wikipedia.org/wiki/Scientific_notation#E_notation">E notation</a>), and show binary conversions in multiple precisions.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></div></div><div id="comments-container-15520" class="comments-container"></div><div id="comment-tools-15520" class="comment-tools"></div><div class="clear"></div><div id="comment-15520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

