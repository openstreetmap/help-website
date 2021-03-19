+++
type = "question"
title = "radiotap header format data rate alignment"
description = '''  hi, I have attached a trace from wireshark. Can someone tell me from where the wireshark is decoding the rate to be 26 MBps. Clicking on the rate points to an invalid location. I am unable to find the reason behind why this is happening. Why is Also, Shouldnt data rate be a 2-byte value? The reaso...'''
date = "2012-03-09T13:14:00Z"
lastmod = "2012-03-19T20:21:00Z"
weight = 9461
keywords = [ "rate", "radiotap" ]
aliases = [ "/questions/9461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [radiotap header format data rate alignment](/questions/9461/radiotap-header-format-data-rate-alignment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9461-score" class="post-score" title="current number of votes">0</div><span id="post-9461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/ws2.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws_alix.png" alt="alt text" /></p><p>hi, I have attached a trace from wireshark. Can someone tell me from where the wireshark is decoding the rate to be 26 MBps. Clicking on the rate points to an invalid location. I am unable to find the reason behind why this is happening. Why is Also, Shouldnt data rate be a 2-byte value? The reason why I am asking is wireshark generally shows rate as (2*rate because unit is in 500KBps) in the bit representation(as seen in the second image). So any rate above 128 Mbps is going to exceed one byte. From the below images, it is visible that the radio tap header format is different for the two packets. Data in the images are obtained from doing tcpdump on monitor interfaces on two machines (one from a remote machine, another from the same machine as the client on the same physical device). The driver used in this case is ath5k. When is this the case? I am pretty confused regarding this and any help will be greatly appreciated.</p><p>Thank you srini</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rate" rel="tag" title="see questions tagged &#39;rate&#39;">rate</span> <span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '12, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/2618453e9194929f291128d350b2a4ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srini_wisc&#39;s gravatar image" /><p><span>srini_wisc</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srini_wisc has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '12, 14:31</strong> </span></p></div></div><div id="comments-container-9461" class="comments-container"><span id="9569"></span><div id="comment-9569" class="comment"><div id="post-9569-score" class="comment-score"></div><div class="comment-text"><p>Does anybody have any comments on this? If the MCS information is showing the data rate, Can someone tell me how it is different from the data rate measured from the client? iwconfig shows a different data rate compare to the data rate in MCS. what does QoS data mean in the sense, does it have the actual data?</p></div><div id="comment-9569-info" class="comment-info"><span class="comment-age">(15 Mar '12, 17:53)</span> <span class="comment-user userinfo">srini_wisc</span></div></div></div><div id="comment-tools-9461" class="comment-tools"></div><div class="clear"></div><div id="comment-9461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9596"></span>

<div id="answer-container-9596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9596-score" class="post-score" title="current number of votes">2</div><span id="post-9596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you've asked several questions here.</p><blockquote><p>Can someone tell me from where the wireshark is decoding the rate to be 26 MBps. Clicking on the rate points to an invalid location.</p></blockquote><p>What do you mean by "an invalid location"? The screenshot shows an offset of 0x1A = 26; it also says the radiotap header length is 29, so that's within the radiotap header.</p><p>For 802.11n, the rate is likely to come from the <a href="http://www.radiotap.org/defined-fields/MCS">MCS field</a>; it's calculated based on the MCS index, channel width, and guard interval length in that field.</p><blockquote><p>Shouldnt data rate be a 2-byte value? The reason why I am asking is wireshark generally shows rate as (2*rate because unit is in 500KBps) in the bit representation(as seen in the second image). So any rate above 128 Mbps is going to exceed one byte</p></blockquote><p>Again, for 802.11n, the data rate is <em>NOT</em> represented by a <a href="http://www.radiotap.org/defined-fields/Rate">Rate field</a>, it's calculated from the values in the MCS field. The MCS field is 3 bytes long; the rate should probably be shown as a calculated value and, when clicked on, select all 3 bytes.</p><blockquote><p>From the below images, it is visible that the radio tap header format is different for the two packets.</p></blockquote><p>Yes. The first capture is 802.11n; the second capture is probably not 802.11n (it says 802.11a).</p><blockquote><p>If the MCS information is showing the data rate, Can someone tell me how it is different from the data rate measured from the client?</p></blockquote><p>What do you mean by "measured"? "Measured" as in "counting the number of bits of data received within a specified amount of time and dividing the bits by the number of time"?</p><blockquote><p>iwconfig shows a different data rate compare to the data rate in MCS.</p></blockquote><p>What is iwconfig showing?</p><blockquote><p>what does QoS data mean in the sense, does it have the actual data?</p></blockquote><p>"QoS data" means that the frame is a QoS Data frame, i.e. a Data frame with a QoS header. See sections 7.1.3.1.2 "Type and Subtype fields", 7.1.3.5 "QoS Control field", and 7.2.2 "Data frames" of IEEE Std 802.11-2007.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '12, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-9596" class="comments-container"><span id="9607"></span><div id="comment-9607" class="comment"><div id="post-9607-score" class="comment-score"></div><div class="comment-text"><p>I've checked into the trunk a change to show the Data Rate as a calculated field, and make it cover all 3 bytes of the MCS field, if it's calculated from items in that field, and will schedule it for the 1.6 branch.</p></div><div id="comment-9607-info" class="comment-info"><span class="comment-age">(17 Mar '12, 14:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9616"></span><div id="comment-9616" class="comment"><div id="post-9616-score" class="comment-score"></div><div class="comment-text"><p>hi, Thanks for the clarification. I can understand a lot of things now from your reply. By mentioning measured "I meant the data rate value from iwconfig". iwconfig at the client shows 130 MbpS where as the one read from my monitor interface is 39 MbpS. Is iwconfig meant to work with 802.11n traffic?</p></div><div id="comment-9616-info" class="comment-info"><span class="comment-age">(19 Mar '12, 12:44)</span> <span class="comment-user userinfo">srini_wisc</span></div></div><span id="9620"></span><div id="comment-9620" class="comment"><div id="post-9620-score" class="comment-score">1</div><div class="comment-text"><p>Looking at the iwconfig source as downloaded from <a href="http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html">here</a>, it prints, somewhere, "Bit Rate" followed by a bit rate, fetched with the <code>SIOCGIWRATE</code> ioctl. I would have to spend a lot of time looking at the Linux kernel source to see where the bit rate comes from in the ath5k driver; if you have any questions about the value returned by iwconfig, I suggest you ask somebody in the Linux wireless networking community, as I have no time to search for an answer for them.</p></div><div id="comment-9620-info" class="comment-info"><span class="comment-age">(19 Mar '12, 20:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9596" class="comment-tools"></div><div class="clear"></div><div id="comment-9596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

