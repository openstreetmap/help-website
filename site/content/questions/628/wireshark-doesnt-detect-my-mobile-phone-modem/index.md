+++
type = "question"
title = "Wireshark doesn&#x27;t detect my mobile phone modem"
description = '''Hi! I&#x27;ve downloaded the latest version of WireShark but I have a problem. I&#x27;m using my phone (Nokia N85) as modem for my pc and WireShark doesen&#x27;t detect it as a modem or anything. Can you help me with a solution or some settings? I&#x27;m using Windows 7. Thank you! '''
date = "2010-10-25T13:10:00Z"
lastmod = "2012-10-25T07:58:00Z"
weight = 628
keywords = [ "nokia", "usb", "modem" ]
aliases = [ "/questions/628" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark doesn't detect my mobile phone modem](/questions/628/wireshark-doesnt-detect-my-mobile-phone-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-628-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I've downloaded the latest version of WireShark but I have a problem. I'm using my phone (Nokia N85) as modem for my pc and WireShark doesen't detect it as a modem or anything. Can you help me with a solution or some settings? I'm using Windows 7. Thank you!</p></div><div id="question-tags" class="tags-container tags">nokia usb modem</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/c46dc71574c269b044bfd368c0f6775b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="last1devil&#39;s gravatar image" /><p>last1devil<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="last1devil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Oct '12, 13:12</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-628" class="comments-container"><span id="658"></span><div id="comment-658" class="comment"><div id="post-658-score" class="comment-score"></div><div class="comment-text"><p>Check out http://wiki.wireshark.org/CaptureSetup. There's a section on troubleshooting.</p><p>If Wireshark doesn't list the interface, then you can't capture on it. I've got two phones that can be set up as modems, but the interfaces are not recognized.</p><p>Question: What do you want to do? Are you trying to capture WLAN traffic to/from your phone or something else?</p></div><div id="comment-658-info" class="comment-info"><span class="comment-age">(26 Oct '10, 08:59)</span> lchappell ♦</div></div></div><div id="comment-tools-628" class="comment-tools"></div><div class="clear"></div><div id="comment-628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="713"></span>

<div id="answer-container-713" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-713-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is with WinPcap, and it affects Wireshark only because Wireshark uses WinPcap to capture traffic on Windows (just as it uses the UN*X library on which the userland part of WinPcap is based, libpcap, on UN*X). That means that a program that <em>does</em> see your mobile phone modem on Windows 7 will have to be a program that <em>doesn't</em> use WinPcap, but uses something else.</p><p>One such program is <a href="http://blogs.technet.com/b/netmon/">Microsoft's Network Monitor</a>; see the links under "Install Network Monitor" to download it for 32-bit x86 Windows, 64-bit x86 Windows, or IA-64 Windows. It's free (in the sense of "it doesn't cost any money"; the source isn't available, but the protocols are described by text files, and you <em>do</em> get the description files with it). I don't know whether it'll see your phone modem or not, but at least it won't cost you any money to find out.</p><p>Some non-free (in the sense of "they cost money") network analyzers for Windows are <a href="http://www.wildpackets.com/products/portable_analysis/omnipeek_software">OmniPeek from WildPackets</a>, <a href="http://www.tamos.com/products/commview/">CommView from TamoSoft</a>, <a href="http://www.javvin.com/packet.html">Network Packet Analyzer CAPSA from Javvin</a>, and <a href="http://www.netscout.com/products/enterprise/Sniffer_Portable_Analyzer/Sniffer_Portable_Professional_Analyzer/Pages/default.aspx">Sniffer Portable from NetScout</a>. I infer from the page for CommView that it will probably see your phone modem (it referred to dial-up adapters); I don't know whether the others will.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '11, 22:24</p></div></div><div id="comments-container-713" class="comments-container"><span id="721"></span><div id="comment-721" class="comment"><div id="post-721-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I've downloaded Microsoft Network Monitor 3.4 and it works.</p></div><div id="comment-721-info" class="comment-info"><span class="comment-age">(28 Oct '10, 06:21)</span> last1devil</div></div></div><div id="comment-tools-713" class="comment-tools"></div><div class="clear"></div><div id="comment-713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="685"></span>

<div id="answer-container-685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-685-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your phone probably appears as a PPP connection on your PC. According to <a href="http://www.winpcap.org/misc/faq.htm#Q-5">question Q-5 in the WinPcap FAQ</a>, on "Windows Vista and more recent" (which includes Windows 7), "It's <em>not</em> possible to capture on PPP/VPN connections".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-685" class="comments-container"><span id="665"></span><div id="comment-665" class="comment"><div id="post-665-score" class="comment-score"></div><div class="comment-text"><p>I just want to capture the taffic between a program from my computer and a web server. Thank you for your answer!</p></div><div id="comment-665-info" class="comment-info"><span class="comment-age">(26 Oct '10, 09:20)</span> last1devil</div></div><span id="668"></span><div id="comment-668" class="comment"><div id="post-668-score" class="comment-score"></div><div class="comment-text"><p>Yeah - you're likely not going to get very far on that interface. Sigh. Maybe someone else with a Nokia will pipe up here.</p></div><div id="comment-668-info" class="comment-info"><span class="comment-age">(26 Oct '10, 09:36)</span> lchappell ♦</div></div><span id="708"></span><div id="comment-708" class="comment"><div id="post-708-score" class="comment-score"></div><div class="comment-text"><p>Ok! Thank you! Do you know other program like WireShark that may work on Windows 7 ?</p></div><div id="comment-708-info" class="comment-info"><span class="comment-age">(27 Oct '10, 12:03)</span> last1devil</div></div></div><div id="comment-tools-685" class="comment-tools"></div><div class="clear"></div><div id="comment-685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15281"></span>

<div id="answer-container-15281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15281-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible to capture with Microsoft Network Monitor 3.4. Then save the file and open it with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '12, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/3f05e71bb562c795ffaebe3efedec208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giegala&#39;s gravatar image" /><p>giegala<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giegala has no accepted answers">0%</span></p></div></div><div id="comments-container-15281" class="comments-container"></div><div id="comment-tools-15281" class="comment-tools"></div><div class="clear"></div><div id="comment-15281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

