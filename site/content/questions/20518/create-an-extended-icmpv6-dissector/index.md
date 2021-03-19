+++
type = "question"
title = "Create an extended ICMPv6 dissector"
description = '''Hello, I&#x27;m trying to implement a dissector for a modification of a message from the ICMPv6 protocol. The modification is basically using an 8-bit reserved field in the ARO (Address Registration Option) message and populating it with 3 new values (4 + 2 + 2 bits). From this documentation link, I can ...'''
date = "2013-04-17T05:54:00Z"
lastmod = "2013-04-17T05:54:00Z"
weight = 20518
keywords = [ "lua", "dissector", "wsgd" ]
aliases = [ "/questions/20518" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create an extended ICMPv6 dissector](/questions/20518/create-an-extended-icmpv6-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20518-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to implement a dissector for a modification of a message from the ICMPv6 protocol. The modification is basically using an 8-bit reserved field in the ARO (Address Registration Option) message and populating it with 3 new values (4 + 2 + 2 bits).</p><p>From <a href="http://www.wireshark.org/docs/dfref/i/icmpv6.html">this documentation link</a>, I can see that Wireshark supports the following ARO related filters: <strong>icmpv6.opt.aro.eui64</strong>, <strong>icmpv6.opt.aro.registration_lifetime</strong> and <strong>icmpv6.opt.aro.status</strong>. What I'd like to do in my dissector is extend the existing ICMPv6 dissector by dissecting the three new values in the reserved 8-bit field, as well as adding three additional filters for each value.</p><p>My doubts are: Is it possible to accomplish this, possibly using a chained dissector or post-dissector? Can I edit/modify a tree created by another dissector, when I call it using <code>third_party_dissector:call(tvb, pinfo, tree)</code>? What is the best choice: the Lua API or <a href="http://wsgd.free.fr">Wireshark Generic Dissector</a> plugin?</p><p>Best regards, and thanks in advance!</p></div><div id="question-tags" class="tags-container tags">lua dissector wsgd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '13, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/258b6e228a70fe84b9cb7df3b89c809b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ojay&#39;s gravatar image" /><p>ojay<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ojay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '13, 05:54</p></div></div><div id="comments-container-20518" class="comments-container"></div><div id="comment-tools-20518" class="comment-tools"></div><div class="clear"></div><div id="comment-20518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

