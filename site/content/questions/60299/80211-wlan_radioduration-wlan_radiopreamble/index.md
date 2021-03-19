+++
type = "question"
title = "802.11 wlan_radio.duration wlan_radio.preamble"
description = '''I am using wireshark in linux to capture 802.11 packet. When I see the resolution result, I see the durationt, preamble, then I find it is actually wlan_radio.duration, wlan_radio.preamble. wlan_radio.preamble is matched with the 802.11 protocol, and its meaning is obvious. But what does wlan_radio....'''
date = "2017-03-24T01:24:00Z"
lastmod = "2017-03-25T18:45:00Z"
weight = 60299
keywords = [ "802.11", "wlan_radio.duration", "wlan_radio.preamble" ]
aliases = [ "/questions/60299" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 wlan\_radio.duration wlan\_radio.preamble](/questions/60299/80211-wlan_radioduration-wlan_radiopreamble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60299-score" class="post-score" title="current number of votes">0</div><span id="post-60299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark in linux to capture 802.11 packet. When I see the resolution result, I see the durationt, preamble, then I find it is actually wlan_radio.duration, wlan_radio.preamble. wlan_radio.preamble is matched with the 802.11 protocol, and its meaning is obvious. But what does wlan_radio.duration mean? When I use (frame length - radiotaoheader length)*8/data rate, then plus preamble time, it is not equal to duration? So, what does wlan_radio.duration mean in wireshark? How/where can I find its definition?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-wlan_radio.duration" rel="tag" title="see questions tagged &#39;wlan_radio.duration&#39;">wlan_radio.duration</span> <span class="post-tag tag-link-wlan_radio.preamble" rel="tag" title="see questions tagged &#39;wlan_radio.preamble&#39;">wlan_radio.preamble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '17, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/c985bfa9f21f8b147e500ebe0dfe0f0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marxwolf&#39;s gravatar image" /><p><span>marxwolf</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marxwolf has no accepted answers">0%</span></p></div></div><div id="comments-container-60299" class="comments-container"></div><div id="comment-tools-60299" class="comment-tools"></div><div class="clear"></div><div id="comment-60299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60325"></span>

<div id="answer-container-60325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60325-score" class="post-score" title="current number of votes">0</div><span id="post-60325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's the following comment in epan/dissectors/packet-ieee80211-radio.c:</p><pre><code>  /* durations in microseconds */
  guint preamble = 0; /* duration of plcp */
  guint duration = 0; /* duration of whole frame (plcp + mac data + any trailing parts) */</code></pre><p>further down the duration for the different types (a, b, g, ...) are calculated and yes, it's different for different types. Also, you need to be aware that the frame will usually change its symbol speed after the first few header (not preamble) bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '17, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p><span>jmayer</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span></p></div></div><div id="comments-container-60325" class="comments-container"></div><div id="comment-tools-60325" class="comment-tools"></div><div class="clear"></div><div id="comment-60325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

