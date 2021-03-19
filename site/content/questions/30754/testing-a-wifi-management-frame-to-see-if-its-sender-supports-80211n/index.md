+++
type = "question"
title = "Testing a WiFi management frame to see if its sender supports 802.11n"
description = '''I&#x27;m using Wireshark to capture packets of wireless communication. Using the display filter&#x27;s parameters wlan_mgt.extented_supported_rates and wlan_mgt.supported_rates, it&#x27;s possible to filter out packets that match the network modes B and G.  How do I test if a packet belongs to an AP that&#x27;s configu...'''
date = "2014-03-13T01:09:00Z"
lastmod = "2014-03-18T01:39:00Z"
weight = 30754
keywords = [ "wireless" ]
aliases = [ "/questions/30754" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Testing a WiFi management frame to see if its sender supports 802.11n](/questions/30754/testing-a-wifi-management-frame-to-see-if-its-sender-supports-80211n)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30754-score" class="post-score" title="current number of votes">0</div><span id="post-30754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark to capture packets of wireless communication. Using the display filter's parameters <code>wlan_mgt.extented_supported_rates</code> and <code>wlan_mgt.supported_rates</code>, it's possible to filter out packets that match the network modes <code>B</code> and <code>G</code>.<br />
</p><p>How do I test if a packet belongs to an AP that's configured with a network mode <code>N</code>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/d7bc992d0b3f0e2db1bf0eec41ba32dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dor_lan&#39;s gravatar image" /><p><span>Dor_lan</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dor_lan has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Mar '14, 01:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-30754" class="comments-container"><span id="30780"></span><div id="comment-30780" class="comment"><div id="post-30780-score" class="comment-score">1</div><div class="comment-text"><p>"Belongs to" in what sense? Do you mean "is this a packet from an AP that's configured to support 802.11n, containing parameters for that AP", such as a beacon from that AP?</p></div><div id="comment-30780-info" class="comment-info"><span class="comment-age">(13 Mar '14, 15:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="30850"></span><div id="comment-30850" class="comment"><div id="post-30850-score" class="comment-score"></div><div class="comment-text"><p><span>@Guy Harris</span>: Exactly!</p></div><div id="comment-30850-info" class="comment-info"><span class="comment-age">(16 Mar '14, 00:19)</span> <span class="comment-user userinfo">Dor_lan</span></div></div></div><div id="comment-tools-30754" class="comment-tools"></div><div class="clear"></div><div id="comment-30754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30918"></span>

<div id="answer-container-30918" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30918-score" class="post-score" title="current number of votes">1</div><span id="post-30918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dor_lan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Though I found the field wlan_mgt.tag with display value of Tag: HT Information (802.11n D1.10); Can I rely on this field?</p></blockquote><p>I don't know whether you can <em>rely</em> on that field for certain (I'd have to go back and read 802.11-2012), but I suspect a device that doesn't support 802.11n isn't going to give 802.11n information in its beacon frames (there's no reason for it to do so, and I'm not sure any form of that information can say "I don't do 802.11n"), so try the filter</p><pre><code>wlan_mgt.tag.number == 45</code></pre><p>to look for frames with that tag.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '14, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30918" class="comments-container"></div><div id="comment-tools-30918" class="comment-tools"></div><div class="clear"></div><div id="comment-30918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30863"></span>

<div id="answer-container-30863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30863-score" class="post-score" title="current number of votes">1</div><span id="post-30863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are some fields in the Radiotap and PPI headers</p><blockquote><p>radiotap.channel.type<br />
ppi.80211-common.chan.type</p></blockquote><p>See:</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/r/radiotap.html">http://www.wireshark.org/docs/dfref/r/radiotap.html</a><br />
<a href="http://www.wireshark.org/docs/dfref/p/ppi.html">http://www.wireshark.org/docs/dfref/p/ppi.html</a></p></blockquote><p>There are other fields in the Radiotap/PPI header that should help to identify 802.11n, like frequency used (2GHz versus 5Ghz) or the data rate.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-30863" class="comments-container"><span id="30874"></span><div id="comment-30874" class="comment"><div id="post-30874-score" class="comment-score"></div><div class="comment-text"><p>Sorry but I didn't find these fields either in BG or BGN packet (both are in PDML format if it matters)</p></div><div id="comment-30874-info" class="comment-info"><span class="comment-age">(17 Mar '14, 03:04)</span> <span class="comment-user userinfo">Dor_lan</span></div></div><span id="30875"></span><div id="comment-30875" class="comment"><div id="post-30875-score" class="comment-score"></div><div class="comment-text"><p>can you post some sample frames in pcap format on google drive, dropbox or cloudshark.org?</p></div><div id="comment-30875-info" class="comment-info"><span class="comment-age">(17 Mar '14, 03:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30878"></span><div id="comment-30878" class="comment"><div id="post-30878-score" class="comment-score"></div><div class="comment-text"><p>My mistake! :) The field <code>radiotap.channel.type</code> <em>exists</em> in both packets (<code>BG</code> &amp; <code>BGN</code>) and in both it equals to <code>0xa000</code> (display value is <code>Channel type: 802.11b (0x00a0)</code>). The field <code>ppi.80211-common.chan.type</code> <em>doesn't</em> exists in either of them, nor merely <code>ppi</code>. Though I found the field <code>wlan_mgt.tag</code> with display value of <code>Tag: HT Information (802.11n D1.10)</code>; Can I rely on this field? Sorry but I can't post the whole packet (has sensitive info).</p></div><div id="comment-30878-info" class="comment-info"><span class="comment-age">(17 Mar '14, 04:35)</span> <span class="comment-user userinfo">Dor_lan</span></div></div><span id="30881"></span><div id="comment-30881" class="comment"><div id="post-30881-score" class="comment-score"></div><div class="comment-text"><blockquote><p>doesn't exists in either of them, <strong>nor merely ppi</strong>.</p></blockquote><p>Ususally you will only have a radiotap <strong>or</strong> a ppi header.</p><blockquote><p>Sorry but I can't post the whole packet (has sensitive info).</p></blockquote><p>that isn't necessary as you've found the fields yourself.</p></div><div id="comment-30881-info" class="comment-info"><span class="comment-age">(17 Mar '14, 06:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30919"></span><div id="comment-30919" class="comment"><div id="post-30919-score" class="comment-score"></div><div class="comment-text"><p>Checking whether a given frame is an 802.11n frame can tell you if the sender supports 802.11n (if the frame is an 802.11n frame, obviously the sender supports 802.11n), but 802.11n-capable machines can end out non-802.11n packets - I have a capture in front of me in which our 802.11n-capable AirPort Express sent out a non-11n beacon frame (so that non-11n-capable machines, such as my ancient first-generation iPhone, can see it) that advertises its ability to handle 11n (that's the frame from which I determined the display filter in my answer).</p></div><div id="comment-30919-info" class="comment-info"><span class="comment-age">(18 Mar '14, 01:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-30863" class="comment-tools"></div><div class="clear"></div><div id="comment-30863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

