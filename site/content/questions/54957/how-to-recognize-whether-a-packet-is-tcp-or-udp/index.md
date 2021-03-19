+++
type = "question"
title = "How to recognize whether a packet is tcp or udp?"
description = '''Hi,  I am trying to find out whether a packet is TCP or UDP in my dissector. The way I am doing this is:-  pinfo.cols.protocol == &quot;tcp&quot; , but for some reason, it is showing as false for valid TCP packets. Hence I wanted to know the correct way to recognize whether a packet is TCP or UDP in the disse...'''
date = "2016-08-18T10:38:00Z"
lastmod = "2016-08-18T10:38:00Z"
weight = 54957
keywords = [ "lua", "dissector", "pinfo", "wireshark" ]
aliases = [ "/questions/54957" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to recognize whether a packet is tcp or udp?](/questions/54957/how-to-recognize-whether-a-packet-is-tcp-or-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54957-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to find out whether a packet is TCP or UDP in my dissector. The way I am doing this is:- pinfo.cols.protocol == "tcp" , but for some reason, it is showing as false for valid TCP packets. Hence I wanted to know the correct way to recognize whether a packet is TCP or UDP in the dissector. I am using Lua to create my dissector. Thanks.</p></div><div id="question-tags" class="tags-container tags">lua dissector pinfo wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p>shobhit_garg91<br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div></div><div id="comments-container-54957" class="comments-container"><span id="54997"></span><div id="comment-54997" class="comment"><div id="post-54997-score" class="comment-score"></div><div class="comment-text"><p>I've only written a postdissector in LUA but assuming your dissector sits above the IP layer can you not just extract the ip.protocol value?</p></div><div id="comment-54997-info" class="comment-info"><span class="comment-age">(19 Aug '16, 15:24)</span> PaulOfford</div></div><span id="55003"></span><div id="comment-55003" class="comment"><div id="post-55003-score" class="comment-score"></div><div class="comment-text"><p>@PaulOfford is right except that the exact field name provided by Wireshark's IP dissector is <code>ip.proto</code>.</p></div><div id="comment-55003-info" class="comment-info"><span class="comment-age">(20 Aug '16, 11:04)</span> sindy</div></div></div><div id="comment-tools-54957" class="comment-tools"></div><div class="clear"></div><div id="comment-54957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

