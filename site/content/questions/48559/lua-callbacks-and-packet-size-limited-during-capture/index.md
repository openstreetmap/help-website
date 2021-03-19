+++
type = "question"
title = "Lua callbacks and &quot;Packet size limited during capture&quot;"
description = '''I compare tshark performances with tsv output with Lua script vs &quot;-T fields&quot; output on HTTP packets. (Disclaimer: Lua is 2x faster!) I have some differences in output, some HTTP packets are missing in Lua&#x27;s output. When I digged in, I realized that they concern truncated packets during capture that ...'''
date = "2015-12-16T01:52:00Z"
lastmod = "2015-12-16T01:52:00Z"
weight = 48559
keywords = [ "lua", "capture-filter", "truncated" ]
aliases = [ "/questions/48559" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua callbacks and "Packet size limited during capture"](/questions/48559/lua-callbacks-and-packet-size-limited-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48559-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I compare tshark performances with tsv output with Lua script vs "-T fields" output on HTTP packets. (Disclaimer: Lua is 2x faster!)</p><p>I have some differences in output, some HTTP packets are missing in Lua's output. When I digged in, I realized that they concern truncated packets during capture that seem to not match my Listener.new("http")</p><p>It seems that if a packet is truncated, in the middle of HTTP for ex, and the dissector can not be fully applied, then Lua's callback on http.packet() is not called.</p><p>But my truncated HTTP is well displayed in Wireshark and tshark with "-T fields"</p><p>Can someone confirm me this behavior with Lua listeners? Is there a workaround?</p></div><div id="question-tags" class="tags-container tags">lua capture-filter truncated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-48559" class="comments-container"></div><div id="comment-tools-48559" class="comment-tools"></div><div class="clear"></div><div id="comment-48559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

