+++
type = "question"
title = "Malformed and unresolved LWAPP-encapsulated 802.11 packets"
description = '''I use tshark to capture packets at 20 to 30 MB/s, then a lot of malformed and unresolved(e.g. 802.11 association packet whose body only shows data) packets appears. How to solve the problem? Or what&#x27;s tshark/dumpcap &#x27;s capture limitation?'''
date = "2014-04-13T18:04:00Z"
lastmod = "2014-05-09T00:08:00Z"
weight = 31772
keywords = [ "capture", "enlarge", "capbility" ]
aliases = [ "/questions/31772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed and unresolved LWAPP-encapsulated 802.11 packets](/questions/31772/malformed-and-unresolved-lwapp-encapsulated-80211-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31772-score" class="post-score" title="current number of votes">0</div><span id="post-31772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use tshark to capture packets at 20 to 30 MB/s, then a lot of malformed and unresolved(e.g. 802.11 association packet whose body only shows data) packets appears. How to solve the problem? Or what's tshark/dumpcap 's capture limitation?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-enlarge" rel="tag" title="see questions tagged &#39;enlarge&#39;">enlarge</span> <span class="post-tag tag-link-capbility" rel="tag" title="see questions tagged &#39;capbility&#39;">capbility</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '14, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Apr '14, 01:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-31772" class="comments-container"><span id="31774"></span><div id="comment-31774" class="comment"><div id="post-31774-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I use tshark to capture packets at 20 to 30 MB/s, then a lot of malformed and unresolved(e.g. 802.11 association packet whose body only shows data) packets appears.</p></blockquote><p>Do those packets have a radiotap header? If so, do those packets have the "Flags" field in the radiotap header ("Flags", not "Present flags") and, if so, is the "Bad FCS" flag set for those packets?</p></div><div id="comment-31774-info" class="comment-info"><span class="comment-age">(13 Apr '14, 23:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31775"></span><div id="comment-31775" class="comment"><div id="post-31775-score" class="comment-score"></div><div class="comment-text"><p>Also, do those packets have the "Protected flag" set in the Flags field of the 802.11 header?</p></div><div id="comment-31775-info" class="comment-info"><span class="comment-age">(13 Apr '14, 23:45)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31777"></span><div id="comment-31777" class="comment"><div id="post-31777-score" class="comment-score"></div><div class="comment-text"><p>There seems no such flags, I upload first 2000 packets' file (<a href="https://www.cloudshark.org/captures/86c0d8f568e4">https://www.cloudshark.org/captures/86c0d8f568e4</a> ). It contains lwapp encapsulated wlan packets(using "wlan.fc.type eq 0 and wlan.fc.subtype eq 0" to see association packets)</p></div><div id="comment-31777-info" class="comment-info"><span class="comment-age">(14 Apr '14, 01:00)</span> <span class="comment-user userinfo">metamatrix</span></div></div></div><div id="comment-tools-31772" class="comment-tools"></div><div class="clear"></div><div id="comment-31772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31779"></span>

<div id="answer-container-31779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31779-score" class="post-score" title="current number of votes">0</div><span id="post-31779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This has nothing whatsoever to do with TShark's, dumpcap's, or libpcap's/WinPcap's abilities.</p><p>The 802.11 frames are encapsulated within LWAPP packets. LWAPP is described by <a href="http://tools.ietf.org/html/rfc5412">RFC 5412</a>; as section 2, "Protocol Overview", or RFC 5412 says, "LWAPP data messages are forwarded wireless frames.". Those forwarded frames are what are being transported here over UDP.</p><p>Either the device sending out the LWAPP data messages is putting malformed packets into the LWAPP data messages, or they are getting mangled by one of the networks over which the packets are being transported. I suspect it's the first of those.</p><p>There are several types of bad packets in the capture:</p><ol><li>invalid LWAPP control messages - those are presumably due to the device sending out bad control messages or due to the messages being mangled by one of the networks;</li><li>LWAPP data messages containing "QoS Data" packets or "Unrecognized (Reserved frame" packets - those have the Protected bit set, and are therefore presumably encrypted using WEP or WPA/WPA2, and you'd need the password for the network in question to decrypt them.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31779" class="comments-container"><span id="32657"></span><div id="comment-32657" class="comment"><div id="post-32657-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid they are neither neither malformed nor unresolved packets. In fact, they're fragment http packets which are wrongly identified to 802.11 packets by wireshark.</p></div><div id="comment-32657-info" class="comment-info"><span class="comment-age">(09 May '14, 00:08)</span> <span class="comment-user userinfo">metamatrix</span></div></div></div><div id="comment-tools-31779" class="comment-tools"></div><div class="clear"></div><div id="comment-31779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

