+++
type = "question"
title = "Unable to capture SOAP response"
description = '''Hi everyone, I am having an issue trying to capture the incoming message from my webservice. The situation is as follows: 1) We have a portable device used for sending and receiving SOAP messages from our webservice. We are trying to capture the messages sent back and forth. 2) We set up a test conf...'''
date = "2012-03-05T18:25:00Z"
lastmod = "2012-03-07T18:07:00Z"
weight = 9375
keywords = [ "xml", "soap", "webservice" ]
aliases = [ "/questions/9375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to capture SOAP response](/questions/9375/unable-to-capture-soap-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9375-score" class="post-score" title="current number of votes">0</div><span id="post-9375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, I am having an issue trying to capture the incoming message from my webservice.</p><p>The situation is as follows:</p><p>1) We have a portable device used for sending and receiving SOAP messages from our webservice. We are trying to capture the messages sent back and forth.</p><p>2) We set up a test configuration where the device will connect via wifi to a laptop (set to Access Point mode using Connectify) that is connected to the Internet using an Ethernet cable. The laptop's running on Windows 7.</p><p>3) We run Wireshark 1.6.5 to capture in promiscuous mode, with capture filter set to "tcp port http"</p><p>4) Capture begins and we make the device send the request message to the webservice. The webservice sends a response and the device received the response.</p><p>5) We ended the capture and viewed the http/xml protocol packets, selecting "Follow TCP stream".</p><p>6) What we get are all outgoing capture and no incoming packets being captured. There should be some data being captured but there is none!</p><p>What could be the issue here? Thank you and hope for some direction on how to proceed from here, thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span> <span class="post-tag tag-link-webservice" rel="tag" title="see questions tagged &#39;webservice&#39;">webservice</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/92e1faef1b8e6cef6a5b102b0361831c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tkuan&#39;s gravatar image" /><p><span>Tkuan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tkuan has no accepted answers">0%</span></p></div></div><div id="comments-container-9375" class="comments-container"><span id="9377"></span><div id="comment-9377" class="comment"><div id="post-9377-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We set up a test configuration where the device will connect via wifi to a laptop (set to Access Point mode using Connectify) that is connected to the Internet using an Ethernet cable. The laptop's running on Windows 7.</p></blockquote><p>So the laptop is acting as a router between a Wi-FI network and the Ethernet that goes to your Internet access device?</p><blockquote><p>We run Wireshark 1.6.5 to capture in promiscuous mode, with capture filter set to "tcp port http"</p></blockquote><p>Are you capturing on the laptop's Wi-Fi interface or on its Ethernet interface?</p></div><div id="comment-9377-info" class="comment-info"><span class="comment-age">(05 Mar '12, 19:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9378"></span><div id="comment-9378" class="comment"><div id="post-9378-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, the laptop is now acting as an access point with a SSID. The device connects to the laptop with the correct SSID and key set up.</p><p>The laptop needs a separate internet connection, thus the Ethernet acts in this capacity.</p><p>Capturing on the Ethernet interface.</p></div><div id="comment-9378-info" class="comment-info"><span class="comment-age">(05 Mar '12, 19:36)</span> <span class="comment-user userinfo">Tkuan</span></div></div><span id="9379"></span><div id="comment-9379" class="comment"><div id="post-9379-score" class="comment-score"></div><div class="comment-text"><p>I.e., the portable device's SOAP requests to your Web service are going from the portable device to the laptop, which then forwards them to your Web service by sending them over the Ethernet interface onto the Internet?</p></div><div id="comment-9379-info" class="comment-info"><span class="comment-age">(05 Mar '12, 19:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9381"></span><div id="comment-9381" class="comment"><div id="post-9381-score" class="comment-score"></div><div class="comment-text"><p>There is no forwarding done, the laptop's treated invisibly in this case.</p><p>Something to add, when I do a direct HTTP post to the webservice using my browser on my laptop, I was able to capture both outgoing and incoming packets. Strange.</p></div><div id="comment-9381-info" class="comment-info"><span class="comment-age">(05 Mar '12, 20:06)</span> <span class="comment-user userinfo">Tkuan</span></div></div><span id="9382"></span><div id="comment-9382" class="comment"><div id="post-9382-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>There is no forwarding done, the laptop's treated invisibly in this case.</p></blockquote><p>Unless your device is directly communicating with the Web service over Wi-Fi - i.e., if you could power down the laptop, without changing the device or the Web service's configuration, and the traffic would still flow between the device and the Web service - then there's <em>SOME</em> sort of forwarding going on inside the laptop's operating system, whether it's low-level link-layer bridging or IP-layer forwarding.</p></div><div id="comment-9382-info" class="comment-info"><span class="comment-age">(05 Mar '12, 20:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9375" class="comment-tools"></div><div class="clear"></div><div id="comment-9375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9386"></span>

<div id="answer-container-9386" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9386-score" class="post-score" title="current number of votes">0</div><span id="post-9386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tkuan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you do see traffic in WIreshark traversing from the Connectify SSID towards the Ethernet interface, but you don't see the returning traffic, that means that Connectify redirects that traffic <em>before</em> WinPcap gets the chance to capture the incoming packets. Similar things happen with some <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">VPN software</a>. You couldupdate the wiki with your experiences.</p><p>The only way to capture the traffic in your case is to ether <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">capture the wireless traffic</a> or <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">use a hub or switch</a> (with port mirroring capabilities) between your Connectify laptop and the router.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9386" class="comments-container"><span id="9423"></span><div id="comment-9423" class="comment"><div id="post-9423-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I think this is the issue here, I will find an alternative way of capturing the data.</p></div><div id="comment-9423-info" class="comment-info"><span class="comment-age">(07 Mar '12, 18:07)</span> <span class="comment-user userinfo">Tkuan</span></div></div></div><div id="comment-tools-9386" class="comment-tools"></div><div class="clear"></div><div id="comment-9386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

