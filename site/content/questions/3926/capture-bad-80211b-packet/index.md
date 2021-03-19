+++
type = "question"
title = "Capture bad 802.11b packet"
description = '''I want to capture the 802.11b packets with bad CRC. Actually I am sending the packets from some terminal A to terminal B and creating self-defined interference to toggle the bitstream of the packets so that CRC may not be passed. I want to capture that packet for analysis purpose. Any help would be ...'''
date = "2011-05-04T11:11:00Z"
lastmod = "2011-05-08T00:19:00Z"
weight = 3926
keywords = [ "802.11b" ]
aliases = [ "/questions/3926" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture bad 802.11b packet](/questions/3926/capture-bad-80211b-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3926-score" class="post-score" title="current number of votes">0</div><span id="post-3926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture the 802.11b packets with bad CRC. Actually I am sending the packets from some terminal A to terminal B and creating self-defined interference to toggle the bitstream of the packets so that CRC may not be passed. I want to capture that packet for analysis purpose. Any help would be greatly appreciated Nadeem SEECS, NUST</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11b" rel="tag" title="see questions tagged &#39;802.11b&#39;">802.11b</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '11, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/e8dbe45da09a6d997dd0f083786c8044?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nadeem&#39;s gravatar image" /><p><span>Nadeem</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nadeem has no accepted answers">0%</span></p></div></div><div id="comments-container-3926" class="comments-container"><span id="3927"></span><div id="comment-3927" class="comment"><div id="post-3927-score" class="comment-score"></div><div class="comment-text"><p>What platform are you running? Windows, Linux, something else?</p></div><div id="comment-3927-info" class="comment-info"><span class="comment-age">(04 May '11, 11:43)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="3932"></span><div id="comment-3932" class="comment"><div id="post-3932-score" class="comment-score"></div><div class="comment-text"><p>I am using fedora 12 and do not have Airpcap Adapter. Now what is the solution ?</p></div><div id="comment-3932-info" class="comment-info"><span class="comment-age">(04 May '11, 21:34)</span> <span class="comment-user userinfo">Nadeem</span></div></div></div><div id="comment-tools-3926" class="comment-tools"></div><div class="clear"></div><div id="comment-3926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3928"></span>

<div id="answer-container-3928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3928-score" class="post-score" title="current number of votes">1</div><span id="post-3928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're on a Windows host, consider using the AirPcap adapter for capture and setting it to "invalid frames" in the FCS filter setup in either the AirPcap Control Panel or the Capture Options Wireless Settings.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span> </br></p></div></div><div id="comments-container-3928" class="comments-container"></div><div id="comment-tools-3928" class="comment-tools"></div><div class="clear"></div><div id="comment-3928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3970"></span>

<div id="answer-container-3970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3970-score" class="post-score" title="current number of votes">1</div><span id="post-3970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is to capture in monitor mode; fortunately, Linux does a pretty good job of supporting monitor mode.</p><p>You may need to capture on a machine other than terminal A or B; that machine must have an 802.11 adapter (which does not have to be an AirPcap adapter - AirPcap adapters aren't supported on any OS other than Windows).</p><p>If the Wireshark dialog box that pops up if you select "Options" from the "Capture" menu has a "Capture packets in monitor mode" checkbox, select your 802.11 adapter in the "Interface" box; that should make the "Capture packets in monitor mode" checkbox active. Check it, and then start the capture. (You will need to run Wireshark 1.4.x or one of the builds from the trunk to get that dialog box. Unfortunately, from a quick look at pkg.fedora.org, Fedora 12 comes with Wireshark 1.2.x.)</p><p>Otherwise, you'll have to put the adapter into monitor mode by hand. The easiest way to do that is probably with <a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">airmon-ng</a>. This might create a new network interface, e.g. "mon0", on which you'd do the capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3970" class="comments-container"></div><div id="comment-tools-3970" class="comment-tools"></div><div class="clear"></div><div id="comment-3970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3997"></span>

<div id="answer-container-3997" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3997-score" class="post-score" title="current number of votes">0</div><span id="post-3997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks. But in monitor mode, wireshark captures packets from all the SSIDs in range. I dont want to do this and Use Promiscous mode so that get communicated through only one SSID. Second, the question still remains that how would I know that the Packet is not the one retransmitted and it is the actually corrupt packet. Because I ve to do a correspondence between the originally sent packet and received corrupted packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '11, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/e8dbe45da09a6d997dd0f083786c8044?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nadeem&#39;s gravatar image" /><p><span>Nadeem</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nadeem has no accepted answers">0%</span></p></div></div><div id="comments-container-3997" class="comments-container"></div><div id="comment-tools-3997" class="comment-tools"></div><div class="clear"></div><div id="comment-3997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

