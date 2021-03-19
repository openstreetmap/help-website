+++
type = "question"
title = "How do I dissect a weighted integer type?"
description = '''Suppose, I have a header field that is represented by an arbitrary number of bits (we can assume no more than 32), but in stead of interpreting this as an integer, it is really interpreted as the integer value multiplied by some scalar, resulting in a non-integral value. Since FT_FLOAT and FT_DOUBLE...'''
date = "2014-03-28T13:46:00Z"
lastmod = "2014-03-28T13:46:00Z"
weight = 31254
keywords = [ "development", "dissector", "ftypes" ]
aliases = [ "/questions/31254" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I dissect a weighted integer type?](/questions/31254/how-do-i-dissect-a-weighted-integer-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31254-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suppose, I have a header field that is represented by an arbitrary number of bits (we can assume no more than 32), but in stead of interpreting this as an integer, it is really interpreted as the integer value multiplied by some scalar, resulting in a non-integral value. Since <code>FT_FLOAT</code> and <code>FT_DOUBLE</code> can't have bitmasks, how do I add these to my dissector?</p><p>I would just call <code>proto_tree_add_float_bits_value</code> and compute the arguments in the body, but this function isn't part of the API (unusable by a plugin dissector). Do I have to add these as integer types? I don't necessarily need to filter using the computed value (although that would be nice), but I don't want to display the integral value in the dissection tree.</p><p><strong>Example:</strong> A field, <code>ft_myfloat</code> is 11 bits long, with the bitmask <code>0x7FF</code>, and another field occupies the remaining bits within its most significant byte. This field uses the scalar <code>0.101325</code> to encode its "real" value. So, when it has the value <code>0x064</code> (<code>100</code>), the interpreted result should be <code>10.1325</code>.</p><p>So far, I have added them as <code>FT_[U]INT(8|16|24|32)</code> with bitmasks using <code>BASE_CUSTOM</code>, but this is rather cumbersome. I've thought about adding a pair of new <code>ftype</code>s for this since it comes up a lot in the dissectors I write, but so far haven't been able to work out how best to do this.</p><h2 id="tldr">tl;dr:</h2><p>What is the best way to add a "weighted integer" type to the dissection?</p></div><div id="question-tags" class="tags-container tags">development dissector ftypes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-31254" class="comments-container"></div><div id="comment-tools-31254" class="comment-tools"></div><div class="clear"></div><div id="comment-31254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

