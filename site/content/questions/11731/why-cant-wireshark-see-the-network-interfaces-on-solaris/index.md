+++
type = "question"
title = "Why can&#x27;t Wireshark see the network interfaces on Solaris?"
description = '''When I click the Wireshark toolbar button labeled as &quot;List the available capture interfaces&quot;, I see the following error message in a popup:  There are no interfaces on which a capture can be done  and I&#x27;m running Wireshark as root, so I don&#x27;t think there&#x27;s a privilege problem in play here. How can I...'''
date = "2012-06-07T00:27:00Z"
lastmod = "2012-06-07T00:27:00Z"
weight = 11731
keywords = [ "interfaces", "solaris" ]
aliases = [ "/questions/11731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't Wireshark see the network interfaces on Solaris?](/questions/11731/why-cant-wireshark-see-the-network-interfaces-on-solaris)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I click the Wireshark toolbar button labeled as "List the available capture interfaces", I see the following error message in a popup:</p><blockquote><p>There are no interfaces on which a capture can be done</p></blockquote><p>and I'm running Wireshark as root, so I don't think there's a privilege problem in play here. How can I get Wireshark to list my capture interfaces?</p></div><div id="question-tags" class="tags-container tags">interfaces solaris</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '12, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/ebc83d559e57e26e713cb529206a59f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aisling&#39;s gravatar image" /><p>aisling<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aisling has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '12, 15:57</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11731" class="comments-container"><span id="11741"></span><div id="comment-11741" class="comment"><div id="post-11741-score" class="comment-score"></div><div class="comment-text"><p>What does <code>ifconfig -a</code> print? If the only interface it reports is the loopback interface, then (except perhaps on Solaris 11) there <em>are</em> no interfaces on which a capture can be done - the loopback interface isn't a DLPI interface and doesn't support capturing on it. If it lists other interfaces, can you capture on them with <code>snoop</code>?</p></div><div id="comment-11741-info" class="comment-info"><span class="comment-age">(07 Jun '12, 14:37)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-11731" class="comment-tools"></div><div class="clear"></div><div id="comment-11731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

