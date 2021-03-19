+++
type = "question"
title = "Reload capture when clicking on a custom Lua menu"
description = '''I&#x27;ve made the example mytap_menu() of https://wiki.wireshark.org/Lua/Taps  I click on the menu and window opens I reload the capture manually to make the Lua script works  How can I reload the capture directly in the Lua script and have the results directly when clicking on the menu.'''
date = "2016-10-12T03:21:00Z"
lastmod = "2016-10-16T13:42:00Z"
weight = 56313
keywords = [ "lua" ]
aliases = [ "/questions/56313" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Reload capture when clicking on a custom Lua menu](/questions/56313/reload-capture-when-clicking-on-a-custom-lua-menu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56313-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've made the example mytap_menu() of <a href="https://wiki.wireshark.org/Lua/Taps">https://wiki.wireshark.org/Lua/Taps</a></p><ol><li>I click on the menu and window opens</li><li>I reload the capture manually to make the Lua script works</li></ol><p>How can I reload the capture directly in the Lua script and have the results directly when clicking on the menu.</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '16, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-56313" class="comments-container"></div><div id="comment-tools-56313" class="comment-tools"></div><div class="clear"></div><div id="comment-56313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56428"></span>

<div id="answer-container-56428" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56428-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There seems to be a <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Gui.html#lua_fn_reload_packets__"><code>reload_packets()</code></a> function according to Wireshark's Lua API Reference manual. Have you tried that?</p><p>If you are developing a new Lua dissector, note that the <em>Analyze</em> menu has a <em>Reload Lua Plugins</em> (Ctrl+Shift+L) option that will automatically reload the Lua script and capture file as needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '16, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56428" class="comments-container"><span id="56430"></span><div id="comment-56430" class="comment"><div id="post-56430-score" class="comment-score">2</div><div class="comment-text"><p>Try <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Gui.html#lua_fn_retap_packets__"><code>retap_packets()</code></a> first, if the goal is to run the tap so it can process the packets and display the results; if the tap doesn't actually affect the dissection of packets, that's cheaper, as it doesn't cause a redisplay.</p></div><div id="comment-56430-info" class="comment-info"><span class="comment-age">(16 Oct '16, 19:36)</span> Guy Harris ♦♦</div></div><span id="56431"></span><div id="comment-56431" class="comment"><div id="post-56431-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys, both worked, I'll keep in mind the difference</p></div><div id="comment-56431-info" class="comment-info"><span class="comment-age">(16 Oct '16, 20:57)</span> TomLaBaude</div></div></div><div id="comment-tools-56428" class="comment-tools"></div><div class="clear"></div><div id="comment-56428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

