+++
type = "question"
title = "Only capturing broadcast and probe responses."
description = '''I am in a hotel with open wifi (no MAC address filtering or encryption). I am running kali on VMware with an Alfa card 36NH. In Wireshark, I am only seeing broadcast and probe responses. I looked in Wifite and it says that all of the hotel APs are encrypted (WPA2). I am at a loss with what to do fro...'''
date = "2017-03-05T06:05:00Z"
lastmod = "2017-03-05T12:49:00Z"
weight = 59858
keywords = [ "broadcast", "fisher", "probe", "kontak" ]
aliases = [ "/questions/59858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Only capturing broadcast and probe responses.](/questions/59858/only-capturing-broadcast-and-probe-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59858-score" class="post-score" title="current number of votes">0</div><span id="post-59858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am in a hotel with open wifi (no MAC address filtering or encryption). I am running kali on VMware with an Alfa card 36NH. In Wireshark, I am only seeing broadcast and probe responses. I looked in Wifite and it says that all of the hotel APs are encrypted (WPA2). I am at a loss with what to do from this point. My antenna is in monitor mode and is on wlan0 (wlan0mon).<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-fisher" rel="tag" title="see questions tagged &#39;fisher&#39;">fisher</span> <span class="post-tag tag-link-probe" rel="tag" title="see questions tagged &#39;probe&#39;">probe</span> <span class="post-tag tag-link-kontak" rel="tag" title="see questions tagged &#39;kontak&#39;">kontak</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '17, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/cfa1f17ec579300c6470bb0da56a7eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joe08&#39;s gravatar image" /><p><span>joe08</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joe08 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59858" class="comments-container"></div><div id="comment-tools-59858" class="comment-tools"></div><div class="clear"></div><div id="comment-59858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59862"></span>

<div id="answer-container-59862" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59862-score" class="post-score" title="current number of votes">0</div><span id="post-59862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><blockquote><p>I am at a loss with what to do from this point</p></blockquote></blockquote><p>What do you want to do? I wouldn't be trying to crack networks in some hotel as there could be legal ramifications to these types of activities. To practice, set up your own wireless network and attack that one.</p><p>If you expect to see data frames, perhaps your issue is related to one of these:</p><p><a href="https://ask.wireshark.org/questions/53260/cannot-capture-frames-other-than-broadcast-or-multicast-over-wlan">https://ask.wireshark.org/questions/53260/cannot-capture-frames-other-than-broadcast-or-multicast-over-wlan</a> <a href="https://ask.wireshark.org/questions/59652/cant-see-any-tcpudpicmp-traffic?page=1&amp;focusedAnswerId=59656#59656">https://ask.wireshark.org/questions/59652/cant-see-any-tcpudpicmp-traffic?page=1&amp;focusedAnswerId=59656#59656</a> <a href="https://ask.wireshark.org/questions/56658/unable-to-capture-relevant-packets-with-wireshark-airmon-ng-wpa2-psk-aes?page=1&amp;focusedAnswerId=56660#56660">https://ask.wireshark.org/questions/56658/unable-to-capture-relevant-packets-with-wireshark-airmon-ng-wpa2-psk-aes?page=1&amp;focusedAnswerId=56660#56660</a></p><p>I think that is an <a href="https://uwnthesis.wordpress.com/2016/07/02/kali-2-0-how-to-select-the-best-wifi-adapter-for-kali-linux/">RALink chipset</a>, so in particular check the first link above.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '17, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-59862" class="comments-container"></div><div id="comment-tools-59862" class="comment-tools"></div><div class="clear"></div><div id="comment-59862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

