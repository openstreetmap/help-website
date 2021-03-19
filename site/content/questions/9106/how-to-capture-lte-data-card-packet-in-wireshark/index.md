+++
type = "question"
title = "How to capture LTE data card packet in Wireshark?"
description = '''Hi, I would like to know if anyone has tried to use Wireshark with an LTE data card to dissect the RRC messages? If so how should it be done? Thanks, Ganesh'''
date = "2012-02-17T11:51:00Z"
lastmod = "2012-12-27T05:16:00Z"
weight = 9106
keywords = [ "datacard", "rrc", "lte" ]
aliases = [ "/questions/9106" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture LTE data card packet in Wireshark?](/questions/9106/how-to-capture-lte-data-card-packet-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9106-score" class="post-score" title="current number of votes">0</div><span id="post-9106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to know if anyone has tried to use Wireshark with an LTE data card to dissect the RRC messages? If so how should it be done?</p><p>Thanks, Ganesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-datacard" rel="tag" title="see questions tagged &#39;datacard&#39;">datacard</span> <span class="post-tag tag-link-rrc" rel="tag" title="see questions tagged &#39;rrc&#39;">rrc</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/82993f8f5b2094a0d73b490dbd14c576?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VGM&#39;s gravatar image" /><p><span>VGM</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VGM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '12, 12:04</strong> </span></p></div></div><div id="comments-container-9106" class="comments-container"></div><div id="comment-tools-9106" class="comment-tools"></div><div class="clear"></div><div id="comment-9106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="9117"></span>

<div id="answer-container-9117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9117-score" class="post-score" title="current number of votes">0</div><span id="post-9117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If "an LTE data card" means a network adapter that provides Internet access over an LTE mobile phone network, I know of no adapters of that sort that provide anything visible to the host other than a PPP connection; they won't, as far as I know, show you low-level RRC packets. (They might exist, but I don't know of any.)</p><p>The <a href="https://svn.berlin.ccc.de/projects/airprobe/">airprobe</a> project speaks of "[building] an air-interface analysis tool for the GSM (and possible later 3G) mobile phone standard", but given that they speak of "possible later 3G", they're probably <em>very</em> far from providing anything for LTE.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '12, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Feb '12, 00:34</strong> </span></p></div></div><div id="comments-container-9117" class="comments-container"></div><div id="comment-tools-9117" class="comment-tools"></div><div class="clear"></div><div id="comment-9117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9149"></span>

<div id="answer-container-9149" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9149-score" class="post-score" title="current number of votes">0</div><span id="post-9149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some huawei cards, sierrawireles and couple of others dongles have special diagnostic ports that spit out low level messages in proprietary formats. So in theory it's doable with some reverse engineering of those protocols. I'm actually thinking of doing something along those lines one day.</p><p>Anyway you'll be better off by googling "swissqual". They have a lite version of their product that's free and works with about 100 handsets and some cards ( they support 3 lte ) You can't save logs but you can view live. I have no association with the company just trying to be helpful</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-9149" class="comments-container"></div><div id="comment-tools-9149" class="comment-tools"></div><div class="clear"></div><div id="comment-9149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17267"></span>

<div id="answer-container-17267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17267-score" class="post-score" title="current number of votes">0</div><span id="post-17267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Ganesh!</p><p>If you have binary/hex packets and know their type, then you can do it like I do:</p><ul><li>define several entries to user_dlcs</li><li>use tex2pcap + tshark</li><li>merge files more in: <a href="http://ask.wireshark.org/questions/16847/lte-rrc-how-to-prepare-data?page=1#17250">http://ask.wireshark.org/questions/16847/lte-rrc-how-to-prepare-data?page=1#17250</a> including one 6 bytes RRC connect to play with.</li></ul><p>BR, HNY Iztok</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/a01f024a466c4892dcf2243ce7af051f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s52d&#39;s gravatar image" /><p><span>s52d</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s52d has one accepted answer">50%</span></p></div></div><div id="comments-container-17267" class="comments-container"></div><div id="comment-tools-17267" class="comment-tools"></div><div class="clear"></div><div id="comment-17267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

