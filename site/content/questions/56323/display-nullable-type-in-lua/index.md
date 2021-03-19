+++
type = "question"
title = "display nullable type in lua"
description = '''Some binary protocols have nullable types, fields that are valid for all values but a single sentinel value which signifies that this field exists on the wire but is unused for this specific packet. A common example would be a single byte quantity field that was not valid if the wire value was 255. ...'''
date = "2016-10-12T08:47:00Z"
lastmod = "2016-10-16T13:38:00Z"
weight = 56323
keywords = [ "sentinel", "lua", "null", "display" ]
aliases = [ "/questions/56323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [display nullable type in lua](/questions/56323/display-nullable-type-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Some binary protocols have nullable types, fields that are valid for all values but a single sentinel value which signifies that this field exists on the wire but is unused for this specific packet. A common example would be a single byte quantity field that was not valid if the wire value was 255. Is there any simple, standard built in functionality to display the regular value in cases where it exists and something like No Value (255) in cases where the field contains the sentinel value?</p><pre><code>function dissect_example(buffer, offset, packet, parent)
...

  -- Quantity: Unsigned 1 Byte Integer

  local quantitysize = 1

  local quantityrange = buffer(index, quantitysize)

  local element = parent:add(example.fields.quantity, quantityrange)

  if buffer(index - quantitysize, quantitysize):int() == 255 then element:append_text(&quot; [No Value]&quot;)

end</code></pre><p>This brute force example source prints "Quantity: 255 [No value]" but I am wondering if there is some built in function like the value mask. I tried a value mask of {[255]="No Value"} but this mask prints unknown on regular values. Thoughts?</p></div><div id="question-tags" class="tags-container tags">sentinel lua null display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/d03ce1682e2a9e3bd9ed3be60088d031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="william&#39;s gravatar image" /><p>william<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="william has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '16, 13:35</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-56323" class="comments-container"></div><div id="comment-tools-56323" class="comment-tools"></div><div class="clear"></div><div id="comment-56323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56427"></span>

<div id="answer-container-56427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56427-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No this is not possible, you have to explicitly check for the value.</p><p>When you specify a mask, then you must specify all possible values or else these will show up as Unknown as you have observed. Checking for <code>255</code> and then appending the text is indeed the way to go.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '16, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56427" class="comments-container"></div><div id="comment-tools-56427" class="comment-tools"></div><div class="clear"></div><div id="comment-56427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

