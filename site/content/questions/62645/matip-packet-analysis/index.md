+++
type = "question"
title = "MATIP Packet Analysis"
description = '''HI, I am working on MATIP (port 350) over TCP/IP traffic analysis as per the RFC https://tools.ietf.org/html/draft-rfced-info-matip-00#section-8.1.1.1 Would be great if I can get the packet analyzer for MATIP. Any help would be greatly appreciated.'''
date = "2017-07-10T05:22:00Z"
lastmod = "2017-07-10T05:22:00Z"
weight = 62645
keywords = [ "matip" ]
aliases = [ "/questions/62645" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MATIP Packet Analysis](/questions/62645/matip-packet-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI, I am working on MATIP (port 350) over TCP/IP traffic analysis as per the RFC <a href="https://tools.ietf.org/html/draft-rfced-info-matip-00#section-8.1.1.1">https://tools.ietf.org/html/draft-rfced-info-matip-00#section-8.1.1.1</a></p><p>Would be great if I can get the packet analyzer for MATIP. Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">matip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '17, 05:22</strong></p><img src="https://secure.gravatar.com/avatar/989019c7bf9630d8bac7903ecb78ea5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J4jay&#39;s gravatar image" /><p>J4jay<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J4jay has no accepted answers">0%</span></p></div></div><div id="comments-container-62645" class="comments-container"><span id="62646"></span><div id="comment-62646" class="comment"><div id="post-62646-score" class="comment-score"></div><div class="comment-text"><p>If you have some programming experience and you don't want to take the burden of rolling out a Wireshark development environment, you may use <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html">Lua</a> to write your own dissector. The price is slower speed as compared to dissectors written in C, the advantage is the speed and simplicity of development.</p></div><div id="comment-62646-info" class="comment-info"><span class="comment-age">(10 Jul '17, 05:48)</span> sindy</div></div><span id="62648"></span><div id="comment-62648" class="comment"><div id="post-62648-score" class="comment-score"></div><div class="comment-text"><p>If you want to have this protocol supported in some future Wireshark version open an <a href="https://bugs.wireshark.org/bugzilla/">enhancement bug</a> (including sample capture(s)). Maybe someone will look after it.</p><p>There has been a <a href="https://www.wireshark.org/lists/ethereal-dev/200601/msg00252.html">patch for MATIP</a> a long, long time ago, which hasn't been merged.</p></div><div id="comment-62648-info" class="comment-info"><span class="comment-age">(10 Jul '17, 07:45)</span> Uli</div></div></div><div id="comment-tools-62645" class="comment-tools"></div><div class="clear"></div><div id="comment-62645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

