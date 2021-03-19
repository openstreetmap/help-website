+++
type = "question"
title = "Can tshark use &#x27;-e &#x27; values generated within a custom lua disector?"
description = '''Hi, I am capturing some packets that contains private headers within the payload. I have written a quick &amp;amp; dirty lua dissector to decode these headers and everything works well from inside wireshark. That is I am able to &quot;decode as&quot; and see my proprietary headers within wireshark as expected. I ...'''
date = "2013-07-22T13:18:00Z"
lastmod = "2013-07-22T14:30:00Z"
weight = 23249
keywords = [ "decode", "lua", "tshark" ]
aliases = [ "/questions/23249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can tshark use '-e ' values generated within a custom lua disector?](/questions/23249/can-tshark-use-e-values-generated-within-a-custom-lua-disector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am capturing some packets that contains private headers within the payload. I have written a quick &amp; dirty lua dissector to decode these headers and everything works well from inside wireshark. That is I am able to "decode as" and see my proprietary headers within wireshark as expected.</p><p>I am now attempting to do the same from cmd line tshark with something like this:</p><p>tshark -X lua_script:foo.lua -r capture_file -T fields -e private.foo -e private.bar</p><p>Unfortunately my private fields are not being displayed which leads me to believe I am missing the "decode as" as step that I performed above. Is there a tshark equivalent to this step?</p><p>Is there a way to have tshark make use of the ~/.wireshark/decode_as_entries file?</p><p>Thanks for any help, Jax</p></div><div id="question-tags" class="tags-container tags">decode lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/9852dcc52491737b463ddb4075caf776?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaxon&#39;s gravatar image" /><p>Jaxon<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaxon has no accepted answers">0%</span></p></div></div><div id="comments-container-23249" class="comments-container"></div><div id="comment-tools-23249" class="comment-tools"></div><div class="clear"></div><div id="comment-23249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23253"></span>

<div id="answer-container-23253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23253-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <code>tshark -h</code>:</p><pre><code>  -d &lt;layer_type&gt;==&lt;selector&gt;,&lt;decode_as_protocol&gt; ...
                           &quot;Decode As&quot;, see the man page for details
                           Example: tcp.port==8888,http</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23253" class="comments-container"></div><div id="comment-tools-23253" class="comment-tools"></div><div class="clear"></div><div id="comment-23253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

