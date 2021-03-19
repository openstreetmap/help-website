+++
type = "question"
title = "Wireshark causes blue screen on Win7 x64 wih AirPcapNX"
description = '''I am trying to install Riverbed AirPcapNX drivers and Wireshark on a Win7 x64 laptop. I have downloaded version 4.1.3 of the drivers and version 1.12.4 of Wireshark. If I start Wireshark without the AirPcapNx dongle plugged into the laptop, Wireshark comes up fine. If I plug the AirPcapNX dongle int...'''
date = "2015-03-11T13:23:00Z"
lastmod = "2015-03-11T23:40:00Z"
weight = 40485
keywords = [ "airpcap", "crash" ]
aliases = [ "/questions/40485" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark causes blue screen on Win7 x64 wih AirPcapNX](/questions/40485/wireshark-causes-blue-screen-on-win7-x64-wih-airpcapnx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40485-score" class="post-score" title="current number of votes">0</div><span id="post-40485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to install Riverbed AirPcapNX drivers and Wireshark on a Win7 x64 laptop. I have downloaded version 4.1.3 of the drivers and version 1.12.4 of Wireshark. If I start Wireshark without the AirPcapNx dongle plugged into the laptop, Wireshark comes up fine. If I plug the AirPcapNX dongle into the laptop and try to start Wireshark, I get the blue screen of death. How do I troubleshoot this?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '15, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/0dc0de0b4d1e0bb07a94a8b0457572bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joe_2718&#39;s gravatar image" /><p><span>joe_2718</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joe_2718 has no accepted answers">0%</span></p></div></div><div id="comments-container-40485" class="comments-container"></div><div id="comment-tools-40485" class="comment-tools"></div><div class="clear"></div><div id="comment-40485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40486"></span>

<div id="answer-container-40486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40486-score" class="post-score" title="current number of votes">0</div><span id="post-40486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I troubleshoot this?</p></blockquote><p>Wireshark is running with user privileges, so it's (almost) impossible to create a bluescreen.</p><p>This is most certainly a driver issue of AirPcap. Please contact the vendor of that device.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40486" class="comments-container"><span id="40492"></span><div id="comment-40492" class="comment"><div id="post-40492-score" class="comment-score"></div><div class="comment-text"><p>Not sure if this is normal, but I have to run Wireshark with admin privileges if I want to use the AirPCAP adapter, otherwise it's not detected...</p></div><div id="comment-40492-info" class="comment-info"><span class="comment-age">(11 Mar '15, 14:48)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-40486" class="comment-tools"></div><div class="clear"></div><div id="comment-40486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40487"></span>

<div id="answer-container-40487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40487-score" class="post-score" title="current number of votes">0</div><span id="post-40487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you open a ticket at <a href="https://support.riverbed.com/">https://support.riverbed.com/</a> ? AirPcap is produced and sold by Riverbed, not the Wireshark development team.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-40487" class="comments-container"></div><div id="comment-tools-40487" class="comment-tools"></div><div class="clear"></div><div id="comment-40487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40503"></span>

<div id="answer-container-40503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40503-score" class="post-score" title="current number of votes">0</div><span id="post-40503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the others already mentioned it is most certainly a Airpcap issue.</p><p>If you're running it on USB3 see <a href="https://supportkb.riverbed.com/support/index?page=content&amp;id=S16699">https://supportkb.riverbed.com/support/index?page=content&amp;id=S16699</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-40503" class="comments-container"></div><div id="comment-tools-40503" class="comment-tools"></div><div class="clear"></div><div id="comment-40503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

