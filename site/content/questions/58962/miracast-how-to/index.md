+++
type = "question"
title = "Miracast how to?"
description = '''I have Wireshark installed on my Surface Pro 4. When I try to make a miracast connection between the Surface and a MS Wireless Display Adapter, Wireshark shows no packets at all. What am I doing wrong?'''
date = "2017-01-22T23:54:00Z"
lastmod = "2017-01-25T12:58:00Z"
weight = 58962
keywords = [ "miracast" ]
aliases = [ "/questions/58962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Miracast how to?](/questions/58962/miracast-how-to)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark installed on my Surface Pro 4. When I try to make a miracast connection between the Surface and a MS Wireless Display Adapter, Wireshark shows no packets at all. What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">miracast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '17, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/9dc8b9edd0a4e0b358c3d1e87754f223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Geedsen&#39;s gravatar image" /><p>Geedsen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Geedsen has no accepted answers">0%</span></p></div></div><div id="comments-container-58962" class="comments-container"><span id="59045"></span><div id="comment-59045" class="comment"><div id="post-59045-score" class="comment-score"></div><div class="comment-text"><p>Are you able to capture WiFi traffic without performing Miracast?</p><p>Try connecting your Surface Pro 4 to a WiFi router. Start Wireshark and capture on the WiFi interface. Generate some traffic on the tablet (perform a web browse). Do you see any WiFi traffic?</p></div><div id="comment-59045-info" class="comment-info"><span class="comment-age">(25 Jan '17, 07:18)</span> Amato_C</div></div><span id="59046"></span><div id="comment-59046" class="comment"><div id="post-59046-score" class="comment-score"></div><div class="comment-text"><p>Yes, connecting to a Wifi network captures packets just fine. I know for certain that it actually is communicating between the Adapter and the Surface, I can see that on the HDTV screen. It says 'Connecting' but it fails. That is what I am trying to solve. Microsoft support was unable to help me there.</p></div><div id="comment-59046-info" class="comment-info"><span class="comment-age">(25 Jan '17, 07:56)</span> Geedsen</div></div><span id="59053"></span><div id="comment-59053" class="comment"><div id="post-59053-score" class="comment-score"></div><div class="comment-text"><p>Just to clarify - the Miracast connection is failing regardless if you are capturing with Wireshark over the WiFi interface?</p><p>I am trying to determine if the Wireshark capture is causing the Miracast failure or not.</p></div><div id="comment-59053-info" class="comment-info"><span class="comment-age">(25 Jan '17, 10:01)</span> Amato_C</div></div><span id="59061"></span><div id="comment-59061" class="comment"><div id="post-59061-score" class="comment-score"></div><div class="comment-text"><p>Yes regardless, it is/was failing even before Wireshark was installed on the surface. I installed to see if I could get some information out of the miracast communication that could help me solve the problem.</p></div><div id="comment-59061-info" class="comment-info"><span class="comment-age">(25 Jan '17, 11:38)</span> Geedsen</div></div></div><div id="comment-tools-58962" class="comment-tools"></div><div class="clear"></div><div id="comment-58962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59063"></span>

<div id="answer-container-59063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59063-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Good to hear. So now we know that Wireshark is NOT causing the failure for the 2 Miracast devices to connect. So let us do some Miracast troubleshooting. For all these suggestions, please ensure that you are NOT capturing with Wireshark. I am unsure if Wireshark capturing on the WiFi interface during a Miracast connection attempt will cause an unexpected failure.</p><ol><li>Ensure both devices (tablet and adapter) support Miracast and <strong>NOT</strong> some other display protocol (e.g., Chromecast, DLNA, etc). This might seem trivial, but a lot of proprietary protocols exist out there and they all try to use wording close to Miracast or Mirroring.</li><li>Verify what type of connection topology is used to establish the Miracast connection. The Miracast specification (called WiFi Display) allows for either P2P (Peer-to-Peer) or TDLS (Tunneled Direct Link Setup). P2P is the most common for Miracast connection and both topologies <strong>SHOULD</strong> be supported by the tablet and adapter. However, if one only supports P2P and the other only supports TDLS, then the connection will never be made. To test if TDLS is used, connect both the adapter and the tablet to the <strong>SAME</strong> WiFi network. For P2P, connecting to a WiFi network is not required.</li><li>As stated earlier, P2P is the most common topology for a Miracast connection. With P2P, an AP is not required. Therefore, verify that neither the adapter <strong>NOR</strong> the tablet is connected to any WiFi network. There are times when a busy WiFi interface could cause a Miracast connection to fail.</li><li>Try to mirror non-copyrighted material. The easiest thing to do is to try to mirror the screen of your tablet. More about copyright material in the next suggestion :)</li><li>If possible, try to change the copyright settings on your adapter. Some adapters allow you to enable or disable different settings. One of the biggest culprits for causing a Miracast connection to fail is having copyright enabled (or disabled - whichever is the default of the adapter). So if your adapter's default setting for copyright is ON, try turning it OFF.</li></ol><p>Good luck. Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '17, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-59063" class="comments-container"><span id="59075"></span><div id="comment-59075" class="comment"><div id="post-59075-score" class="comment-score"></div><div class="comment-text"><p>Thanks Amato,</p><p>1) Both devices support the Miracast adapter. They are both Microsoft products. 2 + 3) I disconnected the Surface from any network. Then I do a 'Connect' from the Surface. The HDTV then shows 'Connecting to SURFACE', so that must mean it is trying to connect using P2P. The Surface shows 'Couldn't connect' after some time while the HDTV is still showing 'Connecting to SURFACE' for a minute or so, before going back to the start screen. 4 + 5 I never get to the mirroring part. I don't get a connection.</p><p>Interesting might be that I also have a Lumia (Microsoft) 950 XL, that one has no problem connecting to the Display Adapter. Also without having a Network connection to my AP.</p></div><div id="comment-59075-info" class="comment-info"><span class="comment-age">(26 Jan '17, 00:08)</span> Geedsen</div></div><span id="59079"></span><div id="comment-59079" class="comment"><div id="post-59079-score" class="comment-score"></div><div class="comment-text"><ol><li><p>Regarding the copyright settings on the adapter: Some adapters allow the user to make changes BEFORE the Miracast connection is initiated. For example, the adapter connects to a TV. Using the TV's remote control, the user can access the adapter's setting menu and disable/enable the copyright settings (usually referred to as HDCP 2.0 or HDCP2.1).</p></li><li><p>I checked the WiFi Alliance (WFA) website and found that neither the Surface Pro 4 nor the Lumia 950 XL were certified for Miracast. Microsoft did certify other products with the WFA for Miracast, but not the 2 you mentioned. I was hoping to find either product certified by the WFA. Then that could help us. Oh well. :(</p></li><li><p>If you would like to pursue this further, my suggestion is to NOT use the Surface Pro 4 as your wireless packet capture device. Instead, you could use a laptop to capture the WiFi traffic for the attempted Miracast connection. The following link is a good starting point: <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p></li></ol></div><div id="comment-59079-info" class="comment-info"><span class="comment-age">(26 Jan '17, 06:36)</span> Amato_C</div></div></div><div id="comment-tools-59063" class="comment-tools"></div><div class="clear"></div><div id="comment-59063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

