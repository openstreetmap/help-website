+++
type = "question"
title = "Wireshark host file trouble with Windows 7"
description = '''I tried to create a simple host file in Wireshark using Windows 7 64-bit Ultimate edition and in captures, I see a lot of DNS request error packets stating no such name exists. I know with the virtual folders in Windows, i had to go to I assumed C:&#92;%username%&#92;AppData&#92;roaming&#92;wireshark to create the ...'''
date = "2012-01-18T19:12:00Z"
lastmod = "2012-01-19T04:18:00Z"
weight = 8460
keywords = [ "windows7", "hosts", "troubleshooting", "wireshark" ]
aliases = [ "/questions/8460" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark host file trouble with Windows 7](/questions/8460/wireshark-host-file-trouble-with-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to create a simple host file in Wireshark using Windows 7 64-bit Ultimate edition and in captures, I see a lot of DNS request error packets stating no such name exists. I know with the virtual folders in Windows, i had to go to I assumed C:\%username%\AppData\roaming\wireshark to create the text document named "hosts" in notepad. Is this the correct path or anyone else experience similar results?</p></div><div id="question-tags" class="tags-container tags">windows7 hosts troubleshooting wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '12, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/254551017921d3c546b914127aca90ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Pessia&#39;s gravatar image" /><p>Andy Pessia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Pessia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '12, 00:13</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8460" class="comments-container"></div><div id="comment-tools-8460" class="comment-tools"></div><div class="clear"></div><div id="comment-8460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8463"></span>

<div id="answer-container-8463" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8463-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just tested with a "hosts" file in my [...]\AppData\Roaming\Wireshark folder, and it worked fine, so I'd say you have the correct path. I have tons of DNS reverse pointer lookups as soon as I enable Network Name Resolution, but that is normal and often doesn't find a result for internal IPs. The names from the hosts file are working every time though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '12, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8463" class="comments-container"><span id="8483"></span><div id="comment-8483" class="comment"><div id="post-8483-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the fast reply! I tried it again to that same directory path and it still is not working for my ip address on the system I am capturing traffic with. I see all the host names for all my other nodes on my network, i.e. iphone, ipad, mac-mini but it will not resolve for my own machine. I wonder would it have anything to do with using an ALFA wireless USB antenna instead of the on board wireless NIC? I should try that to see if it makes a difference. Following the logic I wouldn't think it would matter. I even tried my (internal) %ipv6, ipv4% LABCOMP..still will not reslove.</p></div><div id="comment-8483-info" class="comment-info"><span class="comment-age">(19 Jan '12, 16:36)</span> Andy Pessia</div></div><span id="8484"></span><div id="comment-8484" class="comment"><div id="post-8484-score" class="comment-score"></div><div class="comment-text"><p>Should I try adding to the Windows host file instead?</p></div><div id="comment-8484-info" class="comment-info"><span class="comment-age">(19 Jan '12, 16:37)</span> Andy Pessia</div></div><span id="8519"></span><div id="comment-8519" class="comment"><div id="post-8519-score" class="comment-score"></div><div class="comment-text"><p>You can try that, or putting the hosts file into the Wireshark program directory, but you'll need to have administrative rights to do that. It'll be interesting to see if it works in those directories. Keep in mind to close and reopen Wireshark each time you change something.</p></div><div id="comment-8519-info" class="comment-info"><span class="comment-age">(20 Jan '12, 14:31)</span> Jasper ♦♦</div></div></div><div id="comment-tools-8463" class="comment-tools"></div><div class="clear"></div><div id="comment-8463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

