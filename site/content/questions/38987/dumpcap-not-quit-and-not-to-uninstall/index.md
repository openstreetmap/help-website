+++
type = "question"
title = "Dumpcap not quit and not to uninstall"
description = '''Hello, i facing the this issue: Dumpcap might not quit if Wireshark or TShark crashes. (Bug 1419) is the any workaround because i cannot use Wireshatk on my W8 64Bit Laptop After i restart the Laptop Wireshark hangs during Start &quot;loading configuration fies&quot;  and thats it. i need to unsinstall Wiresh...'''
date = "2015-01-09T00:24:00Z"
lastmod = "2015-01-09T02:04:00Z"
weight = 38987
keywords = [ "dumpcap" ]
aliases = [ "/questions/38987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap not quit and not to uninstall](/questions/38987/dumpcap-not-quit-and-not-to-uninstall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i facing the this issue: Dumpcap might not quit if Wireshark or TShark crashes. (Bug 1419) is the any workaround because i cannot use Wireshatk on my W8 64Bit Laptop</p><p>After i restart the Laptop Wireshark hangs during Start "loading configuration fies" and thats it. i need to unsinstall Wireshark but this is denied regarding Dumpdap is still running but dumpcap is not to "Task Cancel" using Taskmanager...its a kind of Deadlock situation. please support:-) thany you and best regards Michael</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '15, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/baada888dc89f73d863e1da94b0bec0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haylebob&#39;s gravatar image" /><p>haylebob<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haylebob has no accepted answers">0%</span></p></div></div><div id="comments-container-38987" class="comments-container"><span id="39063"></span><div id="comment-39063" class="comment"><div id="post-39063-score" class="comment-score"></div><div class="comment-text"><p>I had this same error. After reading the previous messages, I attempted to delete the folder Wireshark, which was unsuccessful. I was able to "cut" the folder and paste it somewhere else as the administrator. After the program successfully opened, it now says the NPF driver isn't working. It also suggested I install the update from Wireshark 1.12.1 to Wireshark 1.12.3. While doing the uninstall and re-installing the updated software, it had an error installing WinPCaP. I pushed the "abort" button, but the rest of Wireshark continued to install. I have Window 8.1 64bit OS. This may not help, but I have homework to do so am going to see if this works anyways.<br />
</p><p>~ Skip that... the program works, but now you can't do any captures and it won't let me refresh the interfaces. :(</p></div><div id="comment-39063-info" class="comment-info"><span class="comment-age">(11 Jan '15, 14:46)</span> Stormy Skies</div></div><span id="39072"></span><div id="comment-39072" class="comment"><div id="post-39072-score" class="comment-score"></div><div class="comment-text"><p>That sounds like you need to reinstall WinPCap. You can download a standalone installer from their <a href="http://www.winpcap.org/install/">website</a></p></div><div id="comment-39072-info" class="comment-info"><span class="comment-age">(12 Jan '15, 02:22)</span> grahamb ♦</div></div></div><div id="comment-tools-38987" class="comment-tools"></div><div class="clear"></div><div id="comment-38987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38989"></span>

<div id="answer-container-38989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38989-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A few other folks have run into this situation, without it really being resolved. I suspect (from previous investigations) the issue is actually in WinPCap.</p><p>Random guess, do you have any other networking tools installed on the machine that might have installed their own version of WinPCap?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '15, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-38989" class="comments-container"><span id="38992"></span><div id="comment-38992" class="comment"><div id="post-38992-score" class="comment-score"></div><div class="comment-text"><p>no from my site only Wireshark here installed using WinPCap</p></div><div id="comment-38992-info" class="comment-info"><span class="comment-age">(09 Jan '15, 02:41)</span> haylebob</div></div><span id="38993"></span><div id="comment-38993" class="comment"><div id="post-38993-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>as indicated by Graham it seems to be a known issue between WinPcap and Windows 8/8.1 faced by some users. See those threads for more information and possible workarounds (that worked for some guys):</p><p><a href="https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81">https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81</a></p><p><a href="https://ask.wireshark.org/questions/27855/cant-uninstall-wireshark-on-win8-64bit">https://ask.wireshark.org/questions/27855/cant-uninstall-wireshark-on-win8-64bit</a></p><p>There are other questions treating this subject that can be found with a search</p></div><div id="comment-38993-info" class="comment-info"><span class="comment-age">(09 Jan '15, 02:46)</span> Pascal Quantin</div></div><span id="38994"></span><div id="comment-38994" class="comment"><div id="post-38994-score" class="comment-score"></div><div class="comment-text"><p>The same happens on Windows Server 2012 R2 (s. <a href="https://ask.wireshark.org/questions/36441/server-2012-r2-wireshark-crashes)">https://ask.wireshark.org/questions/36441/server-2012-r2-wireshark-crashes)</a> without Winpcap installed. Imho this is a Wireshark issue.</p></div><div id="comment-38994-info" class="comment-info"><span class="comment-age">(09 Jan '15, 04:00)</span> Uli</div></div><span id="38995"></span><div id="comment-38995" class="comment"><div id="post-38995-score" class="comment-score"></div><div class="comment-text"><p>@Uli,</p><p>As I commented on that question, no-one in the core team is able to replicate the issue on the machines we have access to (both 8\8.1 and server 2k12 R2).</p><p>The only way forward is to debug the issue via either local debugging on affected machines (needs sources and lots of knowledge) or remote debugging using crash dumps from affected machines which no-one seems to be prepared to make available.</p><p>One person with the issue did make crash dumps available (on 8 or 8.1) and the dumpcap process was stuck in a call to WinPCap which is a different project.</p></div><div id="comment-38995-info" class="comment-info"><span class="comment-age">(09 Jan '15, 04:35)</span> grahamb ♦</div></div><span id="39035"></span><div id="comment-39035" class="comment"><div id="post-39035-score" class="comment-score"></div><div class="comment-text"><p>Hi all,</p><p>thank you very much for help :-) this threat from Ling regarding changing Reg-Key <a href="https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81">https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81</a> but im still testing...;-)</p><pre><code>In the registry, change HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NPF\Start to 0x3 (SERVICE_DEMAND_START)
Run your program (i.e., wireshark, gns3, ...) as Administrator! (Run as Administrator)(You can also change it to always run as administrator!)</code></pre><p>seem to hepls me i'll feedback here soon</p><p>best regards Michael</p></div><div id="comment-39035-info" class="comment-info"><span class="comment-age">(10 Jan '15, 23:32)</span> haylebob</div></div><span id="39039"></span><div id="comment-39039" class="comment not_top_scorer"><div id="post-39039-score" class="comment-score"></div><div class="comment-text"><p>I'd missed that answer, so I've added a comment to it which I'll repeat here:</p><p>Although this may fix your issues, running Wireshark with elevated privileges is not recommended. There are millions of lines of unaudited code in Wireshark and a great deal of work has been undertaken to allow Wireshark to run without elevating privs.</p></div><div id="comment-39039-info" class="comment-info"><span class="comment-age">(11 Jan '15, 03:55)</span> grahamb ♦</div></div></div><div id="comment-tools-38989" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-38989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

