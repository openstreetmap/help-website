+++
type = "question"
title = "WLAN fields with tshark"
description = '''Hi, I have done some command-line capturing of WLAN packets with dumpcap. Would like to use a display filter in tshark to extract some info in a table. Have found out how to get the MAC addresses for example, but I&#x27;m looking for a full list of header fields to be able to get other things out as well...'''
date = "2015-03-05T20:43:00Z"
lastmod = "2015-03-06T02:22:00Z"
weight = 40315
keywords = [ "wlan", "tshark" ]
aliases = [ "/questions/40315" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WLAN fields with tshark](/questions/40315/wlan-fields-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40315-score" class="post-score" title="current number of votes">0</div><span id="post-40315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have done some command-line capturing of WLAN packets with dumpcap. Would like to use a display filter in tshark to extract some info in a table. Have found out how to get the MAC addresses for example, but I'm looking for a full list of header fields to be able to get other things out as well.</p><p>The only thing I have come across this far is this documentation of display filter (for Wireshark, not tshark):</p><p><a href="https://www.wireshark.org/docs/dfref/w/wlan_mgt.html">https://www.wireshark.org/docs/dfref/w/wlan_mgt.html</a> <a href="https://www.wireshark.org/docs/dfref/w/wlan_aggregate.html">https://www.wireshark.org/docs/dfref/w/wlan_aggregate.html</a> <a href="https://www.wireshark.org/docs/dfref/w/wlan_mgt.html">https://www.wireshark.org/docs/dfref/w/wlan_mgt.html</a></p><p>Though, these filters don't work well whey I try them out in tshark. And what I get to work is not listed on these pages.</p><p>So I suspect that the filters in tshark look different than in Wireshark. Is this correct? And is there a complete list of tshark WLAN filters to find somewhere?</p><p>Thanks!</p><p>Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 20:43</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p><span>SamA</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '15, 20:58</strong> </span></p></div></div><div id="comments-container-40315" class="comments-container"><span id="40318"></span><div id="comment-40318" class="comment"><div id="post-40318-score" class="comment-score"></div><div class="comment-text"><p>the fields are the same. What exactly is not working with tshark and what is your tshark version (-v)?</p></div><div id="comment-40318-info" class="comment-info"><span class="comment-age">(06 Mar '15, 02:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-40315" class="comment-tools"></div><div class="clear"></div><div id="comment-40315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40319"></span>

<div id="answer-container-40319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40319-score" class="post-score" title="current number of votes">1</div><span id="post-40319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To get a complete list of fields (for all protocols, so it's very big), use:</p><p><code>tshark -G fields &gt; fields.txt</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40319" class="comments-container"></div><div id="comment-tools-40319" class="comment-tools"></div><div class="clear"></div><div id="comment-40319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

