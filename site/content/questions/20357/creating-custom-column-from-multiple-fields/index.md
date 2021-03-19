+++
type = "question"
title = "Creating custom column from multiple fields?"
description = '''I work with packet captures from multiple wireless devices. Some of them use the radiotap headers to insert information like signal strength, channel, data rate, etc. Others use wlan headers for the same. Currently I have multiple custom columns for each, one using the radiotap headers and one with ...'''
date = "2013-04-11T17:40:00Z"
lastmod = "2013-04-26T13:09:00Z"
weight = 20357
keywords = [ "interface", "radiotap", "wlan", "columns", "custom" ]
aliases = [ "/questions/20357" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Creating custom column from multiple fields?](/questions/20357/creating-custom-column-from-multiple-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20357-score" class="post-score" title="current number of votes">0</div><span id="post-20357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I work with packet captures from multiple wireless devices. Some of them use the radiotap headers to insert information like signal strength, channel, data rate, etc. Others use wlan headers for the same.</p><p>Currently I have multiple custom columns for each, one using the radiotap headers and one with the wlan headers, and I either have both sets displaying (one being blank and taking up screen space) or I have to switch back and forth between which ones are displayed.</p><p>Anyone have any ideas if there is a way to have a custom column display one of multiple field names? I haven't found a way, but it would be nice if there were a way to give a custom column multiple criteria for the field name and have the column populate with the first matched.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/4d5bded8ba4ade62074641de57ab6406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YLearn&#39;s gravatar image" /><p><span>YLearn</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YLearn has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-20357" class="comments-container"></div><div id="comment-tools-20357" class="comment-tools"></div><div class="clear"></div><div id="comment-20357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20358"></span>

<div id="answer-container-20358" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20358-score" class="post-score" title="current number of votes">2</div><span id="post-20358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="YLearn has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's currently no mechanism for doing that.</p><p>What ''really'' needs to be done is to have, for at least a subset of the radio metadata, common "wlan." fields, so that, regardless of the way the radio metadata appears in the capture file, those fields will have the same field name and the same value encoding, so that display filters, custom columns, TShark -T fields/-e operations, etc. can be used independently of whether the packet has a radiotap header or an AVS header or a Microsoft NetMon header or Peek Classic radio information or Peek Tagged radio information or....</p><p>Note, of course, that some fields are supported only by some metadata mechanisms; in particular, "signal strength" might be an uninterpretable number labeled as "RSSI" (where the only thing you can say is "the bigger the number the stronger the signal" in some captures and a signal strength in dBm in other captures. Those would be different fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20358" class="comments-container"><span id="20359"></span><div id="comment-20359" class="comment"><div id="post-20359-score" class="comment-score"></div><div class="comment-text"><p>I suspected there wasn't a way but figured I would ask as I can't be the only one in this situation. While I ideally agree with what should "really" be done, I don't see the developers of the drivers and different wireless capture tools/software getting together to agree on this anytime soon (or most likely ever).</p></div><div id="comment-20359-info" class="comment-info"><span class="comment-age">(11 Apr '13, 18:27)</span> <span class="comment-user userinfo">YLearn</span></div></div><span id="20364"></span><div id="comment-20364" class="comment"><div id="post-20364-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I don't see the developers of the drivers and different wireless capture tools/software getting together to agree on this anytime soon</p></blockquote><p>They don't have to. Wireshark just needs to either do that in the Wiretap library (thus presenting all 802.11 packets with a collection of 0 or more radio metadata items with standard labels) or in the dissectors for various radio information (so as to provide to the 802.11 dissector a collection of 0 or more radio metadata items with standard labels), and possibly also provide the raw information (for the benefit of people who actually have a reason to look at raw headers).</p></div><div id="comment-20364-info" class="comment-info"><span class="comment-age">(11 Apr '13, 18:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20820"></span><div id="comment-20820" class="comment"><div id="post-20820-score" class="comment-score"></div><div class="comment-text"><p>I think I am on the same page as you now. Thank you for your response.</p></div><div id="comment-20820-info" class="comment-info"><span class="comment-age">(26 Apr '13, 13:09)</span> <span class="comment-user userinfo">YLearn</span></div></div></div><div id="comment-tools-20358" class="comment-tools"></div><div class="clear"></div><div id="comment-20358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

