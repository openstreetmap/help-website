+++
type = "question"
title = "&quot;Decode As&quot; greyed out Wireshark vers 1.12.11"
description = '''Hello,  How can I overcome a greyed out &quot;Decode As&quot; from the Analyze menu? I need to use Wireshark Sub2.0 for the Adafruit nordic btle sniffer to work.   If this is a version issue, what is another sniffer I can use? reference: Section 10.4.2, “User Specified Decodes” reference: Adafruit btle sniffe...'''
date = "2016-05-17T15:31:00Z"
lastmod = "2016-07-18T14:49:00Z"
weight = 52698
keywords = [ "decode_as" ]
aliases = [ "/questions/52698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Decode As" greyed out Wireshark vers 1.12.11](/questions/52698/decode-as-greyed-out-wireshark-vers-11211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52698-score" class="post-score" title="current number of votes">0</div><span id="post-52698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, How can I overcome a greyed out "Decode As" from the Analyze menu? I need to use Wireshark Sub2.0 for the Adafruit nordic btle sniffer to work.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/DecodeAsOption_Sq8EQY9.png" alt="alt text" /></p><p>If this is a version issue, what is another sniffer I can use?</p><p>reference: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCustProtocolDissectionSection.html#ChAdvDecodeAs">Section 10.4.2, “User Specified Decodes”</a></p><p>reference: <a href="https://learn.adafruit.com/introducing-the-adafruit-bluefruit-le-sniffer/nordic-nrfsniffer">Adafruit btle sniffer</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode_as" rel="tag" title="see questions tagged &#39;decode_as&#39;">decode_as</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/c6eb9026027e86abffb4cb734a7b69ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sonofptolemy&#39;s gravatar image" /><p><span>sonofptolemy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sonofptolemy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52698" class="comments-container"></div><div id="comment-tools-52698" class="comment-tools"></div><div class="clear"></div><div id="comment-52698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54148"></span>

<div id="answer-container-54148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54148-score" class="post-score" title="current number of votes">0</div><span id="post-54148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <em>"Decode As"</em> is initially greyed out when you first launch Wireshark, but it shouldn't be greyed out once you load a capture file. Is it?</p><p>As an alternative, if you know what you're doing, you can also directly edit the "<code>decode_as_entries</code>" file in your personal preferences directory, which can be found via: <code>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal configuration</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54148" class="comments-container"></div><div id="comment-tools-54148" class="comment-tools"></div><div class="clear"></div><div id="comment-54148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

