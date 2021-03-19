+++
type = "question"
title = "how to get values from the buffer?"
description = '''In lua,how to get the buffer value.I have to print the value in the value of buffer on console. I have a offset of 2 (2 bytes) and have to print the value of last 10 bits of buffer. Please help me with this.'''
date = "2015-04-20T12:50:00Z"
lastmod = "2015-06-30T21:21:00Z"
weight = 41604
keywords = [ "print", "lua", "offset" ]
aliases = [ "/questions/41604" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get values from the buffer?](/questions/41604/how-to-get-values-from-the-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In lua,how to get the buffer value.I have to print the value in the value of buffer on console. I have a offset of 2 (2 bytes) and have to print the value of last 10 bits of buffer.</p><p>Please help me with this.</p></div><div id="question-tags" class="tags-container tags">print lua offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/a2e29df6af5eb33f09d1ed5321ea6586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakshmi&#39;s gravatar image" /><p>lakshmi<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakshmi has no accepted answers">0%</span></p></div></div><div id="comments-container-41604" class="comments-container"></div><div id="comment-tools-41604" class="comment-tools"></div><div class="clear"></div><div id="comment-41604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43763"></span>

<div id="answer-container-43763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43763-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You said you have an "offset of 2 (2 bytes)" - do you mean the value you want to get is the last 10 bits of the first and second bytes of the buffer, or do you mean it's the last 10 bits of the 3rd and 4th bytes?</p><p>Something like this:</p><pre><code>-- assuming &quot;myproto&quot; is the name of the Proto object
function myproto.dissector(tvbuf, pinfo, root)
    -- for the first and second bytes:
    if tvbuf:len() &gt; 1 then
        local bytes = tvbuf:range(0,2):uint()
        info( string.format(&quot;Last 10 bits of 1st and 2nd bytes in hex = %x&quot;, bit.band(bytes, 0x03FF)) )
    end

    -- for the third and fourth bytes:
    if tvbuf:len() &gt; 3 then
        local bytes = tvbuf:range(2,2):uint()
        info( string.format(&quot;Last 10 bits of 3rd and 4th bytes in hex = %x&quot;, bit.band(bytes, 0x03FF)) )
    end
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43763" class="comments-container"></div><div id="comment-tools-43763" class="comment-tools"></div><div class="clear"></div><div id="comment-43763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

