+++
type = "question"
title = "How do you use the uncompress method?"
description = '''The uncompress method is mentioned in several places in documentation. I know what it&#x27;s suppose to return, but I&#x27;m not sure about its parameters. Its code comments state that it &quot;uncompresses a zlib compressed packet inside a message of tvb at offset with length comprlen.&quot; I figured the &quot;tvb&quot; is the...'''
date = "2016-04-20T16:59:00Z"
lastmod = "2016-04-21T01:20:00Z"
weight = 51825
keywords = [ "tvbuff_t", "dissector", "uncompressed" ]
aliases = [ "/questions/51825" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you use the uncompress method?](/questions/51825/how-do-you-use-the-uncompress-method)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The uncompress method is mentioned in several places in documentation. I know what it's suppose to return, but I'm not sure about its parameters. Its code comments state that it "uncompresses a zlib compressed packet inside a message of tvb at offset with length comprlen." I figured the "tvb" is the buffer passed unto the dissector and the "offset" is the pointer at which the method is to begin uncompressing data, but I don't know what the length "comprlen" is in relation to the data or the process. Is it the current reported length of the buffer to be uncompressed? Is it the expected length of the uncompressed buffer after decompression?</p><pre><code>tvbuff_t tvb_uncompress(tvbuff_t tvb, const int offset, int comprlen)</code></pre></div><div id="question-tags" class="tags-container tags">tvbuff_t dissector uncompressed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '16, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div></div><div id="comments-container-51825" class="comments-container"></div><div id="comment-tools-51825" class="comment-tools"></div><div class="clear"></div><div id="comment-51825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51832"></span>

<div id="answer-container-51832" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51832-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Uncompresses a zlib compressed packet inside a tvbuff at offset with length comprlen.</code></pre><p>You have received a tvb, and from your protocol know the offset as well as the length of the compressed data. How you know these parts really depends on the protocol at hand. Offset is usually a specific field in the PDU. Length can be also in a field in the PDU or follows from the encapsulating protocol, eg. UDP payload length. So tvb_reported_length_remaining() or tvb_captured_length_remaining() can be of service here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '16, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51832" class="comments-container"><span id="51836"></span><div id="comment-51836" class="comment"><div id="post-51836-score" class="comment-score"></div><div class="comment-text"><p>Thanks, @Jaap. I am using tvb_reported_length_remaining() now, but it's not giving off 100% decompression of all PDUs. I was actually wondering if I am suppose to be using the length value in the first bytes of the PDU as you mentioned. If I do, though, wouldn't I risk decompressing at an erroneous inflation (which might increase errors in decompression)?</p><p>It sounds like the method is flexible enough that the given length may not even be necessary. By that I mean, the method could go in and get its own "comprlen" value from the passed tvbuff_t object, instead. This is the confusing part for me.</p></div><div id="comment-51836-info" class="comment-info"><span class="comment-age">(21 Apr '16, 04:36)</span> coloncm</div></div><span id="51854"></span><div id="comment-51854" class="comment"><div id="post-51854-score" class="comment-score"></div><div class="comment-text"><p>Perhaps, I should rephrase my follow up question. Which of the values you mentioned is the recommended or most widely used value to use for this method: the PDU/payload length value, the tvb_reported_length_remaining() value or the tvb_captured_length_remaining() value?</p></div><div id="comment-51854-info" class="comment-info"><span class="comment-age">(21 Apr '16, 17:55)</span> coloncm</div></div><span id="51859"></span><div id="comment-51859" class="comment"><div id="post-51859-score" class="comment-score">1</div><div class="comment-text"><p>It's up to the dissector calling the method to determine the length of the compressed data in the tvb.</p><p>The length of the compressed data may not be all of the remaining tvb, hopefully the protocol using zlib compression has added a length or some other delimiter so that a normal recipient can decompress the data, and the dissector can use that to pass into the uncompress function.</p><p>If there are no such explicit length indicators all you can do is pass in <code>tvb_reported_length_remaining()</code> as this is what "should" be in the packet.</p><p>Using the <em>captured</em> length in general in any dissector isn't a good idea as your dissector won't be reporting malformed packets due to capture length limitations, and the decompressor will fail if the capture length has been reduced as there will be missing compressed data.</p></div><div id="comment-51859-info" class="comment-info"><span class="comment-age">(22 Apr '16, 00:39)</span> grahamb ♦</div></div><span id="51922"></span><div id="comment-51922" class="comment"><div id="post-51922-score" class="comment-score"></div><div class="comment-text"><p>Clear as mud! Thanks, @grahamb.</p></div><div id="comment-51922-info" class="comment-info"><span class="comment-age">(25 Apr '16, 04:48)</span> coloncm</div></div></div><div id="comment-tools-51832" class="comment-tools"></div><div class="clear"></div><div id="comment-51832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

