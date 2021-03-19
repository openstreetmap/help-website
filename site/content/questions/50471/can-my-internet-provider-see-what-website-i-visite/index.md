+++
type = "question"
title = "Can my internet provider see what website i visite?"
description = '''Hello I use google dns and openvpn. While I use wireshar to check my internet trafik I saw domain name of website which I visited. Example in this image I visit opendns website. Can my internet provider look this domain too? http://postimg.org/image/94knapjn3/'''
date = "2016-02-24T07:56:00Z"
lastmod = "2016-02-25T13:52:00Z"
weight = 50471
keywords = [ "dns" ]
aliases = [ "/questions/50471" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can my internet provider see what website i visite?](/questions/50471/can-my-internet-provider-see-what-website-i-visite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50471-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I use google dns and openvpn. While I use wireshar to check my internet trafik I saw domain name of website which I visited. Example in this image I visit opendns website. Can my internet provider look this domain too?</p><p><a href="http://postimg.org/image/94knapjn3/">http://postimg.org/image/94knapjn3/</a></p></div><div id="question-tags" class="tags-container tags">dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/78c5abff0870f3c59bd7354a69b8782a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hidemyip&#39;s gravatar image" /><p>hidemyip<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hidemyip has no accepted answers">0%</span></p></div></div><div id="comments-container-50471" class="comments-container"></div><div id="comment-tools-50471" class="comment-tools"></div><div class="clear"></div><div id="comment-50471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="50473"></span>

<div id="answer-container-50473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50473-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably.</p><p>At the capture point (your local PC or laptop) the DNS requests are sent as clear traffic. They may be encrypted by your local router\modem, in which case the ISP won't be able to see DNS requests, but only you can tell if you have that setup in place.</p><p>If you want the local DNS traffic to be encrypted by openvpn, then you'll need to set the appropriate config options for that which <strong>isn't</strong> a suitable topic for Ask Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '16, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50473" class="comments-container"><span id="50525"></span><div id="comment-50525" class="comment"><div id="post-50525-score" class="comment-score"></div><div class="comment-text"><p>Note that this is a topic that has come up as a concern at the IETF which since formed a <a href="https://datatracker.ietf.org/wg/dprive/charter/">working group</a> to look at ways to improve DNS privacy.</p></div><div id="comment-50525-info" class="comment-info"><span class="comment-age">(25 Feb '16, 16:58)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50473" class="comment-tools"></div><div class="clear"></div><div id="comment-50473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50515"></span>

<div id="answer-container-50515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50515-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://askleo.com/can_my_isp_monitor_my_internet_usage/">https://askleo.com/can_my_isp_monitor_my_internet_usage/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-50515" class="comments-container"></div><div id="comment-tools-50515" class="comment-tools"></div><div class="clear"></div><div id="comment-50515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50514"></span>

<div id="answer-container-50514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50514-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. You probably can even get a copy of the sites you've visited from your provider, but it may cost you. I know some isp(s) if the noticed that you've got a ton of traffic coming from your network with respond back usually via postal mail that you've been pulling x amount of data from x.x.x.x . But sitting around watch what sites you go to no, there isn't enough time in the day or employees to actively monitor everyone that's subscribed to any particular isp. But yeah they could if they wanted. It's there equipment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-50514" class="comments-container"></div><div id="comment-tools-50514" class="comment-tools"></div><div class="clear"></div><div id="comment-50514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

