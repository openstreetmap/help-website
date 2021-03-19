+++
type = "question"
title = "usbmon captures"
description = '''I captured usb traces using usbmon and got a raw ascii format as output. When I try to open (to analyze) the captures using wireshark, I get an error msg like &quot;The file isn&#x27;t a capture file in a format wireshark understands&quot;.'''
date = "2011-03-14T08:10:00Z"
lastmod = "2011-03-14T11:13:00Z"
weight = 2801
keywords = [ "usb", "usbmon" ]
aliases = [ "/questions/2801" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [usbmon captures](/questions/2801/usbmon-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2801-score" class="post-score" title="current number of votes">0</div><span id="post-2801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured usb traces using usbmon and got a raw ascii format as output. When I try to open (to analyze) the captures using wireshark, I get an error msg like "The file isn't a capture file in a format wireshark understands".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-usbmon" rel="tag" title="see questions tagged &#39;usbmon&#39;">usbmon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '11, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/40673f56786aa248ab0a2c62374ac270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishom&#39;s gravatar image" /><p><span>kishom</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishom has no accepted answers">0%</span></p></div></div><div id="comments-container-2801" class="comments-container"><span id="2802"></span><div id="comment-2802" class="comment"><div id="post-2802-score" class="comment-score"></div><div class="comment-text"><p>I don't know the answer to your question; however http://wiki.wireshark.org/CaptureSetup/USB may be of help</p></div><div id="comment-2802-info" class="comment-info"><span class="comment-age">(14 Mar '11, 08:35)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-2801" class="comment-tools"></div><div class="clear"></div><div id="comment-2801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2803"></span>

<div id="answer-container-2803" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2803-score" class="post-score" title="current number of votes">1</div><span id="post-2803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On my system, I do this:</p><pre><code>modprobe usbmon
mount -t usbfs /dev/bus/usb /proc/bus/usb</code></pre><p>After that, run "<code>tshark -D</code>" to list all the interfaces. You should see the <code>usbmonX</code> interfaces listed. You'll need to figure out which one is applicable to your device, but that shouldn't be too hard if you run "<code>cat /proc/bus/usb/devices</code>".</p><p>For example, if your device shows up as "<code>Bus=04</code>", then you need to capture using "<code>tshark -i usbmon4</code>". And of course, if you want to save the packets to a <code>.pcap</code> file, then you also need to specify "<code>-w outfile</code>".</p><p>You might also take a look at: <a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '11, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2803" class="comments-container"></div><div id="comment-tools-2803" class="comment-tools"></div><div class="clear"></div><div id="comment-2803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2806"></span>

<div id="answer-container-2806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2806-score" class="post-score" title="current number of votes">1</div><span id="post-2806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The usbmon mechanism has several different modes - there's a pure-text mode, which, from "I captured usb traces using usbmon and got a raw ascii format as output.", I assume you used, and there's also a binary mode.</p><p>Wireshark doesn't support directly reading the text files generated by the text mode of usbmon. What it <em>does</em> support is the mechanism in libpcap that uses usbmon to capture on USB; that's what Chris Maynard (cmaynard) described. If you have libpcap 1.1.0 or later ("tshark -v", "wireshark -v", or the "About" item in the "Help" menu for Wireshark, should indicate what version of libpcap you have), you should be able to directly capture on USB with Wireshark or TShark. You can also capture with recent versions of tcpdump and have Wireshark read those captures (tcpdump can also read them, although its ability to dissect them is currently limited).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '11, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2806" class="comments-container"></div><div id="comment-tools-2806" class="comment-tools"></div><div class="clear"></div><div id="comment-2806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

