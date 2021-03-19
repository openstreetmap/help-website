+++
type = "question"
title = "Can&#x27;t get tcp.port of packet in lua"
description = '''Hello how can i get a tcp.port of packet in lua?'''
date = "2012-04-05T01:22:00Z"
lastmod = "2012-04-05T09:48:00Z"
weight = 9952
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/9952" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't get tcp.port of packet in lua](/questions/9952/cant-get-tcpport-of-packet-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello how can i get a tcp.port of packet in lua?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '12, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/1f3e4aeb3a40e8efc02ddde263388b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zvika&#39;s gravatar image" /><p>Zvika<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zvika has no accepted answers">0%</span></p></div></div><div id="comments-container-9952" class="comments-container"></div><div id="comment-tools-9952" class="comment-tools"></div><div class="clear"></div><div id="comment-9952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9965"></span>

<div id="answer-container-9965" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9965-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_attrib_pinfo_src_port"><code>pinfo.src_port</code></a> or <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_attrib_pinfo_dst_port"><code>pinfo.dst_port</code></a>.</p><h3 id="from-a-dissector">From a dissector:</h3><pre><code>function proto_foo.dissector(buf, pinfo, tree)
    print(&#39;src_port&#39;, pinfo.src_port)
    print(&#39;dst_port&#39;, pinfo.dst_port)
end</code></pre><h3 id="from-a-tap">From a tap:</h3><pre><code>function tap.packet(pinfo, buf)
    print(&#39;src_port&#39;, pinfo.src_port)
    print(&#39;dst_port&#39;, pinfo.dst_port)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '12, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-9965" class="comments-container"></div><div id="comment-tools-9965" class="comment-tools"></div><div class="clear"></div><div id="comment-9965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

