+++
type = "question"
title = "How can I use the PTP(IEEE1588) dissector as a postdissector in my LUA script?"
description = '''Hi all, I want to decode a PTP(IEEE1588) message stream which is NOT transported via Ethernet. Basic idea was to unpack the stream from my transport layer and then take the PTP dissector used in Wireshark as a post dissector in my LUA script.  However attempts to get the dissector handle using &quot;loca...'''
date = "2017-01-14T05:13:00Z"
lastmod = "2017-01-14T05:13:00Z"
weight = 58762
keywords = [ "lua", "dissector", "ptp" ]
aliases = [ "/questions/58762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use the PTP(IEEE1588) dissector as a postdissector in my LUA script?](/questions/58762/how-can-i-use-the-ptpieee1588-dissector-as-a-postdissector-in-my-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58762-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I want to decode a PTP(IEEE1588) message stream which is NOT transported via Ethernet. Basic idea was to unpack the stream from my transport layer and then take the PTP dissector used in Wireshark as a post dissector in my LUA script. However attempts to get the dissector handle using "local default_dissector = Dissector.get("ptp")" returned a Lua Error: "bad argument #1 to 'get' (Dissector_get: No such dissector)". Any comments on how the PTP dissector can be accessed? Thanks</p></div><div id="question-tags" class="tags-container tags">lua dissector ptp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '17, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/e46453fe4621a03022dd89f15e431332?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralph%20Paul&#39;s gravatar image" /><p>Ralph Paul<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralph Paul has no accepted answers">0%</span></p></div></div><div id="comments-container-58762" class="comments-container"></div><div id="comment-tools-58762" class="comment-tools"></div><div class="clear"></div><div id="comment-58762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

