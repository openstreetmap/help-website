+++
type = "question"
title = "How to use the existing h264 dissector as a subdissector for a custom one"
description = '''Hi there, I stuck at a point where I could do with some help of the experts :-) I&#x27;m currently writing a dissector for a proprietary protocol which includes h264 data as payload. The dissector for the proprietary protocol elements is working and now I would like to pass the payload to the h264 dissec...'''
date = "2014-04-30T09:03:00Z"
lastmod = "2014-05-01T09:48:00Z"
weight = 32315
keywords = [ "h264", "proprietary", "dissector", "subdissector", "payload" ]
aliases = [ "/questions/32315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use the existing h264 dissector as a subdissector for a custom one](/questions/32315/how-to-use-the-existing-h264-dissector-as-a-subdissector-for-a-custom-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I stuck at a point where I could do with some help of the experts :-) I'm currently writing a dissector for a proprietary protocol which includes h264 data as payload. The dissector for the proprietary protocol elements is working and now I would like to pass the payload to the h264 dissector which is part of wireshark.</p><p>Could someone give me a hint on how to manage this?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">h264 proprietary dissector subdissector payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/379e0140a068c09529b6dad812bc6eec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndyHe&#39;s gravatar image" /><p>AndyHe<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndyHe has no accepted answers">0%</span></p></div></div><div id="comments-container-32315" class="comments-container"></div><div id="comment-tools-32315" class="comment-tools"></div><div class="clear"></div><div id="comment-32315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32354"></span>

<div id="answer-container-32354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32354-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>the H.264 dissector can be retrieved thanks to the "h264" string. In your proto_reg_handoff() function, add the following code:</p><pre><code>h264_handle = find_dissector(&quot;h264&quot;);</code></pre><p>where h264_handle is defined as:</p><pre><code>dissector_handle_t h264_handle;</code></pre><p>Then in your code, call the H.264 dissector like this:</p><pre><code>call_dissector(h264_handle, h264_tvb, pinfo, tree);</code></pre><p>where h264_tvb is a tvb containing your H.264 payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-32354" class="comments-container"><span id="32385"></span><div id="comment-32385" class="comment"><div id="post-32385-score" class="comment-score"></div><div class="comment-text"><p>Pascal,</p><p>thousand thanks for your very helpful answer. Your code works fine and it saved my a lot of time!</p></div><div id="comment-32385-info" class="comment-info"><span class="comment-age">(02 May '14, 02:29)</span> AndyHe</div></div><span id="32386"></span><div id="comment-32386" class="comment"><div id="post-32386-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-32386-info" class="comment-info"><span class="comment-age">(02 May '14, 03:06)</span> grahamb ♦</div></div></div><div id="comment-tools-32354" class="comment-tools"></div><div class="clear"></div><div id="comment-32354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

