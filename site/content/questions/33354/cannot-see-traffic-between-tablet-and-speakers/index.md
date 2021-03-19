+++
type = "question"
title = "Cannot see traffic between tablet and speakers"
description = '''Hi - I&#x27;m trying to figure what HTTP commands are being sent to my IP speakers. I&#x27;ve got most of what I want using firefox inspector on my laptop and the &#x27;airstudio&#x27; site on(?) my speakers. For instance the command for speakers to pickup auxillary jack is GET,http://192.168.1.82:8889/aux. The command...'''
date = "2014-06-03T12:44:00Z"
lastmod = "2014-06-07T13:55:00Z"
weight = 33354
keywords = [ "ip", "wifi", "http", "capture-filter", "get" ]
aliases = [ "/questions/33354" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see traffic between tablet and speakers](/questions/33354/cannot-see-traffic-between-tablet-and-speakers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33354-score" class="post-score" title="current number of votes">0</div><span id="post-33354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi - I'm trying to figure what HTTP commands are being sent to my IP speakers. I've got most of what I want using firefox inspector on my laptop and the 'airstudio' site on(?) my speakers. For instance the command for speakers to pickup auxillary jack is GET,<a href="http://192.168.1.82:8889/aux.">http://192.168.1.82:8889/aux.</a> The command I cant capture is volume up/down. I cant send volume up/down from my laptop as the UI only has a slider control and only captures an absolute value (that looks like this GET,<a href="http://192.168.1.82:8889/VOLUME$VAL$64).">http://192.168.1.82:8889/VOLUME$VAL$64).</a> What I want is the command that gets sent when using phone/tablet volume control as these both have physical volume buttons that the speakers respond to. The speakers are on 192.168.1.82 and the tablet on 192.168.1.126 which i've confirmed on router page. So I fired up Wireshark and pointed it at SpezzaNet wifi. Then I added this filter; "ip.src==192.168.1.126 AND ip.dst==192.168.1.82". Then Wireshark goes all quiet. Clearly I've got something wrong but not sure what. Help appreciated! :-/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '14, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/9a1733de0f509235a08ee51f1e2c68c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spezzer&#39;s gravatar image" /><p><span>spezzer</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spezzer has no accepted answers">0%</span></p></div></div><div id="comments-container-33354" class="comments-container"><span id="33357"></span><div id="comment-33357" class="comment"><div id="post-33357-score" class="comment-score"></div><div class="comment-text"><p>what is your</p><ul><li>OS and OS version?</li><li>Wireshark version?</li><li>wlan/wifi interface on the capturing system?</li><li>did you enable monitor mode on the wlan interface?</li></ul></div><div id="comment-33357-info" class="comment-info"><span class="comment-age">(03 Jun '14, 14:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33398"></span><div id="comment-33398" class="comment"><div id="post-33398-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>OS: Windows 7 HOme Premium SP1 WS: Version 1.10.5 (SVN Rev 54262 from /trunk-1.10) Wifi: 802.11b/g/n Enabled: Not sure - dont seem to have an option on Router or am I looking in wrong place? Would that be relevant when sniffing wifi?</p><p>Also - I can see loads of other traffic. I have to admit though an awful lot of it is on .71 which is my laptop where I'm running WS.</p></div><div id="comment-33398-info" class="comment-info"><span class="comment-age">(04 Jun '14, 11:04)</span> <span class="comment-user userinfo">spezzer</span></div></div></div><div id="comment-tools-33354" class="comment-tools"></div><div class="clear"></div><div id="comment-33354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33465"></span>

<div id="answer-container-33465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33465-score" class="post-score" title="current number of votes">0</div><span id="post-33465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>OS: Windows 7 HOme Premium</p></blockquote><p>O.K. you <strong>cannot</strong> use Wireshark to capture wifi/wlan traffic on Windows in <strong>monitor mode</strong> (meaning: capture traffic of other wlan/wifi clients), <strong>as WinPcap</strong> (the capturing subsystem) <strong>does not support monitor mode on Windows</strong>.</p><p>Your options are:</p><ul><li>buy an Airpcap adapter (please google it)</li><li>use a different (commercial) sniffer on Windows that supports monitor mode (please google it)</li><li>do the wlan/wifi capturing on Linux, e.g. Kali Linux (please google it)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '14, 12:52</strong> </span></p></div></div><div id="comments-container-33465" class="comments-container"><span id="33537"></span><div id="comment-33537" class="comment"><div id="post-33537-score" class="comment-score"></div><div class="comment-text"><p>Hi - Airpcap is a pricey piece of kit - so does a commercial sniffer by the sound of it. I've got a spare drive in a desktop I can use for a Linux boot - are you saying that there is a version of WS that will run on Linux and give me the results I'm looking for?</p></div><div id="comment-33537-info" class="comment-info"><span class="comment-age">(07 Jun '14, 03:09)</span> <span class="comment-user userinfo">spezzer</span></div></div><span id="33539"></span><div id="comment-33539" class="comment"><div id="post-33539-score" class="comment-score"></div><div class="comment-text"><p>As I said: Kali Linux. You can boot it from a cdrom or flash drive.</p></div><div id="comment-33539-info" class="comment-info"><span class="comment-age">(07 Jun '14, 13:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33465" class="comment-tools"></div><div class="clear"></div><div id="comment-33465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33493"></span>

<div id="answer-container-33493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33493-score" class="post-score" title="current number of votes">0</div><span id="post-33493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Other options are: - Enable routing on the capture system and use ARP spoofing. - Wire the capture system into the path (requires two interfaces) and configure it as a bridge.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '14, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/4cf9d0b9f5d61826525247bd5b79cdc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TimB&#39;s gravatar image" /><p><span>TimB</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TimB has no accepted answers">0%</span></p></div></div><div id="comments-container-33493" class="comments-container"><span id="33538"></span><div id="comment-33538" class="comment"><div id="post-33538-score" class="comment-score"></div><div class="comment-text"><p>thanks TimB but sounds a little beyond my capabilities!</p></div><div id="comment-33538-info" class="comment-info"><span class="comment-age">(07 Jun '14, 03:10)</span> <span class="comment-user userinfo">spezzer</span></div></div></div><div id="comment-tools-33493" class="comment-tools"></div><div class="clear"></div><div id="comment-33493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

