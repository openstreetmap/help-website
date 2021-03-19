+++
type = "question"
title = "wireshark shows desktop packets but not laptop packets"
description = '''Ok. I installed wireshark on my desktop unit. All good. I enter the WEP key into wireshark for decryption. I click on start. It shows packets - cool. Using internet explorer, I go to yahoo.com. Wireshark shows I went to yahoo.com. Pretty neat. Ok, I get on my laptop which connects to the wireless ro...'''
date = "2012-08-12T22:44:00Z"
lastmod = "2012-08-20T18:40:00Z"
weight = 13570
keywords = [ "windows", "no", "packets", "wireshark" ]
aliases = [ "/questions/13570" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark shows desktop packets but not laptop packets](/questions/13570/wireshark-shows-desktop-packets-but-not-laptop-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13570-score" class="post-score" title="current number of votes">0</div><span id="post-13570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok. I installed wireshark on my desktop unit. All good. I enter the WEP key into wireshark for decryption. I click on start. It shows packets - cool. Using internet explorer, I go to <a href="http://yahoo.com">yahoo.com</a>. Wireshark shows I went to <a href="http://yahoo.com">yahoo.com</a>. Pretty neat. Ok, I get on my laptop which connects to the wireless router (which, of course, is connected to the desktop). I go to <a href="http://yahoo.com">yahoo.com</a>. It doesn't show up in wireshark. I search for "yahoo" in the packets but nothing there. Shows up easily when I do the same thing on the desktop. So what gives? It is "wire" shark - shouldn't it show all the packets going through the wireless router? Sepcs: desktop is windows xp sp3. Wireless router is Verizon FIOS Actiontec modem/router. Laptop is windows 7 32 bit. Internet explorer is browser for both. Thanks. Larry</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '12, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/4b218a3e91eb3cd9a446b755c4e4f305?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Larry&#39;s gravatar image" /><p><span>Larry</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Larry has no accepted answers">0%</span></p></div></div><div id="comments-container-13570" class="comments-container"></div><div id="comment-tools-13570" class="comment-tools"></div><div class="clear"></div><div id="comment-13570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13572"></span>

<div id="answer-container-13572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13572-score" class="post-score" title="current number of votes">4</div><span id="post-13572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>("Wire" in Wireshark is somewhat historical, given that it handles various wireless protocols and given that the capture mechanisms used by libpcap support Wi-Fi - WinPcap, not so much, as it doesn't support NDIS 6 and thus doesn't support Native Wi-Fi monitor mode.)</p><p>The data sheets I could find on Actiontec's Web site for fiber modems whose descriptions include FIOS are:</p><ol><li><a href="http://www.actiontec.com/products/datasheets/VrznMI424WRrevI_dtsht_Verzn%20brnded.pdf">the datasheet for the MI424WR GigE</a>;</li><li><a href="http://www.actiontec.com/products/datasheets/MI424WR%20Verizon%20FiOS%20Router%20Datasheet.pdf">the datasheet for the MI424WR Rev. E</a>.</li></ol><p>They appear to support two types of WAN connection - Ethernet and <a href="http://en.wikipedia.org/wiki/Multimedia_over_Coax_Alliance">MoCA</a>. If you connect to FIOS via MoCA (the coax port), there might not be a way to plug Wireshark into the wireless router to see all traffic going to or from the Internet through the router; if you connect to FIOS via the Ethernet port, you might be able to interpose <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_an_Ethernet_hub">a hub</a> (not a switch that's called a hub, but a real <em>hub</em>) or <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_network_tap">a network tap</a> to capture traffic going over that Ethernet link. I didn't find anything in the documentation on the Actiontec site to indicate that they support "<a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">port mirroring</a>" (under whatever name), so that doesn't appear to be an option.</p><p>If you want to capture all the traffic on your <em>wireless</em> network, rather than on the <em>wired</em> connection from the wireless router to the Ethernet, you will need to capture on a wireless interface in monitor mode or perhaps promiscuous mode. Unfortunately, WinPcap, as indicated in the parenthetical note at the beginning of my answer, does <em>not</em> support monitor mode, and Wi-Fi drivers on Windows rarely, if ever, support promiscuous mode (in fact, <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff552596(v=vs.85).aspx">NDIS 6 Native Wi-Fi drivers aren't supposed to support promiscuous mode except in monitor or access point mode!</a>), so, on Windows, you won't be able to do that with applications such as Wireshark that use WinPcap. (You could do it on Linux or *BSD or OS X.)</p><p>It works when you're running Wireshark on the machine whose traffic you're trying to capture; it doesn't work if you're running Wireshark on another machine. That's why it captures traffic going to and from your desktop (as that's where you're running Wireshark), but doesn't capture traffic going to and from your laptop if you're running it on your desktop. You'd have to run Wireshark on your laptop in order to capture traffic going to or from your laptop. (NDIS 6, and thus Native Wi-Fi monitor mode, isn't supported on Windows XP, so even if WinPcap <em>did</em> support that, it wouldn't help on your desktop. It also wouldn't, of course, work if your desktop doesn't support Wi-Fi and is connected to your router via Ethernet.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Aug '12, 01:46</strong> </span></p></div></div><div id="comments-container-13572" class="comments-container"><span id="13784"></span><div id="comment-13784" class="comment"><div id="post-13784-score" class="comment-score"></div><div class="comment-text"><p>Thank you much.</p></div><div id="comment-13784-info" class="comment-info"><span class="comment-age">(20 Aug '12, 18:40)</span> <span class="comment-user userinfo">Larry</span></div></div></div><div id="comment-tools-13572" class="comment-tools"></div><div class="clear"></div><div id="comment-13572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13571"></span>

<div id="answer-container-13571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13571-score" class="post-score" title="current number of votes">2</div><span id="post-13571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If both PC and laptop are connecting to the router over WLAN and you have a capture device that can capture all Wireless frames you should see all the traffic.</p><p>I guess in your case either one system is connected to the router via cable, which would lead to only the router getting the packets (and not forwarding it to any other client), and so you can't capture what others do. Or you DO have both systems using WLAN but you don't have a Airpcap capture card that would allow you to see all frames when running Wireshark on Windows. Without an Airpcap adapter you're pretty limited in what you can capture on Windows, which means mostly your own packets. Even the 802.11 radio layer will be missing.</p><p>You can either buy an Airpcap adapter, or try using Linux, which would allow you to run the adapter in monitor mode (which isn't possible on Windows, except with Airpcap adapters).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13571" class="comments-container"><span id="13785"></span><div id="comment-13785" class="comment"><div id="post-13785-score" class="comment-score"></div><div class="comment-text"><p>Thank you much.</p></div><div id="comment-13785-info" class="comment-info"><span class="comment-age">(20 Aug '12, 18:40)</span> <span class="comment-user userinfo">Larry</span></div></div></div><div id="comment-tools-13571" class="comment-tools"></div><div class="clear"></div><div id="comment-13571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

