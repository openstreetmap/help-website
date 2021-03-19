+++
type = "question"
title = "&quot;IEEE 802.11&quot; vs &quot;802.11&quot; as protocol names"
description = '''Wireshark has several protocols handling IEEE 802.11. Some use &quot;IEEE 802.11&quot; and some use only &quot;802.11&quot; in the protocol name. This makes it a bit difficult to find 802.11 protocols in the Preferences and the Enabled Protocols list because the lists are sorted alphabetically and they end up in differ...'''
date = "2017-07-08T11:23:00Z"
lastmod = "2017-07-10T07:49:00Z"
weight = 62616
keywords = [ "ieee802_11" ]
aliases = [ "/questions/62616" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["IEEE 802.11" vs "802.11" as protocol names](/questions/62616/ieee-80211-vs-80211-as-protocol-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62616-score" class="post-score" title="current number of votes">1</div><span id="post-62616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark has several protocols handling IEEE 802.11. Some use "IEEE 802.11" and some use only "802.11" in the protocol name. This makes it a bit difficult to find 802.11 protocols in the Preferences and the Enabled Protocols list because the lists are sorted alphabetically and they end up in different locations.</p><p>If I want to improve this; should we use "IEEE 802.11" or only "802.11" in the protocol name?</p><p>This will affect where the entries are located in all lists using protocol names. The description will still have "IEEE 802.11".</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2017-07-08_at_19.54.46.png" alt="Wireshark protocol list" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ieee802_11" rel="tag" title="see questions tagged &#39;ieee802_11&#39;">ieee802_11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '17, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/193a8e6acdc05d13fb1e59fbe4eaba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stig&#39;s gravatar image" /><p><span>stig ♦</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stig has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62616" class="comments-container"></div><div id="comment-tools-62616" class="comment-tools"></div><div class="clear"></div><div id="comment-62616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62620"></span>

<div id="answer-container-62620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62620-score" class="post-score" title="current number of votes">0</div><span id="post-62620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While renaming the few "802.11" protocols and descriptions to "IEEE 802.11" could work, I think that this dialog shows an alternative which will is much more user friendly: a search box for filtering the protocols list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '17, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '17, 14:19</strong> </span></p></div></div><div id="comments-container-62620" class="comments-container"><span id="62649"></span><div id="comment-62649" class="comment"><div id="post-62649-score" class="comment-score"></div><div class="comment-text"><p>Personally, I'd prefer consistency, not just with 802.11 but with 802.1*, 802.3, 802.15.4, ...</p></div><div id="comment-62649-info" class="comment-info"><span class="comment-age">(10 Jul '17, 07:49)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62620" class="comment-tools"></div><div class="clear"></div><div id="comment-62620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

