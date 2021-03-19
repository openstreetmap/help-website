+++
type = "question"
title = "DIS PDU data extraction with tshark"
description = '''I need to extract just the data from a capture file, something like using &#x27;Follow Stream&#x27; and then saving that as a file, but using tshark. I&#x27;ve discovered that, for other protocols using TCP, I can filter using -e tcp.sequence_data, but there doesn&#x27;t appear to be an equivalent for UDP. (I saw an an...'''
date = "2013-10-08T06:49:00Z"
lastmod = "2013-10-14T04:37:00Z"
weight = 25743
keywords = [ "pdu", "dataextraction", "tshark", "dis" ]
aliases = [ "/questions/25743" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [DIS PDU data extraction with tshark](/questions/25743/dis-pdu-data-extraction-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25743-score" class="post-score" title="current number of votes">0</div><span id="post-25743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to extract just the data from a capture file, something like using 'Follow Stream' and then saving that as a file, but using tshark. I've discovered that, for other protocols using TCP, I can filter using -e tcp.sequence_data, but there doesn't appear to be an equivalent for UDP. (I saw an answer to another question that suggested -e udp.data but that threw up an error.)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-dataextraction" rel="tag" title="see questions tagged &#39;dataextraction&#39;">dataextraction</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dis" rel="tag" title="see questions tagged &#39;dis&#39;">dis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/310c7b54264c9e10ad43acb3bb1d042a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiggers&#39;s gravatar image" /><p><span>wiggers</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiggers has no accepted answers">0%</span></p></div></div><div id="comments-container-25743" class="comments-container"></div><div id="comment-tools-25743" class="comment-tools"></div><div class="clear"></div><div id="comment-25743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25756"></span>

<div id="answer-container-25756" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25756-score" class="post-score" title="current number of votes">1</div><span id="post-25756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiggers has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's how to do it, using http traffic as an example:</p><ol><li>start Wireshark and open the dialog Analyze-&gt;Enabled Protocols...</li><li>choose the protocol or protocols you're interested in extracting (e.g. http) and <strong>disable</strong> them (no, that's not a typo!)</li><li>save that setting and exit Wireshark</li><li>run tshark as tshark -r mydata.pcap -Tfields -edata</li><li>you might wish to go back into Wireshark and re-enable the protocol(s)</li></ol><p>What you'll get is hex dumps of only the undecoded data (which is why you disabled the protocols of interest). Note that this works with both TCP and UDP without change.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p><span>beroset</span><br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-25756" class="comments-container"><span id="25783"></span><div id="comment-25783" class="comment"><div id="post-25783-score" class="comment-score"></div><div class="comment-text"><p>Many thanks. Some more on config files to disable protocols <a href="http://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark">here</a>.</p></div><div id="comment-25783-info" class="comment-info"><span class="comment-age">(09 Oct '13, 01:33)</span> <span class="comment-user userinfo">wiggers</span></div></div><span id="25835"></span><div id="comment-25835" class="comment"><div id="post-25835-score" class="comment-score"></div><div class="comment-text"><p>If that adequately answers your question, please accept the answer so that it no longer shows up as "unanswered." Thanks!</p></div><div id="comment-25835-info" class="comment-info"><span class="comment-age">(09 Oct '13, 08:38)</span> <span class="comment-user userinfo">beroset</span></div></div><span id="25957"></span><div id="comment-25957" class="comment"><div id="post-25957-score" class="comment-score"></div><div class="comment-text"><p>How do you 'accept'?</p></div><div id="comment-25957-info" class="comment-info"><span class="comment-age">(14 Oct '13, 04:13)</span> <span class="comment-user userinfo">wiggers</span></div></div><span id="25959"></span><div id="comment-25959" class="comment"><div id="post-25959-score" class="comment-score"></div><div class="comment-text"><p>To accept an answer you just check on the check mark next to the answer. See <a href="http://ask.wireshark.org/faq/">http://ask.wireshark.org/faq/</a></p></div><div id="comment-25959-info" class="comment-info"><span class="comment-age">(14 Oct '13, 04:37)</span> <span class="comment-user userinfo">beroset</span></div></div></div><div id="comment-tools-25756" class="comment-tools"></div><div class="clear"></div><div id="comment-25756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

