+++
type = "question"
title = "Quick Question.  Need help monitor mobile devices connect to my network"
description = '''Hello, I have a situation that I have to research. The short story is my niece has had to come stay with us after getting into trouble numerous times. My wife decided to give her a cell phone. Against my better judgement, we did and now I need to monitor her while she is under my roof. In reading th...'''
date = "2013-03-21T08:06:00Z"
lastmod = "2013-03-21T08:19:00Z"
weight = 19709
keywords = [ "msn", "wifi", "monitoring", "yahoo-messenger", "cellphone" ]
aliases = [ "/questions/19709" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Quick Question. Need help monitor mobile devices connect to my network](/questions/19709/quick-question-need-help-monitor-mobile-devices-connect-to-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a situation that I have to research. The short story is my niece has had to come stay with us after getting into trouble numerous times. My wife decided to give her a cell phone. Against my better judgement, we did and now I need to monitor her while she is under my roof. In reading thru your website I saw that Wireshark has the capabilities to track wireless devices that communicate with the network. My question is, can I monitor her yahoo/msn messenger conversations using your software? I have already informed her that I will be monitoring her SMS messages remotely using monitoring software. However she is very smart for a teenager and she cranked up her activity on yahoo and MSN and not used her SMS at all recently. Found the loophole I guess. So I need to target her chat platforms now because she deletes every conversation after she finishes her chats.</p><p>So I'm on windows 7, use Verizon Fios for my internet, everyone in the house connects to the same network for WiFi, and I have all of the cell phone information, i.e. IP address. Can someone please help me get started on what needs to go into the setup for Wireshark if its possible. I'm a web developer so I'm pretty computer savvy, just not in the networking arena. I'm still going thru your documentation but wow, a lot of that is clearly over my head. Thanks in advance.</p><p>Concerned Uncle</p></div><div id="question-tags" class="tags-container tags">msn wifi monitoring yahoo-messenger cellphone</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/2e0b6c8d5e23aaf044c9111ed854a20e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tigercane&#39;s gravatar image" /><p>Tigercane<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tigercane has no accepted answers">0%</span></p></div></div><div id="comments-container-19709" class="comments-container"></div><div id="comment-tools-19709" class="comment-tools"></div><div class="clear"></div><div id="comment-19709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19710"></span>

<div id="answer-container-19710" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19710-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to monitor what's going out onto the internet you need to find a way to either capture data at the router (if it allows to do that, it needs to have a monitoring option for this), or you can capture wireless traffic using an <a href="http://www.riverbed.com/de/products/cascade/wireshark_enhancements/airpcap.php">AirPCAP</a> adapter (at least if you want to capture wireless data using a Windows PC). In the latter case you'll need to decrypt the packets since I guess your AP is encrypted - at least I hope it is.</p><p>Don't get your hopes up though... Yahoo, MSN etc do encrypt their protocols nowadays in most cases, so even if you manage to capture the packets you'll only see the encrypted stuff. There is no way of reading anything unless you can break the application encryption, which I doubt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19710" class="comments-container"><span id="19713"></span><div id="comment-19713" class="comment"><div id="post-19713-score" class="comment-score"></div><div class="comment-text"><p>[Updated] The comments field would not let me type enough to fit in that area so I posted this under answer. Sorry for that.</p><p>Jasper, first and foremost, thanks for the speedy reply. I guess I was misinformed from the article that I read on Wi-Fi Eavesdropping which you can refer to here:<br />
</p><p><a href="http://www.nowiressecurity.com/articles/wi-fi_eavesdroppers_hackers_see_unsecured_open_wireless_network.htm">http://www.nowiressecurity.com/articles/wi-fi_eavesdroppers_hackers_see_unsecured_open_wireless_network.htm</a></p><p>It talks about what can be access from unsecured wireless networks. So I made the assumption that if someone with no direct access to your home and hardware could pull information directly from your wireless network, the premise of that idea could also work for what I was trying to do. The article actually uses your application and took a screen shot of an intercepted yahoo message captured over the network.</p><p>Is that they are doing there different that what Wireshark is intended to do? The protocol that was used to capture the Yahoo message was listed as "ARP". Not sure if that helps. Again thanks for all of your help! Its very much appreciated.</p></div><div id="comment-19713-info" class="comment-info"><span class="comment-age">(21 Mar '13, 09:05)</span> Tigercane</div></div><span id="19714"></span><div id="comment-19714" class="comment"><div id="post-19714-score" class="comment-score"></div><div class="comment-text"><p>[I converted your answer for you]</p><p>Okay, that article is talking about <strong>unencrypted</strong> networks, which I hope you don't run at home - WPA/WPA2 encryption is mandatory nowadays in my opinion ;-)</p><p>Basically, it is a question of what you niece is doing. If she is using unencrypted application protocols you can capture and read what she is doing, maybe with the minor obstacle of having to decrypt your own WiFi packets first.</p><p>ARP has nothing to do with it, it is a protocol for address resolution and sometimes used in attacks to capture packets that you'd normally not get.</p></div><div id="comment-19714-info" class="comment-info"><span class="comment-age">(21 Mar '13, 09:27)</span> Jasper ♦♦</div></div><span id="19715"></span><div id="comment-19715" class="comment"><div id="post-19715-score" class="comment-score"></div><div class="comment-text"><p>Ahh Ok. Yes my network is encrypted so I assumed inside of it, I could bypass all of that can be able to see the info that is getting posted to the router to go out into the wild. I will have to check to see if my router allows for monitor capturing. I suppose I could load up Linux as a dual boot on my laptop but if the packets I get from the chat programs are also encrypted, I suppose it will not be of much help.</p></div><div id="comment-19715-info" class="comment-info"><span class="comment-age">(21 Mar '13, 09:32)</span> Tigercane</div></div></div><div id="comment-tools-19710" class="comment-tools"></div><div class="clear"></div><div id="comment-19710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

