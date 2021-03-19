+++
type = "question"
title = "ipv6 routing header dissector update"
description = '''I&#x27;m sending and processing IPv6 packets with a routing extension header (protocol 43). I&#x27;m using a new type field (within the protocol 43 extension header) as the contents are custom. Wireshark understands how to dissect protocol 43 type=0 packets but not my packets. I&#x27;d like to either:  override wi...'''
date = "2014-03-26T04:40:00Z"
lastmod = "2014-03-26T04:40:00Z"
weight = 31169
keywords = [ "override", "dissector", "routing", "extension", "ipv6" ]
aliases = [ "/questions/31169" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ipv6 routing header dissector update](/questions/31169/ipv6-routing-header-dissector-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31169-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sending and processing IPv6 packets with a routing extension header (protocol 43). I'm using a new type field (within the protocol 43 extension header) as the contents are custom. Wireshark understands how to dissect protocol 43 type=0 packets but not my packets. I'd like to either:</p><ul><li>override wireshark's protocol 43 dissector with mine which can parse protocol=43 and the contents of my new type field.</li><li>tell wireshark to invoke my dissector when it sees protocol 43 with my type field value.<br />
</li></ul><p>What are the steps to do either of the above?<br />
</p><p>Note that currently my dissector is written in LUA.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">override dissector routing extension ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/530568ff96b9380fc92e410053efc97c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="314&#39;s gravatar image" /><p>314<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="314 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-31169" class="comments-container"></div><div id="comment-tools-31169" class="comment-tools"></div><div class="clear"></div><div id="comment-31169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

