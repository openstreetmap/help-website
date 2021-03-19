+++
type = "question"
title = "Closed-Source Wireshark Dissectors/Plugins"
description = '''We, and our customers, love Wireshark. We want to further it&#x27;s use as an amazing tool! As an organization, would like to create a closed-source dissector to inspect proprietary wire-formats that we send data in and give this dissector to the customers to use to inspect their own traffic. However, we...'''
date = "2015-02-27T13:25:00Z"
lastmod = "2015-02-28T02:56:00Z"
weight = 40139
keywords = [ "gpl", "dissector", "license", "plugin" ]
aliases = [ "/questions/40139" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Closed-Source Wireshark Dissectors/Plugins](/questions/40139/closed-source-wireshark-dissectorsplugins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40139-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We, and our customers, love Wireshark. We want to further it's use as an amazing tool!</p><p>As an organization, would like to create a closed-source dissector to inspect proprietary wire-formats that we send data in and give this dissector to the customers to use to inspect their own traffic. However, we don't want to expose the fundamentals of how we process packets/messages for fear of exposing too much of the intellectual property we own.</p><p>How can we create a plugin to Wireshark so that the plugin created does not accidentally become GPL? Are there clauses in the Wireshark License that allows specifically for plugin/dissector additions?</p></div><div id="question-tags" class="tags-container tags">gpl dissector license plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '15, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/32a416408111c97c587eef5e8b7f90f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beadon&#39;s gravatar image" /><p>beadon<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beadon has no accepted answers">0%</span></p></div></div><div id="comments-container-40139" class="comments-container"></div><div id="comment-tools-40139" class="comment-tools"></div><div class="clear"></div><div id="comment-40139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40142"></span>

<div id="answer-container-40142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40142-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Short and quick answer: No, there's no way allowed for you to make use of the APIs of wireshark without being bound by the GPL.</p><p>However: if you can enter into a gentlemen's agreement with your customer that you'll be supplying a binary only plugin and that they'll refrain from using the rights under the GPL, you could be ok. Still these are untested legal grounds as in they could later set aside the agreement and call for the source code to be provided anyway.</p><p>In essence you cannot take this product, which we build in our spare time and provide for free and use it to leverage your commercial efforts without giving back to this community. A BSD license would allow that, but that's not the license under which Wireshark is distributed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '15, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40142" class="comments-container"></div><div id="comment-tools-40142" class="comment-tools"></div><div class="clear"></div><div id="comment-40142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40145"></span>

<div id="answer-container-40145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40145-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All plugins link with the Wireshark binaries and are thus regarded as a combined work under the GPL and must comply with the GPL licensing requirements when distributing such a combined work.</p><p>My view is a little different than Jaap's, in that there can't be any "gentlemen's agreement" as the <a href="http://www.gnu.org/licenses/gpl-2.0.html">GPL</a> (v2 Sect 3) <strong>requires</strong> you to either supply the source code, or make a written offer of the source for <strong>any</strong> third party when you distribute the Program. Sect 3c won't apply to you as you state you are making a commercial distribution.</p><p>Also Section 4 states you may not modify the licence which IMHO a "gentlemen's agreement" does, so this would also prohibit you from doing so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '15, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40145" class="comments-container"><span id="40146"></span><div id="comment-40146" class="comment"><div id="post-40146-score" class="comment-score"></div><div class="comment-text"><p>"A gentlemen's agreement (or gentleman's agreement) is an informal and legally non-binding agreement between two or more parties". That's why I said these are untested legal grounds, as in the customer could exercise their GPL rights anyway in the future and (legally) acquire the source code anyway.</p></div><div id="comment-40146-info" class="comment-info"><span class="comment-age">(28 Feb '15, 03:59)</span> Jaap ♦</div></div><span id="40147"></span><div id="comment-40147" class="comment"><div id="post-40147-score" class="comment-score"></div><div class="comment-text"><p><strong>Any</strong> third-party can also request the source if the written offer from 3b is made. I just don't want folks to think there is any wiggle room.</p></div><div id="comment-40147-info" class="comment-info"><span class="comment-age">(28 Feb '15, 04:31)</span> grahamb ♦</div></div></div><div id="comment-tools-40145" class="comment-tools"></div><div class="clear"></div><div id="comment-40145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

