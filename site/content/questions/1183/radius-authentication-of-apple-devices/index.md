+++
type = "question"
title = "Radius Authentication of Apple devices"
description = '''We are authenticating to radius servers with varying degrees of success. When I look at successful authentications, I frequently see Radius Protocol Malformed SSL packet. Each of these packets shows a LEN=1098 sometimes but no always failing the authentication MS-CHAP four way hand shake. Any insigh...'''
date = "2010-11-30T11:12:00Z"
lastmod = "2011-03-02T10:50:00Z"
weight = 1183
keywords = [ "radius", "apple" ]
aliases = [ "/questions/1183" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Radius Authentication of Apple devices](/questions/1183/radius-authentication-of-apple-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1183-score" class="post-score" title="current number of votes">0</div><span id="post-1183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are authenticating to radius servers with varying degrees of success. When I look at successful authentications, I frequently see Radius Protocol Malformed SSL packet. Each of these packets shows a LEN=1098 sometimes but no always failing the authentication MS-CHAP four way hand shake. Any insight is appreciated. These are Apple Ipad devices that Doctors are carrying into our Hospitals, so we're somewhat limited to capturing packets from the wireless controllers into the wired network (radius servers etc) since we cant load wireshark on the Apple devices.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-apple" rel="tag" title="see questions tagged &#39;apple&#39;">apple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/8dcd2da497394e285a5e995a8e3ab1e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swglover&#39;s gravatar image" /><p><span>swglover</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swglover has no accepted answers">0%</span></p></div></div><div id="comments-container-1183" class="comments-container"><span id="1212"></span><div id="comment-1212" class="comment"><div id="post-1212-score" class="comment-score"></div><div class="comment-text"><p>Are their any messages in the Radius server log?</p></div><div id="comment-1212-info" class="comment-info"><span class="comment-age">(02 Dec '10, 12:56)</span> <span class="comment-user userinfo">erics</span></div></div></div><div id="comment-tools-1183" class="comment-tools"></div><div class="clear"></div><div id="comment-1183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1216"></span>

<div id="answer-container-1216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1216-score" class="post-score" title="current number of votes">0</div><span id="post-1216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure you are running RADIUS from your iPads? Generally RADIUS is transported over UDP, and probably is not going to all that reliable over wireless. You might want to explain your authentication architecture more fully. (Normally I would expect to use 802.1x from your wireless device and RADIUS from the access point).</p><p>You can use a regular laptop running Wireshark to capture wireless traffic (depending on your wireless card you might need a 3rd party adapter to capture traffic promiscuously)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '10, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1216" class="comments-container"><span id="1226"></span><div id="comment-1226" class="comment"><div id="post-1226-score" class="comment-score"></div><div class="comment-text"><p>Martyvis You are entirely correct. The whole package is 802.1x PEAP Digicert certificates and 'Radiator'/Steel Belted Radius The problem with capturing is the laptop authenticates perfectly, it is only the Apple devices that are the problem</p></div><div id="comment-1226-info" class="comment-info"><span class="comment-age">(03 Dec '10, 03:45)</span> <span class="comment-user userinfo">swglover</span></div></div><span id="1235"></span><div id="comment-1235" class="comment"><div id="post-1235-score" class="comment-score"></div><div class="comment-text"><p>I am not suggesting using the laptop to authenticate, but using Wireshark on it to capture the wireless traffic to and from your iPads.</p><p>Also if you are getting RADIUS protocol issues, there won't be coming directly from your iPad, but to and from your AP on the wire. Your iPad will be using 802.1x, not RADIUS. You might find if you turn up the logging level on your AP and RADIUS servers you will get more info.</p></div><div id="comment-1235-info" class="comment-info"><span class="comment-age">(03 Dec '10, 15:09)</span> <span class="comment-user userinfo">martyvis</span></div></div><span id="2631"></span><div id="comment-2631" class="comment"><div id="post-2631-score" class="comment-score"></div><div class="comment-text"><p>Was there any progress doing this? I'm seeing the same problem at my location. I love wireshark, and it would help me if it was on the iPad, but how does one capture wireless traffic between an AP, and an Ipad on a windows running laptop? are you suggesting putting it before the AP? I believe all that is encrypted.</p></div><div id="comment-2631-info" class="comment-info"><span class="comment-age">(02 Mar '11, 07:18)</span> <span class="comment-user userinfo">jabbyjim</span></div></div><span id="2637"></span><div id="comment-2637" class="comment"><div id="post-2637-score" class="comment-score"></div><div class="comment-text"><p>We're suggesting putting the laptop's 802.11 adapter into monitor mode if it's running Linux, *BSD, or Mac OS X, or using an AirPcap adapter if it's running Windows, and giving Wireshark the password for the network. That won't work if the network is using WPA or WPA2 in enterprise mode, however; see <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki "How to Decrypt 802.11" page</a>.</p></div><div id="comment-2637-info" class="comment-info"><span class="comment-age">(02 Mar '11, 10:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1216" class="comment-tools"></div><div class="clear"></div><div id="comment-1216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

