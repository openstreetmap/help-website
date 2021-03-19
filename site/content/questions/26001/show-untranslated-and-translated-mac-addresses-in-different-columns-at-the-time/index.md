+++
type = "question"
title = "Show untranslated and translated mac addresses in different columns at the time"
description = '''Hi all,  Tshark mac address translation works pretty fine, but somehow if i wanna get translated &amp;amp;&amp;amp; untranslated mac addresses in 2 different columns (as SYN-bit within the below link) it doesn&#x27;t work. Related link On one hand it shows only mac untranslated mac addresses: $ ./tshark -i wlan1...'''
date = "2013-10-15T06:59:00Z"
lastmod = "2013-10-15T07:41:00Z"
weight = 26001
keywords = [ "translated", "mac", "address", "tshark", "unstranslated" ]
aliases = [ "/questions/26001" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show untranslated and translated mac addresses in different columns at the time](/questions/26001/show-untranslated-and-translated-mac-addresses-in-different-columns-at-the-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26001-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Tshark mac address translation works pretty fine, but somehow if i wanna get translated &amp;&amp; untranslated mac addresses in 2 different columns (as SYN-bit within the below link) it doesn't work.</p><p><a href="http://ask.wireshark.org/questions/21730/mac-reverse-name-resolution-in-tshark">Related link</a></p><p>On one hand it shows only mac untranslated mac addresses:</p><pre><code>$ ./tshark -i wlan1 -Nn -o column.format:&#39;&quot;Unres&quot;,&quot;%us&quot;,&quot;Res&quot;,&quot;%rs&quot;&#39;

74:de:2b:94:b4:cf 74:de:2b:94:b4:cf

c8:d7:19:ed:d5:38 c8:d7:19:ed:d5:38

74:de:2b:94:b4:cf 74:de:2b:94:b4:cf</code></pre><p>On the other hand it shows only mac untranslated mac addresses:</p><pre><code>$ ./tshark -i wlan1 -o column.format:&#39;&quot;Unres&quot;,&quot;%us&quot;,&quot;Res&quot;,&quot;%rs&quot;&#39;

LiteonTe_94:b4:cf LiteonTe_94:b4:cf

CiscoCon_ed:d5:38 CiscoCon_ed:d5:38

TrapezeN_94:b4:cf TrapezeN_94:b4:cf</code></pre><p>Actually the output that i'm looking for should be as below:</p><pre><code>LiteonTe_94:b4:cf 74:de:2b:94:b4:cf

CiscoCon_ed:d5:38 c8:d7:19:ed:d5:38

TrapezeN_94:b4:cf c9:e4:32:94:b4:cf</code></pre><p>I've been checking tshark man page, and it especifies how to translate or not (including -N m), but my questions is: how to show untranslated and translated content in different columns at the same time? Any advice about how to manage it?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">translated mac address tshark unstranslated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '13, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/fe34eb5043cdb7fbde263c1a27c39d10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="legramo&#39;s gravatar image" /><p>legramo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="legramo has no accepted answers">0%</span></p></div></div><div id="comments-container-26001" class="comments-container"></div><div id="comment-tools-26001" class="comment-tools"></div><div class="clear"></div><div id="comment-26001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26007"></span>

<div id="answer-container-26007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26007-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't say which version you're using, but using the very latest version (1.11.0 built from source), this works:</p><pre><code>tshark -r sample.pcap -o column.format:&#39;&quot;unres&quot;,&quot;%uhs&quot;,&quot;res&quot;,&quot;%rhs&quot;&#39;</code></pre><p>Note that the "h" in "uhs" specifies a hardware address -- in other words, the MAC address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-26007" class="comments-container"><span id="26009"></span><div id="comment-26009" class="comment"><div id="post-26009-score" class="comment-score"></div><div class="comment-text"><p>I'm using TShark 1.8.2 (not 1.11.0) due to some problems installing the last Tshark version within a Raspberry Pi:</p><p>Linux raspberrypi 3.2.27+ armv6l GNU/Linux</p><p>Have you tried to do it without sample.pcap? I mean:</p><p>./tshark -i wlan1 -o column.format:'"Unres","%us","Res","%rs"'</p></div><div id="comment-26009-info" class="comment-info"><span class="comment-age">(15 Oct '13, 08:19)</span> legramo</div></div><span id="26011"></span><div id="comment-26011" class="comment"><div id="post-26011-score" class="comment-score"></div><div class="comment-text"><p>Yes, I have tried it just now with the default device (Ethernet in my case) as:</p><p>tshark -o column.format:'"Unres","%uhs","Res","%rhs"'</p><p>It should be noted that although this works with 1.11.0, the preferred form is with "gui.column.format" instead of "column.format" due to some renaming that has been done recently to improve consistency.</p></div><div id="comment-26011-info" class="comment-info"><span class="comment-age">(15 Oct '13, 08:28)</span> beroset</div></div><span id="26012"></span><div id="comment-26012" class="comment"><div id="post-26012-score" class="comment-score"></div><div class="comment-text"><p>... except that there's nothing <em>graphical</em> about tshark, so maybe <code>gui.column.format</code> should be changed to <code>ui.column.format</code> so it's more generic and applicable to either the graphical or command-line user interfaces. A discussion for wireshark-dev maybe ...</p></div><div id="comment-26012-info" class="comment-info"><span class="comment-age">(15 Oct '13, 08:45)</span> cmaynard ♦♦</div></div><span id="26013"></span><div id="comment-26013" class="comment"><div id="post-26013-score" class="comment-score"></div><div class="comment-text"><p>By the way, starting with <a href="http://anonsvn.wireshark.org/viewvc?revision=51742&amp;view=revision">r51742</a>, which will be part of 1.11.0 when it's released, you can also add new custom columns in Wireshark for the following fields:</p><ul><li><code>eth.dst_resolved</code></li><li><code>eth.src_resolved</code></li><li><code>eth.addr_resolved</code></li><li><code>wlan.da_resolved</code></li><li><code>wlan.sa_resolved</code></li><li><code>wlan.addr_resolved</code></li><li><code>wlan.ra_resolved</code></li><li><code>wlan.ta_resolved</code></li><li><code>wlan.bssid_resolved</code></li></ul><p>Tshark will then display these columns when the <code>-P</code> option is specified, and you won't need to use <code>-o column.format</code>. I'm not sure which would method would be easier for you or preferred, but at least you'd have the choice.</p><p>See also: <a href="http://ask.wireshark.org/questions/24314/possible-to-use-the-mac-info-in-the-wireshark-manuf-file-as-part-of-display-filter">this</a> question.</p></div><div id="comment-26013-info" class="comment-info"><span class="comment-age">(15 Oct '13, 09:50)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-26007" class="comment-tools"></div><div class="clear"></div><div id="comment-26007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

