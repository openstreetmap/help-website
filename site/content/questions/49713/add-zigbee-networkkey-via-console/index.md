+++
type = "question"
title = "Add ZigBee Networkkey via console"
description = '''Hey guys, I have got a question concerning the ZigBee network key. I want to add the networkkey via command line. So I mean now I start a piped wireshark - get over to Edit -&amp;gt; Preferences -&amp;gt; Protocolls -&amp;gt; ZigBeeNWK -&amp;gt; Edit -&amp;gt; New -&amp;gt; (enter key, enter label)  Maybe someone knows a c...'''
date = "2016-02-02T03:32:00Z"
lastmod = "2016-02-02T04:50:00Z"
weight = 49713
keywords = [ "zigbee", "zigbee-network", "wep", "network", "key" ]
aliases = [ "/questions/49713" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add ZigBee Networkkey via console](/questions/49713/add-zigbee-networkkey-via-console)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49713-score" class="post-score" title="current number of votes">0</div><span id="post-49713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I have got a question concerning the ZigBee network key. I want to add the networkkey via command line. So I mean now I start a piped wireshark - get over to</p><p>Edit -&gt; Preferences -&gt; Protocolls -&gt; ZigBeeNWK -&gt; Edit -&gt; New -&gt; (enter key, enter label)</p><p>Maybe someone knows a command to add one or preferred three keys via command line. This would be really nice.</p><p>Thanks in advance, ElectricBlue</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zigbee" rel="tag" title="see questions tagged &#39;zigbee&#39;">zigbee</span> <span class="post-tag tag-link-zigbee-network" rel="tag" title="see questions tagged &#39;zigbee-network&#39;">zigbee-network</span> <span class="post-tag tag-link-wep" rel="tag" title="see questions tagged &#39;wep&#39;">wep</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/0258237eb64c884dc43ea86769043e35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElectricBlue&#39;s gravatar image" /><p><span>ElectricBlue</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElectricBlue has no accepted answers">0%</span></p></div></div><div id="comments-container-49713" class="comments-container"><span id="49714"></span><div id="comment-49714" class="comment"><div id="post-49714-score" class="comment-score"></div><div class="comment-text"><p>Do you need to automate addition of the keys because you expect to set many of them dynamically in a scripting environment? If not, configuring them once using the GUI Wireshark is enough that tshark could then use them.</p></div><div id="comment-49714-info" class="comment-info"><span class="comment-age">(02 Feb '16, 04:05)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49715"></span><div id="comment-49715" class="comment"><div id="post-49715-score" class="comment-score"></div><div class="comment-text"><p>I Would prefer a automated addition of this keys in a scripting environment. The setting once is not the problem - but I change the keys often and want to add them via script.</p></div><div id="comment-49715-info" class="comment-info"><span class="comment-age">(02 Feb '16, 04:32)</span> <span class="comment-user userinfo">ElectricBlue</span></div></div></div><div id="comment-tools-49713" class="comment-tools"></div><div class="clear"></div><div id="comment-49713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49717"></span>

<div id="answer-container-49717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49717-score" class="post-score" title="current number of votes">0</div><span id="post-49717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm afraid that as you want to provide the keys dynamically, you'll have to generate (or change) the file zigbee_pc_keys in your configuration profile directory before start of tshark/Wireshark. Define some keys using the GUI Wireshark, close it, and then look at the file structure. Maybe some developer will suggest a more noblesse method but this one works if you don't want to wait.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '16, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49717" class="comments-container"></div><div id="comment-tools-49717" class="comment-tools"></div><div class="clear"></div><div id="comment-49717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

