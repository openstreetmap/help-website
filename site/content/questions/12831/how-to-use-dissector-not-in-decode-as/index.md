+++
type = "question"
title = "How to use dissector not in &quot;decode as&quot;"
description = '''I have made a custom dissector but do not know how to use it in wireshark. It appears that it should work, as I am able to type it into the filter bar and it turns green. However, it is not listed in the &quot;decode as&quot; menu, therefore I do not know of anyway to use it. Is there a way to add this custom...'''
date = "2012-07-18T08:48:00Z"
lastmod = "2012-07-18T10:31:00Z"
weight = 12831
keywords = [ "decode_as", "dissector", "custom" ]
aliases = [ "/questions/12831" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use dissector not in "decode as"](/questions/12831/how-to-use-dissector-not-in-decode-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12831-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have made a custom dissector but do not know how to use it in wireshark.<br />
It appears that it should work, as I am able to type it into the filter bar and it turns green. However, it is not listed in the "decode as" menu, therefore I do not know of anyway to use it.</p><p>Is there a way to add this custom dissector to the decode as menu or simply use it some other way?</p></div><div id="question-tags" class="tags-container tags">decode_as dissector custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span> </br></p></div></div><div id="comments-container-12831" class="comments-container"></div><div id="comment-tools-12831" class="comment-tools"></div><div class="clear"></div><div id="comment-12831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12832"></span>

<div id="answer-container-12832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12832-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should read <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">README.developer</a>, which shows you how to add your dissector to another dissector's table similar to this:</p><pre><code>void proto_reg_handoff_myproto(void)
{
    //...
    dissector_add_uint(&quot;tcp.port&quot;, myport, myproto_handle);
    //...
}</code></pre><p>...where <code>myproto</code> is your protocol's abbreviation. The above assumes your protocol is built on top of another. If your protocol is supposed to be the lowest-level protocol, you may need more code.</p><p>Also note that your dissector may not be automatically added to the "Decode As..." menu (<a href="http://ask.wireshark.org/questions/10046#10048">see here</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '12, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-12832" class="comments-container"><span id="12834"></span><div id="comment-12834" class="comment"><div id="post-12834-score" class="comment-score">1</div><div class="comment-text"><p>It's also possible to use <code>dissector_add_handle("tcp.port", myproto_handle);</code> instead of <code>dissector_add_uint(...);</code> if you want your protocol accessible only in the "decode as" menu.</p><p>Look at <code>proto_reg_handoff...(){...}</code> in various dissectors in <code>epan/dissectors</code> for examples.</p></div><div id="comment-12834-info" class="comment-info"><span class="comment-age">(18 Jul '12, 10:57)</span> Bill Meier ♦♦</div></div><span id="12920"></span><div id="comment-12920" class="comment"><div id="post-12920-score" class="comment-score"></div><div class="comment-text"><p>I tried the dissector_add_uint method, but my dissector only decodes a few UDP packets rather than all of them. Also wouldnt this method only decode UDP packets that use the same source port as "myport"?<br />
What would I have to do to have it decode any UDP packet, regardless of the ports?</p></div><div id="comment-12920-info" class="comment-info"><span class="comment-age">(23 Jul '12, 08:14)</span> bball2601</div></div><span id="12923"></span><div id="comment-12923" class="comment"><div id="post-12923-score" class="comment-score"></div><div class="comment-text"><blockquote><p>wouldnt this method only decode UDP packets that use the same source port as "myport"? yes (well source or dest port and the port can be made a preference.)</p></blockquote><p>You could try a heuristic dissector but that means that your dissector will have to "look at" a number of bytes in the packet and determine if it's your protocol or not.</p></div><div id="comment-12923-info" class="comment-info"><span class="comment-age">(23 Jul '12, 08:54)</span> Anders ♦</div></div></div><div id="comment-tools-12832" class="comment-tools"></div><div class="clear"></div><div id="comment-12832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

