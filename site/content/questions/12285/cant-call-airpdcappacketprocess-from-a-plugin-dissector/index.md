+++
type = "question"
title = "Can&#x27;t call AirPDcapPacketProcess from a plugin dissector"
description = '''packet-foo.obj : error LNK2019: unresolved external symbol _AirPDcapPacket Process referenced in function _try_decrypt foo.dll : fatal error LNK1120: 1 unresolved externals  Currently, for some reason, even with all the includes added, there doesn&#x27;t seem to be any linking occuring to airpdcap.c, whe...'''
date = "2012-06-28T11:52:00Z"
lastmod = "2012-06-28T13:58:00Z"
weight = 12285
keywords = [ "airpdcap", "airpcap", "linker" ]
aliases = [ "/questions/12285" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't call AirPDcapPacketProcess from a plugin dissector](/questions/12285/cant-call-airpdcappacketprocess-from-a-plugin-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>packet-foo.obj : error LNK2019: unresolved external symbol _AirPDcapPacket
Process referenced in function _try_decrypt
foo.dll : fatal error LNK1120: 1 unresolved externals</code></pre><p>Currently, for some reason, even with all the includes added, there doesn't seem to be any linking occuring to airpdcap.c, where the definition and declaration for AirPDcapPacketProcess are.</p><pre><code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;glib.h&gt;
#include &lt;epan/emem.h&gt;
#include &lt;epan/packet.h&gt;
#include &lt;epan/dissectors/packet-tcp.h&gt;
#include &lt;epan/prefs.h&gt;
#include &lt;epan/crypt/wep-wpadefs.h&gt;
#include &lt;math.h&gt;
#include &quot;packet-foo.h&quot;
#include &lt;epan/bitswap.h&gt;
#include &lt;epan/proto.h&gt;
#include &lt;epan/addr_resolv.h&gt;
#include &lt;epan/strutil.h&gt;
#include &lt;epan/etypes.h&gt;
#include &lt;epan/oui.h&gt;
#include &lt;epan/greproto.h&gt;
#include &lt;epan/crc32.h&gt;
#include &lt;epan/tap.h&gt;
#include &lt;epan/expert.h&gt;
#include &lt;epan/reassemble.h&gt;
#include &lt;glibconfig.h&gt;
#include &lt;gmodule.h&gt;
#include &lt;epan/crypt/airpdcap_ws.h&gt;</code></pre><p>Is there anything I am missing? Thanks.</p></div><div id="question-tags" class="tags-container tags">airpdcap airpcap linker</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/40b1f396144af1f57dd3b8a211387e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ian&#39;s gravatar image" /><p>Ian<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '12, 20:12</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12285" class="comments-container"></div><div id="comment-tools-12285" class="comment-tools"></div><div class="clear"></div><div id="comment-12285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12292"></span>

<div id="answer-container-12292" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12292-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you're trying to build a plugin rather than a built-in dissector.</p><p>AirPDcapPacket() is in epan/crypt but the symbol is NOT exported (in epan/libwireshark.def) so the symbol can't be used from plugins.</p><p>Options:</p><ol><li>Make your plugin a built-in dissector</li><li>(or) add AirPDcapPacket() (and any other necessary symbols) to epan/libwireshark.def</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12292" class="comments-container"><span id="12311"></span><div id="comment-12311" class="comment"><div id="post-12311-score" class="comment-score"></div><div class="comment-text"><p>Apologies, I am indeed trying to build a plugin: however, libwireshark.def won't make the link for AirPDcapPacketProcess(), so is there any other other way to create a link (short of copying the functions and defintions from the .c to my plugin)?</p></div><div id="comment-12311-info" class="comment-info"><span class="comment-age">(29 Jun '12, 06:24)</span> Ian</div></div><span id="12338"></span><div id="comment-12338" class="comment"><div id="post-12338-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm not sure I understand... libwireshark.def does not currently export AirPDcapPacketProcess but you can add it--unless you want to run your plugin with an unmodified version of Wireshark in which case you'd have to open a bug and ask that Wireshark export the symbol.</p><p>I do assume that you're actually using the function in your plugin?</p><p>If so and if you don't want to modify Wireshark then, yes, copying the function (and any dependencies of that function) would be the only option.</p></div><div id="comment-12338-info" class="comment-info"><span class="comment-age">(29 Jun '12, 14:05)</span> JeffMorriss ♦</div></div><span id="12391"></span><div id="comment-12391" class="comment"><div id="post-12391-score" class="comment-score"></div><div class="comment-text"><p>Mostly working when the function and dependencies were copied, I'll keep trucking away @ it. Thanks :)</p></div><div id="comment-12391-info" class="comment-info"><span class="comment-age">(03 Jul '12, 06:03)</span> Ian</div></div></div><div id="comment-tools-12292" class="comment-tools"></div><div class="clear"></div><div id="comment-12292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

