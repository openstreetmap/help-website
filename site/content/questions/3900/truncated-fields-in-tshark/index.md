+++
type = "question"
title = "truncated fields in tshark"
description = '''When I try to fetch ntlm fields from a sniff file the fields are truncated to the first byte. tshark -r file.pcap -T fields -e ntlmssp.auth.domain -e ntlmssp.auth.username -R ntlmssp.auth.username output: NULL NULL B A E A D a NULL NULL B A A A D A E a For other string fields, this works fine, also ...'''
date = "2011-05-03T07:42:00Z"
lastmod = "2011-05-03T07:42:00Z"
weight = 3900
keywords = [ "fields", "tshark", "truncated" ]
aliases = [ "/questions/3900" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [truncated fields in tshark](/questions/3900/truncated-fields-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to fetch ntlm fields from a sniff file the fields are truncated to the first byte.<br />
tshark -r file.pcap -T fields -e ntlmssp.auth.domain -e ntlmssp.auth.username -R ntlmssp.auth.username<br />
output:<br />
NULL NULL<br />
B A<br />
E A<br />
D a<br />
NULL NULL<br />
B A<br />
A A<br />
D A<br />
E a<br />
For other string fields, this works fine, also in Wireshark itself, I get the complete string. Is this a bug or am I missing something.</p></div><div id="question-tags" class="tags-container tags">fields tshark truncated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/f8a68bc98d1e4df270dc0007c8280ddd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruwi&#39;s gravatar image" /><p>ruwi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruwi has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '11, 19:18</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></br></p></div></div><div id="comments-container-3900" class="comments-container"><span id="3903"></span><div id="comment-3903" class="comment"><div id="post-3903-score" class="comment-score"></div><div class="comment-text"><p>What version of tshark are you using and upon what platform/OS are you running it?</p></div><div id="comment-3903-info" class="comment-info"><span class="comment-age">(03 May '11, 08:42)</span> cmaynard ♦♦</div></div><span id="4065"></span><div id="comment-4065" class="comment"><div id="post-4065-score" class="comment-score"></div><div class="comment-text"><p>sorry for the late feedback Wireshark 1.4.6 OS Win XP</p></div><div id="comment-4065-info" class="comment-info"><span class="comment-age">(13 May '11, 07:15)</span> ruwi</div></div><span id="4066"></span><div id="comment-4066" class="comment"><div id="post-4066-score" class="comment-score"></div><div class="comment-text"><p>OK, that's a new enough version of Wireshark, so I would expect this to work, but unfortunately I can't think of any reason why it wouldn't work. Unless someone else on this forum has any idea, you will probably need to post a capture file somewhere for someone to take a look at.</p></div><div id="comment-4066-info" class="comment-info"><span class="comment-age">(13 May '11, 08:40)</span> cmaynard ♦♦</div></div><span id="4067"></span><div id="comment-4067" class="comment"><div id="post-4067-score" class="comment-score"></div><div class="comment-text"><p>It looks like we may be trying to print wide characters. After glancing through the code I don't see any obvious reason for this.</p></div><div id="comment-4067-info" class="comment-info"><span class="comment-age">(13 May '11, 09:07)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-3900" class="comment-tools"></div><div class="clear"></div><div id="comment-3900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

