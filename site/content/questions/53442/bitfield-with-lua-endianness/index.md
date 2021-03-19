+++
type = "question"
title = "Bitfield with lua endianness"
description = '''I&#x27;m writing a dissector that must be capable of extracting numeric values from a TvbRange that spans multiple bytes, while only considering certain bits. I&#x27;m a bit concerned about chossing the right method that will also ensure the correct endianess and signedness. From my understanding I could add ...'''
date = "2016-06-14T11:44:00Z"
lastmod = "2016-06-14T11:44:00Z"
weight = 53442
keywords = [ "lua", "bit", "bitmask", "little-endian" ]
aliases = [ "/questions/53442" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bitfield with lua endianness](/questions/53442/bitfield-with-lua-endianness)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53442-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a dissector that must be capable of extracting numeric values from a TvbRange that spans multiple bytes, while only considering certain bits. I'm a bit concerned about chossing the right method that will also ensure the correct endianess and signedness.</p><p>From my understanding I could add a bitmask when creating the ProtoField. However this fails with "bad argument #4 to 'uint16' (must be a table)". <code>ProtoField.uint16("abc","abc",base.DEC, 0x3000, nil, "")</code> Any idea what is causing this? Does Wireshark apply the mask on the raw data and then start coverting to uint16?</p><p>Secondly, I would also like to have the value in an local variable. If I for instance call <code>buf(1,2):bitfield(2,2)</code>, it will return a number, but is there some way of ensuring the correct endianess and signing? Can I maybe retrieve the values from the TreeItem?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua bit bitmask little-endian</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '16, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/d735898289dc3174f1a9a17cf45070d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luanda&#39;s gravatar image" /><p>Luanda<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luanda has no accepted answers">0%</span></p></div></div><div id="comments-container-53442" class="comments-container"></div><div id="comment-tools-53442" class="comment-tools"></div><div class="clear"></div><div id="comment-53442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

