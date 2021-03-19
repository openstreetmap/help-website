+++
type = "question"
title = "A question about &#x27;kind window size&#x27;"
description = '''Hello All Can someone please help me with the following question I was watching an excellent video from Shark Fest (2013 I think) by Betty DuBios where she is focusing on the tcp three way handshake and the various flags and options that come out of this.  I understand Windows Size and Window Scalin...'''
date = "2016-11-26T11:58:00Z"
lastmod = "2016-11-26T13:58:00Z"
weight = 57648
keywords = [ "tcpwindowscaling", "window" ]
aliases = [ "/questions/57648" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [A question about 'kind window size'](/questions/57648/a-question-about-kind-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57648-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All Can someone please help me with the following question</p><p>I was watching an excellent video from Shark Fest (2013 I think) by Betty DuBios where she is focusing on the tcp three way handshake and the various flags and options that come out of this.</p><p>I understand Windows Size and Window Scaling factor. There was however part of here video which mentioned 'Kind window size' she only touched on this lightly and I did not get a clear sense or its purpose.</p><p>I posted an image from the video <a href="https://1drv.ms/i/s!AqL5zUwOWToZa5dzp7jYs11-2XA">here</a> to show you want I mean.</p><p>I believe it is meant to convey to the other party in the tcp conversation hay I can scale my windows right up to x10 (1024) but prefer x3 (8) as I am under load. Is that the meaning of the 'kind window size' ?</p><p>Any advise, most welcome</p><p>Thanks Ernie</p></div><div id="question-tags" class="tags-container tags">tcpwindowscaling window</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '16, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/ff39c11ae2cb05528da757366e76d84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EBrant&#39;s gravatar image" /><p>EBrant<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EBrant has no accepted answers">0%</span></p></div></div><div id="comments-container-57648" class="comments-container"></div><div id="comment-tools-57648" class="comment-tools"></div><div class="clear"></div><div id="comment-57648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57655"></span>

<div id="answer-container-57655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57655-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>@EBrant, it's not as sophisticated as you've interpreted it.</p><p>Your picture shows the last part of the dissection tree below.</p><pre><code>Options: (12 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted, No-Operation (NOP), Window scale
    Maximum segment size: 1400 bytes
    No-Operation (NOP)
    No-Operation (NOP)
    TCP SACK Permitted Option: True
    No-Operation (NOP)
    Window scale: 7 (multiply by 128)
        Kind: Window Scale (3)
        Length: 3
        Shift count: 7
        [Multiplier: 128]</code></pre><p>It is an illustrative example of how Wireshark displays the dissection tree. On the topmost line, there is a summary of the TCP Options portion of the TCP header. If you "expand" this line, you get all the options listed, each at its individual line. And if you expand any of these, you get the dissection of the internal structure of that particular option itself. Each option is identified by the contents of its first byte, and the RFC calls that distinctive field "kind" - therefore, the dissector names it the same way.</p><p>So the "kind" value for the option "Window Scale" is 3, the total length of the option (i.e. including the kind and length fields) is 3 octets, and the actual value of the payload, called <code>Shift count</code>, is 7. The last line, <code>[Multiplier: 128]</code>, is a "pseudo-field" - it is not actually present in the captured frame but the dissector calculates it from the actual contents of the frame (and sometimes also of related frames). In this case, it is the value of 2^7.</p><p>The window size scaling factor does not change throughout the session, it is only announced once during session establishment. So the one and only value announced is the one in the <code>Shift count</code> field, which is 10 in your example and 7 in mine. It may possibly depend on the load of its sender, but there wouldn't be any purpose in advertising that the sender could support a different value if its life was easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57655" class="comments-container"><span id="57664"></span><div id="comment-57664" class="comment"><div id="post-57664-score" class="comment-score"></div><div class="comment-text"><p>Hello Sandy</p><p>Thanks very much for the excellent and detailed answer you gave above (explains it very well indeed).</p><p>I appreciate you taking the time :)</p><p>Ernie</p></div><div id="comment-57664-info" class="comment-info"><span class="comment-age">(27 Nov '16, 05:13)</span> EBrant</div></div></div><div id="comment-tools-57655" class="comment-tools"></div><div class="clear"></div><div id="comment-57655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

