+++
type = "question"
title = "Do I need airpcap on my Mac to monitor my router?"
description = '''I am trying to monitor my own network, using a Mac running OS X 10.8, as I have multiple devices that connects to my router. Do I need an airpcap to monitor my own Apple Extreme?'''
date = "2013-02-17T08:19:00Z"
lastmod = "2013-05-07T13:20:00Z"
weight = 18683
keywords = [ "airpcap" ]
aliases = [ "/questions/18683" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Do I need airpcap on my Mac to monitor my router?](/questions/18683/do-i-need-airpcap-on-my-mac-to-monitor-my-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18683-score" class="post-score" title="current number of votes">0</div><span id="post-18683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to monitor my own network, using a Mac running OS X 10.8, as I have multiple devices that connects to my router. Do I need an airpcap to monitor my own Apple Extreme?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/23c0e7f6c143323061654b97ee622480?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trungy&#39;s gravatar image" /><p><span>Trungy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trungy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '13, 16:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18683" class="comments-container"></div><div id="comment-tools-18683" class="comment-tools"></div><div class="clear"></div><div id="comment-18683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18689"></span>

<div id="answer-container-18689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18689-score" class="post-score" title="current number of votes">2</div><span id="post-18689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, you don't need AirPcap.</p><p>Your machine is running OS X, so your AirPort adapter won't be called "wlan". If your Mac has a built-in Ethernet adapter, the AirPort adapter will be called en1 (with the Ethernet interface being en0), and if your Mac doesn't have a built-in Ethernet adapter (if, for example, it's a MacBook Air or a Retina MacBook Pro), the AirPort adapter will be called en0.</p><p>AirPcap devices only work on Windows, and are only needed on Windows; Apple's AirPort adapters support monitor mode, and OS X supports putting adapters into monitor mode. In Wireshark 1.8, select Options from the Capture menu, make sure the AirPort adapter is checked in the list of interfaces, double-click it, check the "Capture packets in monitor mode" checkbox in the dialog box that pops up, click "OK", and then click "Start" in the Capture Options dialog box.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '13, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18689" class="comments-container"></div><div id="comment-tools-18689" class="comment-tools"></div><div class="clear"></div><div id="comment-18689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18684"></span>

<div id="answer-container-18684" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18684-score" class="post-score" title="current number of votes">0</div><span id="post-18684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you need to see 802.11 radio layer information (Beacon frames etc) and you are running Windows, then, yes. If you don't need to see the radio layer then your existing laptop card should be enough. If you can run an OS that has tools to allow you to put the WiFi card into monitor/promiscuous mode (for example a Linux Distribution, like Backtrack), then you also do not need Airpcap. It might be a good idea to have a capture WiFi card though, because if you're connecting to the router by WiFi yourself you cannot capture with it while using it normally (or the other way around - capture might work, but normal operation doesn't while you do it).</p><p>Take a look at this: <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X">http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '13, 10:59</strong> </span></p></div></div><div id="comments-container-18684" class="comments-container"><span id="18685"></span><div id="comment-18685" class="comment"><div id="post-18685-score" class="comment-score"></div><div class="comment-text"><p>I forgot to mention that I am running OS X 10.8. (Though I mentioned Apple Extreme.) Do I still need an airpcap?</p></div><div id="comment-18685-info" class="comment-info"><span class="comment-age">(17 Feb '13, 09:51)</span> <span class="comment-user userinfo">Trungy</span></div></div><span id="18686"></span><div id="comment-18686" class="comment"><div id="post-18686-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm not really familiar with the Apple products, I thought Apple Extreme is an Access Point, which would be connectable from any OS.</p><p>I added a link to the capture setup page to my original answer.</p></div><div id="comment-18686-info" class="comment-info"><span class="comment-age">(17 Feb '13, 10:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="18687"></span><div id="comment-18687" class="comment"><div id="post-18687-score" class="comment-score"></div><div class="comment-text"><p>First of all, thank you for your help! I have looked at that document before (as well as numerous of others), but it seems like for whatever I do, I cannot get anything resembling wlan as one of my interface options. I was hoping someone could fill me into that one final step that I might be missing. Again, thanks for your help!</p></div><div id="comment-18687-info" class="comment-info"><span class="comment-age">(17 Feb '13, 12:01)</span> <span class="comment-user userinfo">Trungy</span></div></div><span id="21008"></span><div id="comment-21008" class="comment"><div id="post-21008-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span>: an Airport Extreme might be <em>connectable-to</em> from any OS, but if you want to monitor traffic on its network, you'll need something running in monitor mode or the equivalent; on Windows, with Wireshark, you'd need an AirPcap device, but you won't need one for OS X.</p></div><div id="comment-21008-info" class="comment-info"><span class="comment-age">(07 May '13, 13:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="21009"></span><div id="comment-21009" class="comment"><div id="post-21009-score" class="comment-score"></div><div class="comment-text"><p><span>@Trungy</span>: on Leopard and later (and 10.8 is definitely later), your Wi-Fi interface (if you have one; most modern Macs do), won't be called anything with "wlan" in it, it'll be called "en1" (if you have a built-in Ethernet interface, as the built-in Ethernet interface will be "en0") or "en0" (if you have no built-in Ethernet interface, e.g. on a MacBook Air or a Retina MacBook Pro).</p></div><div id="comment-21009-info" class="comment-info"><span class="comment-age">(07 May '13, 13:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-18684" class="comment-tools"></div><div class="clear"></div><div id="comment-18684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

