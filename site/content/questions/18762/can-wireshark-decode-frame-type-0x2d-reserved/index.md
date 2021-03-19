+++
type = "question"
title = "Can Wireshark decode frame type 0x2d (reserved)"
description = '''A WLAN packet capture using the AirPcap card and then opened in Wireshark was unable to decode the frame type 0x2d (a &quot;reserved&quot; frame type). I did notice that the FCS was incorrect and wondered if this was a factor. So I changed the preferences but to no avail: Edit &amp;gt; Preferences (802.11 Radiota...'''
date = "2013-02-20T02:52:00Z"
lastmod = "2013-02-20T02:52:00Z"
weight = 18762
keywords = [ "airpcap", "802.11", "0x2d" ]
aliases = [ "/questions/18762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark decode frame type 0x2d (reserved)](/questions/18762/can-wireshark-decode-frame-type-0x2d-reserved)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18762-score" class="post-score" title="current number of votes">0</div><span id="post-18762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A WLAN packet capture using the AirPcap card and then opened in Wireshark was unable to decode the frame type 0x2d (a "reserved" frame type).</p><p>I did notice that the FCS was incorrect and wondered if this was a factor. So I changed the preferences but to no avail:</p><p>Edit &gt; Preferences (802.11 Radiotap) “Assume bit 14 means FCS in header” – made no difference.</p><p>The first header is identified as 802.11a and we expect next the HT header to be decoded. But, it is shown as unknown frame type (0x2d). I think because of this, there is no HT header decoded. I am wondering if we are missing some driver that supports the decode of HT MCS?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-0x2d" rel="tag" title="see questions tagged &#39;0x2d&#39;">0x2d</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/2daef5bf476a14f61913095e5d2b0e29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darenmatthews&#39;s gravatar image" /><p><span>darenmatthews</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darenmatthews has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '13, 02:56</strong> </span></p></div></div><div id="comments-container-18762" class="comments-container"></div><div id="comment-tools-18762" class="comment-tools"></div><div class="clear"></div><div id="comment-18762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

