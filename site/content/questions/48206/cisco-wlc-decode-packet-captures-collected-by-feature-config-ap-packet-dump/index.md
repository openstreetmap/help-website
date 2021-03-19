+++
type = "question"
title = "Cisco WLC Decode Packet Captures Collected by Feature &quot;config ap packet-dump&quot;"
description = '''I am collecting packet captures from a Cisco WLC using the &quot;config ap packet-dump&quot; feature. This feature collects bidirectional traffic involving the specified client from the AP radio perspective so that all 802.11 data is preserved but the data in unencrypted regardless of SSID operation.  To view...'''
date = "2015-12-02T10:59:00Z"
lastmod = "2015-12-07T10:04:00Z"
weight = 48206
keywords = [ "decode", "wireless", "wlc", "802.11", "llc" ]
aliases = [ "/questions/48206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cisco WLC Decode Packet Captures Collected by Feature "config ap packet-dump"](/questions/48206/cisco-wlc-decode-packet-captures-collected-by-feature-config-ap-packet-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48206-score" class="post-score" title="current number of votes">0</div><span id="post-48206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am collecting packet captures from a Cisco WLC using the "config ap packet-dump" feature. This feature collects bidirectional traffic involving the specified client from the AP radio perspective so that all 802.11 data is preserved but the data in unencrypted regardless of SSID operation.</p><p>To view this data in Wireshark I need to change "Ignore the Protection Bit" from "No" to something else. The behavior I am seeing is that when "Yes - without IV" is selected only the client side of the conversation is decoded properly and when "Yes - with IV" is selected only the server side of the conversation is decoded properly.</p><p>Question: what is the IV and why would only one side of the conversation present it? Request: a radio button for "Yes - regardless of IV" to decode both with and without IV</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-wlc" rel="tag" title="see questions tagged &#39;wlc&#39;">wlc</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/8fe90729a6821f69138bbc80c471bcbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsjaoui&#39;s gravatar image" /><p><span>dsjaoui</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsjaoui has no accepted answers">0%</span></p></div></div><div id="comments-container-48206" class="comments-container"></div><div id="comment-tools-48206" class="comment-tools"></div><div class="clear"></div><div id="comment-48206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48268"></span>

<div id="answer-container-48268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48268-score" class="post-score" title="current number of votes">0</div><span id="post-48268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After investigating the Wireshark code (dissector-packet-ieee80211) that option has to do with WEP decryption.<br />
WEP = Wired Equivalent Privacy, is the first encryption method that was implemented in WiFi. It is very easily cracked and no longer deployed.</p><p>IV = Initialization vector, used in the cryptography for WEP.</p><p>According the code, if you ignore the protection bit, then the WiFi frames are not encrypted using WEP. The other selections assume that WEP is being used to encrypt the frames.</p><p>Now the question is why does the Cisco WLC encrypt these frames using WEP? Maybe we are missing something?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '15, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></div></div><div id="comments-container-48268" class="comments-container"><span id="48332"></span><div id="comment-48332" class="comment"><div id="post-48332-score" class="comment-score"></div><div class="comment-text"><p>That is fascinating. I see in the capture that the frames dissected using "without IV" do not in fact have the IV My best guess would be that the point at which this packet capture occurs prior to the actual encryption but I don't know when the IV would be added to the radio header</p><p>If it's any help I can provide samples of this Here is a link for a simple DNS request: <a href="https://www.dropbox.com/s/5l2hjb7csnpzmsa/802.11%20wireshark%20with%20IV%20vs%20without%20IV.pcap?dl=0">https://www.dropbox.com/s/5l2hjb7csnpzmsa/802.11%20wireshark%20with%20IV%20vs%20without%20IV.pcap?dl=0</a></p></div><div id="comment-48332-info" class="comment-info"><span class="comment-age">(07 Dec '15, 10:04)</span> <span class="comment-user userinfo">dsjaoui</span></div></div></div><div id="comment-tools-48268" class="comment-tools"></div><div class="clear"></div><div id="comment-48268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

