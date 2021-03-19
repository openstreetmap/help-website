+++
type = "question"
title = "[closed] The NPF driver isn&#x27;t running"
description = '''Hello, installed wireshark 1.6.0 with wincap 4.1.2 on windows server 2008 R2. When starting wireshark I get the error &quot;The NPF driver isn&#x27;t running&quot;. Logged on as local administrator did not help. Running &quot;SC QC NPF&quot; in command prompt gave me &quot;[SC] OpenService FAILED 1060: The specified service does...'''
date = "2011-06-30T01:49:00Z"
lastmod = "2017-04-17T13:13:00Z"
weight = 4843
keywords = [ "npf" ]
aliases = [ "/questions/4843" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] The NPF driver isn't running](/questions/4843/the-npf-driver-isnt-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4843-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, installed wireshark 1.6.0 with wincap 4.1.2 on windows server 2008 R2. When starting wireshark I get the error "The NPF driver isn't running". Logged on as local administrator did not help. Running "SC QC NPF" in command prompt gave me "[SC] OpenService FAILED 1060: The specified service does not exist as an installed service." Checked in Device Manager and the "NetGroup Packet Filter Driver" does not exist. Please advise. Mario</p></div><div id="question-tags" class="tags-container tags">npf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '11, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/bd103eefa0a7b72674bcd8ae8ef39223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blindpepper&#39;s gravatar image" /><p>Blindpepper<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blindpepper has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 18 Apr '17, 03:02</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-4843" class="comments-container"><span id="30224"></span><div id="comment-30224" class="comment"><div id="post-30224-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem but I DID consciously selected "No" to the prompt because I DON'T ALWAYS run Wireshark every time my machine is up. Is there a way to automatically/manually load this driver when loading Wireshark? (I don't necessarily need NPF unloaded when Wireshark terminates, as long as it does not auto load during the next reboot.)</p><p>As a general rule of thumb, the less stuff you load during boot up the better.</p><p>Thanks</p></div><div id="comment-30224-info" class="comment-info"><span class="comment-age">(26 Feb '14, 22:16)</span> IfM</div></div><span id="30236"></span><div id="comment-30236" class="comment"><div id="post-30236-score" class="comment-score"></div><div class="comment-text"><p>@lfm, you are asking a new question, i.e., "Is there a way to automatically/manually load the NPF driver when loading Wireshark?</p><p>Please submit a new question rather than piggy-backing on this one.</p></div><div id="comment-30236-info" class="comment-info"><span class="comment-age">(27 Feb '14, 08:38)</span> cmaynard ♦♦</div></div><span id="30260"></span><div id="comment-30260" class="comment"><div id="post-30260-score" class="comment-score"></div><div class="comment-text"><p>humm,</p><p>I thought I was just expanding on "kucf Uoy's" post. I did say "I have the same problem..." and he did have the correct solution to the major part of my problem.</p><p>but sure, what ever you want...</p><p>Just keep in mind that the 2/3 of my question in this new thread will be identical to this thread and anyone who has the same concern will now require to peruse two different thread to obtain the solution. (Assuming there is a solution.)</p><p>Hope you see this as an efficient use of this forum.</p></div><div id="comment-30260-info" class="comment-info"><span class="comment-age">(28 Feb '14, 00:56)</span> IfM</div></div><span id="30261"></span><div id="comment-30261" class="comment"><div id="post-30261-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Is there a way to automatically/manually load this driver when loading Wireshark</p></blockquote><p>A (totally) automatic way? No, because you must start the NPF service as administrator, but <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">you shall <strong>not run</strong> Wireshark as administrator</a>.</p><p>You can do it manually (or with a scripted solution):</p><ul><li>start an elevated DOS box ('Run as Administrator')</li><li>run: <code>sc start npf</code></li><li>start Wireshark in your regular environment, <strong>without</strong> Admin privileges.</li></ul></div><div id="comment-30261-info" class="comment-info"><span class="comment-age">(28 Feb '14, 01:14)</span> Kurt Knochner ♦</div></div><span id="30263"></span><div id="comment-30263" class="comment"><div id="post-30263-score" class="comment-score"></div><div class="comment-text"><p>Works great! A quick precise productive response instead of ...</p><p>Thank you Kurt!!</p></div><div id="comment-30263-info" class="comment-info"><span class="comment-age">(28 Feb '14, 01:28)</span> IfM</div></div><span id="30264"></span><div id="comment-30264" class="comment not_top_scorer"><div id="post-30264-score" class="comment-score"></div><div class="comment-text"><p>To ride on Kurt's coat tail;</p><p>sc stop npf</p><p>will unload the npf drivers.</p></div><div id="comment-30264-info" class="comment-info"><span class="comment-age">(28 Feb '14, 01:42)</span> IfM</div></div><span id="30615"></span><div id="comment-30615" class="comment not_top_scorer"><div id="post-30615-score" class="comment-score"></div><div class="comment-text"><p>Thanks - it works!</p></div><div id="comment-30615-info" class="comment-info"><span class="comment-age">(09 Mar '14, 05:17)</span> Guby</div></div><span id="60873"></span><div id="comment-60873" class="comment not_top_scorer"><div id="post-60873-score" class="comment-score"></div><div class="comment-text"><p>I closed the question as it's just attracting random answers.</p></div><div id="comment-60873-info" class="comment-info"><span class="comment-age">(18 Apr '17, 03:03)</span> grahamb ♦</div></div></div><div id="comment-tools-4843" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-4843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by grahamb 18 Apr '17, 03:02

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

7 Answers:

</div>

</div>

<span id="12499"></span>

<div id="answer-container-12499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12499-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>download winpcap. <a href="http://www.winpcap.org/install/default.htm">http://www.winpcap.org/install/default.htm</a> problem solve.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '12, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/8cb6217dc8df1a5476487449406b8045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Safiro21&#39;s gravatar image" /><p>Safiro21<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Safiro21 has no accepted answers">0%</span></p></div></div><div id="comments-container-12499" class="comments-container"><span id="13560"></span><div id="comment-13560" class="comment"><div id="post-13560-score" class="comment-score"></div><div class="comment-text"><p>Thank you! Got wireshark up and running again!</p></div><div id="comment-13560-info" class="comment-info"><span class="comment-age">(11 Aug '12, 12:11)</span> prittypixy</div></div></div><div id="comment-tools-12499" class="comment-tools"></div><div class="clear"></div><div id="comment-12499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38691"></span>

<div id="answer-container-38691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38691-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To cllear this error, you need to open the file called npf.sys which is located at</p><pre><code>* C:\Windows\System32\Drivers\</code></pre><p>in Windows 7. Follow the below guide to open the <em>npf.sys</em> file.</p><p>Firstly, make sure that you have installed winpcap, if you didn't install it, just go to its official site and download it for installation: <a href="http://www.winpcap.org"></a><a href="http://www.winpcap.org">http://www.winpcap.org</a> Next, find cmd.exe which is located at</p><pre><code>* C:\Windows\System32</code></pre><p>in Windows 7, right click and "Run as administrator". When it opened, input <em>net start npf</em>, then the NPF driver is successfully opened. That is,the file npf.sys is opened.</p><p>At last, restart Wireshark, it will be OK now.</p><p>BTW, if you have other driver problems or want to update, backup or restore drivers, the free program DriveTheLife (official site: <a href="http://www.drivethelife.com"></a><a href="http://www.drivethelife.com">http://www.drivethelife.com</a>) is a perfect one.</p><p><strong>Note:</strong> If you are using Linux or Ubuntu, after WinpCap is installed, use the common " &gt;$ su Administrator " to switch to the highest authority account, then input net start npf .</p><p>If you are using Windows XP, login with administrator account then open cmd, input net start npf.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/0bc6696cb16a86e51f6ae1fd661a3bac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OliviaLewis&#39;s gravatar image" /><p>OliviaLewis<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OliviaLewis has no accepted answers">0%</span></p></div></div><div id="comments-container-38691" class="comments-container"><span id="39320"></span><div id="comment-39320" class="comment"><div id="post-39320-score" class="comment-score"></div><div class="comment-text"><p>This worked for me and seems to be the best solution if you don't want the WinPCap-Drivers being loaded everytime when Windows starts.</p><p>Thank you :)</p></div><div id="comment-39320-info" class="comment-info"><span class="comment-age">(20 Jan '15, 10:04)</span> chickenforce</div></div><span id="46046"></span><div id="comment-46046" class="comment"><div id="post-46046-score" class="comment-score"></div><div class="comment-text"><p>ditto w chickenforce</p></div><div id="comment-46046-info" class="comment-info"><span class="comment-age">(22 Sep '15, 01:45)</span> mediawhapper</div></div></div><div id="comment-tools-38691" class="comment-tools"></div><div class="clear"></div><div id="comment-38691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18750"></span>

<div id="answer-container-18750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18750-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right-click wireshark, Run As Administrator</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/ca78990612b1e0cda42d7a78c0b31afe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IcebergTitanic&#39;s gravatar image" /><p>IcebergTitanic<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IcebergTitanic has no accepted answers">0%</span></p></div></div><div id="comments-container-18750" class="comments-container"><span id="18751"></span><div id="comment-18751" class="comment"><div id="post-18751-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Right-click wireshark, Run As Administrator</p></blockquote><p><strong>Don't do that!!</strong>. There is a good reason (security) for the privilege separation.</p><blockquote><p><code>http://wiki.wireshark.org/Development/PrivilegeSeparation</code></p></blockquote></div><div id="comment-18751-info" class="comment-info"><span class="comment-age">(19 Feb '13, 13:11)</span> Kurt Knochner ♦</div></div><span id="36834"></span><div id="comment-36834" class="comment"><div id="post-36834-score" class="comment-score"></div><div class="comment-text"><p>Run as Administrator worked for me, Thanks.</p></div><div id="comment-36834-info" class="comment-info"><span class="comment-age">(03 Oct '14, 23:33)</span> Wasike</div></div><span id="36837"></span><div id="comment-36837" class="comment"><div id="post-36837-score" class="comment-score"></div><div class="comment-text"><p>Really not recommended from a security (of your system) point of view, see the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges</a></p></div><div id="comment-36837-info" class="comment-info"><span class="comment-age">(04 Oct '14, 01:47)</span> grahamb ♦</div></div><span id="45949"></span><div id="comment-45949" class="comment"><div id="post-45949-score" class="comment-score"></div><div class="comment-text"><p>You can start WireSharp as admin. It starts winpCap driver then you close WireSharp and start it again as a user without admins privileges.</p></div><div id="comment-45949-info" class="comment-info"><span class="comment-age">(18 Sep '15, 09:56)</span> druzh</div></div></div><div id="comment-tools-18750" class="comment-tools"></div><div class="clear"></div><div id="comment-18750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23323"></span>

<div id="answer-container-23323" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23323-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's possibl that you said "No" to the prompt "start WinPcap driver at boot time." So try restarting the driver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/d1513cba2c4ca7df28c2673ad9827904?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kucf%20Uoy&#39;s gravatar image" /><p>Kucf Uoy<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kucf Uoy has no accepted answers">0%</span></p></div></div><div id="comments-container-23323" class="comments-container"></div><div id="comment-tools-23323" class="comment-tools"></div><div class="clear"></div><div id="comment-23323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4845"></span>

<div id="answer-container-4845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4845-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you refer to the <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">CapturePrivileges</a> wiki page, I think you will find the help you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '11, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4845" class="comments-container"><span id="10969"></span><div id="comment-10969" class="comment"><div id="post-10969-score" class="comment-score"></div><div class="comment-text"><p>same problem. this wiki page didn't help. any other sugestions? I'm thinking I have to uninstall and re-install wireshark just to get it working.</p></div><div id="comment-10969-info" class="comment-info"><span class="comment-age">(14 May '12, 11:14)</span> desert_dweller5</div></div><span id="10970"></span><div id="comment-10970" class="comment"><div id="post-10970-score" class="comment-score"></div><div class="comment-text"><p>Although WinPCap is distributed along with Wireshark, it's actually a separate project. You could try un-installing and re-installing WinPCap.</p></div><div id="comment-10970-info" class="comment-info"><span class="comment-age">(14 May '12, 12:51)</span> grahamb ♦</div></div></div><div id="comment-tools-4845" class="comment-tools"></div><div class="clear"></div><div id="comment-4845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41069"></span>

<div id="answer-container-41069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41069-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I used to always unclick for 'pcap to run at startup' and it was not an issue. With the latest version I installed, it seems it does not install pcap if you choose that. To workaround, I just reinstalled Wireshark and selected to run at startup. I guess you could also run manually install pcap from <a href="https://www.winpcap.org">https://www.winpcap.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '15, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/8ef39d8f8ed0b50b04abf0502efda63a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyDazed&#39;s gravatar image" /><p>CrazyDazed<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyDazed has no accepted answers">0%</span></p></div></div><div id="comments-container-41069" class="comments-container"></div><div id="comment-tools-41069" class="comment-tools"></div><div class="clear"></div><div id="comment-41069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60869"></span>

<div id="answer-container-60869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60869-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>open the Setup once the setup gives the Error open CMD as Administrator and type net stop npf now klik on retry it will continue then again in CMD type net start npf and wireshark will work fine</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '17, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/6511a86b41fdbd81d259b0e739cbdc98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mathias1xxX&#39;s gravatar image" /><p>mathias1xxX<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mathias1xxX has no accepted answers">0%</span></p></div></div><div id="comments-container-60869" class="comments-container"></div><div id="comment-tools-60869" class="comment-tools"></div><div class="clear"></div><div id="comment-60869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

